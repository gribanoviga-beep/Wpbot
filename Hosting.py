import os
import json
import logging
import threading
import subprocess
import re
import sys
import asyncio
from flask import Flask
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    CallbackQueryHandler,
)

# IMPORTANT:
# 1) Generate a NEW Telegram bot token in @BotFather because the old token was shared.
# 2) Paste the new token below. Do not share it publicly.
TOKEN = "8196966190:AAFOC32xVPLND99ss6Ee6RumEi1OYHUASOk"

OWNER_ID = 7069720635
BOT_PASSWORD = "Gojoera"
CHANNEL_URL = "https://t.me/NARAK_LOCK"
WELCOME_PHOTO = "https://files.catbox.moe/7dqow9.jpg"

APPROVED_FILE = "approved_users.json"
DOWNLOAD_DIR = "downloads"

# --- Logging ---
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# --- Keep-alive web server ---
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_flask():
    app.run(host="0.0.0.0", port=5000, debug=False, threaded=True, use_reloader=False)

def keep_alive():
    thread = threading.Thread(target=run_flask, daemon=True)
    thread.start()

# --- User approval persistence ---
def load_approved_users():
    try:
        with open(APPROVED_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        return {str(user_id): True for user_id in data}
    except (FileNotFoundError, json.JSONDecodeError, TypeError):
        return {}

approved_users = load_approved_users()
pending_password = set()

def save_approved_users():
    try:
        with open(APPROVED_FILE, "w", encoding="utf-8") as file:
            json.dump(list(approved_users.keys()), file)
    except OSError as error:
        logger.error("Could not save approved users: %s", error)

def is_approved(user_id):
    return user_id == OWNER_ID or str(user_id) in approved_users

# Running process records: {user_id: [{"name": ..., "proc": ..., "log": ...}]}
running_scripts = {}

# --- Dependency scanners ---
def scan_python_dependencies(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            content = file.read()
        imports = re.findall(
            r"^\s*(?:from|import)\s+([a-zA-Z0-9_]+)",
            content,
            re.MULTILINE,
        )
        stdlib = getattr(sys, "stdlib_module_names", set())
        ignored = {"__future__"}
        return sorted({
            module for module in imports
            if module not in stdlib and module not in ignored
        })
    except Exception:
        logger.exception("Error scanning Python dependencies")
        return []

def scan_js_dependencies(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            content = file.read()
        requires = re.findall(r'require\([\'"](.+?)[\'"]\)', content)
        imports = re.findall(r'from\s+[\'"](.+?)[\'"]', content)
        builtins = {"fs", "path", "os", "http", "https", "url", "util", "crypto",
                    "events", "stream", "child_process", "readline", "buffer",
                    "timers", "assert", "net", "dns", "zlib", "querystring"}
        packages = set()
        for name in requires + imports:
            if name.startswith((".", "/")) or name.startswith("node:"):
                continue
            package = name.split("/")[0] if name.startswith("@") else name.split("/")[0]
            if package not in builtins:
                packages.add(package)
        return sorted(packages)
    except Exception:
        logger.exception("Error scanning JavaScript dependencies")
        return []


# --- Welcome Screen with Photo ---
async def show_welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    welcome_text = (
        f"╭━━━『 👑 GOJO HOST 👑 』━━━╮\n\n"
        f"⚡ 𝐖𝐄𝐋𝐂𝐎𝐌𝐄, {user.first_name} 💞\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"🆔 𝐔𝐒𝐄𝐑 𝐈𝐃: {user.id}\n"
        f"✳️ 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄: @{user.username if user.username else 'Not Set'}\n"
        f"🔰 𝐒𝐓𝐀𝐓𝐔𝐒: 🆓 Free User\n"
        f"📁 𝐅𝐈𝐋𝐄𝐒: 0 / 10\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"🐍 Python (.py) Hosting\n"
        f"🟨 JavaScript (.js) Hosting\n"
        f"📦 File Upload Support\n\n"
        f"💫 𝐘𝐎𝐔𝐑 𝐂𝐎𝐃𝐄. 𝐘𝐎𝐔𝐑 𝐒𝐄𝐑𝐕𝐄𝐑.\n"
        f"╰━━━『 🚀 GET STARTED 』━━━╯"
    )

    reply_keyboard = [
        [
            KeyboardButton("𝐔𝐏𝐋𝐎𝐀𝐃 𝐅𝐈𝐋𝐄𝐒 👾"),
            KeyboardButton("📂 𝐂𝐇𝐄𝐀𝐊 𝐅𝐈𝐋𝐄𝐒")
        ],
        [
            KeyboardButton("⚡ 𝐁𝐎𝐓 𝐒𝐏𝐄𝐄𝐃"),
            KeyboardButton("📊 Statistics")
        ],
        [
            KeyboardButton("📩 Send Command"),
            KeyboardButton("📞 Contact Owner")
        ],
        [KeyboardButton("🛑 𝐒𝐓𝐎𝐏 𝐒𝐂𝐑𝐈𝐏𝐓")]
    ]

    reply_markup = ReplyKeyboardMarkup(
        reply_keyboard,
        resize_keyboard=True
    )

    inline_markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "📢 Updates Channel",
                url="https://t.me/NARAK_LOCK"
            )
        ]
    ])

    try:
        await update.effective_message.reply_photo(
            photo="https://files.catbox.moe/7dqow9.jpg",
            caption=welcome_text,
            reply_markup=reply_markup
        )
    except Exception as e:
        logger.error("Welcome photo error: %s", e)
        await update.effective_message.reply_text(
            welcome_text,
            reply_markup=reply_markup
        )

    await update.effective_message.reply_text(
        "📢 Join our Updates Channel:",
        reply_markup=inline_markup
    )


# --- Commands ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if is_approved(user_id):
        pending_password.discard(user_id)
        await show_welcome(update, context)
        return

    pending_password.add(user_id)
    await update.effective_message.reply_text(
        "🔐 ACCESS PROTECTED\n\n"
        "Bot use karne ke liye password bhejo:"
    )

async def install_module(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not is_approved(user_id):
        await update.effective_message.reply_text("🔐 Pehle /start karke password verify karo.")
        return

    if not context.args:
        await update.effective_message.reply_text("Usage: /install <package_name>")
        return

    package = context.args[0]
    if package.lower() == "telegram":
        package = "python-telegram-bot"

    await update.effective_message.reply_text(f"⏳ Installing {package}...")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", package, "--no-cache-dir"],
            capture_output=True,
            text=True,
            timeout=180,
        )
        if result.returncode == 0:
            await update.effective_message.reply_text(f"✅ Successfully installed {package}!")
        else:
            await update.effective_message.reply_text(
                f"❌ Installation failed:\n{result.stderr[-1200:]}"
            )
    except Exception as error:
        await update.effective_message.reply_text(f"❌ Error: {error}")

async def stop_script(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not is_approved(user_id):
        await update.effective_message.reply_text("🔐 Pehle password verify karo.")
        return

    scripts = running_scripts.get(user_id, [])
    active_scripts = [
        (index, item) for index, item in enumerate(scripts)
        if item["proc"].poll() is None
    ]

    if not active_scripts:
        await update.effective_message.reply_text("❌ You have no scripts running.")
        return

    if context.args:
        requested_name = context.args[0]
        for item in scripts:
            if item["name"] == requested_name:
                if item["proc"].poll() is None:
                    item["proc"].terminate()
                    try:
                        item["log"].close()
                    except Exception:
                        pass
                    await update.effective_message.reply_text(f"✅ Stopped {requested_name}.")
                else:
                    await update.effective_message.reply_text(f"ℹ️ {requested_name} is already stopped.")
                return
        await update.effective_message.reply_text(f"❌ Script {requested_name} not found.")
        return

    keyboard = [
        [InlineKeyboardButton(f"🛑 Stop {item['name']}", callback_data=f"stop_{index}")]
        for index, item in active_scripts
    ]
    await update.effective_message.reply_text(
        "Select a script to stop:",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = update.effective_user.id

    if not is_approved(user_id):
        await query.edit_message_text("🔐 Please verify the password first with /start.")
        return

    if query.data.startswith("stop_"):
        try:
            index = int(query.data.split("_", 1)[1])
            scripts = running_scripts.get(user_id, [])
            if not 0 <= index < len(scripts):
                await query.edit_message_text("❌ Script index not found.")
                return

            script = scripts[index]
            if script["proc"].poll() is None:
                script["proc"].terminate()
                try:
                    script["log"].close()
                except Exception:
                    pass
                await query.edit_message_text(f"✅ Stopped {script['name']}.")
            else:
                await query.edit_message_text(f"ℹ️ {script['name']} is already stopped.")
        except (ValueError, IndexError) as error:
            await query.edit_message_text(f"❌ Invalid stop request: {error}")

# --- Text and file handling ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    user = update.effective_user
    user_id = user.id
    text = (message.text or "").strip()

    # Password gate: only users who started the password flow can submit it.
    if not is_approved(user_id):
        if user_id not in pending_password:
            if text:
                await message.reply_text("🔐 Send /start first to request password access.")
            else:
                await message.reply_text("🔐 Send /start first to request password access.")
            return

        if not text:
            await message.reply_text("🔐 Please send the password as text.")
            return

        if text == BOT_PASSWORD:
            pending_password.discard(user_id)
            approved_users[str(user_id)] = True
            save_approved_users()
            await message.reply_text("✅ Password accepted! Access approved.")
            await show_welcome(update, context)
        else:
            await message.reply_text("❌ Wrong password. Try again.")
        return

    # Menu text handlers
    if text == "𝐔𝐏𝐋𝐎𝐀𝐃 𝐅𝐈𝐋𝐄𝐒 👾":
        await message.reply_text("📤 Send your Python (.py), JS (.js), or ZIP (.zip) file.")
        return
    if text == "📂 𝐂𝐇𝐄𝐀𝐊 𝐅𝐈𝐋𝐄𝐒":
        scripts = running_scripts.get(user_id, [])
        if not scripts:
            await message.reply_text("📂 You have no scripts running.")
        else:
            status_msg = "📂 Your scripts:\n"
            for item in scripts:
                status = "Running" if item["proc"].poll() is None else "Stopped"
                status_msg += f"- {item['name']}: {status}\n"
            await message.reply_text(status_msg)
        return
    if text == "⚡ 𝐁𝐎𝐓 𝐒𝐏𝐄𝐄𝐃":
        await message.reply_text("⚡ Bot is responsive.")
        return
    if text == "📊 Statistics":
        total_running = sum(
            sum(1 for item in items if item["proc"].poll() is None)
            for items in running_scripts.values()
        )
        await message.reply_text(f"📊 Currently running scripts: {total_running}")
        return
    if text == "📩 Send Command":
        await message.reply_text("📩 Feature coming soon.")
        return
    if text == "📞 Contact Owner":
        await message.reply_text("📞 Contact: https://t.me/Narak_lok_era")
        return
    if text == "🛑 𝐒𝐓𝐎𝐏 𝐒𝐂𝐑𝐈𝐏𝐓":
        await stop_script(update, context)
        return

    if not message.document:
        await message.reply_text("Please use the menu buttons or send a .py, .js, or .zip file.")
        return

    doc = message.document
    file_name = os.path.basename(doc.file_name or "uploaded_file")
    extension = os.path.splitext(file_name)[1].lower()

    if extension not in {".py", ".js", ".zip"}:
        await message.reply_text("❌ Unsupported file type. Please send .py, .js, or .zip.")
        return
    if extension == ".zip":
        await message.reply_text("📦 ZIP upload received, but ZIP extraction/launch is not enabled yet.")
        return

    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    file_path = os.path.join(DOWNLOAD_DIR, file_name)
    status_msg = await message.reply_text(f"⏳ Downloading {file_name}...")

    try:
        telegram_file = await context.bot.get_file(doc.file_id)
        await telegram_file.download_to_drive(file_path)

        if extension == ".py":
            deps = scan_python_dependencies(file_path)
            command = [sys.executable, os.path.abspath(file_path)]
            for dep in deps:
                try:
                    subprocess.run(
                        [sys.executable, "-m", "pip", "install", dep, "--no-cache-dir"],
                        capture_output=True,
                        text=True,
                        timeout=60,
                    )
                except Exception as error:
                    logger.warning("Could not install Python dependency %s: %s", dep, error)
        else:
            deps = scan_js_dependencies(file_path)
            command = ["node", "--max-old-space-size=512", os.path.abspath(file_path)]
            if deps:
                try:
                    subprocess.run(
                        ["npm", "install", *deps, "--no-audit", "--no-fund"],
                        cwd=os.path.abspath(DOWNLOAD_DIR),
                        capture_output=True,
                        text=True,
                        timeout=180,
                    )
                except Exception as error:
                    logger.warning("Could not install JS dependencies: %s", error)

        await status_msg.edit_text(f"🚀 Launching {file_name}...")
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"

        log_path = f"{file_path}.log"
        log_file = open(log_path, "w", encoding="utf-8", errors="replace")
        try:
            proc = subprocess.Popen(
                command,
                stdout=log_file,
                stderr=subprocess.STDOUT,
                env=env,
                cwd=os.path.abspath(DOWNLOAD_DIR),
                start_new_session=(os.name != "nt"),
            )
        except Exception:
            log_file.close()
            raise

        running_scripts.setdefault(user_id, []).append({
            "name": file_name,
            "proc": proc,
            "log": log_file,
        })

        await asyncio.sleep(3)
        if proc.poll() is not None:
            log_file.close()
            try:
                with open(log_path, "r", encoding="utf-8", errors="ignore") as file:
                    error_log = file.read()[-2500:]
            except OSError:
                error_log = "Could not read process log."
            await status_msg.edit_text(f"❌ {file_name} stopped after launch.\n\n{error_log}")
        else:
            await status_msg.edit_text(f"✅ {file_name} is running.")

    except Exception as error:
        logger.exception("File handling failed")
        await status_msg.edit_text(f"❌ Error handling file: {error}")

def main():
    if not TOKEN or TOKEN == "PASTE_YOUR_NEW_BOT_TOKEN_HERE":
        raise SystemExit("Set TOKEN to your NEW Telegram bot token before running.")

    keep_alive()
    application = (
        ApplicationBuilder()
        .token(TOKEN)
        .connect_timeout(60)
        .read_timeout(60)
        .write_timeout(60)
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("install", install_module))
    application.add_handler(CommandHandler("stop", stop_script))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(
        MessageHandler(filters.Document.ALL | (filters.TEXT & ~filters.COMMAND), handle_message)
    )

    logger.info("Bot is starting...")
    application.run_polling()

if __name__ == "__main__":
    main()
