#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║                    🔱 𝗚𝖔𝖏𝖔 ~ #𝔬𝔣𝔣 ✞︎໋🌙 𝐔sᴇʀ𝐁ᴏᴛ 🔱                    ║
║                         Version 1.0                           ║
║                                                               ║
║              ⚡ The Almighty Telegram Userbot ⚡               ║
║                                                               ║
║           "Bow down, mortals. Your God has arrived."          ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
"""

import subprocess
import sys
import importlib.util
import os

# ==================== AUTO INSTALL REQUIRED PACKAGES ====================
REQUIRED_PACKAGES = [
    "telethon",
]

def install_package(package):
    """Install a package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", package])
        return True
    except Exception:
        return False

def check_and_install_packages():
    """Check if required packages are installed, install if missing"""
    missing_packages = []
    
    for package in REQUIRED_PACKAGES:
        spec = importlib.util.find_spec(package)
        if spec is None:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n📦 Required packages not found: {', '.join(missing_packages)}")
        print("⏳ Attempting to install missing packages...\n")
        
        for package in missing_packages:
            print(f"  Installing {package}...")
            if install_package(package):
                print(f"  ✅ {package} installed successfully!")
            else:
                print(f"  ❌ Failed to install {package}")
        
        print("\n✅ Installation complete!")
    else:
        print("✅ All required packages are already installed.")

# Run package check before importing anything else
check_and_install_packages()

# ==================== NOW IMPORT ALL MODULES ====================
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import asyncio
async def delete_after(message, delay):
    await asyncio.sleep(delay)
    try:
        await message.delete()
    except Exception:
        pass

import json
import random
import logging
import time
import re
import math
import itertools
import os
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Set
from collections import deque
import aiohttp

# ==================== TELEGRAM IMPORTS ====================
from telethon import TelegramClient, events, functions, utils, Button
from telethon.tl.functions.channels import InviteToChannelRequest, EditAdminRequest, EditBannedRequest, CreateChannelRequest, DeleteChannelRequest, EditPhotoRequest, EditTitleRequest, LeaveChannelRequest, JoinChannelRequest
from telethon.tl.functions.messages import AddChatUserRequest, CreateChatRequest, ExportChatInviteRequest, ImportChatInviteRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.types import ChatAdminRights, ChannelParticipantsAdmins, InputPeerChannel, Chat, Channel, InputPhoto, MessageEntityMentionName, MessageActionChatEditTitle, ChatBannedRights, InputMediaDice, PeerUser, SendMessageTypingAction, SendMessageRecordAudioAction, SendMessageGamePlayAction, SendMessageRecordVideoAction, SendMessageRecordRoundAction, SendMessageUploadPhotoAction, SendMessageUploadDocumentAction, SendMessageGeoLocationAction, SendMessageChooseContactAction, SendMessageCancelAction, InputStickerSetShortName, InputMediaUploadedDocument, MessageMediaDocument, DocumentAttributeFilename, MessageMediaPhoto
from telethon.errors import FloodWaitError, MessageNotModifiedError, RPCError, ChatWriteForbiddenError, UserBannedInChannelError, UserNotParticipantError, ChatAdminRequiredError
from telethon.events import InlineQuery, CallbackQuery

# ==================== CONFIG ====================
API_ID = 39019669
API_HASH = 'fcfb260835b3cbcade6e849897451eee'
PHONE = '+919142687433'
BOT_TOKEN = '8614074215:AAEZ7YAT0SuuTZXRZjljuLyR50EuYuWSCBM'
TG_BOT_USERNAME = "Copyrightbot_x_bot"
OWNER_ID = 7069720635
𝗚𝖔𝖏𝖔_BOT_OWNER = 7069720635
DEFAULTUSER = "𝗚𝖔𝖏𝖔 ~ #𝔬𝔣𝔣 ✞︎໋🌙"

# ==================== CLIENT INITIALIZATION ====================
client = TelegramClient("𝗚𝖔𝖏𝖔UserBot", API_ID, API_HASH)

# ==================== RAID CONFIG ====================
RAID_DELAY = 0.00001
RAID_LIMIT = 999999

# Default bot list
DEFAULT_BOTS = [
"Gojox4tg_bot",
"gojox1tg_bot",
"gojox5tg_bot",
"gojoxtg_bot",
"gojo7xtg_bot",
"gojo7tg_bot",
"gojox7tg_bot",
"gojox9tg_bot",
"gojow7tg_bot",
"gojo7ztg_bot",
"gojo11tg_bot",
"gojoc7tg_bot",
"gojomztxg_bot",
"gojo7nztxg_bot",
"gojo7xtxg_bot",
"gojo_7cbot",
]

# Default PM permit media URL
DEFAULT_PMPERMIT_MEDIA_URL = "https://files.catbox.moe/7dqow9.jpg"

# Directories
PROJECT_ROOT = Path(__file__).parent
DB_DIR = PROJECT_ROOT / "𝗚𝖔𝖏𝖔DB"
DB_DIR.mkdir(exist_ok=True)

# Files
SAFE_USERS_FILE = DB_DIR / "safe_users.json"
AUTO_DELETE_FILE = DB_DIR / "auto_delete.json"
DELETE_USERS_FILE = DB_DIR / "delete_users.json"
AFK_USERS_FILE = DB_DIR / "afk_users.json"
AFK_STATS_FILE = DB_DIR / "afk_stats.json"
ADMIN_ONLY_FILE = DB_DIR / "admin_only.json"
PM_DELETE_FILE = DB_DIR / "pm_delete.json"
ASSISTANT_DB_FILE = DB_DIR / "assistant_db.json"
USER_BOT_LISTS_FILE = DB_DIR / "user_bot_lists.json"
BOT_LIST_FILE = DB_DIR / "bot_list.json"
CUSTOM_RAIDS_FILE = DB_DIR / "custom_raids.json"
SUDO_FILE = DB_DIR / "sudo_users.json"
FLASH_DB_DIR = DB_DIR / "flashvault"
FLASH_DB_DIR.mkdir(parents=True, exist_ok=True)
FLASH_DB_PATH = FLASH_DB_DIR / "flashvault_db.json"
VAULT_DB_DIR = DB_DIR / "ghostvault"
VAULT_DB_DIR.mkdir(parents=True, exist_ok=True)
VAULT_DB_PATH = VAULT_DB_DIR / "vault_db.json"
GLOBALTOOLS_DB_DIR = DB_DIR / "globaltools"
GLOBALTOOLS_DB_DIR.mkdir(parents=True, exist_ok=True)
GLOBALTOOLS_DB_PATH = GLOBALTOOLS_DB_DIR / "globaltools.json"
PMPERMIT_CONFIG_FILE = DB_DIR / "pmpermit_config.json"


# ==================== WORD ARRAYS ====================

LOVE_WORDS = [
    "Pyaar", "Ishq", "Mohabbat", "Bhalobasha", "Prem", 
    "Kaadhal", "Prema", "Preethi", "Sneham", "Maya",
    "Hubb", "Eshgh", "Mehr",
    "Amour", "Amor", "Amore", "Liebe", "Lyubov", "Agapi", "Ai", "Sarang", "Cinta", "Rak", "Pag-ibig", "Aloha", "Aroha", "Amo"
]

FUCK_WORDS = [ "bullshit", "whore", "bitch", "bastard", "asshole",
    "motherfucker", "son of a bitch", "dickhead", "prick", 
    "shit", "cunt", "slut", "wanker", "twat", "pussy",
    "douchebag", "jackass"]

BULLY_WORDS = [
    "kid", "poor thing", "son of a bitch", "whore",
    "bastard", "brat", "loser",
    "weakling", "coward", "scaredy cat", "worthless", "pathetic",
    "pitiful"
]

CHUD_WORDS = [
    "kirito se cud", "rndi", "gulam", "hijda", "cudakad", "gareeb",
    "chamar", "maa chuda tery", "lun ki topi", "kamzor", "aand choos kirito ke", "bhencod",
    "rndy ka beta", "majdur ki aulaad", "chudai kha tatte", "madrcod"]

LUN_WORDS = [ "𝗚𝖔𝖏𝖔 से चुद", "रंडी", "गुलाम", "हिजदा", "चुदाकड़", "गरीब", "चमार", "माँ चुदा तेरी", "लंड की टोपी", "कमज़ोर", "आंड चूस 𝗚𝖔𝖏𝖔 के", "भहनचोद", "रंडी का बेटा", "मजदूर की औलाद", "चुदाई खा टट्टे", "मादरचोद"]

# ==================== STATE VARIABLES ====================

# Raid System
active_raids = {
    "users": {}, 
    "stats": {}, 
    "start_time": {}, 
    "raid_type": {}, 
    "chat_id": {}, 
    "msg_index": {}, 
    "template": {},
    "target_name": {},
    "custom_name": {},
    "is_multi": {},
    "messages": {}
}

# Spam System
spam_delay = 0.05
spam_tasks = {}
cipher_spam_tasks = {}

# Admin & Moderation
admin_only_chats = {}
muted_users = {}  # {chat_id: set(user_ids)}
auto_delete_chats = {}  # {chat_id: True/False}
ncdel_enabled = {}
ncdel_status = {}

# PM System
pm_delete_enabled = False
pmpermit_enabled = True

# AFK System
afk_users = {}
afk_stats = {}

# Tagger System
tagger_active_chats = set()
processed_msgs = deque(maxlen=2000)

# Purge System
cancellation_flags = {}

# Bait System
BAIT_TASKS = {}

# Ghost Vault System
MESSAGE_CACHE = {}
MAX_CACHE_SIZE = 5000
cache_keys = []

# Sudo Users
SUDO_USERS = []

# Bot Lists
bots_state = {"bots_list": []}

# Start Time
START_TIME = datetime.now()

# ==================== CMD_LIST FOR HELP SYSTEM ====================
CMD_LIST = {}
PLUGINS_PER_PAGE = 9
PLUGINS_PER_ROW = 3

def add_handler(plugin_name, commands, description=""):
    """Register commands for the help system"""
    if plugin_name not in CMD_LIST:
        CMD_LIST[plugin_name] = {
            "commands": commands.copy() if isinstance(commands, list) else [commands],
            "description": description
        }

# ==================== PLUGIN EMOJIS ====================
PLUGIN_EMOJIS = {
    "help": "📜",
    "bot_manager": "🤖",
    "games": "🎮",
    "emojigames": "🎲",
    "animations": "🎨",
    "tools": "🛠️",
    "protect": "🛡️",
    "clone": "👥",
    "admin": "👑",
    "moderation": "🔇",
    "afk": "🌌",
    "raid": "⚔️",
    "replyraid": "🔄",
    "spam": "📢",
    "pm_assistant": "🔧",
    "setup": "⚙️",
    "extra": "✨",
    "customraid": "🎭",
    "bait": "🎣",
    "flashvault": "📸",
    "ghostvault": "🕵️",
    "globaltools": "🌍",
    "tagger": "🏷️",
    "purge": "🧹",
    "sudo": "🔑",
    "chats": "📁"
}

def get_plugin_emoji(plugin_name):
    return PLUGIN_EMOJIS.get(plugin_name, "🔹")

def get_plugin_display_name(plugin_name):
    display_names = {
        "help": "Help",
        "bot_manager": "Bots",
        "games": "Games",
        "emojigames": "Emoji Games",
        "animations": "Animate",
        "tools": "Tools",
        "protect": "Protect",
        "clone": "Clone",
        "admin": "Admin",
        "moderation": "Moderate",
        "afk": "AFK",
        "raid": "Raid",
        "replyraid": "ReplyRaid",
        "spam": "Spam",
        "pm_assistant": "PM",
        "setup": "Setup",
        "extra": "Extra",
        "customraid": "Custom Raid",
        "bait": "Bait",
        "flashvault": "FlashVault",
        "ghostvault": "GhostVault",
        "globaltools": "GlobalTools",
        "tagger": "Tagger",
        "purge": "Purge",
        "sudo": "Sudo",
        "chats": "Chats"
    }
    return display_names.get(plugin_name, plugin_name.title().replace('_', ' '))

# ==================== REGISTER PLUGINS ====================

# HELP SYSTEM
add_handler("help", [
    ".help - Summon the divine help menu",
    ".help <plugin> - Seek guidance for a specific power",
    ".plugins - Reveal all loaded artifacts",
    ".helpstats - View sacred statistics",
    ".quickhelp - Quick divine guidance"
], "📜 Divine Guidance - Seek wisdom from the Gods")

# BOT MANAGER
add_handler("bot_manager", [
    ".setbots <bot1> <bot2>... - Summon your bot army",
    ".mybots - View your summoned army",
    ".resetbots - Return to default army",
    ".addbot - Summon ALL bots to your realm at once",
    ".giveadmin - Elevate ALL bots to 𝗚𝖔𝖏𝖔 God rank",
    ".takeadmin - Demote ALL bots from rank",
    ".removebots - Banish ALL bots from your realm",
    ".creategc <count> - Create multiple groups with your bots"
], "🤖 Bot Manager - Command your bot army")

# GAMES
add_handler("games", [
    ".dice - Roll the sacred dice 🎲",
    ".coin - Flip the blessed coin 🪙",
    ".decide <question> - Seek divine guidance ❓",
    ".xogame - Play the holy XO game ❌⭕",
    ".task [category] - Random truth or dare task",
    ".truth [category] - Random truth task",
    ".dare [category] - Random dare task",
    ".game <code> - Play inline games via @inlinegamesbot"
], "🎮 Games - Play games blessed by the Gods")

# EMOJI GAMES
add_handler("emojigames", [
    ".dart [1-6] - Throw dart emoji",
    ".dice [1-6] - Roll animated dice",
    ".bb [1-5] - Basketball emoji",
    ".fb [1-5] - Football emoji",
    ".jp [1-64] - Jackpot slot emoji",
    ".bowl [1-6] - Bowling emoji"
], "🎲 Animated emoji games")

# ANIMATIONS
add_handler("animations", [
    ".muth - Muth animation 🍆",
    ".animate <text> - Typing animation ✍️",
    ".spinner [sec] - Spinner animation 🔄",
    ".love [mention] - Love heart animation ❤️",
    ".hearts <text> - Hearts animation 💖",
    ".countdown <n> - Countdown animation ⏰",
    ".blink <sec> <text> - Blink animation 👁️",
    ".matrix [sec] - Matrix digital rain 💻",
    ".wave <text> - Wave text animation 🌊",
    ".rainbow <text> - Rainbow text animation 🌈",
    ".glitch <text> - Glitch text animation ⚡"
], "🎨 Animations - Sacred text animations")

# TOOLS
add_handler("tools", [
    ".id - Reveal a mortal's ID 🆔",
    ".uptime - Check the God's uptime 🕐",
    ".ping - Test the God's response time 🏓",
    ".clock - Reveal the sacred Indian time 🕐",
    ".rand min max - Random number 🎲",
    ".pick item1,item2 - Pick random item 🎯",
    ".count <text> - Count characters and words 📊",
    ".date - Show current date 📅"
], "🛠️ Tools - Various sacred tools")

# PROTECT
add_handler("protect", [
    ".safe - Place a mortal under God's protection 🛡️",
    ".unsafe - Remove divine protection 🚫",
    ".safelist - List all protected souls 📋",
    ".clearsafe - Remove all divine protections ⚠️"
], "🛡️ Protect - Protect souls from harm")

# CLONE
add_handler("clone", [
    ".clone - Steal a mortal's identity 👥",
    ".revert - Restore your true identity 🔄"
], "👥 Clone - Steal and restore identities")

# ADMIN
add_handler("admin", [
    ".ban - Banish a mortal from your realm 🚫",
    ".unban - Forgive and allow return ✅",
    ".kick - Cast out a mortal 👢",
    ".promote <rank> - Elevate a mortal to rank 👑",
    ".demote - Demote from rank 📉",
    ".pin - Immortalize a message 📌",
    ".unpin - Release from eternity 📌",
    ".pinall - Immortalize ALL messages ⚠️",
    ".unpinall - Release ALL from eternity 🔓",
    ".slowmode <s> - Set cooldown ⏱️",
    ".lock - Seal the realm 🔒",
    ".unlock - Unseal the realm 🔓",
    ".adminonly - Only divine beings may speak 🔐",
    ".adminoff - All mortals may speak 🔓"
], "👑 Admin - Rule your realm with divine authority")

# MODERATION
add_handler("moderation", [
    ".muteall - Silence all non-protected souls 🔇",
    ".unmuteall - Restore voices to all 🔊",
    ".mute - Silence a specific mortal 🤐",
    ".unmute - Restore a mortal's voice 🗣️"
], "🔇 Moderation - Manage chat silence")

# AFK
add_handler("afk", [
    ".afk [reason] - Go into slumber 🌙",
    ".unafk - Awaken from slumber ☀️",
    ".afkstats - View slumber statistics 📊",
    ".afkquote - Random divine quote 💭"
], "🌌 AFK - Away from keyboard management")

# RAID
add_handler("raid", [
    ".raid hindi @user - Hindi raid 🔥",
    ".raid english @user - English raid 🌍",
    ".raid flirthin @user - Flirt Hindi raid 💘",
    ".raid flirteng @user - Flirt English raid 💞",
    ".raid <custom_name> @user - Custom raid 🎭",
    ".crtraid <name> <template> - Create custom raid 📝",
    ".delraid <name> - Delete custom raid 🗑️",
    ".listraids - List all custom raids 📋",
    ".stopraid - Stop all raids in this realm 🛑",
    ".stopraid @user - Stop raid for specific mortal 🛑",
    ".stopraidall - Stop all raids everywhere 🌍",
    ".stopraidall @user - Stop raid for specific mortal globally 🌍",
    ".raidinfo - View active raids 📡",
    ".delayraid <s> - Set raid delay ⏳"
], "⚔️ RAID - Unleash divine wrath with custom raids")

# REPLYRAID
add_handler("replyraid", [
    ".replyraid <type> @user - Auto-reply raid 🧠",
    ".replyraid <custom_name> - Custom reply raid 🎭",
    ".dreplyraid @user - Stop reply raid 🛑"
], "🔄 ReplyRAID - Auto-reply raid attacks")

# SPAM
add_handler("spam", [
    ".spam <msg> - Infinite text spam 💥",
    ".spam (reply to text) - Spam replied text 💥",
    ".stopspam - Stop text spam 🛑",
    ".setspamdelay <s> - Set spam delay ⏱️",
    ".stopallspam - Stop ALL spam 🛑",
    ".dspam [count] [delay] [message] - Spam with custom delay",
    ".mspam [count] [reply to media] - Spam media/files multiple times",
    ".listspam - Show all active spam operations",
    ".spamstats - Show spam engine statistics"
], "📢 SPAM - Unleash divine spam with advanced features")

# PM ASSISTANT
add_handler("pm_assistant", [
    ".approve - Bless a mortal in PM ✅ (reply to their message)",
    ".disapprove - Revoke blessing from mortal ❌ (reply to their message)",
    ".listapproved - List all blessed souls 📋",
    ".block - Banish a mortal from PM 🚫",
    ".setpmedia - Set permit media 🖼️ (any media: photo, video, GIF, document)",
    ".tpmedia - Toggle permit media 🔄",
    ".pmp on/off - Toggle global PM permit protection 🛡️",
    ".pmpstatus - Check PM permit status",
    ".pmdel - Enable PM deletion 🧹",
    ".pmdeloff - Disable PM deletion ✅"
], "🔧 PM Assistant - Manage personal messages")

# SETUP
add_handler("setup", [
    ".setupbot - Auto-enable inline mode 🚀"
], "⚙️ Setup - Auto-configure your bot")

# EXTRA
add_handler("extra", [
    ".leave - Depart from this realm 🚪",
    ".delete - Delete replied message 🗑️",
    ".deleteall - Delete all your messages 🗑️",
    ".users - List users in chat 👥"
], "✨ Extra - Additional commands")

# BAIT
add_handler("bait", [
    ".typing on/off - Infinite typing status",
    ".recording on/off - Infinite recording voice note status",
    ".gaming on/off - Infinite playing game status",
    ".video on/off - Infinite recording video status",
    ".round on/off - Infinite recording round video status",
    ".photo on/off - Infinite sending photo status",
    ".document on/off - Infinite sending file status",
    ".sticker on/off - Infinite choosing sticker status",
    ".location on/off - Infinite picking location status",
    ".contact on/off - Infinite choosing contact status",
    ".<action> on <seconds> - Timed bait, auto-stops",
    ".baitlist - List all active baits in all chats",
    ".baitstop - Stop all baits in the current chat",
    ".baitstopall - PANIC: stop every bait in every chat"
], "🎣 Bait - Infinite chat actions for psychological trolling")

# FLASHVAULT
add_handler("flashvault", [
    ".flash on/off - Turn Auto-Save ON/OFF globally for all incoming View-Once media",
    ".flashchat on/off - Turn Auto-Save ON/OFF for the current chat only",
    ".flashlist - View your active FlashVault monitoring settings",
    ".saveflash - Reply to ANY media to manually save it to your Log Group",
    ".setlog <chat_id> - Set your Log Group for saving media"
], "📸 FlashVault - Anti-View-Once media saver")

# GHOSTVAULT
add_handler("ghostvault", [
    ".vault on/off - Turn Ghost Vault ON or OFF globally for ALL chats",
    ".vaultchat on/off - Turn Ghost Vault ON or OFF for the CURRENT chat",
    ".vaultlist - View all explicitly monitored chats"
], "🕵️ GhostVault - Anti-Delete & Edit tracker")

# GLOBALTOOLS
add_handler("globaltools", [
    ".gban <reply/username> - Ban user globally in all groups",
    ".ungban <reply/username> - Unban user globally",
    ".gmute <reply/username> - Mute user globally",
    ".ungmute <reply/username> - Unmute user globally",
    ".gkick <reply/username> - Kick user from all groups",
    ".gpromote <reply/username> - Promote user in all admin chats",
    ".gdemote <reply/username> - Demote user in all admin chats",
    ".listgban - List all gbanned users",
    ".gstat <reply/username> - Check if user is gbanned"
], "🌍 GlobalTools - Global moderation across all groups")

# TAGGER
add_handler("tagger", [
    ".btag <msg> - Bulk tag (5 users/msg) with custom message",
    ".utag <msg> - Tag every member individually with message",
    ".btaggm - Bulk tag all users with Good Morning",
    ".utaggm - Tag all users individually with Good Morning",
    ".btaggn - Bulk tag all users with Good Night",
    ".utaggn - Tag all users individually with Good Night",
    ".btagvc - Bulk tag all users to join Voice Chat",
    ".utagvc - Tag all users individually to join Voice Chat",
    ".canceltag - Stop any ongoing tagging process in the current chat"
], "🏷️ Tagger - Advanced group tagging with anti-ban protection")

# PURGE
add_handler("purge", [
    ".purge — Delete all messages from replied message to current (DM/Group)",
    ".p — Alias for .purge",
    ".delall — Delete all messages (optionally for a specific user) with 20s delay",
    ".cancel — Cancel a pending .delall operation"
], "🧹 Purge - Message deletion tool")

# SUDO
add_handler("sudo", [
    ".sudo <reply|id> - Add a sudo user",
    ".addsudo <reply|id> - Add a sudo user",
    ".delsudo <reply|id> - Remove a sudo user",
    ".listsudo - List sudo users"
], "🔑 Sudo - Super user management")

# CHATS
add_handler("chats", [
    ".delchat - Delete/leave current chat",
    ".getlink - Get chat invite link",
    ".create <group/channel> <name> - Create new group/channel",
    ".setgpic <reply> - Set group photo",
    ".setgname <name> - Set group name"
], "📁 Chats - Chat management")

# ==================== CUSTOM RAID MANAGER ====================

class CustomRaidManager:
    def __init__(self):
        self.raids = {}
        self._load()
    
    def _load(self):
        try:
            if CUSTOM_RAIDS_FILE.exists():
                with open(CUSTOM_RAIDS_FILE, 'r') as f:
                    self.raids = json.load(f)
        except:
            self.raids = {}
    
    def _save(self):
        try:
            with open(CUSTOM_RAIDS_FILE, 'w') as f:
                json.dump(self.raids, f, indent=2)
        except Exception as e:
            print(f"Error saving custom raids: {e}")
    
    def parse_template(self, template: str) -> dict:
        word_arrays = {
            "love": LOVE_WORDS,
            "fuck": FUCK_WORDS,
            "bully": BULLY_WORDS,
            "chud": CHUD_WORDS,
            "lun": LUN_WORDS
        }
        
        if '|' in template:
            messages = [msg.strip() for msg in template.split('|') if msg.strip()]
            is_multi = True
        else:
            messages = [template]
            is_multi = False
        
        all_arrays = set()
        for msg in messages:
            pattern = r'\{([^}]+)\}'
            matches = re.findall(pattern, msg)
            for match in matches:
                if match in word_arrays:
                    all_arrays.add(match)
        
        return {
            "template": template,
            "messages": messages,
            "is_multi": is_multi,
            "arrays_used": list(all_arrays)
        }
    
    def generate_message(self, template: str, target_name: str, self_name: str, emoji: str, msg_index: int = 0):
        word_arrays = {
            "love": LOVE_WORDS,
            "fuck": FUCK_WORDS,
            "bully": BULLY_WORDS,
            "chud": CHUD_WORDS,
            "lun": LUN_WORDS
        }
        
        raid_data = self.raids.get(template.lower(), {})
        messages = raid_data.get("messages", [template])
        is_multi = raid_data.get("is_multi", False)
        
        if is_multi and messages:
            msg_template = messages[msg_index % len(messages)]
        else:
            msg_template = template
        
        result = msg_template
        
        if "{target}" in result:
            result = result.replace("{target}", target_name)
        if "{self}" in result:
            result = result.replace("{self}", self_name)
        if "{emoji}" in result:
            result = result.replace("{emoji}", emoji)
        
        for array_name, words in word_arrays.items():
            placeholder = f"{{{array_name}}}"
            if placeholder in result:
                random_word = random.choice(words)
                result = result.replace(placeholder, random_word)
        
        return result
    
    def create_raid(self, name: str, template: str):
        name = name.lower().strip()
        if not name:
            return False, "Raid name cannot be empty!"
        if name in self.raids:
            return False, f"Raid '{name}' already exists!"
        if not template or not template.strip():
            return False, "Template cannot be empty!"
        
        parsed = self.parse_template(template)
        self.raids[name] = {
            "template": template,
            "messages": parsed["messages"],
            "is_multi": parsed["is_multi"],
            "arrays_used": parsed["arrays_used"],
            "created": datetime.now().isoformat()
        }
        self._save()
        return True, f"✅ Raid '{name}' created!"
    
    def delete_raid(self, name: str):
        name = name.lower().strip()
        if name not in self.raids:
            return False, f"Raid '{name}' not found!"
        del self.raids[name]
        self._save()
        return True, f"✅ Raid '{name}' deleted!"
    
    def get_raid(self, name: str):
        name = name.lower().strip()
        return self.raids.get(name)
    
    def list_raids(self):
        if not self.raids:
            return "📭 **No custom raids created yet!**"
        msg = "🎭 **Custom Raids**\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
        for name, data in self.raids.items():
            msg += f"🔹 **{name.title()}**\n"
            msg += f"   📝 Messages: {len(data['messages'])}\n"
            msg += f"   🔄 Rotation: {'✅' if data['is_multi'] else '❌'}\n\n"
        return msg

custom_raid_manager = CustomRaidManager()

# ==================== COOL THEME STYLES ====================

AFK_QUOTES = [
    "⚡ I am away, but my power remains. Be back soon!",
    "🌩️ The God is temporarily offline. Feel free to leave a message!",
    "🔥 Away from keyboard, but still watching over you.",
    "💫 In the void between worlds. Back shortly!",
    "⚡ Even Gods need rest. I'll return soon!",
    "🌙 The night calls me. Be back at dawn!",
    "👁️ I see everything, even when I'm away.",
]

# ==================== DEFAULT RAID MESSAGES ====================

HINDI_RAID = [
    "{emoji} 💀 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐇ᴀᴛʜɪ 𝐆ʜᴜꜱ 𝐆ᴀʏᴇ 💀 {emoji}",
    "{emoji} 🍆 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐋ᴜɴᴅ 𝐂ʜᴀᴛ 𝐑ᴀʜɪ 𝐑ᴏᴢ 🍆 {emoji}",
    "{emoji} 👺 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐏ᴜʀᴀ 𝐆ᴀᴏɴ 𝐁ᴀꜱᴛᴀ 𝐇ᴀɪ 👺 {emoji}",
    "{emoji} 🖕 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐊ᴀ 𝐁ʜᴀʀᴏꜱᴀ 𝐍ʜɪ 🖕 {emoji}",
    "{emoji} 🔞 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐓ʀᴀɪɴ 𝐂ʜᴀʟᴛɪ 𝐇ᴀɪ 🔞 {emoji}",
    "{emoji} 💩 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐀ɴᴅʜᴇʀᴀ 𝐇ᴀɪ 💩 {emoji}",
    "{emoji} 🗑️ 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐒ᴀᴅᴀᴋ 𝐌ᴇ 𝐂ʜᴜᴅᴛɪ 𝐇ᴀɪ 🗑️ {emoji}",
    "{emoji} 🤡 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐇ᴀɪ 𝐑ᴀɴᴅ𝐈 𝐊ɪ 𝐑ᴀᴀɴɪ 🤡 {emoji}",
    "{emoji} 🚮 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐏ᴜʀɪ 𝐍ᴀᴅɪ 𝐁ʜᴀʀ 𝐉ᴀʏᴇ 🚮 {emoji}",
    "{emoji} 🧠 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐍ᴇ 𝐋ᴜɴᴅ 𝐊ʜᴀʏᴀ 𝐍ᴀꜱʜᴛᴇ 𝐌ᴇ 🧠 {emoji}",
    "{emoji} 💀 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐃ᴜʙᴋɪ 𝐋ɢᴀᴜɴɢᴀ💀 {emoji}",
    "{emoji} 🍑 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐀ʙ 𝐀ᴜʀ 𝐁ᴀᴅɪ 𝐇ᴏɢʏɪ 🍑 {emoji}",
    "{emoji} 👅 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐂ʜᴀᴛᴛɪ 𝐇ᴀɪ 𝙂ꪮ꠹'ꪮ 𝐊ᴀ 𝐋ᴜɴᴅ 👅 {emoji}",
    "{emoji} 🔥 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐀ᴀɢ 𝐋ɢɪ 🔥 {emoji}",
    "{emoji} 🦴 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐍ᴇ 𝐒ᴀʙ 𝐊ᴀ 𝐋ᴜɴᴅ 𝐂ʜᴜsᴀ 𝐇ᴀɪ 🦴 {emoji}",
    "{emoji} 🧟 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐇ᴀɪ 𝐆ᴀᴏɴ 𝐊ɪ 𝐑ᴀɴᴅ 🧟 {emoji}",
    "{emoji} 🎯 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐋ᴜɴᴅ 𝐊ᴀ 𝐍ɪꜱʜᴀɴᴀ 🎯 {emoji}",
    "{emoji} 🚽 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐇ᴀɪ 𝐏ᴜʙʟɪᴄ 𝐓ᴏɪʟᴇᴛ 🚽 {emoji}",
    "{emoji} 🪦 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐊ᴏ 𝐃ᴀғɴᴀ 𝐃ɪʏᴀ 🪦 {emoji}",
    "{emoji} 🐷 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ʜᴀᴛɪ 𝐇ᴀɪ 𝐒ᴜᴠᴀʀ 𝐖ᴀʟɪ 𝐂ʜᴜᴅᴀɪ 🐷 {emoji}",
    "{emoji} 🍆 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ᴏ 𝐂ʜᴀʜɪʏᴇ 𝟸𝟺 𝐆ʜᴀɴᴛᴇ 𝐋ᴜɴᴅ 🍆 {emoji}",
    "{emoji} 💀 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐁ʜᴏᴏᴛ 𝐑ᴇʜᴛᴇ 💀 {emoji}",
    "{emoji} 🔞 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐊ᴀʟɪ 🔞 {emoji}",
    "{emoji} 🖕 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐍ᴇ 𝐊ʜᴀʏᴇ 𝐇ᴀɪ 𝐁ᴏʜᴏᴛ 𝐒ᴀᴀʀᴇ 𝐋ᴜɴᴅ 🖕 {emoji}",
    "{emoji} 🗑️ 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐊ᴏ 𝐅ᴇɴᴋ 𝐃ᴜ 𝐃ᴜsᴛʙɪɴ 𝐌ᴇ🗑️ {emoji}",
    "{emoji} 🧠 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐏ᴇᴇᴛɪ 𝐇ᴀɪ 𝐋ᴜɴᴅ 𝐊ɪ 𝐏ᴀᴀɴɪ 🧠 {emoji}",
    "{emoji} 👺 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐊ᴜᴛᴛᴇ 𝐊ᴀ 𝐋ᴜɴᴅ 👺 {emoji}",
    "{emoji} 💩 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐒ᴇ 𝐁ᴀᴅʙᴜ 𝐀ᴀᴛɪ 𝐇ᴀɪ 💩 {emoji}",
    "{emoji} 🍑 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐇ᴀɪ 𝟷𝟶𝟶 𝐒ᴀᴀʟ 𝐏ᴜʀᴀɴɪ 🍑 {emoji}",
    "{emoji} 🚮 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐇ᴀɪ 𝐒ᴇx 𝐌ᴀᴄʜɪɴᴇ 🚮 {emoji}",
    "{emoji} 🎯 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐍ɪꜱʜᴀɴᴀ 𝐋ᴜɴᴅ 𝐊ᴀ 🎯 {emoji}",
    "{emoji} 🔥 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐍ᴇ 𝐊ʜᴀʏᴀ 𝐇ᴀɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐓ʜᴀᴘᴘᴀᴅ 🔥 {emoji}",
    "{emoji} 🦴 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐍ᴇ 𝐊ʜᴀʏɪ 𝐇ᴀɪ 𝐂ʜᴜᴅᴀɪ 🦴 {emoji}",
    "{emoji} 💀 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐃ʜᴀʀᴛɪ 𝐃ɪᴋʜᴛɪ 💀 {emoji}",
    "{emoji} 🍆 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐂ʜᴀᴛᴛɪ 𝐇ᴀɪ 𝐇ᴀʀ 𝐋ᴜɴᴅ 🍆 {emoji}",
    "{emoji} 🧟 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐙ᴏᴍʙɪ𝐄 🧟 {emoji}",
    "{emoji} 🖕 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐍ᴇ 𝐊ʜᴀʏᴀ 𝐇ᴀɪ 𝐋ᴜɴᴅ 𝐊ᴀ 𝐇ᴀᴍʟᴀ 🖕 {emoji}",
    "{emoji} 🐷 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐒ᴜᴠᴀʀ 𝐊ᴀ 𝐋ᴜɴᴅ  🐷 {emoji}",
    "{emoji} 🤡 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐇ᴀɪ 𝐂ʜᴜᴅᴀɪ 𝐊ʜᴀɴᴇ 𝐊ɪ 𝐌ᴀᴄʜɪɴᴇ 🤡 {emoji}",
    "{emoji} 🍑 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐇ᴀɪ 𝐁ʟᴀᴄᴋ 𝐇ᴏʟᴇ 🍑 {emoji}",
    "{emoji} 💀 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐓ᴏᴏғᴀɴ 𝐀ᴀʏᴀ 💀 {emoji}",
    "{emoji} 🍆 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ᴏ 𝐂ʜᴏᴅɴᴇ 𝐀ᴀʏᴇ 𝐂ʀᴏʀᴏɴ 𝐀ᴅᴍɪ 🍆 {emoji}",
    "{emoji} 👺 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐁ɪᴍᴀʀɪ 𝐅ᴀɪʟɪ 👺 {emoji}",
    "{emoji} 🖕 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐊ᴏ 𝐊ᴏɪ 𝐁ᴀɴᴅ 𝐍ᴀʜɪ 𝐊ʀ sᴀᴋᴛᴀ 🖕 {emoji}",
    "{emoji} 🔥 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐍ᴇ 𝐂ʜᴜᴛ 𝐒ᴇ 𝐇ᴀᴛʜɪ 𝐍ɪᴋᴀʟᴀ 🔥 {emoji}",
    "{emoji} 🗑️ 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐊ᴀʀᴛɪ 𝐇ᴀɪ 𝐓ʀᴀꜱʜ 𝐊ɪ 𝐒ᴀғᴀɪ 🗑️ {emoji}",
    "{emoji} 👅 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ᴇ 𝐁ɪᴏ 𝐃ᴀᴛᴀ 𝐌ᴇ 𝐋ɪᴋʜᴀ 𝐇ᴀɪ - '𝐀ʟᴡᴀʏꜱ 𝐀ᴠᴀɪʟᴀʙʟᴇ 𝐅ᴏʀ 𝐂ʜᴜᴅᴀɪ' 👅 {emoji}",
    "{emoji} 🎯 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐇ᴀʀ 𝐊ᴏɪ 𝐋ᴜɴᴅ 𝐃ᴀʟᴛᴀ 🎯 {emoji}",
    "{emoji} 💀 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐊ᴀ 𝐍ᴀᴍ 𝐇ᴀɪ '𝐖ᴇʟᴄᴏᴍᴇ' 💀 {emoji}",
    "{emoji} 🧟 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐋ᴜɴᴅ 𝐅ʟᴏᴀᴛ 𝐊ᴀʀᴛᴇ 🧟 {emoji}"
]

ENGLISH_RAID = [
    "{emoji} 💀 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ'ꜱ 𝐏ᴜꜱꜱʏ 𝐈ꜱ 𝐖ɪᴅᴇ𝐑 𝐓ʜᴀɴ 𝐀 𝐂ᴀᴠ𝐄 💀 {emoji}",
    "{emoji} 🍆 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ 𝐒ᴜᴄᴋꜱ 𝐃ɪᴄᴋ 𝐋ɪᴋᴇ 𝐀 𝐕ᴀᴄᴜᴜᴍ 𝐂ʟᴇᴀɴᴇʀ 🍆 {emoji}",
    "{emoji} 👺 𝐘ᴏᴜ'ʀᴇ 𝐀 𝐖ʜᴏʀᴇ'ꜱ 𝐁ʀᴀᴛ 𝐖ʜᴏ 𝐂ʀᴀᴠᴇꜱ 𝐃ɪᴄᴋ 𝟸𝟺/𝟽 👺 {emoji}",
    "{emoji} 🖕 𝐘ᴏᴜʀ 𝐒ʟᴜᴛ 𝐎ꜰ 𝐀 𝐌ᴏᴛʜᴇʀ 𝐆ᴇᴛꜱ 𝐅ᴜᴄᴋᴇᴅ 𝐃ᴀɪʟʏ 🖕 {emoji}",
    "{emoji} 🔞 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ'ꜱ 𝐏ᴜꜱꜱʏ 𝐇ᴀꜱ 𝐌ᴏʀ𝐄 𝐌ɪʟᴇꜱ 𝐓ʜᴀɴ 𝐀 𝐓ᴀxɪ 🔞 {emoji}",
    "{emoji} 💩 𝐘ᴏᴜʀ 𝐖ʜᴏʀ𝐄 𝐅ᴀᴄ𝐄 𝐂ᴏᴜʟᴅ 𝐌ᴀᴋᴇ 𝐀 𝐃ɪᴄᴋ 𝐆ᴏ 𝐅ʟᴀᴄᴄɪᴅ 💩 {emoji}",
    "{emoji} 🗑️ 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ'ꜱ 𝐏ᴜꜱꜱʏ 𝐒ᴍᴇʟʟꜱ 𝐋ɪᴋᴇ 𝐑ᴏᴛᴛᴇɴ 𝐅ɪꜱʜ 🗑️ {emoji}",
    "{emoji} 🤡 𝐘ᴏᴜ'ʀᴇ 𝐀 𝐏ʀᴏꜱᴛɪᴛᴜᴛᴇ'ꜱ 𝐒ᴏɴ 𝐖ʜᴏ 𝐋ɪᴄᴋꜱ 𝐃ɪᴄᴋ 𝐅ᴏʀ 𝐅ʀᴇᴇ 🤡 {emoji}",
    "{emoji} 🚮 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ'ꜱ 𝐏ᴜꜱꜱʏ 𝐈ꜱ 𝐀 𝐏ᴜʙʟɪ𝐂 𝐓ᴏɪʟᴇ𝐓 𝐅ᴏʀ 𝐃ɪᴄᴋꜱ 🚮 {emoji}",
    "{emoji} 🧠 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇ𝐑 𝐋ɪᴄᴋꜱ 𝐂ᴜɴᴛ 𝐀ɴᴅ 𝐒ᴡᴀʟʟᴏᴡꜱ 𝐂ᴜᴍ 🧠 {emoji}",
    "{emoji} 💀 𝐘ᴏᴜʀ 𝐂ᴜɴᴛ 𝐅ᴀᴄ𝐄 𝐖ᴀꜱ 𝐁ᴏʀɴ 𝐅ʀᴏᴍ 𝐀 𝐖ʜᴏʀᴇ'ꜱ 𝐏ᴜꜱꜱʏ 💀 {emoji}",
    "{emoji} 🍑 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ'ꜱ 𝐏ᴜꜱꜱʏ 𝐈ꜱ 𝐋ᴏᴏꜱ𝐄 𝐄ɴᴏᴜɢʜ 𝐅ᴏʀ 𝐀 𝐅ɪʀᴇ 𝐇ᴏꜱᴇ 🍑 {emoji}",
    "{emoji} 👅 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ 𝐓ᴀᴋᴇꜱ 𝐃ɪᴄᴋ 𝐈ɴ 𝐄ᴠᴇʀʏ 𝐇ᴏʟᴇ 👅 {emoji}",
    "{emoji} 🔥 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ 𝐆ᴇᴛꜱ 𝐅ᴜᴄᴋᴇᴅ 𝐁ʏ 𝐓ʜᴇ 𝐖ʜᴏʟ𝐄 𝐍ᴇɪɢʜʙᴏʀʜᴏᴏᴅ 🔥 {emoji}",
    "{emoji} 🦴 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ'ꜱ 𝐏ᴜꜱꜱʏ 𝐍ᴇᴇᴅꜱ 𝐀 𝐂ʜᴀꜱᴛɪᴛʏ 𝐁ᴇʟᴛ 🦴 {emoji}",
    "{emoji} 🧟 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ 𝐈ꜱ 𝐓ʜᴇ 𝐓ᴏᴡɴ'ꜱ 𝐏ᴜʙʟɪᴄ 𝐖ʜᴏʀᴇ 🧟 {emoji}",
    "{emoji} 🎯 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ'ꜱ 𝐏ᴜꜱꜱʏ 𝐈ꜱ 𝐀 𝐃ᴜᴍᴘꜱᴛᴇʀ 𝐅ᴏʀ 𝐃ɪᴄᴋ 🎯 {emoji}",
    "{emoji} 🚽 𝐘ᴏᴜ'ʀᴇ 𝐀 𝐖ᴀʟᴋɪɴɢ 𝐏ɪᴇᴄᴇ 𝐎ꜰ 𝐒ʜɪᴛ 𝐅ʀᴏᴍ 𝐀 𝐖ʜᴏʀᴇ'ꜱ 𝐂ᴜɴᴛ 🚽 {emoji}",
    "{emoji} 🪦 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ'ꜱ 𝐏ᴜꜱꜱʏ 𝐒ʜᴏᴜʟᴅ 𝐁ᴇ 𝐁ᴜʀɪᴇᴅ 🪦 {emoji}",
    "{emoji} 🐷 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ 𝐅ᴜᴄᴋꜱ 𝐋ɪᴋᴇ 𝐀 𝐏ɪɢ 🐷 {emoji}",
    "{emoji} 🍆 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ 𝐂ʀᴀᴠᴇꜱ 𝐃ɪᴄᴋ 𝐌ᴏʀᴇ 𝐓ʜᴀɴ 𝐅ᴏᴏᴅ 🍆 {emoji}",
    "{emoji} 💀 𝐘ᴏᴜʀ 𝐖ʜᴏʀ𝐄 𝐌ᴏᴛʜᴇʀ 𝐍ᴇᴇᴅꜱ 𝐀 𝐌ᴜᴢᴢʟᴇ 💀 {emoji}",
    "{emoji} 🔞 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ'ꜱ 𝐏ᴜꜱꜱʏ 𝐈ꜱ 𝐀 𝐁ʟᴀᴄᴋ 𝐇ᴏʟᴇ 𝐅ᴏʀ 𝐃ɪᴄᴋ 🔞 {emoji}",
    "{emoji} 🖕 𝐘ᴏᴜ'ʀᴇ 𝐀 𝐅ᴜᴄᴋɪɴɢ 𝐃ɪꜱɢʀᴀᴄ𝐄 𝐓ᴏ 𝐘ᴏᴜʀ 𝐖ʜᴏʀ𝐄 𝐌ᴏᴛʜᴇʀ 🖕 {emoji}",
    "{emoji} 🗑️ 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ'ꜱ 𝐏ᴜꜱꜱʏ 𝐒ʜᴏᴜʟᴅ 𝐁ᴇ 𝐓ʜʀᴏᴡɴ 𝐈ɴ 𝐓ʀᴀꜱʜ 🗑️ {emoji}",
    "{emoji} 🧠 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ 𝐒ᴡᴀʟʟᴏᴡꜱ 𝐂ᴜᴍ 𝐅ᴏʀ 𝐁ʀᴇᴀᴋꜰᴀꜱᴛ 🧠 {emoji}",
    "{emoji} 👺 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ 𝐆ᴇᴛꜱ 𝐅ᴜᴄᴋᴇᴅ 𝐁ʏ 𝐃ᴏɢꜱ 👺 {emoji}",
    "{emoji} 💩 𝐘ᴏᴜ'ʀᴇ 𝐓ʜ𝐄 𝐑ᴇᴀꜱᴏɴ 𝐖ʜʏ 𝐂ᴏɴᴅᴏᴍꜱ 𝐖ᴇʀ𝐄 𝐈ɴᴠᴇɴᴛᴇᴅ 💩 {emoji}",
    "{emoji} 🍑 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ'ꜱ 𝐏ᴜꜱꜱʏ 𝐇ᴀꜱ 𝐀 𝐋ɪꜰ𝐄𝐓ɪᴍ𝐄 𝐖ᴀʀʀᴀɴᴛʏ 🍑 {emoji}",
    "{emoji} 🚮 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ 𝐈ꜱ 𝐀 𝐖ᴀʟᴋɪɴɢ 𝐒ᴇx 𝐃ᴏʟʟ 🚮 {emoji}",
    "{emoji} 🎯 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ'ꜱ 𝐏ᴜꜱꜱʏ 𝐈ꜱ 𝐀 𝐏ᴀʀᴋɪɴɢ 𝐋ᴏᴛ 𝐅ᴏʀ 𝐃ɪᴄᴋ 🎯 {emoji}",
    "{emoji} 🔥 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ 𝐃ʀɪɴᴋꜱ 𝐂ᴜᴍ 𝐋ɪᴋᴇ 𝐖ᴀᴛᴇʀ 🔥 {emoji}",
    "{emoji} 🦴 𝐘ᴏᴜʀ 𝐖ʜᴏʀ𝐄 𝐌ᴏᴛʜᴇʀ 𝐍ᴇᴇᴅꜱ 𝐀 𝐋ᴇᴀꜱʜ 🦴 {emoji}",
    "{emoji} 💀 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ'ꜱ 𝐂ᴜɴᴛ 𝐈ꜱ 𝐀 𝐓ᴏᴜʀɪꜱᴛ 𝐀ᴛᴛʀᴀᴄᴛɪᴏɴ 💀 {emoji}",
    "{emoji} 🍆 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ 𝐓ᴀᴋᴇꜱ 𝐃ɪᴄᴋ 𝐅ʀᴏᴍ 𝐄ᴠᴇʀʏᴏɴᴇ 🍆 {emoji}",
    "{emoji} 🧟 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ'ꜱ 𝐏ᴜꜱꜱʏ 𝐈ꜱ 𝐀 𝐙ᴏᴍʙɪ𝐄 𝐇ᴏʟᴇ 🧟 {emoji}",
    "{emoji} 🖕 𝐘ᴏᴜ'ʀᴇ 𝐓ʜ𝐄 𝐖ᴏʀꜱᴛ 𝐌ɪꜱᴛᴀᴋ𝐄 𝐎ꜰ 𝐀 𝐖ʜᴏʀ𝐄 🖕 {emoji}",
    "{emoji} 🐷 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ'ꜱ 𝐏ᴜꜱꜱʏ 𝐒ᴍᴇʟʟꜱ 𝐋ɪᴋᴇ 𝐀 𝐏ɪɢꜱᴛʏ 🐷 {emoji}",
    "{emoji} 🤡 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ 𝐈ꜱ 𝐀 𝐂ʟᴏᴡɴ'ꜱ 𝐖ʜᴏʀ𝐄 🤡 {emoji}",
    "{emoji} 🚽 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ'ꜱ 𝐏ᴜꜱꜱʏ 𝐍ᴇᴇᴅꜱ 𝐀 𝐏ʟᴜɴɢᴇʀ 🚽 {emoji}",
    "{emoji} 💩 𝐘ᴏᴜʀ 𝐖ʜᴏʀ𝐄 𝐌ᴏᴛʜᴇʀ 𝐒ʜᴏᴜʟᴅ 𝐁ᴇ 𝐒ᴛᴇʀɪʟɪᴢᴇᴅ 💩 {emoji}",
    "{emoji} 🍑 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ'ꜱ 𝐏ᴜꜱꜱʏ 𝐇ᴀꜱ 𝐍ᴏ 𝐁ᴏᴜɴᴅᴀʀɪᴇꜱ 🍑 {emoji}",
    "{emoji} 🔞 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ 𝐒ᴜᴄᴋꜱ 𝐃ɪᴄᴋ 𝐎ɴ 𝐓ʜᴇ 𝐂ᴏʀɴᴇʀ 🔞 {emoji}",
    "{emoji} 🗑️ 𝐘ᴏᴜ'ʀᴇ 𝐀 𝐁ʏᴘʀᴏᴅᴜᴄᴛ 𝐎ꜰ 𝐀 𝐏ᴜʙʟɪᴄ 𝐖ʜᴏʀ𝐄 🗑️ {emoji}",
    "{emoji} 👅 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ 𝐋ɪᴄᴋꜱ 𝐃ɪᴄᴋ 𝐅ᴏʀ 𝐏ᴇɴɴɪᴇꜱ 👅 {emoji}",
    "{emoji} 🎯 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ'ꜱ 𝐏ᴜꜱꜱʏ 𝐈ꜱ 𝐀 𝐓ᴀʀɢᴇ𝐓 𝐅ᴏʀ 𝐄ᴠᴇʀʏ 𝐃ɪᴄᴋ 🎯 {emoji}",
    "{emoji} 💀 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ'ꜱ 𝐂ᴜɴᴛ 𝐍ᴇᴇᴅꜱ 𝐀 𝐑ᴇꜱᴛʀᴀɪɴᴛ 💀 {emoji}",
    "{emoji} 🧟 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ'ꜱ 𝐏ᴜꜱꜱʏ 𝐈ꜱ 𝐀 𝐆ʀᴀᴠ𝐄 𝐅ᴏʀ 𝐃ɪᴄᴋ 🧟 {emoji}",
    "{emoji} 🔥 𝐘ᴏᴜʀ 𝐖ʜᴏʀ𝐄 𝐌ᴏᴛʜᴇʀ 𝐁ᴜʀɴꜱ 𝐈ɴ 𝐇ᴇʟʟ 🔥 {emoji}",
    "{emoji} 🚮 𝐘ᴏᴜʀ 𝐌ᴏᴛʜᴇʀ'ꜱ 𝐏ᴜꜱꜱʏ 𝐒ʜᴏᴜʟ𝐃 𝐁ᴇ 𝐂ʟᴏꜱᴇ𝐃 🚮 {emoji}"
]

FLIRTHIN_RAID = [
    "{emoji} 🦋 𝐌ᴇʀɪ 𝐃ᴜɴɪʏᴀ 𝐓ᴜᴍ 𝐒ᴇ 𝐒ʜᴜʀᴜ 𝐓ᴜᴍ 𝐏ᴇ 𝐊ᴀᴛʜᴀᴍ 💘 🎀 {emoji}",
    "{emoji} 🌸 𝐓ᴜᴍʜᴀʀɪ 𝐀ᴀɴᴋʜᴏɴ 𝐌ᴇ 𝐁ᴀꜱᴛᴇ 𝐇ᴀɪ 𝐌ᴇʀɪ 𝐏ᴜʀɪ 𝐃ᴜɴɪʏᴀ 🌸 {emoji}",
    "{emoji} 💕 𝐓ᴜᴍ 𝐌ᴇʀᴇ 𝐋ɪʏᴇ 𝐊ʜᴡᴀʙ 𝐒ᴇ 𝐁ʜɪ 𝐇ᴀꜱɪɴ 𝐇ᴏ 💕 {emoji}",
    "{emoji} 🌹 𝐓ᴜᴍʜᴀʀɪ 𝐌ᴜꜱᴋᴀɴ 𝐌ᴇʀᴀ 𝐃ɪɴ 𝐁ᴀɴᴀᴛɪ 𝐇ᴀɪ 🌹 {emoji}",
    "{emoji} 💖 𝐓ᴜᴍ 𝐌ᴇʀᴇ 𝐃ɪʟ 𝐊ɪ 𝐃ʜᴀᴅᴋᴀɴ 𝐇ᴏ 💖 {emoji}",
    "{emoji} 🎀 𝐓ᴜᴍʜᴀʀɪ 𝐄ᴋ 𝐉ʜᴀʟᴀᴋ 𝐌ᴇʀɪ 𝐒ᴀᴀʀɪ 𝐓ʜᴀᴋᴀɴ 𝐃ᴏᴏʀ 𝐊ᴀʀᴅᴇᴛɪ 𝐇ᴀɪ 🎀 {emoji}",
    "{emoji} ✨ 𝐓ᴜᴍ 𝐌ᴇʀᴇ 𝐉ᴀʜᴀɴ 𝐊ᴀ 𝐒ᴀʙꜱᴇ 𝐊ʜᴜʙꜱᴜʀᴀᴛ 𝐒ɪᴛᴀʀᴀ 𝐇ᴏ ✨ {emoji}",
    "{emoji} 💗 𝐓ᴜᴍʜᴀʀɪ 𝐁ᴀᴀᴛᴇɪɴ 𝐌ᴇʀɪ 𝐑ᴜʜ 𝐊ᴏ 𝐒ᴜᴋᴏᴏɴ 𝐃ᴇᴛɪ 𝐇ᴀɪ 💗 {emoji}",
    "{emoji} 🌺 𝐓ᴜᴍ 𝐌ᴇʀɪ 𝐉ɪɴᴅᴀɢɪ 𝐊ɪ 𝐒ᴀʙꜱᴇ 𝐊ʜᴜʙꜱᴜʀᴀᴛ 𝐂ʜᴀᴘᴛᴇʀ 𝐇ᴏ 🌺 {emoji}",
    "{emoji} 💘 𝐓ᴜᴍʜᴀʀᴇ 𝐁ɪɴᴀ 𝐀ᴅʜᴜʀɪ 𝐇ᴀɪ 𝐌ᴇʀɪ 𝐇ᴀʀ 𝐊ᴀʜᴀɴɪ 💘 {emoji}",
    "{emoji} 🌙 𝐓ᴜᴍ 𝐂ʜᴀɴᴅ 𝐇ᴏ 𝐀ᴜʀ 𝐌ᴀɪɴ 𝐒ɪᴛᴀʀᴀ - 𝐓ᴜᴍʜᴀʀᴇ 𝐁ɪɴᴀ 𝐀ᴅʜᴜʀᴀ 🌙 {emoji}",
    "{emoji} 💫 𝐓ᴜᴍʜᴀʀɪ 𝐇ᴀꜱɪ 𝐌ᴇʀɪ 𝐃ᴜɴɪʏᴀ 𝐊ᴏ 𝐑ᴏꜱʜᴀɴ 𝐊ᴀʀᴅᴇᴛɪ 𝐇ᴀɪ 💫 {emoji}",
    "{emoji} 🌷 𝐓ᴜᴍ 𝐌ᴇʀᴇ 𝐃ɪʟ 𝐌ᴇ 𝐁ᴀꜱᴛᴇ 𝐇ᴏ 𝐉ᴀɪꜱᴇ 𝐊ᴏɪ 𝐊ʜᴜʙꜱᴜʀᴀᴛ 𝐊ʜᴡᴀʙ 🌷 {emoji}",
    "{emoji} 💝 𝐓ᴜᴍʜᴀʀɪ 𝐁ᴀᴀᴛᴇɪɴ 𝐌ᴇʀɪ 𝐅ᴀꜱʟᴏɴ 𝐊ᴏ 𝐁ʜɪ 𝐇ᴀʀᴀ 𝐊ᴀʀᴅᴇᴛɪ 𝐇ᴀɪ 💝 {emoji}",
    "{emoji} 🌹 𝐓ᴜᴍ 𝐌ᴇʀᴇ 𝐋ɪʏᴇ 𝐐ᴀᴛɪʟ 𝐇ᴏ - 𝐇ᴀʀ 𝐌ᴜꜱᴋᴀɴ 𝐌ᴇɪɴ 𝐌ᴀᴀʀᴅᴏ 🌹 {emoji}",
    "{emoji} 🎀 𝐓ᴜᴍʜᴀʀɪ 𝐀ᴀɴᴋʜᴇɪɴ 𝐌ᴜᴊʜᴇ 𝐊ʜᴏʏᴀ 𝐇ᴜᴀ 𝐑ᴀᴀʜ ᴅɪᴋʜᴀᴛɪ 𝐇ᴀɪ 🎀 {emoji}",
    "{emoji} ✨ 𝐓ᴜᴍ 𝐌ᴇʀɪ 𝐙ɪɴᴅᴀɢɪ 𝐊ɪ 𝐖ᴏ 𝐊ɪʀɴ 𝐇ᴏ 𝐉ᴏ 𝐊ᴀʙʜɪ 𝐁ᴜᴊʜᴛɪ 𝐍ʜɪ ✨ {emoji}",
    "{emoji} 💕 𝐓ᴜᴍʜᴀʀᴇ 𝐁ɪɴᴀ 𝐃ᴜɴɪʏᴀ 𝐒ᴜɴɪ 𝐇ᴀɪ - 𝐓ᴜᴍ 𝐀ᴀᴏ 𝐓ᴏ 𝐑ᴀɴɢɪɴ 💕 {emoji}",
    "{emoji} 🌸 𝐓ᴜᴍ 𝐌ᴇʀɪ 𝐒ᴜʙᴀʜ 𝐊ɪ 𝐏ᴇʜʟɪ 𝐊ɪʀɴ 𝐇ᴏ 🌸 {emoji}",
    "{emoji} 💖 𝐓ᴜᴍʜᴀʀɪ 𝐌ᴜꜱᴋᴀɴ 𝐌ᴇʀᴇ 𝐃ɪʟ 𝐊ɪ 𝐃ʜᴀᴅᴋᴀɴ 𝐇ᴀɪ 💖 {emoji}",
    "{emoji} 🦋 𝐓ᴜᴍ 𝐌ᴇʀᴇ 𝐊ʜᴡᴀʙᴏɴ 𝐊ɪ 𝐑ᴀɴɪ 𝐇ᴏ 🦋 {emoji}",
    "{emoji} 💗 𝐓ᴜᴍʜᴀʀɪ 𝐀ᴡᴀᴀᴢ 𝐌ᴇʀᴀ 𝐌ᴀɴᴅᴏʟɪɴ 𝐇ᴀɪ 💗 {emoji}",
    "{emoji} 🌺 𝐓ᴜᴍ 𝐌ᴇʀᴇ 𝐋ɪʏᴇ 𝐇ᴀʀ 𝐌ᴏᴅ ᴘᴇ 𝐑ᴀʜᴀᴛ 𝐇ᴏ 🌺 {emoji}",
    "{emoji} 💘 𝐓ᴜᴍʜᴀʀᴀ 𝐍ᴀᴀᴍ 𝐌ᴇʀɪ 𝐃ᴜᴀᴏɴ 𝐌ᴇ 𝐇ᴀɪ 💘 {emoji}",
    "{emoji} 🌙 𝐓ᴜᴍ 𝐂ʜᴀɴᴅ 𝐒ᴇ 𝐁ʜɪ 𝐙ʏᴀᴅᴀ 𝐊ʜᴜʙꜱᴜʀᴀᴛ 𝐇ᴏ 🌙 {emoji}",
    "{emoji} 💫 𝐓ᴜᴍʜᴀʀɪ 𝐄ᴋ 𝐉ʜᴀʟᴀᴋ 𝐌ᴜᴊʜᴇ 𝐏ᴀɢᴀʟ 𝐊ᴀʀᴅᴇᴛɪ 𝐇ᴀɪ 💫 {emoji}",
    "{emoji} 🌷 𝐓ᴜᴍ 𝐌ᴇʀɪ 𝐉ɪɴᴅᴀɢɪ 𝐊ᴀ 𝐒ᴀʙꜱᴇ 𝐏ʏᴀʀᴀ 𝐇ᴀᴅɪꜱᴀ 🌷 {emoji}",
    "{emoji} 💝 𝐓ᴜᴍʜᴀʀɪ 𝐁ᴀᴀᴛᴇɪɴ 𝐌ᴇʀɪ 𝐑ᴏᴜʜ 𝐓ᴀᴋ 𝐏ʜᴏʜᴏᴄʜᴛɪ 𝐇ᴀɪ 💝 {emoji}",
    "{emoji} 🌹 𝐓ᴜᴍ 𝐌ᴇʀᴇ 𝐋ɪʏᴇ 𝐀sᴍᴀɴ 𝐒ᴇ 𝐋ᴀʏɪ 𝐇ᴜɪ 𝐇ᴏ 🌹 {emoji}",
    "{emoji} 🎀 𝐓ᴜᴍʜᴀʀɪ 𝐇ᴀꜱɪ 𝐌ᴇʀɪ 𝐃ᴜɴɪʏᴀ 𝐊ᴏ 𝐉ᴀɴɴᴀᴛ 𝐁ᴀɴᴀᴅᴇᴛɪ 𝐇ᴀɪ 🎀 {emoji}",
    "{emoji} ✨ 𝐓ᴜᴍ 𝐌ᴇʀɪ 𝐙ɪɴᴅᴀɢɪ 𝐊ᴀ 𝐖ᴏ 𝐐ɪꜱᴍᴀᴛ 𝐇ᴏ ✨ {emoji}",
    "{emoji} 💕 𝐓ᴜᴍʜᴀʀɪ 𝐀ᴀɴᴋʜᴇɪɴ 𝐌ᴜᴊʜᴇ 𝐆ʜᴀʏᴀʟ 𝐊ᴀʀᴅᴇᴛɪ 𝐇ᴀɪ 💕 {emoji}",
    "{emoji} 🌸 𝐓ᴜᴍ 𝐌ᴇʀᴇ 𝐋ɪʏᴇ 𝐅ᴜʟʟ 𝐒ᴛᴏᴘ 𝐇ᴏ - 𝐌ᴇʀɪ 𝐇ᴀʀ 𝐁ᴀᴀᴛ 𝐓ᴜᴍ 𝐏ᴇ 🌸 {emoji}",
    "{emoji} 💖 𝐓ᴜᴍʜᴀʀɪ 𝐌ᴜꜱᴋᴀɴ 𝐌ᴇʀɪ 𝐏ʜɪʟᴏꜱᴏꜰʏ 𝐇ᴀɪ 💖 {emoji}",
    "{emoji} 🦋 𝐓ᴜᴍ 𝐌ᴇʀᴇ 𝐊ʜᴡᴀʙᴏɴ 𝐊ɪ 𝐓ᴀʙɪʀ 𝐇ᴏ 🦋 {emoji}",
    "{emoji} 💗 𝐓ᴜᴍʜᴀʀɪ 𝐀ᴡᴀᴀᴢ 𝐌ᴇʀɪ 𝐍ᴇᴇɴᴅ 𝐇ᴀɪ 💗 {emoji}",
    "{emoji} 🌺 𝐓ᴜᴍ 𝐌ᴇʀɪ 𝐉ɪɴᴅᴀɢɪ 𝐊ɪ 𝐑ᴀɴɢɪɴ 𝐊ʜᴡᴀʙ 𝐇ᴏ 🌺 {emoji}",
    "{emoji} 💘 𝐓ᴜᴍʜᴀʀᴇ 𝐁ɪɴᴀ 𝐌ᴀɪɴ 𝐊ᴜᴄʜ 𝐍ʜɪ 💘 {emoji}",
    "{emoji} 🌙 𝐓ᴜᴍ 𝐑ᴀᴀᴛ 𝐊ɪ 𝐑ᴀɴɪ 𝐇ᴏ 𝐀ᴜʀ 𝐌ᴀɪɴ 𝐓ᴜᴍʜᴀʀᴀ 𝐃ɪᴡᴀɴᴀ 🌙 {emoji}",
    "{emoji} 💫 𝐓ᴜᴍʜᴀʀɪ 𝐄ᴋ 𝐍ᴀᴢᴀʀ 𝐊ᴀꜰɪ 𝐇ᴀɪ 𝐌ᴇʀɪ 𝐙ɪɴᴅᴀɢɪ 𝐊ᴇ 𝐋ɪʏᴇ 💫 {emoji}",
    "{emoji} 🌷 𝐓ᴜᴍ 𝐌ᴇʀɪ 𝐉ɪɴᴅᴀɢɪ 𝐊ɪ 𝐖ᴏ 𝐊ᴜsʜʙᴏᴏ 𝐇ᴏ 🌷 {emoji}",
    "{emoji} 💝 𝐓ᴜᴍʜᴀʀɪ 𝐁ᴀᴀᴛᴇɪɴ 𝐌ᴇʀɪ 𝐑ᴜʜ 𝐊ᴏ 𝐂ʜʜᴜʟᴛɪ 𝐇ᴀɪ 💝 {emoji}",
    "{emoji} 🌹 𝐓ᴜᴍ 𝐌ᴇʀᴇ 𝐋ɪʏᴇ 𝐀ꜱᴍᴀɴ 𝐊ɪ 𝐓ᴀʀᴀꜰ 𝐇ᴏ 🌹 {emoji}",
    "{emoji} 🎀 𝐓ᴜᴍʜᴀʀɪ 𝐌ᴜꜱᴋᴀɴ 𝐌ᴇʀɪ 𝐒ᴜʙᴀʜ 𝐊ɪ 𝐏ᴇʜʟɪ 𝐃ᴜᴀ 🎀 {emoji}",
    "{emoji} ✨ 𝐓ᴜᴍ 𝐌ᴇʀɪ 𝐙ɪɴᴅᴀɢɪ 𝐊ɪ 𝐖ᴏ 𝐂ʜᴀᴀɴᴅ 𝐇ᴏ ✨ {emoji}",
    "{emoji} 💕 𝐓ᴜᴍʜᴀʀɪ 𝐀ᴀɴᴋʜᴇɪɴ 𝐌ᴜᴊʜᴇ 𝐊ᴀʙʜɪ 𝐍ʜɪ 𝐁ʜᴏᴏʟᴛɪ 💕 {emoji}",
    "{emoji} 🌸 𝐓ᴜᴍ 𝐌ᴇʀᴇ 𝐃ɪʟ 𝐊ɪ 𝐖ᴏ 𝐀ᴡᴀᴀᴢ 𝐇ᴏ 🌸 {emoji}",
    "{emoji} 💖 𝐓ᴜᴍʜᴀʀɪ 𝐇ᴀꜱɪ 𝐌ᴇʀɪ 𝐓ᴀᴋᴅɪʀ 𝐇ᴀɪ 💖 {emoji}",
    "{emoji} 🦋 𝐓ᴜᴍ 𝐌ᴇʀɪ 𝐃ᴜɴɪʏᴀ 𝐊ɪ 𝐖ᴏ 𝐑ᴏɴɢ 𝐇ᴏ 🦋 {emoji}",
    "{emoji} 💗 𝐓ᴜᴍʜᴀʀᴇ 𝐁ɪɴᴀ 𝐌ᴀɪɴ 𝐀ᴅʜᴜʀᴀ - 𝐓ᴜᴍ 𝐀ᴀᴏ 𝐓ᴏ 𝐏ᴜʀᴀ 💗 {emoji}"
]

FLIRTENG_RAID = [
    "{emoji} 💖 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐅ɪʀꜱᴛ 𝐓ʜɪɴɢ 𝐎ɴ 𝐌ʏ 𝐌ɪɴᴅ 𝐄ᴠᴇʀʏ 𝐌ᴏʀɴɪɴɢ 💖 {emoji}",
    "{emoji} 🌹 𝐘ᴏᴜʀ 𝐒ᴍɪʟᴇ 𝐈ꜱ 𝐓ʜᴇ 𝐁ᴇꜱᴛ 𝐏ᴀʀᴛ 𝐎ꜰ 𝐌ʏ 𝐃ᴀʏ 🌹 {emoji}",
    "{emoji} ✨ 𝐘ᴏᴜ'ʀᴇ 𝐍ᴏᴛ 𝐉ᴜꜱᴛ 𝐀 𝐃ʀᴇᴀᴍ, 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐄ɴᴛɪʀᴇ 𝐔ɴɪᴠᴇʀꜱᴇ ✨ {emoji}",
    "{emoji} 💕 𝐈 𝐅ᴇʟʟ 𝐅ᴏʀ 𝐘ᴏᴜ 𝐋ɪᴋᴇ 𝐀 𝐒ᴛᴀʀ 𝐅ᴀʟʟꜱ 𝐅ʀᴏᴍ 𝐓ʜᴇ 𝐒ᴋʏ 💕 {emoji}",
    "{emoji} 🎀 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐏ᴏᴇᴛʀʏ 𝐌ʏ 𝐇ᴇᴀʀᴛ 𝐍ᴇᴠᴇʀ 𝐊ɴᴇᴡ 𝐈ᴛ 𝐂ᴏᴜʟᴅ 𝐖ʀɪᴛᴇ 🎀 {emoji}",
    "{emoji} 💗 𝐘ᴏᴜʀ 𝐋ᴀᴜɢʜᴛᴇʀ 𝐈ꜱ 𝐌ʏ 𝐅ᴀᴠᴏʀɪᴛᴇ 𝐒ᴏᴜɴᴅ 💗 {emoji}",
    "{emoji} 🌺 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐒ᴜɴꜱʜɪɴᴇ 𝐓ʜᴀᴛ 𝐁ʀɪɢʜᴛᴇɴꜱ 𝐌ʏ 𝐃ᴀʀᴋᴇꜱᴛ 𝐃ᴀʏꜱ 🌺 {emoji}",
    "{emoji} 💘 𝐈 𝐃ᴏɴ'ᴛ 𝐍ᴇᴇᴅ 𝐀 𝐅ᴀɪʀʏᴛᴀʟᴇ - 𝐈 𝐍ᴇᴇᴅ 𝐘ᴏᴜ 💘 {emoji}",
    "{emoji} 🦋 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐌ᴏꜱᴛ 𝐁ᴇᴀᴜᴛɪꜰᴜʟ 𝐓ʜᴏᴜɢʜᴛ 𝐈ɴ 𝐌ʏ 𝐌ɪɴᴅ 🦋 {emoji}",
    "{emoji} 🌸 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐑ᴇᴀꜱᴏɴ 𝐌ʏ 𝐇ᴇᴀʀᴛ 𝐁ᴇᴀᴛꜱ 𝐅ᴀꜱᴛᴇʀ 🌸 {emoji}",
    "{emoji} 💎 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐌ᴏꜱᴛ 𝐕ᴀʟᴜᴀʙʟᴇ 𝐓ʀᴇᴀꜱᴜʀᴇ 𝐈ɴ 𝐌ʏ 𝐋ɪꜰᴇ 💎 {emoji}",
    "{emoji} 🌹 𝐘ᴏᴜʀ 𝐕ᴏɪᴄᴇ 𝐈ꜱ 𝐌ʏ 𝐅ᴀᴠᴏʀɪᴛᴇ 𝐌ᴇʟᴏᴅʏ 🌹 {emoji}",
    "{emoji} ✨ 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐁ʀɪɢʜᴛᴇꜱᴛ 𝐒ᴛᴀʀ 𝐈ɴ 𝐌ʏ 𝐆ᴀʟᴀxʏ ✨ {emoji}",
    "{emoji} 💕 𝐄ᴠᴇʀʏ 𝐃ᴀʏ 𝐖ɪᴛʜ 𝐘ᴏᴜ 𝐈ꜱ 𝐀 𝐏ᴇʀꜰᴇᴄᴛ 𝐃ᴀʏ 💕 {emoji}",
    "{emoji} 🎀 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐀ɴꜱᴡᴇʀ 𝐓ᴏ 𝐀ʟʟ 𝐌ʏ 𝐐ᴜᴇꜱᴛɪᴏɴꜱ 🎀 {emoji}",
    "{emoji} 💗 𝐘ᴏᴜʀ 𝐄ʏᴇꜱ 𝐇ᴏʟᴅ 𝐓ʜᴇ 𝐖ʜᴏʟᴇ 𝐔ɴɪᴠᴇʀꜱᴇ 💗 {emoji}",
    "{emoji} 🌺 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐁ᴇꜱᴛ 𝐓ʜɪɴɢ 𝐓ʜᴀᴛ 𝐇ᴀꜱ 𝐄ᴠᴇʀ 𝐇ᴀᴘᴘᴇɴᴇᴅ 𝐓ᴏ 𝐌ᴇ 🌺 {emoji}",
    "{emoji} 💘 𝐈 𝐋ᴏᴠᴇ 𝐓ʜᴇ 𝐖ᴀʏ 𝐘ᴏᴜ 𝐌ᴀᴋᴇ 𝐌ᴇ 𝐅ᴇᴇʟ 💘 {emoji}",
    "{emoji} 🦋 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐌ᴀɢɪᴄ 𝐈ɴ 𝐌ʏ 𝐖ᴏʀʟᴅ 🦋 {emoji}",
    "{emoji} 🌸 𝐘ᴏᴜʀ 𝐓ᴏᴜᴄʜ 𝐈ꜱ 𝐌ʏ 𝐅ᴀᴠᴏʀɪᴛᴇ 𝐅ᴇᴇʟɪɴɢ 🌸 {emoji}",
    "{emoji} 💎 𝐘ᴏᴜ'ʀᴇ 𝐌ʏ 𝐃ʀᴇᴀᴍ 𝐂ᴏᴍᴇ 𝐓ʀᴜᴇ 💎 {emoji}",
    "{emoji} 🌹 𝐘ᴏᴜʀ 𝐒ᴍɪʟᴇ 𝐂ᴜʀᴇꜱ 𝐄ᴠᴇʀʏᴛʜɪɴɢ 🌹 {emoji}",
    "{emoji} ✨ 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐋ɪɢʜᴛ 𝐈ɴ 𝐌ʏ 𝐃ᴀʀᴋᴇꜱᴛ 𝐍ɪɢʜᴛ ✨ {emoji}",
    "{emoji} 💕 𝐘ᴏᴜʀ 𝐇ᴀᴘᴘɪɴᴇꜱꜱ 𝐈ꜱ 𝐌ʏ 𝐇ᴀᴘᴘɪɴᴇꜱꜱ 💕 {emoji}",
    "{emoji} 🎀 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐎ɴʟʏ 𝐎ɴᴇ 𝐅ᴏʀ 𝐌ᴇ 🎀 {emoji}",
    "{emoji} 💗 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐑ᴇᴀꜱᴏɴ 𝐈 𝐖ᴀᴋᴇ 𝐔ᴘ 𝐒ᴍɪʟɪɴɢ 💗 {emoji}",
    "{emoji} 🌺 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐌ᴏꜱᴛ 𝐁ᴇᴀᴜᴛɪꜰᴜʟ 𝐒ᴏᴜʟ 𝐈'ᴠᴇ 𝐄ᴠᴇʀ 𝐊ɴᴏᴡɴ 🌺 {emoji}",
    "{emoji} 💘 𝐌ʏ 𝐖ᴏʀʟᴅ 𝐑ᴇᴠᴏʟᴠᴇꜱ 𝐀ʀᴏᴜɴᴅ 𝐘ᴏᴜ 💘 {emoji}",
    "{emoji} 🦋 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐁ᴇꜱᴛ 𝐏ᴀʀᴛ 𝐎ꜰ 𝐌ʏ 𝐒ᴛᴏʀʏ 🦋 {emoji}",
    "{emoji} 🌸 𝐘ᴏᴜʀ 𝐍ᴀᴍᴇ 𝐈ꜱ 𝐌ʏ 𝐅ᴀᴠᴏʀɪᴛᴇ 𝐖ᴏʀᴅ 🌸 {emoji}",
    "{emoji} 💎 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐏ɪᴇᴄᴇ 𝐈'ᴠᴇ 𝐀ʟᴡᴀʏꜱ 𝐁ᴇᴇɴ 𝐌ɪꜱꜱɪɴɢ 💎 {emoji}",
    "{emoji} 🌹 𝐘ᴏᴜʀ 𝐋ᴏᴠᴇ 𝐈ꜱ 𝐌ʏ 𝐅ᴀᴠᴏʀɪᴛᴇ 𝐅ᴇᴇʟɪɴɢ 🌹 {emoji}",
    "{emoji} ✨ 𝐘ᴏᴜ'ʀᴇ 𝐄ᴠᴇʀʏᴛʜɪɴɢ 𝐈 𝐍ᴇᴠᴇʀ 𝐊ɴᴇᴡ 𝐈 𝐍ᴇᴇᴅᴇᴅ ✨ {emoji}",
    "{emoji} 💕 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐎ɴʟʏ 𝐓ʜɪɴɢ 𝐈 𝐖ᴀɴᴛ 💕 {emoji}",
    "{emoji} 🎀 𝐘ᴏᴜ'ʀᴇ 𝐌ʏ 𝐄ᴠᴇʀʏᴛʜɪɴɢ 🎀 {emoji}",
    "{emoji} 💗 𝐘ᴏᴜʀ 𝐏ʀᴇꜱᴇɴᴄᴇ 𝐈ꜱ 𝐌ʏ 𝐏ᴇᴀᴄᴇ 💗 {emoji}",
    "{emoji} 🌺 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐁ʀᴇᴀᴛʜ 𝐈ɴ 𝐌ʏ 𝐋ᴜɴɢꜱ 🌺 {emoji}",
    "{emoji} 💘 𝐈'ᴍ 𝐒ᴏ 𝐆ʀᴀᴛᴇꜰᴜʟ 𝐘ᴏᴜ'ʀᴇ 𝐌ɪɴᴇ 💘 {emoji}",
    "{emoji} 🦋 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐂ᴏʟᴏʀ 𝐈ɴ 𝐌ʏ 𝐁ʟᴀᴄᴋ & 𝐖ʜɪᴛᴇ 𝐖ᴏʀʟᴅ 🦋 {emoji}",
    "{emoji} 🌸 𝐘ᴏᴜʀ 𝐋ᴏᴠᴇ 𝐈ꜱ 𝐌ʏ 𝐅ᴀᴠᴏʀɪᴛᴇ 𝐏ᴏᴇᴍ 🌸 {emoji}",
    "{emoji} 💎 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐂ʀᴏᴡɴ 𝐎ꜰ 𝐌ʏ 𝐇ᴇᴀʀᴛ 💎 {emoji}",
    "{emoji} 🌹 𝐘ᴏᴜʀ 𝐓ᴏᴜᴄʜ 𝐈ꜱ 𝐌ʏ 𝐅ᴀᴠᴏʀɪᴛᴇ 𝐌ᴇᴍᴏʀʏ 🌹 {emoji}",
    "{emoji} ✨ 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐆ᴜɪᴅɪɴɢ 𝐋ɪɢʜᴛ 𝐈ɴ 𝐌ʏ 𝐋ɪꜰᴇ ✨ {emoji}",
    "{emoji} 💕 𝐘ᴏᴜ'ʀᴇ 𝐌ʏ 𝐏ᴇʀꜰᴇᴄᴛ 𝐏ʟᴀᴄᴇ 💕 {emoji}",
    "{emoji} 🎀 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐎ɴʟʏ 𝐓ʀᴜᴇ 𝐋ᴏᴠᴇ 🎀 {emoji}",
    "{emoji} 💗 𝐘ᴏᴜʀ 𝐖ᴏʀᴅꜱ 𝐀ʀᴇ 𝐌ʏ 𝐅ᴀᴠᴏʀɪᴛᴇ 𝐌ᴜꜱɪᴄ 💗 {emoji}",
    "{emoji} 🌺 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐁ᴇꜱᴛ 𝐃ᴇᴄɪꜱɪᴏɴ 𝐈'ᴠᴇ 𝐄ᴠᴇʀ 𝐌ᴀᴅᴇ 🌺 {emoji}",
    "{emoji} 💘 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐅ᴏᴜɴᴅᴀᴛɪᴏɴ 𝐎ꜰ 𝐌ʏ 𝐖ᴏʀʟᴅ 💘 {emoji}",
    "{emoji} 🦋 𝐘ᴏᴜ'ʀᴇ 𝐓ʜᴇ 𝐌ᴏꜱᴛ 𝐁ᴇᴀᴜᴛɪꜰᴜʟ 𝐂ʀᴇᴀᴛɪᴏɴ 🦋 {emoji}",
    "{emoji} 🌸 𝐘ᴏᴜʀ 𝐋ᴏᴠᴇ 𝐈ꜱ 𝐌ʏ 𝐅ᴀᴠᴏʀɪᴛᴇ 𝐏ʟᴀᴄᴇ 🌸 {emoji}"
]

# RAID BANNER
RAID_BANNER = (
    "🔥 ═══════════════════════════════════════ 🔥\n"
    "          ⚡ 𝗚𝖔𝖏𝖔 GOD RAID SYSTEM ⚡\n"
    "🔥 ═══════════════════════════════════════ 🔥"
)

# ==================== ROTATING EMOJIS ====================
ROTATING_EMOJIS = itertools.cycle([
    "❤️","🧡","💛","💚","💙","💜","🖤","🤍","🤎",
    "💔","❤️‍🔥","❤️‍🩹","❣️","💕","💞","💓","💗",
    "💖","💘","💝","💟","♥","🩷","🩵","🩶",
    "😽","😻","💋","🙌","🙀","🤭","😍","🥰","😘",
    "😊","🤗","🫶","🫣","🫠","🥹","🤌","🫨","🙈",
    "🐣","🦋","🕊","🍁","🍄","🌷","🌹","🥀",
    "🌻","🌼","🌸","🌺","🍃",
    "🌎","🌍","🌏","🌕","🌖","🌗","🌘","🌑",
    "🌒","🌓","🌔","🌚","🌝","🌞","🌛","🌜",
    "🌙","🪐","💫","⭐","🌟","✨",
    "🧁","🍰","🎂","🍮","🍭","🍬","🍫","🍩",
    "🍿","🍻","🥂","🍷","🍹","🧉","🧃","🥤",
    "🧋","🍡","🍧","🍨","🍦","🥧",
    "💎","🧿","🧸","🎁","🎈","🎀","🪄","💌"
])

# ==================== HELPER FUNCTIONS ====================
def readable_time(seconds):
    if seconds < 60:
        return f"{seconds}s"
    elif seconds < 3600:
        return f"{seconds//60}m {seconds%60}s"
    elif seconds < 86400:
        return f"{seconds//3600}h {(seconds%3600)//60}m"
    else:
        return f"{seconds//86400}d {(seconds%86400)//3600}h"

async def is_user_admin(client, chat_id, user_id):
    try:
        async for admin in client.iter_participants(chat_id, filter=ChannelParticipantsAdmins):
            if admin.id == user_id:
                return True
        return False
    except:
        return False

async def get_user_from_event(event):
    try:
        if event.is_reply:
            reply_message = await event.get_reply_message()
            return await event.client.get_entity(reply_message.sender_id)
        args = event.text.strip().split()
        if len(args) > 1:
            user_input = args[1].strip()
            return await event.client.get_entity(user_input)
        return None
    except Exception as e:
        logging.error(f"User fetch error: {e}")
        return None

async def get_target_user(event, target_input):
    try:
        if target_input and target_input.isdigit():
            try:
                return await event.client.get_entity(int(target_input))
            except:
                pass
        if target_input and target_input.startswith('@'):
            target_input = target_input[1:]
        if target_input:
            try:
                return await event.client.get_entity(target_input)
            except:
                pass
        if event.is_reply:
            reply = await event.get_reply_message()
            return await reply.get_sender()
        return None
    except:
        return None

# ==================== PM PERMIT CONFIG FUNCTIONS ====================

def load_pmpermit_config():
    global pmpermit_enabled
    try:
        if PMPERMIT_CONFIG_FILE.exists():
            with open(PMPERMIT_CONFIG_FILE, 'r') as f:
                data = json.load(f)
                pmpermit_enabled = data.get("enabled", True)
                return pmpermit_enabled
    except:
        pass
    pmpermit_enabled = True
    return pmpermit_enabled

def save_pmpermit_config():
    try:
        with open(PMPERMIT_CONFIG_FILE, 'w') as f:
            json.dump({"enabled": pmpermit_enabled, "updated": datetime.now().isoformat()}, f, indent=2)
    except Exception as e:
        print(f"Error saving PM permit config: {e}")

load_pmpermit_config()

# ==================== USER BOT LIST MANAGER ====================
def load_user_bot_lists():
    if USER_BOT_LISTS_FILE.exists():
        try:
            with open(USER_BOT_LISTS_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_user_bot_lists(data):
    try:
        with open(USER_BOT_LISTS_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Error saving bot lists: {e}")

def get_user_bots(user_id):
    lists = load_user_bot_lists()
    return lists.get(str(user_id), DEFAULT_BOTS)

# ==================== BOT LIST MANAGER ====================
bots_state = {"bots_list": []}

def load_bot_list():
    global bots_state
    try:
        if BOT_LIST_FILE.exists():
            with open(BOT_LIST_FILE, 'r') as f:
                data = json.load(f)
                bots_state["bots_list"] = data.get("bots_list", [])
        if not bots_state["bots_list"]:
            bots_state["bots_list"] = [b.lstrip('@') for b in DEFAULT_BOTS]
            save_bot_list()
    except:
        pass

def save_bot_list():
    try:
        with open(BOT_LIST_FILE, 'w') as f:
            json.dump({"bots_list": bots_state["bots_list"]}, f)
    except:
        pass

load_bot_list()

# ==================== RANK NAME CLEANER ====================
def clean_rank_name(rank):
    if not rank:
        return "Admin"
    
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U0001F700-\U0001F77F"
        "\U0001F780-\U0001F7FF"
        "\U0001F800-\U0001F8FF"
        "\U0001F900-\U0001F9FF"
        "\U0001FA00-\U0001FA6F"
        "\U0001FA70-\U0001FAFF"
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE
    )
    
    clean = emoji_pattern.sub('', rank)
    clean = re.sub(r'[^\w\s\-_.]', '', clean, flags=re.UNICODE)
    clean = re.sub(r'\s+', ' ', clean).strip()
    
    if len(clean) > 16:
        clean = clean[:16]
    
    if not clean:
        clean = "Admin"
    
    return clean

# ==================== PM ASSISTANT WITH MEDIA SUPPORT ====================

class PersonalAssistant:
    def __init__(self):
        self.data = {
            "config": {
                "alive_name": "𝗚𝖔𝖏𝖔 ~ #𝔬𝔣𝔣 ✞︎໋🌙", 
                "assistant_name": "𝗚𝖔𝖏𝖔 ~ #𝔬𝔣𝔣 ✞︎໋🌙 𝐔sᴇʀ𝐁ᴏᴛ", 
                "pmpermit_media": DEFAULT_PMPERMIT_MEDIA_URL,
                "pmpermit_media_type": "photo",
                "use_media": True, 
                "max_warnings": 3
            },
            "users": {}, "warnings": {}, "approved_users": [], "user_states": {},
        }
        self._load()

    def _load(self):
        try:
            if ASSISTANT_DB_FILE.exists():
                with open(ASSISTANT_DB_FILE, "r") as f:
                    self.data.update(json.load(f))
        except:
            pass

    def _save(self):
        try:
            with open(ASSISTANT_DB_FILE, "w") as f:
                json.dump(self.data, f, indent=2)
        except:
            pass

    async def send_message(self, event, mtype, **kwargs):
        try:
            sender = await event.get_sender()
            target_name = sender.first_name or "Mortal"
        except Exception:
            sender = None
            target_name = "Mortal"

        cfg = self.data["config"]

        texts = {
            "introduction": [
                f"😴 **𝗚𝖔𝖏𝖔 Papa so raha hai, {target_name}!**\n\n🌙 Abhi disturb mat karo.\n⏰ Papa uthne ke baad baat karna.",
                f"🌙 **𝗚𝖔𝖏𝖔 Papa ka sleep time hai, {target_name}!**\n\n💤 Thoda wait karo, baad mein baat hogi.",
                f"😈 **𝗚𝖔𝖏𝖔 abhi offline hai, {target_name}!**\n\n🌌 Sabr karo, Papa ke active hone par baat karna."
            ],
            "acknowledgment": [
                f"😴 **Papa abhi so rahe hain, {target_name}.**\n\n🌙 Thoda wait karo!",
                f"💤 **Message mil gaya, {target_name}!**\n\n⏰ 𝗚𝖔𝖏𝖔 ke active hone tak intezaar karo."
            ],
            "warning": [
                f"⚠️ **Warning {target_name}!**\n\nPlease ek hi message bhejo aur wait karo.",
                f"🌙 **𝗚𝖔𝖏𝖔 ka PM abhi closed hai, {target_name}.**\n\nPlease wait!"
            ],
            "approved": [
                f"✅ **{target_name}, tum approved ho!**\n\n😈 Ab 𝗚𝖔𝖏𝖔 se baat kar sakte ho.",
                f"💙 **Access granted, {target_name}!**\n\nWelcome to Gojo's PM."
            ],
            "disapproved": [
                f"❌ **{target_name}, approval reject kar diya gaya.**",
                f"😈 **Access denied, {target_name}!**\n\n𝗚𝖔𝖏𝖔 ne abhi permission nahi di."
            ],
            "blocked": [
                f"🚫 **{target_name}, tum blocked ho.**",
                f"🌑 **Access denied, {target_name}!**"
            ]
        }

        choices = texts.get(mtype, ["😴 𝗚𝖔𝖏𝖔 abhi offline hai."])
        msg = random.choice(choices)

        if mtype == "introduction" and cfg.get("use_media", True):
            try:
                media_path = cfg.get("pmpermit_media")
                media_type = cfg.get("pmpermit_media_type", "photo")

                if media_path:
                    await event.client.send_file(
                        event.chat_id,
                        media_path,
                        caption=msg,
                        force_document=(media_type == "document")
                    )
                    return

            except Exception as e:
                print(f"Failed to send permit media: {e}")

        await event.reply(msg)

    async def handle_message(self, event):
        global pmpermit_enabled
        if not pmpermit_enabled:
            return
        
        if not event.is_private:
            return
        sender = await event.get_sender()
        uid = str(sender.id)
        if sender.bot or uid in self.data["approved_users"]:
            return
        
        target_name = sender.first_name or "Mortal"
        
        text = (event.message.text or "").lower()
        if uid not in self.data["users"]:
            self.data["users"][uid] = {"name": target_name, "first_seen": datetime.now().isoformat()}
            self.data["user_states"][uid] = "introduced"
            self.data["warnings"][uid] = 0
            await self.send_message(event, "introduction", max_warnings=self.data["config"]["max_warnings"])
            self._save()
            return
        if self.data["user_states"].get(uid) == "introduced" and text in ("ok", "okay"):
            self.data["user_states"][uid] = "acknowledged"
            await self.send_message(event, "acknowledgment")
            self._save()
            return
        self.data["warnings"][uid] = self.data["warnings"].get(uid, 0) + 1
        await self.send_message(
            event,
            "warning",
            warn_count=self.data["warnings"][uid],
            max_warnings=self.data["config"]["max_warnings"]
        )
        self._save()

assistant = PersonalAssistant()

# ==================== PM PERMIT TOGGLE COMMAND ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.pmp\s+(on|off)"))
async def toggle_pmpermit(event):
    """Toggle global PM permit protection on/off"""
    global pmpermit_enabled
    state = event.pattern_match.group(1).lower()
    
    if state == "on":
        pmpermit_enabled = True
        save_pmpermit_config()
        await event.reply(
            "🛡️ **PM Permit Protection ENABLED!**\n\n"
            "✅ All PM messages will be filtered.\n"
            "👑 Unknown users must seek approval.\n"
            "🔒 Your privacy is now protected."
        )
    elif state == "off":
        pmpermit_enabled = False
        save_pmpermit_config()
        await event.reply(
            "🔓 **PM Permit Protection DISABLED!**\n\n"
            "⚠️ All PM messages will be allowed.\n"
            "📨 Unknown users can message freely.\n"
            "🛡️ Protection is now OFF."
        )
    else:
        await event.reply(
            "❌ **Invalid command!**\n\n"
            "💡 **Usage:** `.pmp on` or `.pmp off`\n\n"
            f"📊 **Current Status:** {'🟢 ON' if pmpermit_enabled else '🔴 OFF'}"
        )

@client.on(events.NewMessage(outgoing=True, pattern=r"\.pmpstatus"))
async def pmpermit_status(event):
    """Check current PM permit status"""
    global pmpermit_enabled
    status = "🟢 **ENABLED**" if pmpermit_enabled else "🔴 **DISABLED**"
    
    await event.reply(
        f"🛡️ **PM Permit Protection Status**\n\n"
        f"📊 **Status:** {status}\n"
        f"👑 **Owner:** {DEFAULTUSER}\n"
        f"📝 **Approved Users:** {len(assistant.data['approved_users'])}\n"
        f"🖼️ **Media Type:** {assistant.data['config'].get('pmpermit_media_type', 'photo')}\n\n"
        f"💡 **Toggle:** `.pmp on` or `.pmp off`"
    )

# ==================== PM APPROVAL COMMANDS ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.(?:a|approve)(?:$|\s)"))
async def approve_cmd(event):
    if event.is_reply:
        reply_msg = await event.get_reply_message()
        sender = await reply_msg.get_sender()
        uid = str(sender.id)
        target_name = sender.first_name or "Mortal"
        
        if uid not in assistant.data["approved_users"]:
            assistant.data["approved_users"].append(uid)
        assistant.data["warnings"].pop(uid, None)
        assistant._save()
        
        await event.reply(
            f"✅ **You are blessed, {target_name}!**\n\n"
            f"{assistant.data['config']['alive_name']} has accepted your devotion.\n"
            f"⚡ **You may now speak with the Almighty.**\n"
            f"👑 *Walk the righteous path, and you shall be protected.*"
        )
    else:
        await event.reply("❌ **Reply to a mortal's message to bless them!**")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.(?:da|disapprove)(?:$|\s)"))
async def disapprove_cmd(event):
    if event.is_reply:
        reply_msg = await event.get_reply_message()
        sender = await reply_msg.get_sender()
        uid = str(sender.id)
        target_name = sender.first_name or "Mortal"
        
        assistant.data["approved_users"] = [u for u in assistant.data["approved_users"] if u != uid]
        assistant.data["warnings"][uid] = 0
        assistant._save()
        
        await event.reply(
            f"❌ **Your blessing is revoked, {target_name}!**\n\n"
            f"You have lost favor with {assistant.data['config']['alive_name']}.\n"
            f"⚡ *Kneel and beg for forgiveness if you wish to be heard again.*"
        )
    else:
        await event.reply("❌ **Reply to a mortal's message to revoke their blessing!**")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.listapproved"))
async def listapproved_cmd(event):
    approved = assistant.data["approved_users"]
    if not approved:
        return await event.reply("📋 **No blessed souls found.**")
    text = "📋 **Blessed Souls:**\n"
    for uid in approved:
        info = assistant.data["users"].get(uid, {})
        text += f"• {info.get('name', 'Unknown')} (`{uid}`)\n"
    await event.reply(text)

@client.on(events.NewMessage(outgoing=True, pattern=r"\.block"))
async def block_cmd(event):
    if event.is_reply:
        reply_msg = await event.get_reply_message()
        sender = await reply_msg.get_sender()
        uid = str(sender.id)
        target_name = sender.first_name or "Mortal"
        
        assistant.data["approved_users"] = [u for u in assistant.data["approved_users"] if u != uid]
        assistant.data["warnings"].pop(uid, None)
        assistant.data["user_states"].pop(uid, None)
        assistant._save()
        await client(BlockRequest(int(uid)))
        await event.reply(f"🚫 **{target_name} has been banished from PM!**")
    else:
        await event.reply("❌ **Reply to a mortal to banish them!**")

# ==================== SETPMEDIA COMMAND ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.setpmedia(?:$|\s)"))
async def setpmedia_cmd(event):
    """Set PM permit media (supports any media: photo, video, GIF, document)"""
    if not event.is_reply:
        await event.reply("❌ **Reply to any media (photo, video, GIF, document) to set as PM permit media!**")
        return
    
    reply = await event.get_reply_message()
    
    if not reply.media:
        await event.reply("❌ **Reply to a media file!**\n\nSupported: Photo, Video, GIF, Document, Sticker")
        return
    
    status = await event.reply("📥 **Setting PM permit media...**")
    
    try:
        media_path = await event.client.download_media(reply.media)
        
        if not media_path:
            await status.edit("❌ Failed to download media!")
            return
        
        media_type = "photo"
        if reply.photo:
            media_type = "photo"
        elif reply.video:
            media_type = "video"
        elif reply.document:
            if reply.document.mime_type == "video/mp4" and "gif" in str(reply.document.attributes):
                media_type = "gif"
            else:
                media_type = "document"
        elif reply.sticker:
            media_type = "photo"
        
        assistant.data["config"]["pmpermit_media"] = media_path
        assistant.data["config"]["pmpermit_media_type"] = media_type
        assistant._save()
        
        media_emoji = {
            "photo": "🖼️",
            "video": "🎬",
            "gif": "🎞️",
            "document": "📄"
        }.get(media_type, "📎")
        
        await status.edit(f"✅ **PM permit media set successfully!**\n\n"
                         f"{media_emoji} **Type:** {media_type.title()}\n"
                         f"📁 **File:** `{os.path.basename(media_path)}`\n"
                         f"💡 **Use:** `.tpmedia` to toggle on/off")
        
    except Exception as e:
        await status.edit(f"❌ Failed to set PM permit media: {str(e)}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.tpmedia(?:$|\s)"))
async def tpmedia_cmd(event):
    """Toggle PM permit media on/off"""
    current = assistant.data["config"].get("use_media", True)
    assistant.data["config"]["use_media"] = not current
    assistant._save()
    
    status = "ENABLED" if assistant.data["config"]["use_media"] else "DISABLED"
    await event.reply(f"🔄 **PM permit media {status}!**")
# ==================== BOT MANAGER COMMANDS ====================
@client.on(events.NewMessage(outgoing=True, pattern=r'\.addbot'))
async def addbot_cmd(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    managed_bots = get_user_bots(user_id)
    if not managed_bots:
        return await event.respond("❌ **No bots in your army!** Use `.setbots` to summon them.")
    status = await event.respond(f"⏳ **Summoning {len(managed_bots)} bots to this realm...**")
    try:
        full_chat = await client.get_entity(chat_id)
    except Exception as e:
        await status.edit(f"❌ **Error:** `{e}`")
        return
    bot_entities = []
    valid_bots = []
    for bot_username in managed_bots:
        try:
            bot_entity = await client.get_input_entity(bot_username)
            bot_entities.append(bot_entity)
            valid_bots.append(bot_username)
        except Exception as e:
            print(f"Could not get entity for {bot_username}: {e}")
    if not bot_entities:
        await status.edit("❌ **No valid bots found!**")
        asyncio.create_task(delete_after(status, 5.0))
        return
    await status.edit(f"⏳ **Summoning {len(bot_entities)} bots to the realm...**")
    added_count = 0
    try:
        if isinstance(full_chat, Channel):
            result = await client(InviteToChannelRequest(
                channel=InputPeerChannel(full_chat.id, full_chat.access_hash),
                users=bot_entities
            ))
            added_count = len(bot_entities)
        elif isinstance(full_chat, Chat):
            for bot_entity in bot_entities:
                try:
                    await client(AddChatUserRequest(
                        chat_id=full_chat.id,
                        user_id=bot_entity,
                        fwd_limit=0
                    ))
                    added_count += 1
                except Exception as e:
                    if "USER_ALREADY_PARTICIPANT" not in str(e):
                        print(f"Error adding bot: {e}")
        await status.edit(f"✅ **Summoned {added_count}/{len(managed_bots)} bots to the realm!**")
        asyncio.create_task(delete_after(status, 10.0))
    except Exception as e:
        error_msg = str(e)
        if "USER_ALREADY_PARTICIPANT" in error_msg:
            await status.edit(f"⚠️ **Some bots are already in the realm.**")
        else:
            await status.edit(f"❌ **Error:** `{error_msg[:100]}`")
        asyncio.create_task(delete_after(status, 10.0))

@client.on(events.NewMessage(outgoing=True, pattern=r'\.removebots'))
async def removebots_cmd(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    managed_bots = get_user_bots(user_id)
    if not managed_bots:
        return await event.respond("❌ **No bots in your army!**")
    chat = await event.get_chat()
    status_msg = await event.reply(f"🤖 **Banishing {len(managed_bots)} bots...**")
    removed_count = 0
    for bot_username in managed_bots:
        try:
            user = await event.client.get_entity(bot_username)
            await event.client.kick_participant(chat, user)
            removed_count += 1
            await status_msg.edit(f"⏳ **Banished {removed_count}/{len(managed_bots)} bots...**")
            await asyncio.sleep(1)
        except Exception as e:
            print(f"Error removing {bot_username}: {e}")
    await status_msg.edit(
        f"🤖 **Banishment Complete**\n\n"
        f"👋 **Banished:** {removed_count}/{len(managed_bots)}"
    )
    asyncio.create_task(delete_after(status_msg, 10.0))

@client.on(events.NewMessage(outgoing=True, pattern=r'\.setbots\s+(.+)'))
async def setbots_cmd(event):
    user_id = event.sender_id
    bots_text = event.pattern_match.group(1)
    new_bots = [b.strip().replace('@', '') for b in bots_text.split() if b.strip()]
    if not new_bots:
        return await event.reply("❌ **Invalid format!** Provide bot usernames.\nExample: `.setbots bot1 bot2 bot3`")
    lists = load_user_bot_lists()
    lists[str(user_id)] = new_bots
    save_user_bot_lists(lists)
    await event.reply(f"✅ **Army updated!** {len(new_bots)} bots summoned.\n\n📋 **Your Army:**\n" + "\n".join([f"@{b}" for b in new_bots]))

@client.on(events.NewMessage(outgoing=True, pattern=r'\.mybots'))
async def mybots_cmd(event):
    user_id = event.sender_id
    user_bots = get_user_bots(user_id)
    msg = "🤖 **Your Army:**\n\n" + "\n".join([f"@{b}" for b in user_bots])
    await event.reply(msg)

@client.on(events.NewMessage(outgoing=True, pattern=r'\.resetbots'))
async def resetbots_cmd(event):
    user_id = event.sender_id
    lists = load_user_bot_lists()
    if str(user_id) in lists:
        del lists[str(user_id)]
        save_user_bot_lists(lists)
    await event.reply(f"✅ **Army reset to default.**\n\nDefault bots:\n" + "\n".join([f"@{b}" for b in DEFAULT_BOTS]))

@client.on(events.NewMessage(outgoing=True, pattern=r'\.creategc\s+(\d+)'))
async def creategc_cmd(event):
    try:
        count = int(event.pattern_match.group(1))
        if count <= 0 or count > 50:
            return await event.reply("❌ **Count must be between 1 and 50!**")
    except:
        return await event.reply("❌ **Usage:** `.creategc <count>`\nExample: `.creategc 5`")
    
    user_id = event.sender_id
    managed_bots = get_user_bots(user_id)
    if not managed_bots:
        await event.reply("❌ **No bots in your army!** Use `.setbots` to summon them.")
        return
    
    status = await event.reply(f"⏳ **Creating {count} groups with your bots...**")
    bot_entities = []
    for bot in managed_bots[:10]:
        try:
            bot_entities.append(await client.get_input_entity(bot))
        except:
            pass
    
    if not bot_entities:
        await status.edit("❌ **No valid bots found!**")
        return
    
    created = 0
    failed = 0
    GROUP_PIC_URL = "https://files.catbox.moe/7dqow9.jpg"
    
    for i in range(count):
        try:
            title = f"GC {i+1}"
            await status.edit(f"⏳ **Creating group {i+1}/{count}:** `{title}`")
            
            result = await client(CreateChatRequest(
                users=bot_entities[:10],
                title=title
            ))
            
            created += 1
            
            try:
                pic_path = await download_picture(GROUP_PIC_URL)
                if pic_path:
                    uploaded_file = await client.upload_file(pic_path)
                    await client(EditChatPhotoRequest(
                        chat_id=result.chats[0].id,
                        photo=InputChatUploadedPhoto(file=uploaded_file)
                    ))
                    if os.path.exists(pic_path):
                        os.remove(pic_path)
            except:
                pass
            
            await status.edit(f"✅ **Group {i+1} Created!** ({created}/{count})")
            await asyncio.sleep(3)
            
        except Exception as e:
            print(f"GC {i+1} error: {e}")
            failed += 1
            await asyncio.sleep(2)
    
    await status.edit(
        f"✅ **Group Creation Complete!**\n\n"
        f"📊 **Created:** {created}/{count}\n"
        f"❌ **Failed:** {failed}/{count}\n"
        f"🖼️ **Picture:** Set successfully"
    )
    asyncio.create_task(delete_after(status, 15.0))

async def download_picture(url):
    try:
        if not REQUESTS_AVAILABLE:
            return None
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            path = f"temp_pic_{randint(0,99999)}.jpg"
            with open(path, 'wb') as f:
                f.write(response.content)
            return path
        return None
    except:
        return None

@client.on(events.NewMessage(outgoing=True, pattern=r'\.giveadmin'))
async def giveadmin_cmd(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    managed_bots = get_user_bots(user_id)
    if not managed_bots:
        return await event.respond("❌ **No bots in your army!** Use `.setbots` to summon them.")
    status = await event.respond(f"🔍 **Elevating {len(managed_bots)} bots...**")
    rights = ChatAdminRights(
        change_info=True, post_messages=True, edit_messages=True,
        delete_messages=True, ban_users=True, invite_users=True,
        pin_messages=True, add_admins=False, anonymous=False,
        manage_call=True, other=True
    )
    try:
        full_chat = await client.get_entity(chat_id)
        input_chat = await client.get_input_entity(chat_id)
    except Exception as e:
        await status.edit(f"❌ **Error:** `{e}`")
        return
    admin_ids = set()
    try:
        async for admin in client.iter_participants(chat_id, filter=ChannelParticipantsAdmins):
            admin_ids.add(admin.id)
    except:
        pass
    already_admin = 0
    promoted = 0
    added = 0
    failed = 0
    total = len(managed_bots)
    rank_counter = 1
    for bot_username in managed_bots:
        try:
            await status.edit(f"⏳ **Processing @{bot_username}...**")
            bot_entity = await client.get_entity(bot_username)
            try:
                await client.get_participants(chat_id, filter=bot_entity.id)
                in_group = True
            except:
                in_group = False
            if not in_group:
                try:
                    if isinstance(full_chat, Channel):
                        await client(InviteToChannelRequest(
                            channel=input_chat,
                            users=[bot_entity]
                        ))
                    else:
                        await client(AddChatUserRequest(
                            chat_id=full_chat.id,
                            user_id=bot_entity,
                            fwd_limit=0
                        ))
                    added += 1
                    await asyncio.sleep(1)
                except Exception as e:
                    if "USER_ALREADY_PARTICIPANT" not in str(e):
                        print(f"Add error for {bot_username}: {e}")
            if bot_entity.id in admin_ids:
                already_admin += 1
                continue
            rank_name = f"𝗚𝖔𝖏𝖔God{rank_counter}"
            rank_counter += 1
            try:
                try:
                    await client(EditAdminRequest(
                        channel=input_chat,
                        user_id=bot_entity,
                        admin_rights=rights,
                        rank=rank_name
                    ))
                except TypeError:
                    await client(EditAdminRequest(
                        channel=input_chat,
                        user_id=bot_entity,
                        admin_rights=rights
                    ))
                promoted += 1
                admin_ids.add(bot_entity.id)
                await status.edit(f"👑 **@{bot_username} → {rank_name}!**")
            except Exception as e:
                error_msg = str(e)
                if "ADMIN_RANK_EMOJI_NOT_ALLOWED" in error_msg:
                    clean_rank = f"EG{rank_counter-1}"
                    try:
                        await client(EditAdminRequest(
                            channel=input_chat,
                            user_id=bot_entity,
                            admin_rights=rights,
                            rank=clean_rank
                        ))
                        promoted += 1
                        admin_ids.add(bot_entity.id)
                        await status.edit(f"👑 **@{bot_username} → {clean_rank}!**")
                    except:
                        failed += 1
                else:
                    failed += 1
            await asyncio.sleep(1.5)
        except Exception as e:
            print(f"Error with {bot_username}: {e}")
            failed += 1
    await status.edit(
        f"🤖 **Elevation Complete**\n\n"
        f"👑 **Already Elevated:** {already_admin}/{total}\n"
        f"✅ **Newly Elevated:** {promoted}/{total}\n"
        f"➕ **Summoned to Realm:** {added}/{total}\n"
        f"❌ **Failed:** {failed}/{total}\n\n"
        f"📊 **Total Bots:** {total}"
    )
    asyncio.create_task(delete_after(status, 15.0))

@client.on(events.NewMessage(outgoing=True, pattern=r'\.takeadmin'))
async def takeadmin_cmd(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    managed_bots = get_user_bots(user_id)
    if not managed_bots:
        return await event.respond("❌ **No bots in your army!**")
    status = await event.respond(f"⏳ **Demoting {len(managed_bots)} bots...**")
    try:
        full_chat = await client.get_entity(chat_id)
        input_chat = await client.get_input_entity(chat_id)
    except Exception as e:
        await status.edit(f"❌ **Error:** `{e}`")
        return
    empty_rights = ChatAdminRights(
        change_info=False, post_messages=False, edit_messages=False,
        delete_messages=False, ban_users=False, invite_users=False,
        pin_messages=False, add_admins=False, anonymous=False,
        manage_call=False, other=False
    )
    removed = 0
    failed = 0
    total = len(managed_bots)
    for bot_username in managed_bots:
        try:
            await status.edit(f"⏳ **Demoting @{bot_username}...** ({removed+1}/{total})")
            bot_entity = await client.get_entity(bot_username)
            try:
                await client(EditAdminRequest(
                    channel=input_chat,
                    user_id=bot_entity,
                    admin_rights=empty_rights,
                    rank=""
                ))
                removed += 1
            except Exception as e:
                error_msg = str(e)
                if "USER_NOT_PARTICIPANT" in error_msg or "NOT_MUTUAL_CONTACT" in error_msg:
                    print(f"@{bot_username} not in group")
                elif "USER_NOT_ADMIN" in error_msg:
                    removed += 1
                else:
                    print(f"Demote error for {bot_username}: {e}")
                    failed += 1
            await asyncio.sleep(1)
        except Exception as e:
            print(f"Error with {bot_username}: {e}")
            failed += 1
    await status.edit(
        f"✅ **Demotion Complete!**\n\n"
        f"👑 **Demoted:** {removed}/{total}\n"
        f"❌ **Failed:** {failed}/{total}\n"
        f"📊 **Total Bots:** {total}"
    )
    asyncio.create_task(delete_after(status, 10.0))
# ==================== COMPLETE GAME SYSTEM ====================

# ==================== GAME CODES ====================

GAME_CODES = {
    "ttt": {"name": "Tic-Tac-Toe", "emoji": "❌⭕"},
    "ttf": {"name": "Tic-Tac-Four", "emoji": "🎯"},
    "ex": {"name": "Elephant XO", "emoji": "🐘"},
    "cf": {"name": "Connect Four", "emoji": "🃏"},
    "rps": {"name": "Rock-Paper-Scissors", "emoji": "🪨📄✂️"},
    "rpsls": {"name": "RPS-Lizard-Spock", "emoji": "🦎🖖"},
    "rr": {"name": "Russian Roulette", "emoji": "🔫"},
    "c": {"name": "Checkers", "emoji": "👑"},
    "pc": {"name": "Pool Checkers", "emoji": "🎱"}
}

GAME_SEARCH = {
    "ttt": "tic tac toe",
    "ttf": "tic tac four",
    "ex": "elephant xo",
    "cf": "connect four",
    "rps": "rock paper scissors",
    "rpsls": "rps lizard spock",
    "rr": "russian roulette",
    "c": "checkers",
    "pc": "pool checkers"
}

# ==================== TRUTH OR DARE TASKS ====================

TRUTH_QUESTIONS = [
    "What's your biggest fear? 😨",
    "Have you ever lied to your best friend? 🤥",
    "What's the most embarrassing thing you've done? 😳",
    "Who do you have a crush on? 😍",
    "What's your deepest secret? 🤐",
    "Have you ever cheated on a test? 📝",
    "What's the worst thing you've ever said to someone? 😬",
    "Have you ever been in love? 💕",
    "What's your biggest regret? 😔",
    "Do you have any guilty pleasures? 😈",
    "What's the most illegal thing you've done? 🚔",
    "Have you ever ghosted someone? 👻",
    "What's your biggest insecurity? 😰",
    "Have you ever lied to your parents? 🙊",
    "What's the most awkward date you've been on? 😅",
    "Have you ever broken someone's heart? 💔",
    "What's the biggest lie you've ever told? 🤥",
    "Have you ever stalked someone on social media? 👀",
    "What's your most embarrassing childhood memory? 🧒",
    "Have you ever peed in a pool? 🏊"
]

DARE_TASKS = [
    "Do 20 pushups right now 💪",
    "Sing your favorite song loudly 🎤",
    "Do a silly dance for 30 seconds 💃",
    "Send a random emoji to the last person you texted 📱",
    "Do your best impression of a celebrity 🎭",
    "Tell a joke to the chat 😂",
    "Do 10 jumping jacks 🏃",
    "Post a funny meme in the chat 🖼️",
    "Do a handstand (if you can) 🙃",
    "Say the alphabet backwards 🔤",
    "Speak in an accent for the next 5 minutes 🗣️",
    "Take a selfie and send it to the chat 📸",
    "Do 15 squats 🦵",
    "Imitate a famous person 🎬",
    "Tell a funny story 🗣️",
    "Do a magic trick 🪄",
    "Write a poem on the spot 📝",
    "Do 5 pushups with one hand 💪",
    "Speak in rhymes for 2 minutes 🎵",
    "Make everyone in the chat laugh 😆"
]

CATEGORY_TASKS = {
    "1": {"truth": "What's your deepest fear? 😨", "dare": "Do 20 pushups 💪"},
    "2": {"truth": "What's your biggest regret? 😔", "dare": "Sing a song loudly 🎤"},
    "3": {"truth": "Who's your celebrity crush? 😍", "dare": "Do a silly dance 💃"},
    "4": {"truth": "What's your guilty pleasure? 😈", "dare": "Tell a joke 😂"},
    "5": {"truth": "What's the worst date you've been on? 😅", "dare": "Do 10 jumping jacks 🏃"}
}

# ==================== DECIDE COMMAND ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.decide\s+(.+)"))
async def decide_cmd(event):
    """Get divine decision for your question"""
    question = event.pattern_match.group(1)
    
    decisions = [
        "Yes ✅", "No ❌", "Maybe 🤔", "Definitely 💯", 
        "Absolutely not 🚫", "Ask again later ⏳", 
        "The stars say yes ✨", "The cosmos says no 🌌",
        "It is certain 🔮", "Outlook good 🌤️", 
        "Cannot predict now 🌧️", "Very doubtful 🤨", 
        "Without a doubt ✅", "Don't count on it ❌",
        "Signs point to yes 🔮", "Better not tell you now 🤐",
        "Concentrate and ask again 🧘", "Don't do it! 🛑",
        "Go for it! 🚀", "Not in this lifetime ⏰"
    ]
    
    answer = random.choice(decisions)
    
    response = (
        "❓ **Divine Decision**\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📝 **Question:** {question}\n\n"
        f"🔮 **Answer:** {answer}\n\n"
        "🤖 *Powered by 𝗚𝖔𝖏𝖔 God*"
    )
    
    await event.reply(response)

# ==================== DICE COMMAND ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.dice$"))
async def dice_cmd(event):
    """Roll a dice"""
    result = random.randint(1, 6)
    dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    
    response = (
        "🎲 **Dice Roll**\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{dice_faces[result-1]} **{result}**\n\n"
        "🤖 *Powered by 𝗚𝖔𝖏𝖔 God*"
    )
    
    await event.reply(response)

# ==================== COIN COMMAND ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.coin$"))
async def coin_cmd(event):
    """Flip a coin"""
    result = random.choice(["Heads", "Tails"])
    emoji = "🪙" if result == "Heads" else "🪙"
    
    response = (
        f"{emoji} **Coin Flip**\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        f"**{result}!**\n\n"
        "🤖 *Powered by 𝗚𝖔𝖏𝖔 God*"
    )
    
    await event.reply(response)

# ==================== TASK COMMAND ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.task(?:\s+([1-5]))?"))
async def task_cmd(event):
    """Get a random task (truth or dare)"""
    category = event.pattern_match.group(1)
    
    # If category provided, use category tasks
    if category and category in CATEGORY_TASKS:
        choice = random.choice(["truth", "dare"])
        task = CATEGORY_TASKS[category][choice]
        label = "Truth" if choice == "truth" else "Dare"
        emoji = "💭" if choice == "truth" else "⚡"
        
        response = (
            f"{emoji} **{label} Task** (Category {category})\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            f"`{task}`\n\n"
            "🤖 *Powered by 𝗚𝖔𝖏𝖔 God*"
        )
        await event.reply(response)
        return
    
    # Random task
    choice = random.choice(["truth", "dare"])
    
    if choice == "truth":
        task = random.choice(TRUTH_QUESTIONS)
        response = (
            "💭 **Truth Task**\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            f"`{task}`\n\n"
            "🤖 *Powered by 𝗚𝖔𝖏𝖔 God*"
        )
    else:
        task = random.choice(DARE_TASKS)
        response = (
            "⚡ **Dare Task**\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            f"`{task}`\n\n"
            "🤖 *Powered by 𝗚𝖔𝖏𝖔 God*"
        )
    
    await event.reply(response)

# ==================== TRUTH COMMAND ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.truth(?:\s+([1-5]))?"))
async def truth_cmd(event):
    """Get a truth question"""
    category = event.pattern_match.group(1)
    
    if category and category in CATEGORY_TASKS:
        task = CATEGORY_TASKS[category]["truth"]
        response = (
            f"💭 **Truth Question** (Category {category})\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            f"`{task}`\n\n"
            "🤖 *Powered by 𝗚𝖔𝖏𝖔 God*"
        )
    else:
        task = random.choice(TRUTH_QUESTIONS)
        response = (
            "💭 **Truth Question**\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            f"`{task}`\n\n"
            "🤖 *Powered by 𝗚𝖔𝖏𝖔 God*"
        )
    
    await event.reply(response)

# ==================== DARE COMMAND ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.dare(?:\s+([1-5]))?"))
async def dare_cmd(event):
    """Get a dare"""
    category = event.pattern_match.group(1)
    
    if category and category in CATEGORY_TASKS:
        task = CATEGORY_TASKS[category]["dare"]
        response = (
            f"⚡ **Dare** (Category {category})\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            f"`{task}`\n\n"
            "🤖 *Powered by 𝗚𝖔𝖏𝖔 God*"
        )
    else:
        task = random.choice(DARE_TASKS)
        response = (
            "⚡ **Dare**\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            f"`{task}`\n\n"
            "🤖 *Powered by 𝗚𝖔𝖏𝖔 God*"
        )
    
    await event.reply(response)

# ==================== INLINE GAME COMMAND ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.game(?:\s+(.+))?"))
async def game_cmd(event):
    """Play inline games via @inlinegamesbot"""
    args = event.pattern_match.group(1)
    
    # Show available games if no args
    if not args:
        game_list = (
            "🎮 **Available Games**\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        )
        for code, info in GAME_CODES.items():
            game_list += f"• `.game {code}` - {info['emoji']} {info['name']}\n"
        game_list += "\n💡 **Example:** `.game ttt` to play Tic-Tac-Toe\n"
        game_list += "🤖 *Powered by 𝗚𝖔𝖏𝖔 God*"
        return await event.reply(game_list)
    
    # Get the game code
    code = args.strip().lower()
    
    # Check if valid game
    if code not in GAME_SEARCH:
        game_list = "❌ **Invalid game code!**\n\n"
        game_list += "🎮 **Available Games:**\n"
        for c, info in GAME_CODES.items():
            game_list += f"• `{c}` - {info['emoji']} {info['name']}\n"
        game_list += "\n💡 **Example:** `.game ttt`"
        return await event.reply(game_list)
    
    search_term = GAME_SEARCH[code]
    game_name = GAME_CODES[code]['name']
    game_emoji = GAME_CODES[code]['emoji']
    
    status = await event.reply(f"{game_emoji} **Starting {game_name}...**")
    
    try:
        # Search for the specific game
        results = await event.client.inline_query("@inlinegamesbot", search_term)
        
        if not results:
            await status.edit(f"❌ **No results found for {game_name}**\n\nTry: `.game` to see all games")
            return
        
        # Get the reply target
        reply_to = event.reply_to_msg_id
        
        # Try multiple results if first one fails
        for i, result in enumerate(results[:5]):
            try:
                await result.click(
                    event.chat_id,
                    reply_to=reply_to,
                    hide_via=True
                )
                await event.delete()
                await status.delete()
                return
            except Exception as e:
                if i == len(results[:5]) - 1:
                    raise e
                continue
        
    except Exception as e:
        await status.edit(f"❌ **Failed to start {game_name}:** {str(e)[:100]}\n\nTry: `.game` to see all games")

# ==================== GAME HELP COMMAND ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.gamehelp$"))
async def gamehelp_cmd(event):
    """Show detailed game help"""
    help_text = (
        "🎮 **Game Help**\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📋 **Available Games:**\n\n"
    )
    
    for code, info in GAME_CODES.items():
        help_text += f"🔹 **`.game {code}`** - {info['emoji']} {info['name']}\n"
    
    help_text += "\n━━━━━━━━━━━━━━━━━━━━━━\n"
    help_text += "🎯 **Truth or Dare:**\n"
    help_text += "• `.task` - Random truth or dare\n"
    help_text += "• `.truth` - Truth question\n"
    help_text += "• `.dare` - Dare challenge\n"
    help_text += "• `.task 3` - Category specific\n\n"
    
    help_text += "🎲 **Other Games:**\n"
    help_text += "• `.dice` - Roll a dice\n"
    help_text += "• `.coin` - Flip a coin\n"
    help_text += "• `.decide <question>` - Divine decision\n\n"
    
    help_text += "💡 **Usage:** `.game <code>`\n"
    help_text += "📌 **Example:** `.game ttt` to play Tic-Tac-Toe\n"
    help_text += "🔄 **Reply to a message** to play there\n"
    help_text += "🤖 *Powered by 𝗚𝖔𝖏𝖔 God*"
    
    await event.reply(help_text)

# ==================== GAMES MENU COMMAND ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.games$"))
async def games_menu_cmd(event):
    """Show games menu with buttons"""
    menu_text = (
        "🎮 **Games Menu**\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "🎯 **Choose a game to play:**"
    )
    
    buttons = []
    row = []
    for code, info in GAME_CODES.items():
        button_text = f"{info['emoji']} {info['name']}"
        row.append(Button.inline(button_text, f"game_{code}"))
        if len(row) == 2:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)
    
    # Add Truth/Dare buttons
    buttons.append([
        Button.inline("💭 Truth", b"game_truth"),
        Button.inline("⚡ Dare", b"game_dare")
    ])
    
    # Add Dice/Coin buttons
    buttons.append([
        Button.inline("🎲 Dice", b"game_dice"),
        Button.inline("🪙 Coin", b"game_coin")
    ])
    
    await event.reply(menu_text, buttons=buttons)

# ==================== GAME CALLBACK HANDLER ====================

@client.on(events.CallbackQuery(pattern=r"game_(.*)"))
async def game_callback(event):
    """Handle game button clicks"""
    data = event.data_match.group(1).decode()
    
    if data == "truth":
        task = random.choice(TRUTH_QUESTIONS)
        await event.edit(
            f"💭 **Truth Question**\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            f"`{task}`\n\n"
            "🤖 *Powered by 𝗚𝖔𝖏𝖔 God*"
        )
        return
    
    if data == "dare":
        task = random.choice(DARE_TASKS)
        await event.edit(
            f"⚡ **Dare**\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            f"`{task}`\n\n"
            "🤖 *Powered by 𝗚𝖔𝖏𝖔 God*"
        )
        return
    
    if data == "dice":
        result = random.randint(1, 6)
        dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
        await event.edit(
            f"🎲 **Dice Roll**\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            f"{dice_faces[result-1]} **{result}**\n\n"
            "🤖 *Powered by 𝗚𝖔𝖏𝖔 God*"
        )
        return
    
    if data == "coin":
        result = random.choice(["Heads", "Tails"])
        emoji = "🪙" if result == "Heads" else "🪙"
        await event.edit(
            f"{emoji} **Coin Flip**\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            f"**{result}!**\n\n"
            "🤖 *Powered by 𝗚𝖔𝖏𝖔 God*"
        )
        return
    
    # Handle game codes
    code = data
    if code not in GAME_SEARCH:
        await event.answer("❌ Game not found!", alert=True)
        return
    
    search_term = GAME_SEARCH[code]
    game_name = GAME_CODES[code]['name']
    game_emoji = GAME_CODES[code]['emoji']
    
    await event.answer(f"🎮 Starting {game_name}...")
    
    try:
        results = await event.client.inline_query("@inlinegamesbot", search_term)
        
        if not results:
            await event.edit(f"❌ **{game_emoji} {game_name} not available**")
            return
        
        for result in results[:5]:
            try:
                await result.click(
                    event.chat_id,
                    reply_to=event.reply_to_msg_id,
                    hide_via=True
                )
                await event.delete()
                return
            except:
                continue
                
    except Exception as e:
        await event.edit(f"❌ **Failed to start {game_name}:** {str(e)[:100]}")

# ==================== GAME SHORTCUTS ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.ttt$"))
async def ttt_shortcut(event):
    """Quick Tic-Tac-Toe shortcut"""
    try:
        results = await event.client.inline_query("@inlinegamesbot", "tic tac toe")
        if results:
            for result in results[:3]:
                try:
                    await result.click(
                        event.chat_id,
                        reply_to=event.reply_to_msg_id,
                        hide_via=True
                    )
                    await event.delete()
                    return
                except:
                    continue
    except Exception as e:
        await event.reply(f"❌ **Failed to start Tic-Tac-Toe:** {str(e)[:100]}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.connect4$"))
async def connect4_shortcut(event):
    """Quick Connect Four shortcut"""
    try:
        results = await event.client.inline_query("@inlinegamesbot", "connect four")
        if results:
            for result in results[:3]:
                try:
                    await result.click(
                        event.chat_id,
                        reply_to=event.reply_to_msg_id,
                        hide_via=True
                    )
                    await event.delete()
                    return
                except:
                    continue
    except Exception as e:
        await event.reply(f"❌ **Failed to start Connect Four:** {str(e)[:100]}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.rps$"))
async def rps_shortcut(event):
    """Quick Rock-Paper-Scissors shortcut"""
    try:
        results = await event.client.inline_query("@inlinegamesbot", "rock paper scissors")
        if results:
            for result in results[:3]:
                try:
                    await result.click(
                        event.chat_id,
                        reply_to=event.reply_to_msg_id,
                        hide_via=True
                    )
                    await event.delete()
                    return
                except:
                    continue
    except Exception as e:
        await event.reply(f"❌ **Failed to start Rock-Paper-Scissors:** {str(e)[:100]}")
# ==================== EMOJI GAMES COMMANDS ====================

DART_EMOJI = "🎯"
DICE_EMOJI = "🎲"
BALL_EMOJI = "🏀"
FOOT_EMOJI = "⚽"
SLOT_EMOJI = "🎰"
BOWL_EMOJI = "🎳"

@client.on(events.NewMessage(pattern=r"^\.dart(?:\s+([1-6]))?$", outgoing=True))
async def dart(event):
    try:
        await event.delete()
        result = random.randint(1, 6)
        dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
        await event.reply(f"🎯 **Dart Throw**\n━━━━━━━━━━━━━━━━━━━━━━\n{dice_faces[result-1]} **{result}**")
    except Exception as e:
        print(f"Dart error: {e}")

@client.on(events.NewMessage(pattern=r"^\.dice(?:\s+([1-6]))?$", outgoing=True))
async def dice_emoji(event):
    try:
        await event.delete()
        result = random.randint(1, 6)
        dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
        await event.reply(f"🎲 **Dice Roll**\n━━━━━━━━━━━━━━━━━━━━━━\n{dice_faces[result-1]} **{result}**")
    except Exception as e:
        print(f"Dice error: {e}")

@client.on(events.NewMessage(pattern=r"^\.bb(?:\s+([1-5]))?$", outgoing=True))
async def basketball(event):
    try:
        await event.delete()
        result = random.randint(1, 5)
        await event.reply(f"🏀 **Basketball**\n━━━━━━━━━━━━━━━━━━━━━━\n**{result}** point{'s' if result > 1 else ''}!")
    except Exception as e:
        print(f"Basketball error: {e}")

@client.on(events.NewMessage(pattern=r"^\.fb(?:\s+([1-5]))?$", outgoing=True))
async def football(event):
    try:
        await event.delete()
        result = random.randint(1, 5)
        await event.reply(f"⚽ **Football**\n━━━━━━━━━━━━━━━━━━━━━━\n**{result}** goal{'s' if result > 1 else ''}!")
    except Exception as e:
        print(f"Football error: {e}")

@client.on(events.NewMessage(pattern=r"^\.jp(?:\s+([1-9]|[1-5][0-9]|6[0-4]))?$", outgoing=True))
async def jackpot(event):
    try:
        await event.delete()
        result = random.randint(1, 64)
        await event.reply(f"🎰 **Jackpot**\n━━━━━━━━━━━━━━━━━━━━━━\n💎 **{result}**")
    except Exception as e:
        print(f"Jackpot error: {e}")

@client.on(events.NewMessage(pattern=r"^\.bowl(?:\s+([1-6]))?$", outgoing=True))
async def bowling(event):
    try:
        await event.delete()
        result = random.randint(1, 6)
        pins = "🟢" * result + "⚪" * (6 - result)
        await event.reply(f"🎳 **Bowling**\n━━━━━━━━━━━━━━━━━━━━━━\n{pins}\n**{result}** pins knocked!")
    except Exception as e:
        print(f"Bowling error: {e}")

# ==================== ANIMATIONS COMMANDS ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.muth$"))
async def muth_animation(event):
    """Muth animation with emojis"""
    if event.fwd_from:
        return
    
    animation_interval = 0.3
    animation_chars = [
        "8✊️===D",
        "8=✊️==D",
        "8==✊️=D",
        "8===✊️D",
        "8==✊️=D",
        "8=✊️==D",
        "8✊️===D",
        "8✊️===D",
        "8=✊️==D",
        "8==✊️=D",
        "8===✊️D",
        "8==✊️=D",
        "8=✊️==D",
        "8✊️===D",
        "8✊️===D",
        "8=✊️==D",
        "8==✊️=D",
        "8===✊️D",
        "8==✊️=D",
        "8=✊️==D",
        "8✊️===D",
        "8✊️===D",
        "8=✊️==D",
        "8==✊️=D",
        "8===✊️D",
        "8==✊️=D",
        "8=✊️==D",
        "8✊️===D",
        "8✊️===D",
        "8=✊️==D",
        "8==✊️=D",
        "8===✊️D",
        "8==✊️=D",
        "8=✊️==D",
        "8✊️===D",
        "8✊️===D",
        "8=✊️==D",
        "8==✊️=D",
        "8===✊️D",
        "8==✊️=D",
        "8=✊️==D",
        "8✊️===D",
        "8✊️===D",
        "8=✊️==D",
        "8==✊️=D",
        "8===✊️D",
        "8==✊️=D",
        "8=✊️==D",
        "8✊️===D",
        "8✊️===D",
        "8=✊️==D",
        "8==✊️=D",
        "8===✊️D",
        "8==✊️=D",
        "8=✊️==D",
        "8✊️===D",
        "8✊️===D",
        "8=✊️==D",
        "8==✊️=D",
        "8===✊️D",
        "8==✊️=D",
        "8=✊️==D",
        "8✊️===D",
        "8✊️===D",
        "8=✊️==D",
        "8==✊️=D",
        "8===✊️D",
        "8==✊️=D",
        "8=✊️==D",
        "8✊️===D",
        "8✊️===D",
        "8=✊️==D",
        "8==✊️=D",
        "8===✊️D",
        "8==✊️=D",
        "8=✊️==D",
        "8✊️===D",
        "8✊️===D",
        "8=✊️==D",
        "8==✊️=D",
        "8===✊️D",
        "8==✊️=D",
        "8=✊️==D",
        "8✊️===D",
        "8✊️===D",
        "8=✊️==D",
        "8==✊️=D",
        "8===✊️D",
        "8==✊️=D",
        "8=✊️==D",
        "8✊️===D",
        "8✊️===D",
        "8=✊️==D",
        "8==✊️=D",
        "8===✊️D💦",
        "8==✊️=D💦💦",
        "8=✊️==D💦💦💦"
    ]
    
    await event.edit("🔥 Starting muth...")
    
    for i in range(len(animation_chars) * 1):
        try:
            await event.edit(animation_chars[i % len(animation_chars)])
            await asyncio.sleep(animation_interval)
        except MessageNotModifiedError:
            pass
    
    await event.edit("8=✊️==D💦💦💦\n\n\n\n💦 **Lund Ne Faasi Laga Li!**")

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.animate\s+([\s\S]+)$'))
async def animate_text(event):
    """Typing animation ✍️"""
    text = event.pattern_match.group(1).strip()
    if not text:
        return await event.reply("❗️ **Usage:** `.animate <text>`")
    
    msg = await event.reply("⏳")
    for i in range(1, len(text) + 1):
        new_text = text[:i]
        try:
            await msg.edit(new_text)
        except MessageNotModifiedError:
            pass
        await asyncio.sleep(0.05 + random.random() * 0.1)
    await asyncio.sleep(0.5)
    await msg.edit(f"✅ **{text}**")

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.spinner(?:\s+(\d+))?$'))
async def spinner_animation(event):
    """Spinner animation 🔄"""
    sec = event.pattern_match.group(1)
    total = int(sec) if sec and sec.isdigit() else 5
    
    frames = ["⬆️", "↗️", "➡️", "↘️", "⬇️", "↙️", "⬅️", "↖️"]
    msg = await event.reply("⏳ **Starting spinner...**")
    
    start = asyncio.get_event_loop().time()
    idx = 0
    
    while asyncio.get_event_loop().time() - start < total:
        frame = frames[idx % len(frames)]
        try:
            await msg.edit(f"{frame}")
        except MessageNotModifiedError:
            pass
        idx += 1
        await asyncio.sleep(0.15)
    
    await msg.edit("✅ **Spinner done!**")
@client.on(events.NewMessage(outgoing=True, pattern=r'^\.love(?:\s+(.+))?'))
async def love_animation(event):
    """Love heart animation ❤️"""
    hearts = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🖤", "🤍", "🤎", "💔", "❤️‍🔥", "❤️‍🩹", "❣️", "💕", "💞", "💓", "💗", "💖", "💘", "💟", "🩶", "🩵", "🩷"]
    
    user_name = None
    mention_text = event.pattern_match.group(1)
    
    if mention_text:
        try:
            user = await event.client.get_entity(mention_text.strip())
            user_name = utils.get_display_name(user)
        except:
            user_name = mention_text.strip()
    
    if not user_name and event.is_reply:
        reply_msg = await event.get_reply_message()
        if reply_msg:
            user = await reply_msg.get_sender()
            user_name = utils.get_display_name(user)
    
    msg = await event.reply(hearts[0])
    
    for i in range(len(hearts) * 3):
        try:
            await msg.edit(hearts[i % len(hearts)])
        except MessageNotModifiedError:
            pass
        await asyncio.sleep(0.3)
    
    final_msg = f"💖 **I love you {user_name}** 💖" if user_name else "💖 **I love you!** 💖"
    await msg.edit(final_msg)

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.hearts\s+([\s\S]+)$'))
async def hearts_animation(event):
    """Hearts animation 💖"""
    text = event.pattern_match.group(1).strip()
    if not text:
        return await event.reply("❗️ **Usage:** `.hearts <text>`")
    
    heart_emojis = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🖤", "🤍", "🤎", "💔", "❤️‍🔥", "❤️‍🩹", "❣️", "💕", "💞", "💓", "💗", "💖", "💘", "💟", "🩶", "🩵", "🩷"]
    
    msg = await event.reply(f"❤️ {text} ❤️")
    frames = []
    
    for heart in heart_emojis[:8]:
        frames.append(f"{heart} {text} {heart}")
    
    for i in range(len(frames) * 2):
        try:
            await msg.edit(frames[i % len(frames)])
        except MessageNotModifiedError:
            pass
        await asyncio.sleep(0.6)
    
    await msg.edit(f"❤️ **{text}** ❤️")

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.countdown\s+(\d+)$'))
async def countdown_animation(event):
    """Countdown animation ⏰"""
    start_n = int(event.pattern_match.group(1))
    
    if start_n > 60:
        return await event.reply("❌ **Maximum countdown is 60 seconds!**")
    
    msg = await event.reply(f"⏰ **Starting countdown from {start_n}...**")
    await asyncio.sleep(1)
    
    for n in range(start_n, -1, -1):
        try:
            await msg.edit(f"⏰ **{n}**")
        except MessageNotModifiedError:
            pass
        await asyncio.sleep(1.0)
    
    await msg.edit("🎉 **BOOM! Countdown finished!**")

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.blink(?:\s+(\d+))?\s+([\s\S]+)$'))
async def blink_animation(event):
    """Blink animation 👁️"""
    match = event.pattern_match
    sec_str = match.group(1)
    text = match.group(2).strip()
    
    if not text:
        return await event.reply("❗️ **Usage:** `.blink <sec> <text>` or `.blink <text>` (default 5 seconds)")
    
    duration = int(sec_str) if sec_str and sec_str.isdigit() else 5
    hidden_space = ""
    
    msg = await event.reply("⏳ **Starting blink animation...**")
    start_time = time.time()
    blink_count = 0
    
    while time.time() - start_time < duration:
        if blink_count % 2 == 0:
            try:
                await msg.edit(f"✨ **{text}** ✨")
            except MessageNotModifiedError:
                pass
        else:
            try:
                await msg.edit(f"‎‎  ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ")
            except MessageNotModifiedError:
                pass
        blink_count += 1
        await asyncio.sleep(0.5)
    
    await msg.edit(f"✨ **{text}** ✨")
    await asyncio.sleep(0.5)

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.matrix(?:\s+(\d+))?$'))
async def matrix_animation(event):
    """Matrix digital rain animation 💻"""
    sec = event.pattern_match.group(1)
    duration = int(sec) if sec and sec.isdigit() else 10
    
    chars = "01"
    msg = await event.reply("⏳ **Starting Matrix...**")
    
    start_time = time.time()
    while time.time() - start_time < duration:
        lines = []
        for _ in range(10):
            line = ''.join(random.choice(chars) for _ in range(20))
            lines.append(line)
        
        matrix_text = "💻 **Matrix Rain**\n\n" + "\n".join(lines)
        try:
            await msg.edit(matrix_text)
        except MessageNotModifiedError:
            pass
        await asyncio.sleep(0.1)
    
    await msg.edit("✅ **Matrix complete!**")

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.wave\s+([\s\S]+)$'))
async def wave_animation(event):
    """Wave text animation 🌊"""
    text = event.pattern_match.group(1).strip()
    if not text:
        return await event.reply("❗️ **Usage:** `.wave <text>`")
    
    msg = await event.reply("🌊 **Starting wave...**")
    frames = []
    
    for offset in range(5):
        wave_text = ""
        for i, char in enumerate(text):
            if (i + offset) % 4 < 2:
                wave_text += char.upper()
            else:
                wave_text += char.lower()
        frames.append(f"🌊 {wave_text} 🌊")
    
    for i in range(len(frames) * 2):
        try:
            await msg.edit(frames[i % len(frames)])
        except MessageNotModifiedError:
            pass
        await asyncio.sleep(0.3)
    
    await msg.edit(f"🌊 **{text}** 🌊")

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.rainbow\s+([\s\S]+)$'))
async def rainbow_animation(event):
    """Rainbow text animation 🌈"""
    text = event.pattern_match.group(1).strip()
    if not text:
        return await event.reply("❗️ **Usage:** `.rainbow <text>`")
    
    colors = ["🔴", "🟠", "🟡", "🟢", "🔵", "🟣"]
    msg = await event.reply("🌈 **Starting rainbow...**")
    
    for i in range(len(colors) * 2):
        color = colors[i % len(colors)]
        try:
            await msg.edit(f"{color} **{text}** {color}")
        except MessageNotModifiedError:
            pass
        await asyncio.sleep(0.3)
    
    await msg.edit(f"🌈 **{text}** 🌈")

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.glitch\s+([\s\S]+)$'))
async def glitch_animation(event):
    """Glitch text animation ⚡"""
    text = event.pattern_match.group(1).strip()
    if not text:
        return await event.reply("❗️ **Usage:** `.glitch <text>`")
    
    msg = await event.reply("⚡ **Starting glitch...**")
    
    for i in range(10):
        glitch_text = ""
        for char in text:
            if random.random() < 0.3:
                glitch_text += random.choice(["#", "*", "&", "%", "$", "@"])
            else:
                glitch_text += char
        
        try:
            await msg.edit(f"⚡ **{glitch_text}** ⚡")
        except MessageNotModifiedError:
            pass
        await asyncio.sleep(0.1)
    
    await msg.edit(f"⚡ **{text}** ⚡")

# ==================== TOOLS COMMANDS ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.id(?:\s+(.+))?"))
async def id_cmd(event):
    target_input = event.pattern_match.group(1)
    
    if target_input:
        try:
            user = await event.client.get_entity(target_input)
            name = utils.get_display_name(user)
            await event.reply(f"🆔 **ID for {name}:** `{user.id}`")
            return
        except:
            pass
    
    if event.is_reply:
        reply_msg = await event.get_reply_message()
        sender = await reply_msg.get_sender()
        name = utils.get_display_name(sender)
        await event.reply(f"🆔 **ID for {name}:** `{sender.id}`")
        return
    
    me = await event.client.get_me()
    await event.reply(f"🆔 **Your ID:** `{me.id}`\n📝 **Username:** @{me.username if me.username else 'None'}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.uptime"))
async def uptime_cmd(event):
    uptime_seconds = int((datetime.now() - START_TIME).total_seconds())
    await event.reply(f"🕐 **𝗚𝖔𝖏𝖔 Uptime:** {readable_time(uptime_seconds)}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.ping"))
async def ping_cmd(event):
    start = time.time()
    msg = await event.reply("🏓 **Pinging...**")
    end = time.time()
    latency = (end - start) * 1000
    await msg.edit(f"🏓 **Pong!**\n⚡ **Latency:** `{latency:.2f}ms`\n🤖 **Status:** Online")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.clock"))
async def clock_cmd(event):
    now = datetime.now()
    indian_time = now.strftime("%I:%M:%S %p")
    indian_date = now.strftime("%B %d, %Y")
    await event.reply(f"🕐 **Sacred Indian Time**\n━━━━━━━━━━━━━━━━━━━━━━\n⏰ **Time:** {indian_time}\n📅 **Date:** {indian_date}\n🌏 **Timezone:** IST (UTC+5:30)")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.rand\s+(\d+)\s+(\d+)"))
async def rand_cmd(event):
    try:
        min_num = int(event.pattern_match.group(1))
        max_num = int(event.pattern_match.group(2))
        if min_num > max_num:
            min_num, max_num = max_num, min_num
        result = random.randint(min_num, max_num)
        await event.reply(f"🎲 **Random number:** `{result}`\n📊 **Range:** {min_num} - {max_num}")
    except:
        await event.reply("❌ **Usage:** `.rand <min> <max>`")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.pick\s+(.+)"))
async def pick_cmd(event):
    try:
        items = event.pattern_match.group(1).split(',')
        items = [item.strip() for item in items if item.strip()]
        if not items:
            return await event.reply("❌ **No items provided!**")
        chosen = random.choice(items)
        await event.reply(f"🎯 **Random pick:** `{chosen}`\n📋 **From:** {len(items)} items")
    except:
        await event.reply("❌ **Usage:** `.pick item1,item2,item3`")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.count\s+(.+)"))
async def count_cmd(event):
    text = event.pattern_match.group(1)
    char_count = len(text)
    word_count = len(text.split())
    await event.reply(f"📊 **Text Analysis**\n━━━━━━━━━━━━━━━━━━━━━━\n📝 **Characters:** {char_count}\n📝 **Words:** {word_count}\n📏 **Length:** {char_count} chars")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.date"))
async def date_cmd(event):
    now = datetime.now()
    await event.reply(f"📅 **Current Date:** {now.strftime('%A, %B %d, %Y')}")

# ==================== PROTECT COMMANDS ====================

def load_safe_users():
    try:
        if SAFE_USERS_FILE.exists():
            with open(SAFE_USERS_FILE, 'r') as f:
                return json.load(f)
    except:
        pass
    return {}

def save_safe_users(data):
    try:
        with open(SAFE_USERS_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    except:
        pass

safe_users = load_safe_users()

@client.on(events.NewMessage(outgoing=True, pattern=r"\.safe(?:\s+(.+))?"))
async def safe_cmd(event):
    target_input = event.pattern_match.group(1)
    target_user = None
    
    if target_input:
        try:
            target_user = await event.client.get_entity(target_input)
        except:
            pass
    
    if not target_user and event.is_reply:
        reply_msg = await event.get_reply_message()
        target_user = await reply_msg.get_sender()
    
    if not target_user:
        return await event.reply("❌ **Provide a mortal to protect!**\nUsage: `.safe @username`")
    
    uid = str(target_user.id)
    if uid not in safe_users:
        safe_users[uid] = {
            "name": utils.get_display_name(target_user),
            "protected_since": datetime.now().isoformat()
        }
        save_safe_users(safe_users)
        await event.reply(f"🛡️ **{utils.get_display_name(target_user)} is now under divine protection!**")
    else:
        await event.reply(f"🛡️ **{utils.get_display_name(target_user)} is already protected!**")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.unsafe(?:\s+(.+))?"))
async def unsafe_cmd(event):
    target_input = event.pattern_match.group(1)
    target_user = None
    
    if target_input:
        try:
            target_user = await event.client.get_entity(target_input)
        except:
            pass
    
    if not target_user and event.is_reply:
        reply_msg = await event.get_reply_message()
        target_user = await reply_msg.get_sender()
    
    if not target_user:
        return await event.reply("❌ **Provide a mortal to remove protection!**\nUsage: `.unsafe @username`")
    
    uid = str(target_user.id)
    if uid in safe_users:
        del safe_users[uid]
        save_safe_users(safe_users)
        await event.reply(f"🚫 **{utils.get_display_name(target_user)} is no longer protected!**")
    else:
        await event.reply(f"🚫 **{utils.get_display_name(target_user)} is not protected!**")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.safelist"))
async def safelist_cmd(event):
    if not safe_users:
        return await event.reply("📋 **No protected souls found!**")
    
    text = "🛡️ **Protected Souls**\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
    for uid, data in safe_users.items():
        text += f"👤 **{data['name']}**\n"
        text += f"   🆔 `{uid}`\n"
        text += f"   📅 Protected: {data['protected_since'][:10]}\n\n"
    
    await event.reply(text)

@client.on(events.NewMessage(outgoing=True, pattern=r"\.clearsafe"))
async def clearsafe_cmd(event):
    if not safe_users:
        return await event.reply("❌ **No protected souls to clear!**")
    
    count = len(safe_users)
    safe_users.clear()
    save_safe_users(safe_users)
    await event.reply(f"⚠️ **Cleared {count} protected souls!**")

# ==================== CLONE COMMANDS ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.clone"))
async def clone_cmd(event):
    if not event.is_reply:
        return await event.reply("❌ **Reply to a user's message to clone them!**")
    
    reply = await event.get_reply_message()
    target_user = await reply.get_sender()
    
    if target_user.id == OWNER_ID:
        return await event.reply("❌ **Cannot clone the God!**")
    
    try:
        await client(UpdateProfileRequest(
            first_name=target_user.first_name or "",
            last_name=target_user.last_name or ""
        ))
        
        # Clone profile photo
        try:
            photos = await client.get_profile_photos(target_user.id)
            if photos:
                photo = photos[0]
                await client(DeletePhotosRequest([photo]))
                # Wait a bit for deletion
                await asyncio.sleep(1)
                # Get and set the photo
                downloaded = await client.download_media(photo)
                if downloaded:
                    await client(UploadProfilePhotoRequest(
                        file=await client.upload_file(downloaded)
                    ))
                    os.remove(downloaded)
        except:
            pass
        
        await event.reply(f"👥 **Identity stolen from {utils.get_display_name(target_user)}!**\n\n⚡ You are now their clone!")
    except Exception as e:
        await event.reply(f"❌ **Failed to clone:** {str(e)}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.revert"))
async def revert_cmd(event):
    try:
        await client(UpdateProfileRequest(
            first_name=DEFAULTUSER,
            last_name=""
        ))
        await event.reply("🔄 **True identity restored!**\n\n⚡ You are back to being the Almighty!")
    except Exception as e:
        await event.reply(f"❌ **Failed to revert:** {str(e)}")

# ==================== ADMIN COMMANDS ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.ban(?:\s+(.+))?"))
async def ban_cmd(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    
    if not await is_user_admin(client, chat_id, user_id):
        return await event.reply("❌ **You need to be an admin to use this command!**")
    
    target_user = await get_target_user(event, event.pattern_match.group(1))
    if not target_user:
        return await event.reply("❌ **Provide a user or reply to their message!**")
    
    if target_user.id == OWNER_ID:
        return await event.reply("❌ **Cannot ban the God!**")
    
    try:
        await client(EditBannedRequest(
            chat_id,
            target_user.id,
            ChatBannedRights(until_date=None, view_messages=True)
        ))
        await event.reply(f"🚫 **{utils.get_display_name(target_user)} has been banished!**")
    except Exception as e:
        await event.reply(f"❌ **Failed to ban:** {str(e)}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.unban(?:\s+(.+))?"))
async def unban_cmd(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    
    if not await is_user_admin(client, chat_id, user_id):
        return await event.reply("❌ **You need to be an admin to use this command!**")
    
    target_user = await get_target_user(event, event.pattern_match.group(1))
    if not target_user:
        return await event.reply("❌ **Provide a user or reply to their message!**")
    
    try:
        await client(EditBannedRequest(
            chat_id,
            target_user.id,
            ChatBannedRights(until_date=None, view_messages=False)
        ))
        await event.reply(f"✅ **{utils.get_display_name(target_user)} has been forgiven!**")
    except Exception as e:
        await event.reply(f"❌ **Failed to unban:** {str(e)}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.kick(?:\s+(.+))?"))
async def kick_cmd(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    
    if not await is_user_admin(client, chat_id, user_id):
        return await event.reply("❌ **You need to be an admin to use this command!**")
    
    target_user = await get_target_user(event, event.pattern_match.group(1))
    if not target_user:
        return await event.reply("❌ **Provide a user or reply to their message!**")
    
    if target_user.id == OWNER_ID:
        return await event.reply("❌ **Cannot kick the God!**")
    
    try:
        await client.kick_participant(chat_id, target_user.id)
        await event.reply(f"👢 **{utils.get_display_name(target_user)} has been kicked!**")
    except Exception as e:
        await event.reply(f"❌ **Failed to kick:** {str(e)}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.promote\s+(.+)"))
async def promote_cmd(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    
    if not await is_user_admin(client, chat_id, user_id):
        return await event.reply("❌ **You need to be an admin to use this command!**")
    
    args = event.text.split(maxsplit=1)
    if len(args) < 2:
        return await event.reply("❌ **Usage:** `.promote <rank>` (reply to user)")
    
    rank = clean_rank_name(args[1])
    
    if not event.is_reply:
        return await event.reply("❌ **Reply to the user you want to promote!**")
    
    reply = await event.get_reply_message()
    target_user = await reply.get_sender()
    
    if target_user.id == OWNER_ID:
        return await event.reply("❌ **Cannot promote the God!**")
    
    try:
        await client(EditAdminRequest(
            chat_id,
            target_user.id,
            ChatAdminRights(
                change_info=True,
                post_messages=True,
                edit_messages=True,
                delete_messages=True,
                ban_users=True,
                invite_users=True,
                pin_messages=True,
                add_admins=True,
                anonymous=False,
                manage_call=True,
                other=True
            ),
            rank=rank
        ))
        await event.reply(f"👑 **{utils.get_display_name(target_user)} promoted to {rank}!**")
    except Exception as e:
        await event.reply(f"❌ **Failed to promote:** {str(e)}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.demote(?:\s+(.+))?"))
async def demote_cmd(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    
    if not await is_user_admin(client, chat_id, user_id):
        return await event.reply("❌ **You need to be an admin to use this command!**")
    
    target_user = await get_target_user(event, event.pattern_match.group(1))
    if not target_user:
        return await event.reply("❌ **Provide a user or reply to their message!**")
    
    if target_user.id == OWNER_ID:
        return await event.reply("❌ **Cannot demote the God!**")
    
    try:
        await client(EditAdminRequest(
            chat_id,
            target_user.id,
            ChatAdminRights(
                change_info=False,
                post_messages=False,
                edit_messages=False,
                delete_messages=False,
                ban_users=False,
                invite_users=False,
                pin_messages=False,
                add_admins=False,
                anonymous=False,
                manage_call=False,
                other=False
            ),
            rank=""
        ))
        await event.reply(f"⬇️ **{utils.get_display_name(target_user)} has been demoted!**")
    except Exception as e:
        await event.reply(f"❌ **Failed to demote:** {str(e)}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.pin(?:\s+(.+))?"))
async def pin_cmd(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    
    if not await is_user_admin(client, chat_id, user_id):
        return await event.reply("❌ **You need to be an admin to use this command!**")
    
    if not event.is_reply:
        return await event.reply("❌ **Reply to a message to pin it!**")
    
    reply = await event.get_reply_message()
    
    try:
        await client.pin_message(chat_id, reply.id)
        await event.reply(f"📌 **Message pinned successfully!**")
    except Exception as e:
        await event.reply(f"❌ **Failed to pin:** {str(e)}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.unpin(?:\s+(.+))?"))
async def unpin_cmd(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    
    if not await is_user_admin(client, chat_id, user_id):
        return await event.reply("❌ **You need to be an admin to use this command!**")
    
    try:
        await client.unpin_message(chat_id)
        await event.reply(f"📌 **Message unpinned successfully!**")
    except Exception as e:
        await event.reply(f"❌ **Failed to unpin:** {str(e)}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.pinall"))
async def pinall_cmd(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    
    if not await is_user_admin(client, chat_id, user_id):
        return await event.reply("❌ **You need to be an admin to use this command!**")
    
    status = await event.reply("📌 **Pinning all messages...**")
    pinned = 0
    
    async for msg in client.iter_messages(chat_id, limit=100):
        try:
            await client.pin_message(chat_id, msg.id)
            pinned += 1
            await asyncio.sleep(0.5)
        except:
            pass
    
    await status.edit(f"✅ **Pinned {pinned} messages!**")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.unpinall"))
async def unpinall_cmd(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    
    if not await is_user_admin(client, chat_id, user_id):
        return await event.reply("❌ **You need to be an admin to use this command!**")
    
    try:
        await client.unpin_message(chat_id)
        await event.reply("🔓 **All messages unpinned!**")
    except Exception as e:
        await event.reply(f"❌ **Failed to unpin all:** {str(e)}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.slowmode\s+(\d+)"))
async def slowmode_cmd(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    seconds = int(event.pattern_match.group(1))
    
    if not await is_user_admin(client, chat_id, user_id):
        return await event.reply("❌ **You need to be an admin to use this command!**")
    
    if seconds < 0 or seconds > 3600:
        return await event.reply("❌ **Slowmode must be between 0 and 3600 seconds!**")
    
    try:
        await client(EditAdminRequest(
            chat_id,
            user_id,
            ChatAdminRights(
                change_info=True,
                post_messages=True,
                edit_messages=True,
                delete_messages=True,
                ban_users=True,
                invite_users=True,
                pin_messages=True,
                add_admins=False,
                anonymous=False,
                manage_call=True,
                other=True
            ),
            rank="",
            slowmode_seconds=seconds
        ))
        await event.reply(f"⏱️ **Slowmode set to {seconds} seconds!**")
    except Exception as e:
        await event.reply(f"❌ **Failed to set slowmode:** {str(e)}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.lock"))
async def lock_cmd(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    
    if not await is_user_admin(client, chat_id, user_id):
        return await event.reply("❌ **You need to be an admin to use this command!**")
    
    try:
        await client(EditBannedRequest(
            chat_id,
            0,
            ChatBannedRights(until_date=None, send_messages=True)
        ))
        await event.reply("🔒 **Chat locked!**\n\nOnly admins can send messages.")
    except Exception as e:
        await event.reply(f"❌ **Failed to lock chat:** {str(e)}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.unlock"))
async def unlock_cmd(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    
    if not await is_user_admin(client, chat_id, user_id):
        return await event.reply("❌ **You need to be an admin to use this command!**")
    
    try:
        await client(EditBannedRequest(
            chat_id,
            0,
            ChatBannedRights(until_date=None, send_messages=False)
        ))
        await event.reply("🔓 **Chat unlocked!**\n\nEveryone can send messages again.")
    except Exception as e:
        await event.reply(f"❌ **Failed to unlock chat:** {str(e)}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.adminonly"))
async def adminonly_cmd(event):
    chat_id = str(event.chat_id)
    admin_only_chats[chat_id] = True
    
    try:
        with open(ADMIN_ONLY_FILE, 'w') as f:
            json.dump(admin_only_chats, f)
    except:
        pass
    
    await event.reply("🔐 **Admin-only mode ENABLED!**\nOnly admins may speak.")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.adminoff"))
async def adminoff_cmd(event):
    chat_id = str(event.chat_id)
    if chat_id in admin_only_chats:
        del admin_only_chats[chat_id]
        
        try:
            with open(ADMIN_ONLY_FILE, 'w') as f:
                json.dump(admin_only_chats, f)
        except:
            pass
        
        await event.reply("🔓 **Admin-only mode DISABLED!**\nEveryone may speak now.")

# ==================== ADMIN ONLY HANDLER ====================

@client.on(events.NewMessage(incoming=True))
async def admin_only_handler(event):
    chat_id = str(event.chat_id)
    if chat_id in admin_only_chats:
        if event.sender_id != OWNER_ID and event.sender_id != 𝗚𝖔𝖏𝖔_BOT_OWNER:
            try:
                if not await is_user_admin(event.client, event.chat_id, event.sender_id):
                    if event.message.text and not event.message.text.startswith('.'):
                        await event.delete()
            except:
                pass

# ==================== MUTE HANDLER ====================

@client.on(events.NewMessage(incoming=True))
async def mute_handler(event):
    """Delete messages from muted users"""
    if event.chat_id in muted_users:
        if event.sender_id in muted_users[event.chat_id]:
            if event.sender_id != OWNER_ID and event.sender_id != 𝗚𝖔𝖏𝖔_BOT_OWNER:
                    try:
                        await event.delete()
                    except:
                        pass

# ==================== MODERATION COMMANDS ====================
@client.on(events.NewMessage(outgoing=True, pattern=r'\.muteall'))
async def muteall_cmd(event):
    auto_delete_chats[event.chat_id] = True
    await event.respond("🔇 **All non-protected souls have been silenced!**")

@client.on(events.NewMessage(outgoing=True, pattern=r'\.unmuteall'))
async def unmuteall_cmd(event):
    if event.chat_id in auto_delete_chats:
        del auto_delete_chats[event.chat_id]
    await event.respond("🔊 **All voices have been restored!**")

@client.on(events.NewMessage(outgoing=True, pattern=r'\.mute'))
async def mute_cmd(event):
    if event.is_reply:
        reply = await event.get_reply_message()
        user_id = reply.sender_id
        
        if event.chat_id not in muted_users:
            muted_users[event.chat_id] = set()
        muted_users[event.chat_id].add(user_id)
        
        await event.respond("🤐 **The mortal has been silenced!**")
    else:
        await event.respond("❌ **Reply to a mortal to silence them!**")

@client.on(events.NewMessage(outgoing=True, pattern=r'\.unmute'))
async def unmute_cmd(event):
    if event.is_reply:
        reply = await event.get_reply_message()
        user_id = reply.sender_id
        
        if event.chat_id in muted_users and user_id in muted_users[event.chat_id]:
            muted_users[event.chat_id].remove(user_id)
            if not muted_users[event.chat_id]:
                del muted_users[event.chat_id]
            await event.respond("🗣️ **The mortal's voice has been restored!**")
        else:
            await event.respond("❌ **This mortal is not muted!**")
    else:
        await event.respond("❌ **Reply to a mortal to restore their voice!**")

# ==================== AFK COMMANDS ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.afk(?:\s+(.*))?"))
async def afk_cmd(event):
    reason = event.pattern_match.group(1) or "Away from keyboard"
    uid = str(event.sender_id)
    
    afk_users[uid] = {
        "reason": reason,
        "start_time": time.time(),
        "start_date": datetime.now().isoformat()
    }
    
    try:
        with open(AFK_USERS_FILE, 'w') as f:
            json.dump(afk_users, f)
    except:
        pass
    
    if uid not in afk_stats:
        afk_stats[uid] = {"total_afk": 0, "total_time": 0}
    afk_stats[uid]["total_afk"] += 1
    
    try:
        with open(AFK_STATS_FILE, 'w') as f:
            json.dump(afk_stats, f)
    except:
        pass
    
    quote = random.choice(AFK_QUOTES)
    await event.reply(f"🌙 **{quote}**\n\n📝 **Reason:** {reason}\n⏰ **Started:** {datetime.now().strftime('%H:%M:%S')}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.unafk"))
async def unafk_cmd(event):
    uid = str(event.sender_id)
    
    if uid in afk_users:
        start_time = afk_users[uid]["start_time"]
        duration = int(time.time() - start_time)
        
        if uid in afk_stats:
            afk_stats[uid]["total_time"] += duration
        
        del afk_users[uid]
        
        try:
            with open(AFK_USERS_FILE, 'w') as f:
                json.dump(afk_users, f)
        except:
            pass
        
        await event.reply(f"☀️ **Awakened!**\n⏱️ **Slumber duration:** {readable_time(duration)}")
    else:
        await event.reply("❌ **You are not in slumber!**")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.afkstats"))
async def afkstats_cmd(event):
    if not afk_stats:
        return await event.reply("📊 **No AFK statistics available!**")
    
    stats_text = "📊 **AFK Statistics**\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
    total_afk = 0
    total_time = 0
    
    for uid, data in afk_stats.items():
        try:
            user = await client.get_entity(int(uid))
            name = user.first_name or "Unknown"
        except:
            name = "Unknown"
        
        stats_text += f"👤 **{name}**\n"
        stats_text += f"   📝 AFK Count: {data['total_afk']}\n"
        stats_text += f"   ⏱️ Total Time: {readable_time(data['total_time'])}\n\n"
        
        total_afk += data['total_afk']
        total_time += data['total_time']
    
    stats_text += f"━━━━━━━━━━━━━━━━━━━━━━\n"
    stats_text += f"📊 **Total AFKs:** {total_afk}\n"
    stats_text += f"⏱️ **Total Time:** {readable_time(total_time)}"
    
    await event.reply(stats_text)

@client.on(events.NewMessage(outgoing=True, pattern=r"\.afkquote"))
async def afkquote_cmd(event):
    quote = random.choice(AFK_QUOTES)
    await event.reply(f"💭 **Random AFK Quote:**\n\n{quote}")

# ==================== AFK AUTO-RESPONSE HANDLER ====================

@client.on(events.NewMessage(incoming=True))
async def afk_response_handler(event):
    if event.is_private and event.sender_id != OWNER_ID and event.sender_id != 𝗚𝖔𝖏𝖔_BOT_OWNER:
        if afk_users:
            if str(event.sender_id) in afk_users:
                return
            for uid, data in afk_users.items():
                if str(event.sender_id) != uid:
                    try:
                        if event.message.text and not event.message.text.startswith('.'):
                            duration = int(time.time() - data["start_time"])
                            response = f"🌙 **{data['reason']}**\n⏱️ **AFK since:** {readable_time(duration)} ago"
                            await event.reply(response)
                            break
                    except:
                        pass

# ==================== RAID COMMANDS ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.crtraid\s+(\w+)\s+(.+)"))
async def create_raid_cmd(event):
    name = event.pattern_match.group(1)
    template = event.pattern_match.group(2).strip()
    
    success, message = custom_raid_manager.create_raid(name, template)
    await event.reply(f"🎭 **Custom Raid Creation**\n━━━━━━━━━━━━━━━━━━━━━━\n\n{message}")
    
    if success:
        await event.reply(
            f"💡 **How to use:**\n"
            f"• `.raid {name} @user` - Start custom raid\n"
            f"• `.replyraid {name}` - Start custom reply raid\n\n"
            f"📝 **Template:** `{template}`"
        )

@client.on(events.NewMessage(outgoing=True, pattern=r"\.delraid\s+(\w+)"))
async def delete_raid_cmd(event):
    name = event.pattern_match.group(1)
    success, message = custom_raid_manager.delete_raid(name)
    await event.reply(f"🎭 **Delete Custom Raid**\n━━━━━━━━━━━━━━━━━━━━━━\n\n{message}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.listraids$"))
async def list_raids_cmd(event):
    message = custom_raid_manager.list_raids()
    await event.reply(message)


# ==================== RAID COMMAND ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.raid\s+(\w+)(?:\s+(.+))?"))
async def raid_cmd(event):
    try:
        raid_name = event.pattern_match.group(1).lower()
        target_input = event.pattern_match.group(2) if event.pattern_match.group(2) else None
        
        custom_raid = custom_raid_manager.get_raid(raid_name)
        
        if custom_raid:
            target_user = None
            if target_input:
                target_user = await get_target_user(event, target_input)
            elif event.is_reply:
                target_user = await get_target_user(event, None)
            
            if not target_user:
                return await event.reply(f"❌ **Provide a mortal to raid!**\nUsage: `.raid {raid_name} @username`")
            
            if target_user.id == 𝗚𝖔𝖏𝖔_BOT_OWNER:
                return await event.reply("❌ **Cannot raid the God!**")
            
            target_name = utils.get_display_name(target_user)
            target_id = target_user.id
            chat_id = event.chat_id
            
            me = await event.client.get_me()
            self_name = me.first_name or "𝗚𝖔𝖏𝖔"
            template = custom_raid["template"]
            is_multi = custom_raid.get("is_multi", False)
            messages = custom_raid.get("messages", [template])
            
            active_raids["users"][target_id] = True
            active_raids["stats"][target_id] = 0
            active_raids["start_time"][target_id] = time.time()
            active_raids["raid_type"][target_id] = "custom"
            active_raids["chat_id"][target_id] = chat_id
            active_raids["msg_index"][target_id] = 0
            active_raids["target_name"][target_id] = target_name
            active_raids["custom_name"][target_id] = raid_name
            active_raids["template"][target_id] = template
            active_raids["is_multi"][target_id] = is_multi
            active_raids["messages"][target_id] = messages
            
            await event.reply(
                f"{RAID_BANNER}\n"
                f"🎭 **Custom Raid Started!**\n"
                f"🎯 **Target:** {target_name}\n"
                f"📝 **Type:** {raid_name.title()}\n"
                f"🔄 **Rotation:** {'✅ ENABLED' if is_multi else '❌ DISABLED'}\n"
                f"📨 **Messages:** {len(messages)}\n"
                f"📋 **Template:** {template[:50]}{'...' if len(template) > 50 else ''}"
            )
            
            count = 0
            msg_index = 0
            while target_id in active_raids["users"] and count < RAID_LIMIT:
                emoji = next(ROTATING_EMOJIS)
                
                msg = custom_raid_manager.generate_message(
                    template, target_name, self_name, emoji, msg_index
                )
                
                response = f"[{target_name}](tg://user?id={target_id}) {msg}"
                await event.reply(response)
                active_raids["stats"][target_id] += 1
                count += 1
                msg_index += 1
                
                if RAID_DELAY > 0:
                    await asyncio.sleep(RAID_DELAY)
            
            if target_id in active_raids["users"]:
                for key in ["users", "stats", "start_time", "raid_type", "chat_id", 
                           "msg_index", "template", "target_name", "custom_name", 
                           "is_multi", "messages"]:
                    if target_id in active_raids.get(key, {}):
                        del active_raids[key][target_id]
            return
        
        valid = ["hindi", "english", "flirthin", "flirteng"]
        if raid_name not in valid:
            available = list(custom_raid_manager.raids.keys()) + valid
            return await event.reply(f"❌ **Invalid raid type!**\n\nAvailable: {', '.join(available)}\n\n💡 Create custom: `.crtraid <name> <template>`")
        
        target_user = None
        if target_input:
            target_user = await get_target_user(event, target_input)
        elif event.is_reply:
            target_user = await get_target_user(event, None)
        
        if not target_user:
            return await event.reply("❌ **Provide a mortal to raid!**\nUsage: `.raid english @username`")
        
        if target_user.id == 𝗚𝖔𝖏𝖔_BOT_OWNER:
            return await event.reply("❌ **Cannot raid the God!**")
        
        target_name = utils.get_display_name(target_user)
        target_id = target_user.id
        chat_id = event.chat_id
        
        templates = {
            "hindi": HINDI_RAID,
            "english": ENGLISH_RAID,
            "flirthin": FLIRTHIN_RAID,
            "flirteng": FLIRTENG_RAID
        }
        template_list = templates.get(raid_name, ENGLISH_RAID)
        
        active_raids["users"][target_id] = True
        active_raids["stats"][target_id] = 0
        active_raids["start_time"][target_id] = time.time()
        active_raids["raid_type"][target_id] = raid_name
        active_raids["chat_id"][target_id] = chat_id
        active_raids["msg_index"][target_id] = 0
        active_raids["template"][target_id] = template_list
        active_raids["target_name"][target_id] = target_name
        
        type_names = {"hindi": "🔥 HINDI", "english": "⚡ ENGLISH", "flirthin": "💕 FLIRTHIN", "flirteng": "💖 FLIRTENG"}
        
        await event.reply(
            f"{RAID_BANNER}\n"
            f"🎭 **Raid Started!**\n"
            f"🎯 **Target:** {target_name}\n"
            f"🗣️ **Type:** {type_names[raid_name]}"
        )
        
        count = 0
        msg_index = 0
        while target_id in active_raids["users"] and count < RAID_LIMIT:
            emoji = next(ROTATING_EMOJIS)
            msg = template_list[msg_index % len(template_list)].format(emoji=emoji)
            response = f"[{target_name}](tg://user?id={target_id}) {msg}"
            await event.reply(response)
            active_raids["stats"][target_id] += 1
            count += 1
            msg_index += 1
            if RAID_DELAY > 0:
                await asyncio.sleep(RAID_DELAY)
        
        if target_id in active_raids["users"]:
            del active_raids["users"][target_id]
            del active_raids["stats"][target_id]
            del active_raids["start_time"][target_id]
            del active_raids["raid_type"][target_id]
            del active_raids["chat_id"][target_id]
            del active_raids["msg_index"][target_id]
            del active_raids["template"][target_id]
            if target_id in active_raids["target_name"]:
                del active_raids["target_name"][target_id]
    except Exception as e:
        await event.reply(f"❌ **Raid failed:** {str(e)[:100]}")

# ==================== REPLY RAID COMMAND ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.replyraid\s+(\w+)(?:\s+(.+))?"))
async def replyraid_cmd(event):
    try:
        raid_name = event.pattern_match.group(1).lower()
        target_input = event.pattern_match.group(2) if event.pattern_match.group(2) else None
        
        custom_raid = custom_raid_manager.get_raid(raid_name)
        
        if custom_raid:
            target_user = None
            if target_input:
                target_user = await get_target_user(event, target_input)
            elif event.is_reply:
                target_user = await get_target_user(event, None)
            
            if not target_user:
                return await event.reply(f"❌ **Reply to a user's message or provide username!**\nUsage: `.replyraid {raid_name} @user`")
            
            if target_user.id == 𝗚𝖔𝖏𝖔_BOT_OWNER:
                return await event.reply("❌ **Cannot raid the God!**")
            
            if target_user.id in active_raids["users"]:
                return await event.reply(f"❌ **{utils.get_display_name(target_user)} is already being raided!**")
            
            target_name = utils.get_display_name(target_user)
            target_id = target_user.id
            
            me = await event.client.get_me()
            self_name = me.first_name or "𝗚𝖔𝖏𝖔"
            template = custom_raid["template"]
            is_multi = custom_raid.get("is_multi", False)
            messages = custom_raid.get("messages", [template])
            
            active_raids["users"][target_id] = True
            active_raids["stats"][target_id] = 0
            active_raids["start_time"][target_id] = time.time()
            active_raids["raid_type"][target_id] = "custom"
            active_raids["chat_id"][target_id] = event.chat_id
            active_raids["msg_index"][target_id] = 0
            active_raids["target_name"][target_id] = target_name
            active_raids["custom_name"][target_id] = raid_name
            active_raids["template"][target_id] = template
            active_raids["is_multi"][target_id] = is_multi
            active_raids["messages"][target_id] = messages
            
            await event.reply(
                f"{RAID_BANNER}\n"
                f"🎭 **Custom Reply Raid Activated!**\n"
                f"🎯 **Target:** {target_name}\n"
                f"📝 **Type:** {raid_name.title()}\n"
                f"🔄 **Rotation:** {'✅ ENABLED' if is_multi else '❌ DISABLED'}\n"
                f"📨 **Messages:** {len(messages)}\n"
                f"📋 **Template:** {template[:50]}{'...' if len(template) > 50 else ''}"
            )
            return
        
        valid = ["hindi", "english", "flirthin", "flirteng"]
        if raid_name not in valid:
            available = list(custom_raid_manager.raids.keys()) + valid
            return await event.reply(f"❌ **Invalid raid type!**\n\nAvailable: {', '.join(available)}\n\n💡 Create custom: `.crtraid <name> <template>`")
        
        target_user = None
        if target_input:
            target_user = await get_target_user(event, target_input)
        elif event.is_reply:
            target_user = await get_target_user(event, None)
        
        if not target_user:
            return await event.reply("❌ **Provide a mortal for reply raid!**\nUsage: `.replyraid english @username`")
        
        if target_user.id == 𝗚𝖔𝖏𝖔_BOT_OWNER:
            return await event.reply("❌ **Cannot raid the God!**")
        
        if target_user.id in active_raids["users"]:
            return await event.reply(f"❌ **{utils.get_display_name(target_user)} is already being raided!**")
        
        target_name = utils.get_display_name(target_user)
        
        templates = {
            "hindi": HINDI_RAID,
            "english": ENGLISH_RAID,
            "flirthin": FLIRTHIN_RAID,
            "flirteng": FLIRTENG_RAID
        }
        template_list = templates.get(raid_name, ENGLISH_RAID)
        
        active_raids["users"][target_user.id] = True
        active_raids["stats"][target_user.id] = 0
        active_raids["start_time"][target_user.id] = time.time()
        active_raids["raid_type"][target_user.id] = raid_name
        active_raids["chat_id"][target_user.id] = event.chat_id
        active_raids["template"][target_user.id] = template_list
        active_raids["msg_index"][target_user.id] = 0
        active_raids["target_name"][target_user.id] = target_name
        
        type_names = {"hindi": "🔥 HINDI", "english": "⚡ ENGLISH", "flirthin": "💕 FLIRTHIN", "flirteng": "💖 FLIRTENG"}
        
        await event.reply(
            f"{RAID_BANNER}\n"
            f"🎭 **Reply Raid Activated!**\n"
            f"🎯 **Target:** {target_name}\n"
            f"🗣️ **Type:** {type_names[raid_name]}"
        )
    except Exception as e:
        await event.reply(f"❌ **Reply raid failed:** {str(e)[:100]}")

# ==================== REPLY RAID HANDLER ====================

@client.on(events.NewMessage)
async def reply_raid_handler(event):
    if event.sender_id in active_raids["users"]:
        try:
            uid = event.sender_id
            raid_type = active_raids["raid_type"].get(uid, "english")
            target_name = active_raids["target_name"].get(uid, "User")
            
            me = await event.client.get_me()
            self_name = me.first_name or "𝗚𝖔𝖏𝖔"
            
            if raid_type == "custom":
                template = active_raids["template"].get(uid, "{target} {emoji}")
                msg_index = active_raids.get("msg_index", {}).get(uid, 0)
                is_multi = active_raids.get("is_multi", {}).get(uid, False)
                
                emoji = next(ROTATING_EMOJIS)
                msg = custom_raid_manager.generate_message(
                    template, target_name, self_name, emoji, msg_index
                )
                response = f"[{target_name}](tg://user?id={uid}) {msg}"
                await event.reply(response)
                
                if is_multi:
                    messages = active_raids.get("messages", {}).get(uid, [template])
                    if messages:
                        active_raids["msg_index"][uid] = (msg_index + 1) % len(messages)
                else:
                    active_raids["msg_index"][uid] = msg_index + 1
            else:
                template_list = active_raids["template"].get(uid, ENGLISH_RAID)
                msg_index = active_raids["msg_index"].get(uid, 0)
                emoji = next(ROTATING_EMOJIS)
                msg = template_list[msg_index % len(template_list)].format(emoji=emoji)
                response = f"[{target_name}](tg://user?id={uid}) {msg}"
                await event.reply(response)
                active_raids["msg_index"][uid] = msg_index + 1
            
            active_raids["stats"][uid] += 1
            
        except Exception as e:
            print(f"Reply raid error: {e}")

# ==================== STOP RAID COMMANDS ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.stopraid(?:\s+(.+))?"))
async def stopraid_cmd(event):
    target_input = event.pattern_match.group(1) if event.pattern_match.group(1) else None
    chat_id = event.chat_id
    
    if target_input:
        target_user = await get_target_user(event, target_input)
        if not target_user:
            return await event.reply("❌ **Could not find the mortal!**")
        uid = target_user.id
        if uid in active_raids["users"] and active_raids["chat_id"].get(uid) == chat_id:
            hits = active_raids["stats"][uid]
            dur = int(time.time() - active_raids["start_time"][uid])
            target_name = active_raids["target_name"].get(uid, utils.get_display_name(target_user))
            del active_raids["users"][uid]
            del active_raids["stats"][uid]
            del active_raids["start_time"][uid]
            del active_raids["raid_type"][uid]
            del active_raids["chat_id"][uid]
            del active_raids["msg_index"][uid]
            del active_raids["template"][uid]
            if uid in active_raids["target_name"]:
                del active_raids["target_name"][uid]
            if uid in active_raids["custom_name"]:
                del active_raids["custom_name"][uid]
            if uid in active_raids["is_multi"]:
                del active_raids["is_multi"][uid]
            if uid in active_raids["messages"]:
                del active_raids["messages"][uid]
            await event.reply(f"🛑 **Raid stopped for {target_name}!**\n💥 **Messages:** {hits}\n⏱️ **Duration:** {dur}s")
        else:
            await event.reply(f"❌ **No raid for {utils.get_display_name(target_user)} in this realm!**")
    else:
        stopped = 0
        to_remove = []
        for uid, chat in active_raids["chat_id"].items():
            if chat == chat_id:
                to_remove.append(uid)
                stopped += 1
        if stopped == 0:
            return await event.reply("❌ **No raids in this realm!**")
        for uid in to_remove:
            hits = active_raids["stats"][uid]
            dur = int(time.time() - active_raids["start_time"][uid])
            target_name = active_raids["target_name"].get(uid, "Unknown")
            del active_raids["users"][uid]
            del active_raids["stats"][uid]
            del active_raids["start_time"][uid]
            del active_raids["raid_type"][uid]
            del active_raids["chat_id"][uid]
            del active_raids["msg_index"][uid]
            del active_raids["template"][uid]
            if uid in active_raids["target_name"]:
                del active_raids["target_name"][uid]
            if uid in active_raids["custom_name"]:
                del active_raids["custom_name"][uid]
            if uid in active_raids["is_multi"]:
                del active_raids["is_multi"][uid]
            if uid in active_raids["messages"]:
                del active_raids["messages"][uid]
        await event.reply(f"?? **Stopped {stopped} raid(s) in this realm!**")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.stopraidall(?:\s+(.+))?"))
async def stopraidall_cmd(event):
    target_input = event.pattern_match.group(1) if event.pattern_match.group(1) else None
    
    if target_input:
        target_user = await get_target_user(event, target_input)
        if not target_user:
            return await event.reply("❌ **Could not find the mortal!**")
        uid = target_user.id
        if uid in active_raids["users"]:
            hits = active_raids["stats"][uid]
            dur = int(time.time() - active_raids["start_time"][uid])
            target_name = active_raids["target_name"].get(uid, utils.get_display_name(target_user))
            del active_raids["users"][uid]
            del active_raids["stats"][uid]
            del active_raids["start_time"][uid]
            del active_raids["raid_type"][uid]
            del active_raids["chat_id"][uid]
            del active_raids["msg_index"][uid]
            del active_raids["template"][uid]
            if uid in active_raids["target_name"]:
                del active_raids["target_name"][uid]
            if uid in active_raids["custom_name"]:
                del active_raids["custom_name"][uid]
            if uid in active_raids["is_multi"]:
                del active_raids["is_multi"][uid]
            if uid in active_raids["messages"]:
                del active_raids["messages"][uid]
            await event.reply(f"🛑 **Raid stopped globally for {target_name}!**\n💥 **Messages:** {hits}\n⏱️ **Duration:** {dur}s")
        else:
            await event.reply(f"❌ **No raid for {utils.get_display_name(target_user)} anywhere!**")
    else:
        if not active_raids["users"]:
            return await event.reply("❌ **No raids anywhere!**")
        count = len(active_raids["users"])
        total_hits = sum(active_raids["stats"].values())
        active_raids["users"].clear()
        active_raids["stats"].clear()
        active_raids["start_time"].clear()
        active_raids["raid_type"].clear()
        active_raids["chat_id"].clear()
        active_raids["msg_index"].clear()
        active_raids["template"].clear()
        active_raids["target_name"].clear()
        active_raids["custom_name"].clear()
        active_raids["is_multi"].clear()
        active_raids["messages"].clear()
        await event.reply(f"🛑 **Stopped {count} raid(s) globally!**\n💥 **Total messages:** {total_hits}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.raidinfo"))
async def raidinfo_cmd(event):
    if not active_raids["users"]:
        return await event.reply("📡 **No active raids!**")
    
    info = f"{RAID_BANNER}\n🎭 **Active Raids**\n⚙️ **Delay:** {RAID_DELAY}s\n\n"
    for uid in list(active_raids["users"].keys()):
        try:
            user = await client.get_entity(uid)
            dur = time.time() - active_raids["start_time"][uid]
            raid_type = active_raids["raid_type"].get(uid, "english").upper()
            target_name = active_raids["target_name"].get(uid, utils.get_display_name(user))
            
            is_multi = active_raids.get("is_multi", {}).get(uid, False)
            msg_index = active_raids.get("msg_index", {}).get(uid, 0)
            messages = active_raids.get("messages", {}).get(uid, [])
            
            if raid_type == "CUSTOM":
                custom_name = active_raids["custom_name"].get(uid, "Unknown")
                raid_display = f"CUSTOM ({custom_name})"
                rotation_status = "✅" if is_multi else "❌"
                if is_multi and messages:
                    total_msgs = len(messages)
                    current_idx = msg_index % total_msgs if total_msgs > 0 else 0
                    raid_display += f" [{current_idx+1}/{total_msgs}]"
            else:
                raid_display = raid_type
                rotation_status = "✅"
            
            info += f"🎯 **{target_name}**\n"
            info += f"💥 {active_raids['stats'][uid]} msgs | ⏱️ {int(dur)}s\n"
            info += f"🗣️ Type: {raid_display}\n"
            info += f"🔄 Rotation: {rotation_status}\n\n"
        except:
            info += f"🎯 User {uid}\n"
    await event.reply(info)

@client.on(events.NewMessage(outgoing=True, pattern=r"\.delayraid\s+([\d.]+)"))
async def delayraid_cmd(event):
    global RAID_DELAY
    try:
        new_delay = float(event.pattern_match.group(1))
        if new_delay < 0:
            return await event.reply("❌ **Delay cannot be negative!**")
        RAID_DELAY = new_delay
        await event.reply(f"⚙️ **Raid delay set to {RAID_DELAY}s**")
    except:
        await event.reply("❌ **Usage:** `.delayraid 0.05`")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.dreplyraid(?:\s+(.+))?"))
async def dreplyraid_cmd(event):
    try:
        target_input = event.pattern_match.group(1) if event.pattern_match.group(1) else None
        uid = None
        if target_input:
            target_user = await get_target_user(event, target_input)
            if target_user:
                uid = target_user.id
        elif event.is_reply:
            reply = await event.get_reply_message()
            uid = reply.sender_id
        else:
            return await event.reply("❌ **Provide a mortal or reply to stop reply raid!**\nUsage: `.dreplyraid @username`")
        
        if uid in active_raids["users"]:
            hits = active_raids["stats"][uid]
            dur = int(time.time() - active_raids["start_time"][uid])
            target_name = active_raids["target_name"].get(uid, "Unknown")
            del active_raids["users"][uid]
            del active_raids["stats"][uid]
            del active_raids["start_time"][uid]
            del active_raids["raid_type"][uid]
            del active_raids["chat_id"][uid]
            del active_raids["msg_index"][uid]
            del active_raids["template"][uid]
            if uid in active_raids["target_name"]:
                del active_raids["target_name"][uid]
            if uid in active_raids["custom_name"]:
                del active_raids["custom_name"][uid]
            if uid in active_raids["is_multi"]:
                del active_raids["is_multi"][uid]
            if uid in active_raids["messages"]:
                del active_raids["messages"][uid]
            await event.reply(f"🛑 **Reply raid stopped for {target_name}!**\n💥 **Messages:** {hits}\n⏱️ **Duration:** {dur}s")
        else:
            await event.reply("❌ **No active reply raid for this mortal!**")
    except Exception as e:
        await event.reply(f"❌ **Error:** {str(e)[:100]}")

# ==================== SPAM COMMANDS ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.spam(?:\s+(.*))?"))
async def spam_cmd(event):
    global spam_tasks
    
    if event.is_reply:
        reply_msg = await event.get_reply_message()
        if reply_msg.text:
            msg_text = reply_msg.text
        else:
            return await event.reply("❌ **Replied message has no text!**")
    else:
        msg_text = event.pattern_match.group(1)
        if not msg_text:
            return await event.reply("❌ **Usage:** `.spam <message>` or reply to a message")
    
    chat_id = event.chat_id
    if chat_id in spam_tasks:
        spam_tasks[chat_id].cancel()
        del spam_tasks[chat_id]
    
    status_msg = await event.reply(f"📢 **Spam started!**\n📝 {msg_text[:50]}{'...' if len(msg_text) > 50 else ''}\n⏱️ Delay: {spam_delay}s")
    
    async def spam_task():
        try:
            count = 0
            while True:
                await event.reply(msg_text)
                count += 1
                await asyncio.sleep(spam_delay)
        except asyncio.CancelledError:
            pass
    
    spam_tasks[chat_id] = asyncio.create_task(spam_task())
    await asyncio.sleep(1)
    await status_msg.edit(f"📢 **Spam running!**\n📝 {msg_text[:50]}{'...' if len(msg_text) > 50 else ''}\n⏱️ Delay: {spam_delay}s\n🛑 Use `.stopspam` to stop")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.stopspam"))
async def stopspam_cmd(event):
    global spam_tasks
    chat_id = event.chat_id
    
    if chat_id in spam_tasks:
        spam_tasks[chat_id].cancel()
        del spam_tasks[chat_id]
        await event.reply("🛑 **Spam stopped!**")
    else:
        await event.reply("❌ **No spam running in this chat!**")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.setspamdelay\s+([\d.]+)"))
async def setspamdelay_cmd(event):
    global spam_delay
    try:
        new_delay = float(event.pattern_match.group(1))
        if new_delay < 0:
            return await event.reply("❌ **Delay cannot be negative!**")
        spam_delay = new_delay
        await event.reply(f"⚙️ **Spam delay set to {spam_delay}s**")
    except:
        await event.reply("❌ **Usage:** `.setspamdelay 0.5`")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.stopallspam"))
async def stopallspam_cmd(event):
    global spam_tasks
    count = len(spam_tasks)
    for task in spam_tasks.values():
        task.cancel()
    spam_tasks.clear()
    await event.reply(f"🛑 **Stopped {count} spam tasks!**")

# ==================== ADVANCED SPAM ENGINE ====================

class CipherEliteSpamEngine:
    def __init__(self):
        self.spam_stats = {
            'total_sent': 0,
            'active_tasks': 0,
            'completed_operations': 0
        }
    
    async def execute_spam_operation(self, client, chat_id, message_content=None, 
                                   count=1, reply_to=None, delay=0, media_msg=None, 
                                   stop_event=None, operation_type="text"):
        sent_count = 0
        
        for i in range(count):
            if stop_event and stop_event.is_set():
                break
            
            try:
                if operation_type == "media" and media_msg:
                    await client.forward_messages(chat_id, media_msg)
                else:
                    await client.send_message(
                        chat_id,
                        message_content,
                        reply_to=reply_to
                    )
                
                sent_count += 1
                self.spam_stats['total_sent'] += 1
                
                if delay > 0:
                    await asyncio.sleep(delay)
                else:
                    await asyncio.sleep(0.1)
                    
            except Exception as e:
                print(f"❌ Spam Error: {e}")
                continue
        
        try:
            if stop_event:
                stop_event.set()
            task_list = cipher_spam_tasks.get(chat_id, [])
            if stop_event in task_list:
                task_list.remove(stop_event)
            if not task_list:
                cipher_spam_tasks.pop(chat_id, None)
            self.spam_stats['completed_operations'] += 1
        except Exception:
            pass
        
        return sent_count

spam_engine = CipherEliteSpamEngine()

@client.on(events.NewMessage(pattern=r"^\.dspam\s+(\d+)\s+(\d+\.?\d*)\s+(.+)$", outgoing=True))
async def delay_spam(event):
    try:
        count = int(event.pattern_match.group(1))
        delay = float(event.pattern_match.group(2))
        message_content = event.pattern_match.group(3).strip()
        
        if count <= 0 or count > 200:
            await event.reply("❌ **Invalid count!** Use 1-200 for delay spam")
            return
        
        if delay < 0 or delay > 60:
            await event.reply("❌ **Invalid delay!** Use 0-60 seconds")
            return
        
        chat_id = event.chat_id
        reply_to = event.reply_to_msg_id
        
        stop_event = asyncio.Event()
        if chat_id in cipher_spam_tasks:
            cipher_spam_tasks[chat_id].append(stop_event)
        else:
            cipher_spam_tasks[chat_id] = [stop_event]
        
        status_msg = await event.reply(f"🎭 **Delay Spam Engine**\n\n"
                                     f"📊 **Count:** {count} messages\n"
                                     f"⏱️ **Delay:** {delay}s\n"
                                     f"⚡ **Status:** Active...")
        
        await event.delete()
        
        sent_count = await spam_engine.execute_spam_operation(
            event.client, chat_id, message_content=message_content,
            count=count, reply_to=reply_to, delay=delay,
            stop_event=stop_event, operation_type="text"
        )
        
        await status_msg.edit(f"✅ **Delay Spam Complete**\n\n"
                             f"✅ **Sent:** {sent_count}/{count} messages")
        await asyncio.sleep(10)
        await status_msg.delete()
        
    except Exception as e:
        await event.reply(f"❌ **Error:** {str(e)[:100]}...")

@client.on(events.NewMessage(pattern=r"^\.mspam\s+(\d+)$", outgoing=True))
async def media_spam(event):
    try:
        count = int(event.pattern_match.group(1))
        
        if not event.is_reply:
            await event.reply("❌ **Reply to a media message!**")
            return
        
        if count <= 0 or count > 100:
            await event.reply("❌ **Invalid count!** Use 1-100")
            return
        
        reply_message = await event.get_reply_message()
        if not reply_message.media:
            await event.reply("❌ **No media found!**")
            return
        
        chat_id = event.chat_id
        
        stop_event = asyncio.Event()
        if chat_id in cipher_spam_tasks:
            cipher_spam_tasks[chat_id].append(stop_event)
        else:
            cipher_spam_tasks[chat_id] = [stop_event]
        
        media_type = "Unknown"
        if reply_message.photo:
            media_type = "📸 Image"
        elif reply_message.video:
            media_type = "🎬 Video"
        elif reply_message.document:
            media_type = "📄 Document"
        elif reply_message.sticker:
            media_type = "🎨 Sticker"
        
        status_msg = await event.reply(f"🎭 **Media Spam Engine**\n\n"
                                     f"📸 **Type:** {media_type}\n"
                                     f"📊 **Count:** {count} times\n"
                                     f"⚡ **Status:** Active...")
        
        await event.delete()
        
        sent_count = await spam_engine.execute_spam_operation(
            event.client, chat_id, count=count, media_msg=reply_message,
            stop_event=stop_event, operation_type="media"
        )
        
        await status_msg.edit(f"✅ **Media Spam Complete**\n\n"
                             f"✅ **Sent:** {sent_count}/{count} media files")
        await asyncio.sleep(10)
        await status_msg.delete()
        
    except Exception as e:
        await event.reply(f"❌ **Error:** {str(e)[:100]}...")

@client.on(events.NewMessage(pattern=r"^\.listspam$", outgoing=True))
async def list_spam(event):
    if not cipher_spam_tasks:
        await event.reply("✅ **No active spam operations**")
        return
    
    list_msg = f"🎭 **Active Spam Operations**\n\n"
    list_msg += f"⚡ **Total Sent:** {spam_engine.spam_stats['total_sent']}\n"
    list_msg += f"🔄 **Completed:** {spam_engine.spam_stats['completed_operations']}\n\n"
    
    for chat_id, task_list in cipher_spam_tasks.items():
        if task_list:
            try:
                chat = await event.client.get_entity(chat_id)
                chat_name = getattr(chat, 'title', getattr(chat, 'first_name', f'Chat {chat_id}'))
            except:
                chat_name = f"Chat ID: {chat_id}"
            
            list_msg += f"🔸 **{chat_name}** - {len(task_list)} tasks\n"
    
    await event.reply(list_msg)

@client.on(events.NewMessage(pattern=r"^\.spamstats$", outgoing=True))
async def spam_stats(event):
    active_chats = len(cipher_spam_tasks)
    total_active_tasks = sum(len(tasks) for tasks in cipher_spam_tasks.values())
    
    stats_msg = f"🎭 **Spam Engine Statistics**\n\n"
    stats_msg += f"⚡ **Total Sent:** {spam_engine.spam_stats['total_sent']:,}\n"
    stats_msg += f"🔄 **Completed:** {spam_engine.spam_stats['completed_operations']}\n"
    stats_msg += f"🎯 **Active Chats:** {active_chats}\n"
    stats_msg += f"📈 **Active Tasks:** {total_active_tasks}\n"
    
    await event.reply(stats_msg)

# ==================== PM DELETE HANDLERS ====================

@client.on(events.NewMessage(incoming=True))
async def pm_delete_handler(event):
    if pm_delete_enabled and event.is_private and event.sender_id not in [OWNER_ID, 𝗚𝖔𝖏𝖔_BOT_OWNER]:
        try:
            await event.delete()
            return
        except:
            pass

@client.on(events.NewMessage(outgoing=True, pattern=r'\.pmdel'))
async def pmdel_cmd(event):
    global pm_delete_enabled
    pm_delete_enabled = True
    save_pm_delete()
    await event.respond("📬 **PM deletion ENABLED!**")

@client.on(events.NewMessage(outgoing=True, pattern=r'\.pmdeloff'))
async def pmdeloff_cmd(event):
    global pm_delete_enabled
    pm_delete_enabled = False
    save_pm_delete()
    await event.respond("✅ **PM deletion DISABLED!**")

def save_pm_delete():
    try:
        with open(PM_DELETE_FILE, 'w') as f:
            json.dump({"enabled": pm_delete_enabled}, f)
    except:
        pass

# ==================== PM ASSISTANT HANDLER ====================

@client.on(events.NewMessage(incoming=True))
async def assistant_handler(event):
    if pm_delete_enabled and event.is_private and event.sender_id not in [OWNER_ID, 𝗚𝖔𝖏𝖔_BOT_OWNER]:
        return
    await assistant.handle_message(event)

# ==================== SETUP COMMAND ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.setupbot"))
async def setupbot_cmd(event):
    status = await event.reply("🔄 **Setting up bot automatically...**")
    try:
        await status.edit("📌 **Step 1/3:** Enabling inline mode...")
        success = await enable_inline_mode_automatically()
        if not success:
            await status.edit(
                "❌ **Failed to enable inline mode!**\n\n"
                "Enable it manually:\n"
                "1. Open @BotFather\n"
                "2. Send /mybots\n"
                "3. Select your bot\n"
                "4. Bot Settings → Inline Mode → Turn on\n"
                "5. Set placeholder: `Type .help or plugin name`"
            )
            return
        await status.edit("✅ **Inline mode enabled!**\n\n📌 **Step 2/3:** Testing...")
        try:
            test_results = await client.inline_query(TG_BOT_USERNAME, "help")
            if test_results:
                await status.edit("✅ **Working!**\n\n📌 **Step 3/3:** Finalizing...")
                await asyncio.sleep(2)
        except:
            pass
        success_text = (
            "🎉 **Setup Complete!**\n\n"
            "✅ Inline mode enabled\n"
            "✅ Placeholder set\n"
            "✅ Bot ready\n\n"
            "📚 **Try:**\n"
            f"• `@{TG_BOT_USERNAME} help` - Interactive menu\n"
            "• `.help` - Command menu\n"
            "• `.plugins` - List all powers"
        )
        await status.edit(success_text)
    except Exception as e:
        await status.edit(f"❌ **Setup Error:** {str(e)}")

async def enable_inline_mode_automatically():
    print("\n🔄 Enabling inline mode...")
    try:
        botfather = await client.get_entity("@BotFather")
        await client.send_message(botfather, "/start")
        await asyncio.sleep(1)
        await client.send_message(botfather, "/mybots")
        await asyncio.sleep(2)
        msgs = await client.get_messages(botfather, limit=5)
        bot_found = False
        for msg in msgs:
            if msg.text and f"@{TG_BOT_USERNAME}" in msg.text:
                bot_found = True
                if msg.buttons:
                    for row in msg.buttons:
                        for button in row:
                            if TG_BOT_USERNAME in button.text:
                                await button.click()
                                await asyncio.sleep(2)
                                break
                break
        if not bot_found:
            print(f"❌ Bot @{TG_BOT_USERNAME} not found!")
            return False
        msgs = await client.get_messages(botfather, limit=3)
        if msgs:
            for msg in msgs:
                if msg.text and "Bot Settings" in msg.text:
                    if msg.buttons:
                        for row in msg.buttons:
                            for button in row:
                                if "Bot Settings" in button.text:
                                    await button.click()
                                    await asyncio.sleep(2)
                                    break
        msgs = await client.get_messages(botfather, limit=5)
        if msgs:
            for msg in msgs:
                if msg.text and "Inline Mode" in msg.text:
                    if msg.buttons:
                        for row in msg.buttons:
                            for button in row:
                                if "Turn on" in button.text:
                                    await button.click()
                                    await asyncio.sleep(2)
                                    print("✅ Inline mode enabled!")
                                    break
        await client.send_message(botfather, "Type .help or plugin name")
        await asyncio.sleep(1)
        print("✅ Inline mode setup complete!")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

# ==================== HELP COMMANDS ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.help(?:\s+(.+))?"))
async def help_handler(event):
    plugin_name = event.pattern_match.group(1)
    
    if plugin_name:
        plugin_name = plugin_name.strip().lower()
        
        if plugin_name in CMD_LIST:
            plugin_data = CMD_LIST[plugin_name]
            
            help_text = f"🎭 <b>{plugin_name.title().replace('_', ' ')}</b>\n"
            help_text += f"━━━━━━━━━━━━━━━━━━━━━━\n"
            help_text += f"{plugin_data['description']}\n\n"
            help_text += f"<b>📋 Commands:</b>\n\n"
            
            for cmd in plugin_data["commands"]:
                if isinstance(cmd, str) and cmd.strip():
                    if " - " in cmd:
                        cmd_part, desc_part = cmd.split(" - ", 1)
                        escaped_command = cmd_part.strip().replace('<', '&lt;').replace('>', '&gt;')
                        help_text += f"• <code>{escaped_command}</code>\n"
                        help_text += f"  <i>{desc_part.strip()}</i>\n\n"
                    else:
                        escaped_cmd = cmd.strip().replace('<', '&lt;').replace('>', '&gt;')
                        help_text += f"• <code>{escaped_cmd}</code>\n\n"
            
            help_text += f"🔄 <b>Quick Help:</b> <code>.help {plugin_name}</code>\n"
            help_text += f"📚 <b>All Powers:</b> <code>.help</code>\n"
            help_text += f"🤖 <b>Powered by 𝗚𝖔𝖏𝖔 God</b>"
            
            await event.reply(help_text, parse_mode='html')
            return
            
        else:
            available_plugins = list(CMD_LIST.keys())
            
            error_text = f"🎭 <b>Help System</b>\n\n"
            error_text += f"❌ <b>Power '{plugin_name}' not found!</b>\n\n"
            error_text += f"📋 <b>Available Powers:</b>\n"
            
            for i in range(0, len(available_plugins), 3):
                row_plugins = available_plugins[i:i+3]
                plugin_row = " • ".join([f"<code>{p}</code>" for p in row_plugins])
                error_text += f"{plugin_row}\n"
            
            error_text += f"\n💡 <b>Usage:</b> <code>.help &lt;power_name&gt;</code>\n"
            error_text += f"📚 <b>Example:</b> <code>.help spam</code>\n"
            error_text += f"🔍 <b>All Help:</b> <code>.help</code>"
            
            await event.reply(error_text, parse_mode='html')
            return
    
    try:
        results = await event.client.inline_query(
            TG_BOT_USERNAME,
            "help"
        )
        await results[0].click(
            event.chat_id,
            reply_to=event.reply_to_msg_id,
            hide_via=True
        )
        await event.delete()
    except Exception as e:
        await event.reply(f"❌ <b>Help unavailable. Use <code>.plugins</code> to see all powers.</b>\n\n"
                        f"<b>Error:</b> {str(e)}", parse_mode='html')

@client.on(events.NewMessage(outgoing=True, pattern=r"\.plugins"))
async def plugins_cmd(event):
    try:
        if not CMD_LIST:
            await event.reply("🎭 <b>Plugin Manager</b>\n\n"
                            "❌ <b>No powers loaded yet!</b>\n"
                            "💡 <b>Check your plugin directory</b>", parse_mode='html')
            return
        
        total_plugins = len(CMD_LIST)
        total_commands = sum(len(data['commands']) for data in CMD_LIST.values())
        
        plugins_text = f"🎭 <b>Loaded Powers</b>\n"
        plugins_text += f"━━━━━━━━━━━━━━━━━━━━━━\n"
        plugins_text += f"📊 <b>Statistics:</b>\n"
        plugins_text += f"⚡ <b>Total Powers:</b> {total_plugins}\n"
        plugins_text += f"📂 <b>Total Commands:</b> {total_commands}\n\n"
        plugins_text += f"📋 <b>Power List:</b>\n\n"
        
        sorted_plugins = sorted(CMD_LIST.items(), key=lambda x: (x[0] != 'help', x))
        
        for plugin_name, plugin_data in sorted_plugins:
            command_count = len(plugin_data['commands'])
            
            if plugin_name == 'help':
                plugins_text += f"⚡ <b>{plugin_name.title()} (Help System)</b>\n"
            else:
                plugins_text += f"🔸 <b>{plugin_name.title().replace('_', ' ')}</b>\n"
                
            plugins_text += f"   📝 {command_count} command{'s' if command_count != 1 else ''}\n"
            plugins_text += f"   🔍 <code>.help {plugin_name}</code>\n\n"
        
        plugins_text += f"💡 <b>Quick Help:</b> <code>.help &lt;power&gt;</code>\n"
        plugins_text += f"🤖 <b>Powered by 𝗚𝖔𝖏𝖔 God</b>"
        
        await event.reply(plugins_text, parse_mode='html')
        
    except Exception as e:
        await event.reply(f"🎭 <b>Error:</b> {str(e)}", parse_mode='html')

@client.on(events.NewMessage(outgoing=True, pattern=r"\.helpstats"))
async def helpstats_cmd(event):
    try:
        if not CMD_LIST:
            await event.reply("📊 <b>No power data available</b>", parse_mode='html')
            return
        
        real_plugins = {k: v for k, v in CMD_LIST.items() if k != 'help'}
        total_plugins = len(real_plugins)
        total_commands = sum(len(data['commands']) for data in real_plugins.values())
        
        max_commands = 0
        max_plugin = ""
        for plugin_name, plugin_data in real_plugins.items():
            cmd_count = len(plugin_data['commands'])
            if cmd_count > max_commands:
                max_commands = cmd_count
                max_plugin = plugin_name
        
        avg_commands = total_commands / total_plugins if total_plugins > 0 else 0
        
        stats_text = f"📊 <b>Statistics</b>\n"
        stats_text += f"━━━━━━━━━━━━━━━━━━━━━━\n"
        stats_text += f"⚡ <b>Total Powers:</b> {total_plugins}\n"
        stats_text += f"📂 <b>Total Commands:</b> {total_commands}\n"
        stats_text += f"📈 <b>Average/Power:</b> {avg_commands:.1f}\n"
        
        if max_plugin:
            stats_text += f"🏆 <b>Most Commands:</b> {max_plugin.title().replace('_', ' ')} ({max_commands})\n\n"
        
        stats_text += f"🎯 <b>Categories:</b>\n"
        
        light_plugins = [p for p, d in real_plugins.items() if len(d['commands']) <= 3]
        medium_plugins = [p for p, d in real_plugins.items() if 4 <= len(d['commands']) <= 7]
        heavy_plugins = [p for p, d in real_plugins.items() if len(d['commands']) >= 8]
        
        stats_text += f"🟢 <b>Light (≤3):</b> {len(light_plugins)} powers\n"
        stats_text += f"🟡 <b>Medium (4-7):</b> {len(medium_plugins)} powers\n"
        stats_text += f"🔴 <b>Heavy (≥8):</b> {len(heavy_plugins)} powers\n\n"
        
        stats_text += f"🔧 <b>Help System:</b>\n"
        stats_text += f"• <code>.help</code> - Interactive menu\n"
        stats_text += f"• <code>.help &lt;power&gt;</code> - Direct help\n"
        stats_text += f"• <code>.plugins</code> - List all powers\n"
        stats_text += f"• <code>.helpstats</code> - This view\n"
        stats_text += f"• <code>.quickhelp</code> - Quick guide\n\n"
        stats_text += f"🤖 <b>Powered by 𝗚𝖔𝖏𝖔 God</b>"
        
        await event.reply(stats_text, parse_mode='html')
        
    except Exception as e:
        await event.reply(f"📊 <b>Error:</b> {str(e)}", parse_mode='html')

@client.on(events.NewMessage(outgoing=True, pattern=r"\.quickhelp"))
async def quickhelp_cmd(event):
    try:
        guide_text = f"⚡ <b>Quick Help Guide</b>\n"
        guide_text += f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        
        guide_text += f"🎯 <b>Basic Commands:</b>\n"
        guide_text += f"• <code>.help</code> - Full interactive menu\n"
        guide_text += f"• <code>.help spam</code> - Help for spam\n"
        guide_text += f"• <code>.help admin</code> - Help for admin\n\n"
        
        guide_text += f"🔍 <b>Discovery Commands:</b>\n"
        guide_text += f"• <code>.plugins</code> - List all powers\n"
        guide_text += f"• <code>.helpstats</code> - Detailed statistics\n\n"
        
        guide_text += f"💡 <b>Pro Tips:</b>\n"
        guide_text += f"• Use <code>.help &lt;power&gt;</code> for instant help\n"
        guide_text += f"• All commands are case-insensitive\n"
        guide_text += f"• Direct access is faster\n\n"
        
        available_plugins = [p for p in CMD_LIST.keys() if p != 'help']
        if available_plugins:
            sample_plugins = random.sample(available_plugins, min(3, len(available_plugins)))
            guide_text += f"🎲 <b>Try These:</b>\n"
            for plugin in sample_plugins:
                guide_text += f"• <code>.help {plugin}</code>\n"
            guide_text += "\n"
        
        guide_text += f"🤖 <b>Powered by 𝗚𝖔𝖏𝖔 God</b>"
        
        await event.reply(guide_text, parse_mode='html')
        
    except Exception as e:
        await event.reply(f"⚡ <b>Error:</b> {str(e)}", parse_mode='html')

# ==================== EXTRA COMMANDS ====================

@client.on(events.NewMessage(outgoing=True, pattern=r"\.leave"))
async def leave_cmd(event):
    chat_id = event.chat_id
    try:
        await event.reply("🚪 **Departing from this realm...**")
        await asyncio.sleep(1)
        await event.client(LeaveChannelRequest(chat_id))
    except Exception as e:
        try:
            await event.client.delete_dialog(chat_id)
            await event.reply("✅ Left the chat!")
        except Exception as e2:
            await event.reply(f"❌ Failed to leave: {str(e2)}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.delete"))
async def delete_cmd(event):
    if not event.is_reply:
        return await event.reply("❌ **Reply to a message to delete it!**")
    
    reply = await event.get_reply_message()
    try:
        await reply.delete()
        await event.reply("🗑️ **Message deleted!**")
    except Exception as e:
        await event.reply(f"❌ **Failed to delete:** {str(e)}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.deleteall"))
async def deleteall_cmd(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    
    status = await event.reply("🗑️ **Deleting all your messages...**")
    deleted = 0
    
    try:
        async for msg in client.iter_messages(chat_id, from_user=user_id):
            try:
                await msg.delete()
                deleted += 1
                if deleted % 10 == 0:
                    await status.edit(f"🗑️ **Deleting...** ({deleted} deleted)")
                await asyncio.sleep(0.1)
            except:
                pass
        await status.edit(f"✅ **Deleted {deleted} messages!**")
    except Exception as e:
        await status.edit(f"❌ **Error:** {str(e)}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.users"))
async def users_cmd(event):
    try:
        users = []
        async for user in client.iter_participants(event.chat_id):
            users.append(user)
        
        count = len(users)
        text = f"👥 **Users in Chat**\n━━━━━━━━━━━━━━━━━━━━━━\n"
        text += f"📊 **Total:** {count}\n\n"
        
        for i, user in enumerate(users[:20]):
            name = utils.get_display_name(user)
            text += f"• {name}\n"
        
        if count > 20:
            text += f"\n... and {count - 20} more users"
        
        await event.reply(text)
    except:
        await event.reply("❌ **Failed to fetch users!**")

# ==================== BAIT PLUGIN ====================

ACTION_MAP = {
    "typing":    SendMessageTypingAction(),
    "recording": SendMessageRecordAudioAction(),
    "gaming":    SendMessageGamePlayAction(),
    "video":     SendMessageRecordVideoAction(),
    "round":     SendMessageRecordRoundAction(),
    "photo":     SendMessageUploadPhotoAction(progress=1),
    "document":  SendMessageUploadDocumentAction(progress=1),
    "location":  SendMessageGeoLocationAction(),
    "contact":   SendMessageChooseContactAction(),
}

try:
    from telethon.tl.types import SendMessageChooseStickerAction
    ACTION_MAP["sticker"] = SendMessageChooseStickerAction()
except (ImportError, AttributeError):
    print("ℹ️ Sticker action not supported, skipping...")
    pass

BAIT_CMD_PATTERN = r"^\.(" + "|".join(ACTION_MAP.keys()) + r")(?: |$)(.*)"

async def action_runner(client, chat_id, action, task_key, duration=None):
    deadline = (time.time() + duration) if duration else None
    try:
        while True:
            if deadline and time.time() >= deadline:
                break
            await client(functions.messages.SetTypingRequest(
                peer=chat_id, action=action
            ))
            await asyncio.sleep(4)
    except asyncio.CancelledError:
        raise
    except Exception as e:
        print(f"Bait Error [{task_key}]: {e}")
    finally:
        BAIT_TASKS.pop(task_key, None)
        try:
            await client(functions.messages.SetTypingRequest(
                peer=chat_id, action=SendMessageCancelAction()
            ))
        except Exception:
            pass

@client.on(events.NewMessage(pattern=BAIT_CMD_PATTERN, outgoing=True))
async def bait_handler(event):
    action_type = event.pattern_match.group(1).lower()
    args = event.pattern_match.group(2).strip().lower().split()
    state = args[0] if args else ""
    chat_id = event.chat_id

    if action_type not in ACTION_MAP:
        return await event.reply(f"❌ **Unknown action:** {action_type}")

    action = ACTION_MAP[action_type]
    task_key = f"{chat_id}_{action_type}"

    if state == "on":
        if task_key in BAIT_TASKS:
            return await event.reply(f"⚠️ **Already {action_type} infinitely in this chat!**")

        duration = None
        if len(args) > 1 and args[1].isdigit():
            duration = int(args[1])

        task = asyncio.create_task(
            action_runner(event.client, chat_id, action, task_key, duration)
        )
        BAIT_TASKS[task_key] = {"task": task, "since": time.time()}

        await event.delete()

    elif state == "off":
        entry = BAIT_TASKS.pop(task_key, None)
        if not entry:
            return await event.reply(f"⚠️ **No infinite {action_type} is running here.**")

        entry["task"].cancel()
        await event.client(functions.messages.SetTypingRequest(
            peer=chat_id, action=SendMessageCancelAction()
        ))
        await event.reply(f"🛑 **Infinite {action_type} stopped.**")

    else:
        available_actions = ", ".join(ACTION_MAP.keys())
        await event.reply(
            f"❌ **Syntax:** `.{action_type} on`, `.{action_type} on <seconds>` or `.{action_type} off`\n\n"
            f"📋 **Available actions:** {available_actions}"
        )

@client.on(events.NewMessage(pattern=r"^\.baitlist$", outgoing=True))
async def bait_list(event):
    if not BAIT_TASKS:
        return await event.reply("😴 **No baits running anywhere.**")

    lines = ["🎣 **Active Baits:**\n"]
    for key, entry in BAIT_TASKS.items():
        chat_id, _, action = key.rpartition("_")
        mins = int((time.time() - entry["since"]) // 60)
        lines.append(f"• `{action}` in chat `{chat_id}` — running {mins}m")
    await event.reply("\n".join(lines))

@client.on(events.NewMessage(pattern=r"^\.baitstop$", outgoing=True))
async def stop_all_bait(event):
    chat_id = event.chat_id
    keys = [k for k in BAIT_TASKS if k.startswith(f"{chat_id}_")]

    for key in keys:
        BAIT_TASKS.pop(key)["task"].cancel()

    if keys:
        await event.client(functions.messages.SetTypingRequest(
            peer=chat_id, action=SendMessageCancelAction()
        ))
        await event.reply(f"🛑 **Stopped {len(keys)} infinite actions in this chat!**")
    else:
        await event.reply("⚠️ **No bait actions are currently running here.**")

@client.on(events.NewMessage(pattern=r"^\.baitstopall$", outgoing=True))
async def stop_everything(event):
    if not BAIT_TASKS:
        return await event.reply("⚠️ **No baits running anywhere.**")

    chat_ids = set()
    count = len(BAIT_TASKS)
    for key in list(BAIT_TASKS):
        chat_id, _, _ = key.rpartition("_")
        chat_ids.add(int(chat_id))
        BAIT_TASKS.pop(key)["task"].cancel()

    for cid in chat_ids:
        try:
            await event.client(functions.messages.SetTypingRequest(
                peer=cid, action=SendMessageCancelAction()
            ))
        except Exception:
            pass

    await event.reply(f"🛑 **PANIC: Killed {count} baits across {len(chat_ids)} chats!**")

# ==================== FLASHVAULT PLUGIN ====================

def load_flash_db():
    if FLASH_DB_PATH.exists():
        try:
            with open(FLASH_DB_PATH, 'r') as f:
                return json.load(f)
        except Exception:
            pass
    return {"global_flash": False, "monitored_chats": []}

def save_flash_db(db):
    with open(FLASH_DB_PATH, 'w') as f:
        json.dump(db, f, indent=4)

@client.on(events.NewMessage(pattern=r"^\.flash(?: |$)(.*)", outgoing=True))
async def toggle_global_flash(event):
    LOG_CHAT_ID = DB_DIR / "log_chat_id.txt"
    if not LOG_CHAT_ID.exists():
        return await event.reply("❌ **Error:** Please set a Log Group first!\n\nUse: `.setlog <chat_id>`")
    
    args = event.pattern_match.group(1).strip().lower()
    db = load_flash_db()
    
    if args == "on":
        db["global_flash"] = True
        save_flash_db(db)
        await event.reply("📸 **Global FlashVault ENABLED!**\n*I will secretly save all View-Once media to your Log Group.*")
    elif args == "off":
        db["global_flash"] = False
        save_flash_db(db)
        await event.reply("💤 **Global FlashVault DISABLED!**")
    else:
        await event.reply("❌ **Syntax Error:** Use `.flash on` or `.flash off`")

@client.on(events.NewMessage(pattern=r"^\.flashchat(?: |$)(.*)", outgoing=True))
async def toggle_chat_flash(event):
    LOG_CHAT_ID = DB_DIR / "log_chat_id.txt"
    if not LOG_CHAT_ID.exists():
        return await event.reply("❌ **Error:** Please set a Log Group first!\n\nUse: `.setlog <chat_id>`")
    
    args = event.pattern_match.group(1).strip().lower()
    chat_id = str(event.chat_id)
    db = load_flash_db()
    
    if args == "on":
        if chat_id not in db["monitored_chats"]:
            db["monitored_chats"].append(chat_id)
            save_flash_db(db)
        await event.reply("📸 **FlashVault is now monitoring THIS chat for View-Once media!**")
    elif args == "off":
        if chat_id in db["monitored_chats"]:
            db["monitored_chats"].remove(chat_id)
            save_flash_db(db)
        await event.reply("💤 **FlashVault stopped monitoring this chat.**")
    else:
        await event.reply("❌ **Syntax Error:** Use `.flashchat on` or `.flashchat off`")

@client.on(events.NewMessage(pattern=r"^\.flashlist$", outgoing=True))
async def list_flash_chats(event):
    db = load_flash_db()
    
    text = "📸 **FlashVault Status:**\n\n"
    text += f"🌍 **Global Auto-Save:** `{'🟢 ON' if db['global_flash'] else '🔴 OFF'}`\n\n"
    text += "📍 **Specifically Monitored Chats:**\n"
    
    if not db["monitored_chats"]:
        text += "None."
    else:
        for chat in db["monitored_chats"]:
            try:
                entity = await event.client.get_entity(int(chat))
                name = utils.get_display_name(entity)
                text += f"• {name} (`{chat}`)\n"
            except:
                text += f"• `{chat}`\n"
            
    await event.reply(text)

@client.on(events.NewMessage(pattern=r"^\.saveflash$", outgoing=True))
async def manual_flash_download(event):
    LOG_CHAT_ID = DB_DIR / "log_chat_id.txt"
    if not LOG_CHAT_ID.exists():
        return await event.reply("❌ **Error:** Please set a Log Group first!\n\nUse: `.setlog <chat_id>`")

    reply_msg = await event.get_reply_message()
    if not reply_msg or not reply_msg.media:
        return await event.reply("❌ **Please reply to a photo or video to save it!**")

    status = await event.reply("📥 **Downloading media...**")
    try:
        downloaded_file = await reply_msg.download_media()
        if downloaded_file:
            with open(LOG_CHAT_ID, 'r') as f:
                log_chat = int(f.read().strip())
            
            await event.client.send_file(
                log_chat,
                downloaded_file,
                caption="📸 **Manually Saved Media**\n*Source:* Triggered via `.saveflash`"
            )
            os.remove(downloaded_file)
            await status.edit("✅ **Media successfully saved to your Log Group!**")
        else:
            await status.edit("❌ **Failed to download media.**")
    except Exception as e:
        await status.edit(f"❌ **Error:** `{str(e)}`")

@client.on(events.NewMessage(pattern=r"^\.setlog\s+(\d+)$", outgoing=True))
async def set_log_chat(event):
    log_chat_id = event.pattern_match.group(1)
    LOG_CHAT_ID = DB_DIR / "log_chat_id.txt"
    
    try:
        entity = await event.client.get_entity(int(log_chat_id))
        name = utils.get_display_name(entity)
        
        with open(LOG_CHAT_ID, 'w') as f:
            f.write(log_chat_id)
        
        await event.reply(f"✅ **Log Group set successfully!**\n📝 **Chat:** {name} (`{log_chat_id}`)\n\nNow use `.flash on` to enable auto-saving!")
    except Exception as e:
        await event.reply(f"❌ **Error:** Invalid chat ID or cannot access the chat!\n\n`{str(e)}`")

@client.on(events.NewMessage(incoming=True))
async def auto_media_downloader(event):
    LOG_CHAT_ID = DB_DIR / "log_chat_id.txt"
    if not LOG_CHAT_ID.exists():
        return

    if not event.media:
        return

    is_view_once = getattr(event, 'media_unread', False) or getattr(event.media, 'ttl_seconds', None) is not None

    if not is_view_once:
        return

    db = load_flash_db()
    chat_id = str(event.chat_id) if event.chat_id else None
    
    if db.get("global_flash", False) or (chat_id and chat_id in db.get("monitored_chats", [])):
        try:
            downloaded_file = await event.download_media()
            
            if downloaded_file:
                sender = await event.get_sender()
                sender_name = utils.get_display_name(sender) if sender else "Unknown User"
                
                try:
                    chat_entity = await event.client.get_entity(event.chat_id)
                    chat_name = utils.get_display_name(chat_entity)
                except:
                    chat_name = "Unknown Chat"
                
                caption = (
                    f"📸 **INTERCEPTED VIEW-ONCE MEDIA**\n\n"
                    f"👤 **From:** {sender_name}\n"
                    f"💬 **Chat:** {chat_name}\n"
                    f"🆔 **Chat ID:** `{chat_id}`\n"
                    f"🕐 **Time:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                )
                
                with open(LOG_CHAT_ID, 'r') as f:
                    log_chat = int(f.read().strip())
                
                await event.client.send_file(
                    log_chat,
                    downloaded_file,
                    caption=caption
                )
                
                os.remove(downloaded_file)
                
        except Exception as e:
            print(f"FlashVault Auto-Save Error: {e}")


# ==================== GHOST VAULT PLUGIN ====================

def load_vault_db():
    if VAULT_DB_PATH.exists():
        try:
            with open(VAULT_DB_PATH, 'r') as f:
                return json.load(f)
        except Exception:
            pass
    return {"global_vault": False, "monitored_chats": []}

def save_vault_db(db):
    with open(VAULT_DB_PATH, 'w') as f:
        json.dump(db, f, indent=4)

def cache_message(chat_id, msg_id, message_obj):
    global cache_keys
    key = f"{chat_id}_{msg_id}"
    
    if key not in MESSAGE_CACHE:
        cache_keys.append(key)
        
    MESSAGE_CACHE[key] = message_obj
    
    if len(cache_keys) > MAX_CACHE_SIZE:
        oldest_key = cache_keys.pop(0)
        MESSAGE_CACHE.pop(oldest_key, None)

def get_cached_message(chat_id, msg_id):
    return MESSAGE_CACHE.get(f"{chat_id}_{msg_id}")

@client.on(events.NewMessage(pattern=r"^\.vault(?: |$)(.*)", outgoing=True))
async def toggle_global_vault(event):
    LOG_CHAT_ID = DB_DIR / "log_chat_id.txt"
    if not LOG_CHAT_ID.exists():
        return await event.reply("❌ **Error:** Please set a Log Group first!\n\nUse: `.setlog <chat_id>`")
        
    args = event.pattern_match.group(1).strip().lower()
    db = load_vault_db()
    
    if args == "on":
        db["global_vault"] = True
        save_vault_db(db)
        await event.reply("🕵️‍♂️ **Global Ghost Vault ENABLED!**\n*I am now tracking deleted & edited messages in ALL chats.*")
    elif args == "off":
        db["global_vault"] = False
        save_vault_db(db)
        await event.reply("💤 **Global Ghost Vault DISABLED!**")
    else:
        await event.reply("❌ **Syntax Error:** Use `.vault on` or `.vault off`")

@client.on(events.NewMessage(pattern=r"^\.vaultchat(?: |$)(.*)", outgoing=True))
async def toggle_chat_vault(event):
    LOG_CHAT_ID = DB_DIR / "log_chat_id.txt"
    if not LOG_CHAT_ID.exists():
        return await event.reply("❌ **Error:** Please set a Log Group first!\n\nUse: `.setlog <chat_id>`")
        
    args = event.pattern_match.group(1).strip().lower()
    chat_id = str(event.chat_id)
    db = load_vault_db()
    
    if args == "on":
        if chat_id not in db["monitored_chats"]:
            db["monitored_chats"].append(chat_id)
            save_vault_db(db)
        await event.reply("🕵️‍♂️ **Vault is now monitoring THIS chat!**")
    elif args == "off":
        if chat_id in db["monitored_chats"]:
            db["monitored_chats"].remove(chat_id)
            save_vault_db(db)
        await event.reply("💤 **Vault stopped monitoring this chat.**")
    else:
        await event.reply("❌ **Syntax Error:** Use `.vaultchat on` or `.vaultchat off`")

@client.on(events.NewMessage(pattern=r"^\.vaultlist$", outgoing=True))
async def list_vault_chats(event):
    db = load_vault_db()
    
    text = "🕵️‍♂️ **Ghost Vault Status:**\n\n"
    text += f"🌍 **Global Vault:** `{'🟢 ON' if db['global_vault'] else '🔴 OFF'}`\n\n"
    text += "📍 **Specifically Monitored Chats:**\n"
    
    if not db["monitored_chats"]:
        text += "None."
    else:
        for chat in db["monitored_chats"]:
            try:
                entity = await event.client.get_entity(int(chat))
                name = utils.get_display_name(entity)
                text += f"• {name} (`{chat}`)\n"
            except:
                text += f"• `{chat}`\n"
            
    await event.reply(text)

@client.on(events.NewMessage(incoming=True))
async def message_cacher(event):
    db = load_vault_db()
    chat_id = str(event.chat_id) if event.chat_id else None
    
    if db.get("global_vault", False) or (chat_id and chat_id in db.get("monitored_chats", [])):
        cache_message(chat_id, event.id, event.message)

@client.on(events.MessageDeleted())
async def catch_deletions(event):
    LOG_CHAT_ID = DB_DIR / "log_chat_id.txt"
    if not LOG_CHAT_ID.exists():
        return
        
    db = load_vault_db()
    chat_id = str(event.chat_id) if event.chat_id else None
    
    if not db.get("global_vault", False) and (not chat_id or chat_id not in db.get("monitored_chats", [])):
        return
        
    for msg_id in event.deleted_ids:
        cached_msg = get_cached_message(chat_id, msg_id)
        if cached_msg:
            try:
                with open(LOG_CHAT_ID, 'r') as f:
                    log_chat = int(f.read().strip())
                
                try:
                    chat_entity = await event.client.get_entity(int(chat_id))
                    chat_title = utils.get_display_name(chat_entity)
                except:
                    chat_title = "Unknown Chat"
                
                try:
                    sender_entity = await cached_msg.get_sender()
                    sender_name = utils.get_display_name(sender_entity) if sender_entity else "Unknown User"
                except:
                    sender_name = "Unknown User"
                
                log_text = (
                    f"🗑 **DELETED MESSAGE EXPOSED**\n\n"
                    f"👤 **User:** {sender_name}\n"
                    f"💬 **Chat:** {chat_title}\n"
                    f"🆔 **Chat ID:** `{chat_id}`\n"
                    f"🕐 **Time:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                    f"━━━━━━━━━━━━━━━━━━━━\n"
                    f"{cached_msg.text or '[Media/No Text]'}"
                )
                
                await event.client.send_message(log_chat, message=log_text)
                
                if cached_msg.media:
                    await event.client.send_file(
                        log_chat,
                        cached_msg.media,
                        caption="📎 **Media from deleted message**"
                    )
                    
                MESSAGE_CACHE.pop(f"{chat_id}_{msg_id}", None)
                
            except Exception as e:
                print(f"Vault Deletion Error: {e}")

@client.on(events.MessageEdited())
async def catch_edits(event):
    LOG_CHAT_ID = DB_DIR / "log_chat_id.txt"
    if not LOG_CHAT_ID.exists():
        return
        
    db = load_vault_db()
    chat_id = str(event.chat_id) if event.chat_id else None
    
    if not db.get("global_vault", False) and (not chat_id or chat_id not in db.get("monitored_chats", [])):
        return
        
    cached_msg = get_cached_message(chat_id, event.id)
    if cached_msg and cached_msg.text != event.text:
        try:
            with open(LOG_CHAT_ID, 'r') as f:
                log_chat = int(f.read().strip())
            
            try:
                chat_entity = await event.client.get_entity(int(chat_id))
                chat_title = utils.get_display_name(chat_entity)
            except:
                chat_title = "Unknown Chat"
            
            try:
                sender_entity = await event.get_sender()
                sender_name = utils.get_display_name(sender_entity) if sender_entity else "Unknown User"
            except:
                sender_name = "Unknown User"
            
            log_text = (
                f"✏️ **EDITED MESSAGE EXPOSED**\n\n"
                f"👤 **User:** {sender_name}\n"
                f"💬 **Chat:** {chat_title}\n"
                f"🆔 **Chat ID:** `{chat_id}`\n"
                f"🕐 **Time:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f"🛑 **ORIGINAL (Before Edit):**\n{cached_msg.text or '[Media]'}\n\n"
                f"✅ **NEW (After Edit):**\n{event.text}"
            )
            
            await event.client.send_message(log_chat, log_text)
            
            cache_message(chat_id, event.id, event.message)
            
        except Exception as e:
            print(f"Vault Edit Error: {e}")

# ==================== GLOBALTOOLS PLUGIN ====================

def load_global_data():
    if GLOBALTOOLS_DB_PATH.exists():
        try:
            with open(GLOBALTOOLS_DB_PATH, 'r') as f:
                return json.load(f)
        except Exception:
            pass
    return {"gbanned": {}, "gmuted": {}}

def save_global_data(data):
    with open(GLOBALTOOLS_DB_PATH, 'w') as f:
        json.dump(data, f, indent=2)

async def get_global_user(event):
    """Get user ID and name from reply or username - used by globaltools"""
    user_id = None
    user_name = None
    
    if event.is_reply:
        reply = await event.get_reply_message()
        user_id = reply.sender_id
        try:
            user = await event.client.get_entity(user_id)
            user_name = user.first_name or "User"
        except:
            user_name = "User"
    else:
        text = event.text.split(maxsplit=1)
        if len(text) > 1:
            try:
                user = await event.client.get_entity(text[1])
                user_id = user.id
                user_name = user.first_name or "User"
            except:
                await event.reply("❌ Invalid username or user not found!")
                return None, None
        else:
            await event.reply("❌ Reply to a user or provide username!")
            return None, None
    
    return user_id, user_name

@client.on(events.NewMessage(pattern=r"^\.gban(?:\s+(.+))?", outgoing=True))
async def gban(event):
    user_id, user_name = await get_global_user(event)
    if not user_id:
        return
    
    if user_id == OWNER_ID or user_id == 𝗚𝖔𝖏𝖔_BOT_OWNER:
        return await event.reply("❌ Cannot ban the God!")
    
    text_parts = event.text.split(maxsplit=2)
    reason = text_parts[2] if len(text_parts) > 2 else "No reason provided"
    
    data = load_global_data()
    data["gbanned"][str(user_id)] = {
        "name": user_name,
        "reason": reason,
        "date": datetime.now().isoformat()
    }
    save_global_data(data)
    
    msg = await event.reply(f"🔨 **Global Ban Initiated**\n\n👤 User: {user_name} (`{user_id}`)\n📝 Reason: {reason}\n\n⏳ Banning in all groups...")
    
    banned_count = 0
    failed_count = 0
    
    async for dialog in event.client.iter_dialogs():
        if dialog.is_group or dialog.is_channel:
            try:
                await event.client(EditBannedRequest(
                    dialog.id,
                    user_id,
                    ChatBannedRights(until_date=None, view_messages=True)
                ))
                banned_count += 1
                await asyncio.sleep(0.1)
            except:
                failed_count += 1
    
    await msg.edit(f"✅ **Global Ban Complete**\n\n👤 User: {user_name} (`{user_id}`)\n📝 Reason: {reason}\n\n✔️ Banned in: {banned_count} groups\n❌ Failed: {failed_count} groups")

@client.on(events.NewMessage(pattern=r"^\.ungban(?:\s+(.+))?", outgoing=True))
async def ungban(event):
    user_id, user_name = await get_global_user(event)
    if not user_id:
        return
    
    data = load_global_data()
    if str(user_id) not in data["gbanned"]:
        await event.reply(f"❌ {user_name} is not gbanned!")
        return
    
    del data["gbanned"][str(user_id)]
    save_global_data(data)
    
    msg = await event.reply(f"🔓 **Global Unban Initiated**\n\n👤 User: {user_name} (`{user_id}`)\n\n⏳ Unbanning in all groups...")
    
    unbanned_count = 0
    failed_count = 0
    
    async for dialog in event.client.iter_dialogs():
        if dialog.is_group or dialog.is_channel:
            try:
                await event.client(EditBannedRequest(
                    dialog.id,
                    user_id,
                    ChatBannedRights(until_date=None, view_messages=False)
                ))
                unbanned_count += 1
                await asyncio.sleep(0.1)
            except:
                failed_count += 1
    
    await msg.edit(f"✅ **Global Unban Complete**\n\n👤 User: {user_name} (`{user_id}`)\n\n✔️ Unbanned in: {unbanned_count} groups\n❌ Failed: {failed_count} groups")

@client.on(events.NewMessage(pattern=r"^\.gmute(?:\s+(.+))?", outgoing=True))
async def gmute(event):
    user_id, user_name = await get_global_user(event)
    if not user_id:
        return
    
    if user_id == OWNER_ID or user_id == 𝗚𝖔𝖏𝖔_BOT_OWNER:
        return await event.reply("❌ Cannot mute the God!")
    
    text_parts = event.text.split(maxsplit=2)
    reason = text_parts[2] if len(text_parts) > 2 else "No reason provided"
    
    data = load_global_data()
    data["gmuted"][str(user_id)] = {
        "name": user_name,
        "reason": reason,
        "date": datetime.now().isoformat()
    }
    save_global_data(data)
    
    msg = await event.reply(f"🔇 **Global Mute Initiated**\n\n👤 User: {user_name} (`{user_id}`)\n📝 Reason: {reason}\n\n⏳ Muting in all groups...")
    
    muted_count = 0
    failed_count = 0
    
    async for dialog in event.client.iter_dialogs():
        if dialog.is_group or dialog.is_channel:
            try:
                await event.client(EditBannedRequest(
                    dialog.id,
                    user_id,
                    ChatBannedRights(until_date=None, send_messages=True)
                ))
                muted_count += 1
                await asyncio.sleep(0.1)
            except:
                failed_count += 1
    
    await msg.edit(f"✅ **Global Mute Complete**\n\n👤 User: {user_name} (`{user_id}`)\n📝 Reason: {reason}\n\n✔️ Muted in: {muted_count} groups\n❌ Failed: {failed_count} groups")

@client.on(events.NewMessage(pattern=r"^\.ungmute(?:\s+(.+))?", outgoing=True))
async def ungmute(event):
    user_id, user_name = await get_global_user(event)
    if not user_id:
        return
    
    data = load_global_data()
    if str(user_id) not in data["gmuted"]:
        await event.reply(f"❌ {user_name} is not gmuted!")
        return
    
    del data["gmuted"][str(user_id)]
    save_global_data(data)
    
    msg = await event.reply(f"🔊 **Global Unmute Initiated**\n\n👤 User: {user_name} (`{user_id}`)\n\n⏳ Unmuting in all groups...")
    
    unmuted_count = 0
    failed_count = 0
    
    async for dialog in event.client.iter_dialogs():
        if dialog.is_group or dialog.is_channel:
            try:
                await event.client(EditBannedRequest(
                    dialog.id,
                    user_id,
                    ChatBannedRights(until_date=None, send_messages=False)
                ))
                unmuted_count += 1
                await asyncio.sleep(0.1)
            except:
                failed_count += 1
    
    await msg.edit(f"✅ **Global Unmute Complete**\n\n👤 User: {user_name} (`{user_id}`)\n\n✔️ Unmuted in: {unmuted_count} groups\n❌ Failed: {failed_count} groups")

@client.on(events.NewMessage(pattern=r"^\.gkick(?:\s+(.+))?", outgoing=True))
async def gkick(event):
    user_id, user_name = await get_global_user(event)
    if not user_id:
        return
    
    if user_id == OWNER_ID or user_id == 𝗚𝖔𝖏𝖔_BOT_OWNER:
        return await event.reply("❌ Cannot kick the God!")
    
    msg = await event.reply(f"👢 **Global Kick Initiated**\n\n👤 User: {user_name} (`{user_id}`)\n\n⏳ Kicking from all groups...")
    
    kicked_count = 0
    failed_count = 0
    
    async for dialog in event.client.iter_dialogs():
        if dialog.is_group or dialog.is_channel:
            try:
                await event.client.kick_participant(dialog.id, user_id)
                kicked_count += 1
                await asyncio.sleep(0.1)
            except:
                failed_count += 1
    
    await msg.edit(f"✅ **Global Kick Complete**\n\n👤 User: {user_name} (`{user_id}`)\n\n✔️ Kicked from: {kicked_count} groups\n❌ Failed: {failed_count} groups")

@client.on(events.NewMessage(pattern=r"^\.gpromote(?:\s+(.+))?", outgoing=True))
async def gpromote(event):
    user_id, user_name = await get_global_user(event)
    if not user_id:
        return
    
    msg = await event.reply(f"👑 **Global Promote Initiated**\n\n👤 User: {user_name} (`{user_id}`)\n\n⏳ Promoting in all admin chats...")
    
    promoted_count = 0
    failed_count = 0
    
    async for dialog in event.client.iter_dialogs():
        if dialog.is_group or dialog.is_channel:
            try:
                await event.client.edit_admin(
                    dialog.id,
                    user_id,
                    is_admin=True,
                    title="Admin"
                )
                promoted_count += 1
                await asyncio.sleep(0.1)
            except:
                failed_count += 1
    
    await msg.edit(f"✅ **Global Promote Complete**\n\n👤 User: {user_name} (`{user_id}`)\n\n✔️ Promoted in: {promoted_count} chats\n❌ Failed: {failed_count} chats")

@client.on(events.NewMessage(pattern=r"^\.gdemote(?:\s+(.+))?", outgoing=True))
async def gdemote(event):
    user_id, user_name = await get_global_user(event)
    if not user_id:
        return
    
    msg = await event.reply(f"⬇️ **Global Demote Initiated**\n\n👤 User: {user_name} (`{user_id}`)\n\n⏳ Demoting in all admin chats...")
    
    demoted_count = 0
    failed_count = 0
    
    async for dialog in event.client.iter_dialogs():
        if dialog.is_group or dialog.is_channel:
            try:
                await event.client.edit_admin(
                    dialog.id,
                    user_id,
                    is_admin=False
                )
                demoted_count += 1
                await asyncio.sleep(0.1)
            except:
                failed_count += 1
    
    await msg.edit(f"✅ **Global Demote Complete**\n\n👤 User: {user_name} (`{user_id}`)\n\n✔️ Demoted in: {demoted_count} chats\n❌ Failed: {failed_count} chats")

@client.on(events.NewMessage(pattern=r"^\.listgban$", outgoing=True))
async def listgban(event):
    data = load_global_data()
    gbanned = data["gbanned"]
    
    if not gbanned:
        await event.reply("✅ No users are globally banned!")
        return
    
    msg = "📋 **Globally Banned Users**\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
    for user_id, info in gbanned.items():
        msg += f"👤 {info['name']} (`{user_id}`)\n"
        msg += f"📝 Reason: {info['reason']}\n"
        msg += f"📅 Since: {info.get('date', 'Unknown')[:10]}\n\n"
    
    await event.reply(msg)

@client.on(events.NewMessage(pattern=r"^\.gstat(?:\s+(.+))?", outgoing=True))
async def gstat(event):
    user_id, user_name = await get_global_user(event)
    if not user_id:
        return
    
    data = load_global_data()
    
    is_gbanned = str(user_id) in data["gbanned"]
    is_gmuted = str(user_id) in data["gmuted"]
    
    msg = f"📊 **Global Status**\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
    msg += f"👤 User: {user_name} (`{user_id}`)\n\n"
    
    if is_gbanned:
        msg += f"🔨 **Status:** Globally Banned\n"
        msg += f"📝 Reason: {data['gbanned'][str(user_id)]['reason']}\n"
    elif is_gmuted:
        msg += f"🔇 **Status:** Globally Muted\n"
        msg += f"📝 Reason: {data['gmuted'][str(user_id)]['reason']}\n"
    else:
        msg += "✅ **Status:** Clean (No restrictions)"
    
    await event.reply(msg)

# ==================== TAGGER PLUGIN ====================

GM_MESSAGES = [
    "Good Morning {mention}! Have a wonderful day 🌅",
    "Wakey wakey {mention}! It's a beautiful morning ☀️",
    "A very Good Morning to you, {mention}! ☕",
    "Rise and shine {mention}! ✨",
    "Good Morning {mention}! Sending good vibes your way 🌻"
]

GN_MESSAGES = [
    "Good Night {mention}! Sweet dreams 🌙",
    "Sleep tight {mention}! Don't let the bed bugs bite 😴",
    "Good Night {mention}! See you tomorrow 🌌",
    "Rest well {mention}! 🥱",
    "Nighty night {mention}! 🌃"
]

VC_MESSAGES = [
    "Hey {mention}, join the Voice Chat! We are waiting 🎤",
    "{mention} come to VC fast! 🎧",
    "Join the VC {mention}, let's talk! 🗣",
    "We need you in the VC {mention}! 🎵",
    "Hop in the VC {mention}, it's fun inside! 🎉"
]

async def get_users(event):
    users = []
    chat_id = event.chat_id
    if not chat_id:
        return users
        
    try:
        async for user in event.client.iter_participants(chat_id):
            if not user.bot and not user.deleted:
                users.append(user)
    except Exception as e:
        print(f"Error fetching users: {e}")
    return users

async def human_delay(messages_sent):
    if messages_sent > 0 and messages_sent % 10 == 0:
        await asyncio.sleep(random.uniform(10.0, 15.0))
    else:
        await asyncio.sleep(random.uniform(2.5, 4.5))

async def handle_bulk_tag(event, msg_list=None, static_text=None):
    chat_id = event.chat_id
    if chat_id in tagger_active_chats:
        return await event.reply("⚠️ **Tagging is already running in this chat. Type `.canceltag` to stop it.**")
    
    status = await event.reply("✅ **Starting Bulk Tag (Anti-Ban Mode)...**")
    tagger_active_chats.add(chat_id)
    users = await get_users(event)
    
    if not users:
        tagger_active_chats.remove(chat_id)
        return await status.edit("❌ **No users found in this chat!**")
    
    mentions, count, messages_sent = "", 0, 0
    
    try:
        for user in users:
            if chat_id not in tagger_active_chats: 
                break
                
            mentions += f"[{user.first_name}](tg://user?id={user.id}) "
            count += 1
            
            if count == 5:
                base_msg = random.choice(msg_list).replace("{mention}", "").strip() if msg_list else static_text
                
                while True:
                    try:
                        await event.client.send_message(chat_id, f"{base_msg}\n\n{mentions}")
                        messages_sent += 1
                        break 
                    except FloodWaitError as e:
                        if e.seconds > 60:
                            await event.reply(f"🛑 **FloodWait over 60s ({e.seconds}s)! Stopping to protect account.**")
                            tagger_active_chats.remove(chat_id)
                            return
                        await asyncio.sleep(e.seconds + 2) 
                    except (ChatWriteForbiddenError, UserBannedInChannelError):
                        await event.reply("🛑 **Error: I lack permission to send messages here or have been muted. Stopping.**")
                        tagger_active_chats.remove(chat_id)
                        return
                
                mentions, count = "", 0
                await human_delay(messages_sent)
                
        if mentions and chat_id in tagger_active_chats:
            base_msg = random.choice(msg_list).replace("{mention}", "").strip() if msg_list else static_text
            try:
                await event.client.send_message(chat_id, f"{base_msg}\n\n{mentions}")
            except Exception:
                pass
                    
    finally:
        if chat_id in tagger_active_chats:
            tagger_active_chats.remove(chat_id)
        await status.edit("✅ **Bulk tagging completed safely!**")

async def handle_user_tag(event, msg_list=None, static_text=None):
    chat_id = event.chat_id
    if chat_id in tagger_active_chats:
        return await event.reply("⚠️ **Tagging is already running in this chat. Type `.canceltag` to stop it.**")
        
    status = await event.reply("✅ **Starting Per User Tag (Anti-Ban Mode)...**")
    tagger_active_chats.add(chat_id)
    messages_sent = 0
    
    users = await get_users(event)
    if not users:
        tagger_active_chats.remove(chat_id)
        return await status.edit("❌ **No users found in this chat!**")
    
    try:
        for user in users:
            if chat_id not in tagger_active_chats: 
                break
                
            mention = f"[{user.first_name}](tg://user?id={user.id})"
            text = random.choice(msg_list).format(mention=mention) if msg_list else f"{mention} {static_text}"
            
            while True:
                try:
                    await event.client.send_message(chat_id, text)
                    messages_sent += 1
                    break
                except FloodWaitError as e:
                    if e.seconds > 60:
                        await event.reply(f"🛑 **FloodWait over 60s ({e.seconds}s)! Stopping to protect account.**")
                        tagger_active_chats.remove(chat_id)
                        return
                    await asyncio.sleep(e.seconds + 2)
                except (ChatWriteForbiddenError, UserBannedInChannelError):
                    await event.reply("🛑 **Error: I lack permission to send messages here or have been muted. Stopping.**")
                    tagger_active_chats.remove(chat_id)
                    return
                    
            await human_delay(messages_sent)
            
    finally:
        if chat_id in tagger_active_chats:
            tagger_active_chats.remove(chat_id)
        await status.edit("✅ **Per user tag completed safely!**")

@client.on(events.NewMessage(pattern=r"^\.btag(?: |$)(.*)", outgoing=True))
async def bulk_tag(event):
    if event.id in processed_msgs: 
        return
    processed_msgs.append(event.id)
    
    custom_msg = event.pattern_match.group(1).strip()
    if not custom_msg:
        return await event.reply("❌ **Please provide a message. Example:** `.btag Hello everyone!`")
    
    await handle_bulk_tag(event, static_text=custom_msg)

@client.on(events.NewMessage(pattern=r"^\.utag(?: |$)(.*)", outgoing=True))
async def user_tag(event):
    if event.id in processed_msgs: 
        return
    processed_msgs.append(event.id)
    
    custom_msg = event.pattern_match.group(1).strip()
    if not custom_msg:
        return await event.reply("❌ **Please provide a message. Example:** `.utag Hello!`")
        
    await handle_user_tag(event, static_text=custom_msg)

@client.on(events.NewMessage(pattern=r"^\.btaggm$", outgoing=True))
async def btag_gm(event):
    if event.id in processed_msgs: 
        return
    processed_msgs.append(event.id)
    await handle_bulk_tag(event, msg_list=GM_MESSAGES)

@client.on(events.NewMessage(pattern=r"^\.utaggm$", outgoing=True))
async def utag_gm(event):
    if event.id in processed_msgs: 
        return
    processed_msgs.append(event.id)
    await handle_user_tag(event, msg_list=GM_MESSAGES)

@client.on(events.NewMessage(pattern=r"^\.btaggn$", outgoing=True))
async def btag_gn(event):
    if event.id in processed_msgs: 
        return
    processed_msgs.append(event.id)
    await handle_bulk_tag(event, msg_list=GN_MESSAGES)

@client.on(events.NewMessage(pattern=r"^\.utaggn$", outgoing=True))
async def utag_gn(event):
    if event.id in processed_msgs: 
        return
    processed_msgs.append(event.id)
    await handle_user_tag(event, msg_list=GN_MESSAGES)

@client.on(events.NewMessage(pattern=r"^\.btagvc$", outgoing=True))
async def btag_vc(event):
    if event.id in processed_msgs: 
        return
    processed_msgs.append(event.id)
    await handle_bulk_tag(event, msg_list=VC_MESSAGES)

@client.on(events.NewMessage(pattern=r"^\.utagvc$", outgoing=True))
async def utag_vc(event):
    if event.id in processed_msgs: 
        return
    processed_msgs.append(event.id)
    await handle_user_tag(event, msg_list=VC_MESSAGES)

@client.on(events.NewMessage(pattern=r"^\.canceltag$", outgoing=True))
async def cancel_tagging(event):
    if event.id in processed_msgs: 
        return
    processed_msgs.append(event.id)
    
    chat_id = event.chat_id
    if chat_id in tagger_active_chats:
        tagger_active_chats.remove(chat_id)
        await event.reply("🛑 **Tagging process has been successfully canceled in this chat!**")
    else:
        await event.reply("⚠️ **No tagging process is currently running in this chat.**")

# ==================== PURGE PLUGIN ====================

@client.on(events.NewMessage(pattern=r"^\.ncdel$", outgoing=True))
async def ncdel_cmd(event):
    chat_id = event.chat_id
    ncdel_enabled[chat_id] = True
    ncdel_status[chat_id] = True
    await event.reply("🧹 **Name change deletion ENABLED!**\nI will delete all system messages about name changes.")

@client.on(events.NewMessage(pattern=r"^\.ncdeloff$", outgoing=True))
async def ncdeloff_cmd(event):
    chat_id = event.chat_id
    ncdel_enabled[chat_id] = False
    ncdel_status[chat_id] = False
    await event.reply("⏹️ **Name change deletion DISABLED!**")

@client.on(events.NewMessage(pattern=r"^\.ncdelstatus$", outgoing=True))
async def ncdelstatus_cmd(event):
    chat_id = event.chat_id
    status = ncdel_status.get(chat_id, False)
    await event.reply(f"📊 **Name change deletion:** {'🟢 ENABLED' if status else '🔴 DISABLED'}")

@client.on(events.NewMessage(pattern=r"^\.(purge|p)$", outgoing=True))
async def purge(event):
    if not event.is_reply:
        await event.reply("❌ **Please reply to a message to start purging from there.**")
        return

    chat_id = event.chat_id
    user_id = event.sender_id

    if not await is_user_admin(client, chat_id, user_id):
        await event.reply("❌ **You need to be an admin to purge messages in this chat.**")
        return

    replied_msg = await event.get_reply_message()
    start_msg_id = replied_msg.id
    end_msg_id = event.message.id

    if start_msg_id >= end_msg_id:
        await event.reply("❌ **No messages to purge.**")
        return

    status = await event.reply("🗑️ **Purging messages...**")
    batch_size = 100
    
    try:
        msg_ids = list(range(start_msg_id, end_msg_id + 1))
        total = len(msg_ids)
        
        for i in range(0, len(msg_ids), batch_size):
            await client.delete_messages(chat_id, msg_ids[i:i + batch_size])
            await asyncio.sleep(0.5)
            
            if i % (batch_size * 5) == 0:
                progress = min(i + batch_size, total)
                await status.edit(f"🗑️ **Purging messages...** ({progress}/{total})")

        await status.edit(f"✅ **Purge completed successfully!** ({total} messages deleted)")
        await asyncio.sleep(3)
        await status.delete()
        
    except RPCError as e:
        await status.edit(f"❌ **Error during purge:** `{str(e)}`")
        await asyncio.sleep(5)
        await status.delete()
    except Exception as e:
        await status.edit(f"❌ **An unexpected error occurred:** `{str(e)}`")
        await asyncio.sleep(5)
        await status.delete()

@client.on(events.NewMessage(pattern=r"^\.delall$", outgoing=True))
async def delall(event):
    chat = event.chat
    user_id = event.sender_id
    is_private = isinstance(chat, PeerUser)
    
    try:
        await event.delete()
    except Exception:
        pass

    target_user = None
    target_name = "all messages"
    
    if event.is_reply:
        reply = await event.get_reply_message()
        target_user = reply.sender_id
        try:
            sender = await reply.get_sender()
            target_name = f"messages from {sender.first_name or 'User'}"
        except:
            target_name = "messages from that user"
    else:
        target_name = "ALL messages"

    if not is_private:
        if target_user and target_user != user_id:
            if not await is_user_admin(client, chat, user_id):
                msg = await event.respond("🚫 **You need admin rights to delete other users' messages!**")
                await asyncio.sleep(5)
                await msg.delete()
                return
        elif not target_user:
            if not await is_user_admin(client, chat, user_id):
                msg = await event.respond("🚫 **You need admin rights to delete all messages!**")
                await asyncio.sleep(5)
                await msg.delete()
                return

    cancellation_flags[event.chat_id] = asyncio.Event()
    cancel_flag = cancellation_flags[event.chat_id]

    warning_msg = await event.respond(
        f"⚠️ **Deleting {target_name} in 20 seconds!**\n\n"
        f"Type `.cancel` to abort.\n"
        f"📌 **This will affect ALL messages in this chat.**"
    )

    try:
        await asyncio.wait_for(cancel_flag.wait(), timeout=20)
        await warning_msg.edit("🚫 **Deletion cancelled!**")
        await asyncio.sleep(3)
        await warning_msg.delete()
        return
    except asyncio.TimeoutError:
        pass
    finally:
        cancellation_flags.pop(event.chat_id, None)

    await warning_msg.edit("🗑️ **Deleting messages...**")
    deleted_count = 0

    try:
        async for message in client.iter_messages(
            event.chat_id,
            from_user=target_user,
            reverse=True
        ):
            if message.id == warning_msg.id:
                continue
                
            try:
                await message.delete()
                deleted_count += 1
                if deleted_count % 10 == 0:
                    await warning_msg.edit(f"🗑️ **Deleting messages...** ({deleted_count} deleted)")
                    await asyncio.sleep(0.5)
            except Exception:
                pass
                
        await warning_msg.edit(f"✅ **Deleted {deleted_count} messages!**")
        await asyncio.sleep(3)
        
    except Exception as e:
        await warning_msg.edit(f"❌ **Error:** `{str(e)}`")
        await asyncio.sleep(5)
    
    try:
        await warning_msg.delete()
    except Exception:
        pass

@client.on(events.NewMessage(pattern=r"^\.cancel$", outgoing=True))
async def cancel_delall(event):
    chat_id = event.chat_id
    if chat_id in cancellation_flags:
        cancellation_flags[chat_id].set()
        try:
            await event.delete()
            confirm = await event.respond("✅ **Deletion cancelled!**")
            await asyncio.sleep(3)
            await confirm.delete()
        except Exception:
            pass
    else:
        await event.reply("❌ **No pending deletion to cancel.**")

# ==================== SUDO PLUGIN ====================

def load_sudo_users():
    global SUDO_USERS
    if not SUDO_FILE.exists():
        return
    
    try:
        with open(SUDO_FILE, "r") as f:
            data = json.load(f)
        
        for uid in data.get("users", []):
            uid = int(uid)
            if uid not in SUDO_USERS:
                SUDO_USERS.append(uid)
    except Exception as e:
        print(f"⚠️ Failed to load sudo users: {e}")

def save_sudo_users():
    global SUDO_USERS
    try:
        users = [int(x) for x in SUDO_USERS]
        with open(SUDO_FILE, "w") as f:
            json.dump({"users": users, "last_updated": datetime.now().isoformat()}, f, indent=2)
    except Exception as e:
        print(f"⚠️ Failed to save sudo users: {e}")

async def _resolve_user(event):
    text = event.pattern_match.group(1).strip() if event.pattern_match.group(1) else ""
    
    if event.is_reply:
        msg = await event.get_reply_message()
        try:
            user = await event.client.get_entity(msg.sender_id)
            return user, None
        except Exception as e:
            return None, f"⚠️ Could not resolve user: {e}"
    
    if text:
        try:
            user = await event.client.get_entity(text)
            return user, None
        except Exception:
            try:
                user = await event.client.get_entity(int(text))
                return user, None
            except Exception as e:
                return None, f"⚠️ Could not resolve user: {e}"
    
    return None, "❌ Reply to a user or provide a username/ID."

# Load sudo users on startup
load_sudo_users()

@client.on(events.NewMessage(pattern=r"^\.(?:sudo|addsudo)(?:\s+(.*))?$", outgoing=True))
async def add_sudo(event):
    global SUDO_USERS
    user, err = await _resolve_user(event)
    if err:
        await event.reply(err)
        return
    
    if user.id == event.sender_id:
        await event.reply("🚫 **You cannot add yourself as sudo.**")
        return
    
    if user.id in SUDO_USERS:
        await event.reply(f"👤 **{user.first_name}** is already a sudo user.")
        return
    
    SUDO_USERS.append(user.id)
    save_sudo_users()
    
    date = datetime.now().strftime("%d %B %Y")
    await event.reply(
        f"✅ **Added to sudo users**\n\n"
        f"👤 **Name:** [{user.first_name}](tg://user?id={user.id})\n"
        f"🆔 **ID:** `{user.id}`\n"
        f"📅 **Added on:** `{date}`\n\n"
        f"🔑 **Total sudo users:** {len(SUDO_USERS)}"
    )

@client.on(events.NewMessage(pattern=r"^\.delsudo(?:\s+(.*))?$", outgoing=True))
async def del_sudo(event):
    global SUDO_USERS
    user, err = await _resolve_user(event)
    if err:
        await event.reply(err)
        return
    
    if user.id == event.sender_id:
        await event.reply("🚫 **You cannot remove yourself as sudo.**")
        return
    
    if user.id not in SUDO_USERS:
        await event.reply(f"👤 **{user.first_name}** is not a sudo user.")
        return
    
    SUDO_USERS.remove(user.id)
    save_sudo_users()
    
    await event.reply(
        f"✅ **Removed from sudo users**\n\n"
        f"👤 **Name:** [{user.first_name}](tg://user?id={user.id})\n"
        f"🆔 **ID:** `{user.id}`\n\n"
        f"🔑 **Remaining sudo users:** {len(SUDO_USERS)}"
    )

@client.on(events.NewMessage(pattern=r"^\.listsudo$", outgoing=True))
async def list_sudo(event):
    global SUDO_USERS
    if not SUDO_USERS:
        await event.reply("📭 **No sudo users configured.**\n\n"
                         "💡 **Add one:** `.sudo @username` or reply to a user")
        return
    
    lines = ["?? **Sudo Users**\n━━━━━━━━━━━━━━━━━━━━━━\n"]
    lines.append(f"📊 **Total:** {len(SUDO_USERS)}\n")
    
    for idx, uid in enumerate(SUDO_USERS, 1):
        try:
            user = await event.client.get_entity(uid)
            name = user.first_name or "Unknown"
            username = f"@{user.username}" if user.username else "N/A"
            
            lines.append(
                f"{idx}. **{name}**\n"
                f"   🆔 `{uid}`\n"
                f"   👤 {username}\n"
            )
        except Exception:
            lines.append(
                f"{idx}. **Unknown User**\n"
                f"   🆔 `{uid}`\n"
                f"   👤 N/A\n"
            )
    
    await event.reply("\n".join(lines))

# ==================== CHATS PLUGIN ====================

@client.on(events.NewMessage(pattern=r"^\.delchat$", outgoing=True))
async def delchat(event):
    chat = await event.get_chat()
    
    if event.is_private:
        await event.reply("❌ This command only works in groups and channels!")
        return
    
    chat_name = utils.get_display_name(chat) or "Unknown Chat"
    status = await event.reply(f"🗑️ **Deleting/Leaving {chat_name}...**")
    
    try:
        await event.client(DeleteChannelRequest(chat.id))
        await status.edit(f"✅ **Chat deleted successfully!**\n📝 **Chat:** {chat_name}")
    except Exception as e:
        try:
            await event.client.delete_dialog(chat.id)
            await status.edit(f"✅ **Left the chat successfully!**\n📝 **Chat:** {chat_name}")
        except Exception as e2:
            await status.edit(f"❌ Failed to delete/leave chat: {str(e2)}")

@client.on(events.NewMessage(pattern=r"^\.getlink$", outgoing=True))
async def getlink(event):
    if event.is_private:
        await event.reply("❌ This command only works in groups and channels!")
        return
    
    status = await event.reply("🔗 **Generating invite link...**")
    
    try:
        invite = await event.client(ExportChatInviteRequest(event.chat_id))
        
        chat = await event.get_chat()
        chat_name = utils.get_display_name(chat) or "Unknown Chat"
        
        await status.edit(f"🔗 **Invite Link for {chat_name}**\n\n{invite.link}\n\n"
                         f"💡 **Share this link to invite others!**")
    except Exception as e:
        await status.edit(f"❌ Failed to get invite link: {str(e)}")

@client.on(events.NewMessage(pattern=r"^\.create\s+(group|channel)\s+(.+)$", outgoing=True))
async def create(event):
    chat_type = event.pattern_match.group(1).lower()
    chat_name = event.pattern_match.group(2).strip()
    
    if not chat_name:
        await event.reply("❌ Please provide a name!\n\n"
                         "💡 **Usage:** `.create group My Group`")
        return
    
    status = await event.reply(f"🏗️ **Creating {chat_type}...**")
    
    try:
        if chat_type == "channel":
            result = await event.client(CreateChannelRequest(
                title=chat_name,
                about=f"Created by {DEFAULTUSER} on {datetime.now().strftime('%Y-%m-%d')}",
                megagroup=False
            ))
            
            channel = result.chats[0]
            await status.edit(f"✅ **Channel Created!**\n\n"
                            f"📢 **Name:** {chat_name}\n"
                            f"🆔 **ID:** `{channel.id}`\n"
                            f"👤 **Username:** @{channel.username if channel.username else 'None'}\n\n"
                            f"🔗 **Get link:** `.getlink`\n"
                            f"📸 **Set photo:** `.setgpic` (reply to photo)")
            
        elif chat_type == "group":
            result = await event.client(CreateChannelRequest(
                title=chat_name,
                about=f"Created by {DEFAULTUSER} on {datetime.now().strftime('%Y-%m-%d')}",
                megagroup=True
            ))
            
            group = result.chats[0]
            await status.edit(f"✅ **Group Created!**\n\n"
                            f"👥 **Name:** {chat_name}\n"
                            f"🆔 **ID:** `{group.id}`\n"
                            f"👤 **Username:** @{group.username if group.username else 'None'}\n\n"
                            f"🔗 **Get link:** `.getlink`\n"
                            f"📸 **Set photo:** `.setgpic` (reply to photo)")
        
    except Exception as e:
        await status.edit(f"❌ Failed to create chat: {str(e)}")

@client.on(events.NewMessage(pattern=r"^\.setgpic$", outgoing=True))
async def setgpic(event):
    if event.is_private:
        await event.reply("❌ This command only works in groups and channels!")
        return
    
    if not event.is_reply:
        await event.reply("❌ Reply to a photo to set it as group picture!\n\n"
                         "💡 **Usage:** Reply to a photo with `.setgpic`")
        return
    
    reply = await event.get_reply_message()
    
    if not reply.photo:
        await event.reply("❌ Reply to a photo, not text or other media!")
        return
    
    status = await event.reply("📸 **Setting group photo...**")
    
    try:
        photo_path = await event.client.download_media(reply.photo)
        
        if not photo_path:
            await status.edit("❌ Failed to download photo!")
            return
        
        file = await event.client.upload_file(photo_path)
        
        await event.client(EditPhotoRequest(
            channel=event.chat_id,
            photo=file
        ))
        
        chat = await event.get_chat()
        chat_name = utils.get_display_name(chat) or "Unknown Chat"
        
        await status.edit(f"✅ **Group photo updated successfully!**\n"
                         f"📝 **Chat:** {chat_name}")
        
        if os.path.exists(photo_path):
            os.remove(photo_path)
            
    except Exception as e:
        await status.edit(f"❌ Failed to set group photo: {str(e)}")

@client.on(events.NewMessage(pattern=r"^\.setgname\s+(.+)$", outgoing=True))
async def setgname(event):
    if event.is_private:
        await event.reply("❌ This command only works in groups and channels!")
        return
    
    new_name = event.pattern_match.group(1).strip()
    
    if not new_name:
        await event.reply("❌ Please provide a new name!\n\n"
                         "💡 **Usage:** `.setgname New Group Name`")
        return
    
    status = await event.reply(f"✏️ **Changing group name to: {new_name}...**")
    
    try:
        await event.client(EditTitleRequest(
            channel=event.chat_id,
            title=new_name
        ))
        
        await status.edit(f"✅ **Group name updated successfully!**\n"
                         f"📝 **New Name:** {new_name}")
        
    except Exception as e:
        await status.edit(f"❌ Failed to update group name: {str(e)}")

# ==================== INLINE HELP SYSTEM ====================

async def setup_inline_bot():
    """Setup the inline bot for help menu"""
    bot = TelegramClient('𝗚𝖔𝖏𝖔_bot', API_ID, API_HASH)
    await bot.start(bot_token=BOT_TOKEN)
    
    @bot.on(InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        if event.text == "help":
            if event.query.user_id != OWNER_ID:
                text = (
                    "🚫 **ACCESS DENIED!**\n\n"
                    "⚡ This divine help menu is **only** for 𝗚𝖔𝖏𝖔 God**.\n"
                    "👑 You are not worthy to access this sacred power.\n\n"
                    "⚠️ **ALERT:** Unauthorized access attempt detected!\n"
                    "🔒 Your IP and ID have been logged.\n\n"
                    "💀 *Turn back now, mortal!*"
                )
                result = builder.article(
                    title="Access Denied - 𝗚𝖔𝖏𝖔 Only",
                    text=text,
                    parse_mode='html'
                )
                await event.answer([result], cache_time=0)
                return
            
            plugin_names = list(CMD_LIST.keys())
            plugin_names.sort(key=lambda x: (x != 'help', x))
            
            total_plugins = len(plugin_names)
            total_commands = sum(len(data['commands']) for data in CMD_LIST.values())
            total_pages = (total_plugins + 8) // 9
            
            text_page1 = (
                "🔥 <b>𝗚𝖔𝖏𝖔 USERBOT</b> 🔥\n"
                "━━━━━━━━━━━━━━━━━━━━━━\n"
                f"⚡ <b>Powers:</b> <code>{total_plugins}</code>\n"
                f"📂 <b>Commands:</b> <code>{total_commands}</code>\n"
                "━━━━━━━━━━━━━━━━━━━━━━\n"
                f"<b>📋 Page 1/{total_pages}</b>\n\n"
                "<i>Select a power</i>\n"
                "━━━━━━━━━━━━━━━━━━━━━━"
            )
            
            buttons_page1 = []
            row = []
            for i, plugin in enumerate(plugin_names[:9]):
                emoji = get_plugin_emoji(plugin)
                display_name = get_plugin_display_name(plugin)
                button_text = f"{emoji} {display_name}"
                row.append(Button.inline(button_text, f"help_plugin_{plugin}"))
                if (i + 1) % 3 == 0:
                    buttons_page1.append(row)
                    row = []
            if row:
                buttons_page1.append(row)
            
            nav_row = []
            if len(plugin_names) > 9:
                nav_row.append(Button.inline("➡️ Next", f"help_page_1"))
            if nav_row:
                buttons_page1.append(nav_row)
            
            result1 = builder.article(
                title="𝗚𝖔𝖏𝖔 Help - Page 1",
                text=text_page1,
                buttons=buttons_page1,
                parse_mode='html'
            )
            
            results = [result1]
            
            if len(plugin_names) > 9:
                text_page2 = (
                    "🔥 <b>𝗚𝖔𝖏𝖔 USERBOT</b> 🔥\n"
                    "━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"⚡ <b>Powers:</b> <code>{total_plugins}</code>\n"
                    f"📂 <b>Commands:</b> <code>{total_commands}</code>\n"
                    "━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"<b>📋 Page 2/{total_pages}</b>\n\n"
                    "<i>Select a power</i>\n"
                    "━━━━━━━━━━━━━━━━━━━━━━"
                )
                
                buttons_page2 = []
                row = []
                for i, plugin in enumerate(plugin_names[9:18]):
                    emoji = get_plugin_emoji(plugin)
                    display_name = get_plugin_display_name(plugin)
                    button_text = f"{emoji} {display_name}"
                    row.append(Button.inline(button_text, f"help_plugin_{plugin}"))
                    if (i + 1) % 3 == 0:
                        buttons_page2.append(row)
                        row = []
                if row:
                    buttons_page2.append(row)
                
                nav_row = []
                nav_row.append(Button.inline("⬅️ Back", f"help_page_0"))
                if len(plugin_names) > 18:
                    nav_row.append(Button.inline("➡️ Next", f"help_page_2"))
                buttons_page2.append(nav_row)
                
                result2 = builder.article(
                    title="𝗚𝖔𝖏𝖔 Help - Page 2",
                    text=text_page2,
                    buttons=buttons_page2,
                    parse_mode='html'
                )
                results.append(result2)
            
            if len(plugin_names) > 18:
                text_page3 = (
                    "🔥 <b>𝗚𝖔𝖏𝖔 USERBOT</b> 🔥\n"
                    "━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"⚡ <b>Powers:</b> <code>{total_plugins}</code>\n"
                    f"📂 <b>Commands:</b> <code>{total_commands}</code>\n"
                    "━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"<b>📋 Page 3/{total_pages}</b>\n\n"
                    "<i>Select a power</i>\n"
                    "━━━━━━━━━━━━━━━━━━━━━━"
                )
                
                buttons_page3 = []
                row = []
                for i, plugin in enumerate(plugin_names[18:27]):
                    emoji = get_plugin_emoji(plugin)
                    display_name = get_plugin_display_name(plugin)
                    button_text = f"{emoji} {display_name}"
                    row.append(Button.inline(button_text, f"help_plugin_{plugin}"))
                    if (i + 1) % 3 == 0:
                        buttons_page3.append(row)
                        row = []
                if row:
                    buttons_page3.append(row)
                
                nav_row = []
                nav_row.append(Button.inline("⬅️ Back", f"help_page_1"))
                buttons_page3.append(nav_row)
                
                result3 = builder.article(
                    title="𝗚𝖔𝖏𝖔 Help - Page 3",
                    text=text_page3,
                    buttons=buttons_page3,
                    parse_mode='html'
                )
                results.append(result3)
            
            await event.answer(results)

    @bot.on(CallbackQuery(pattern=r"help_(.*)"))
    async def callback_handler(event):
        if event.sender_id != OWNER_ID:
            await event.answer(
                "🚫 ACCESS DENIED! Only 𝗚𝖔𝖏𝖔 God can use this!",
                alert=True
            )
            return
        
        data = event.data_match.group(1).decode()
        
        if data.startswith("plugin_"):
            plugin_name = data.replace("plugin_", "")
            if plugin_name in CMD_LIST:
                emoji = get_plugin_emoji(plugin_name)
                display_name = get_plugin_display_name(plugin_name)
                text = (
                    f"{emoji} <b>{display_name}</b>\n"
                    "━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"<i>{CMD_LIST[plugin_name]['description']}</i>\n\n"
                    "<b>Commands:</b>\n"
                )
                
                for cmd in CMD_LIST[plugin_name]["commands"]:
                    if isinstance(cmd, str) and cmd.strip():
                        if " - " in cmd:
                            cmd_part, desc_part = cmd.split(" - ", 1)
                            escaped_command = cmd_part.strip().replace('<', '&lt;').replace('>', '&gt;')
                            text += f"• <code>{escaped_command}</code>\n"
                            text += f"  <i>{desc_part.strip()}</i>\n\n"
                        else:
                            escaped_cmd = cmd.strip().replace('<', '&lt;').replace('>', '&gt;')
                            text += f"• <code>{escaped_cmd}</code>\n\n"
                
                buttons = [[Button.inline("⬅️ Back", f"help_page_0")]]
                await event.edit(text, buttons=buttons, parse_mode='html')
            return
        
        if data.startswith("page_"):
            page = int(data.replace("page_", ""))
            plugin_names = list(CMD_LIST.keys())
            plugin_names.sort(key=lambda x: (x != 'help', x))
            
            total_plugins = len(plugin_names)
            total_commands = sum(len(data['commands']) for data in CMD_LIST.values())
            total_pages = (total_plugins + 8) // 9
            
            start_idx = page * 9
            end_idx = min(start_idx + 9, total_plugins)
            current_plugins = plugin_names[start_idx:end_idx]
            
            text = (
                "🔥 <b>𝗚𝖔𝖏𝖔 USERBOT</b> 🔥\n"
                "━━━━━━━━━━━━━━━━━━━━━━\n"
                f"⚡ <b>Powers:</b> <code>{total_plugins}</code>\n"
                f"📂 <b>Commands:</b> <code>{total_commands}</code>\n"
                "━━━━━━━━━━━━━━━━━━━━━━\n"
                f"<b>📋 Page {page+1}/{total_pages}</b>\n\n"
                "<i>Select a power</i>\n"
                "━━━━━━━━━━━━━━━━━━━━━━"
            )
            
            buttons = []
            row = []
            for i, plugin in enumerate(current_plugins):
                emoji = get_plugin_emoji(plugin)
                display_name = get_plugin_display_name(plugin)
                button_text = f"{emoji} {display_name}"
                row.append(Button.inline(button_text, f"help_plugin_{plugin}"))
                if (i + 1) % 3 == 0:
                    buttons.append(row)
                    row = []
            if row:
                buttons.append(row)
            
            nav_row = []
            if page > 0:
                nav_row.append(Button.inline("⬅️ Back", f"help_page_{page-1}"))
            if end_idx < total_plugins:
                nav_row.append(Button.inline("➡️ Next", f"help_page_{page+1}"))
            if nav_row:
                buttons.append(nav_row)
            
            await event.edit(text, buttons=buttons, parse_mode='html')
            return
    
    return bot

# ==================== MAIN ====================

async def main():
    print("†" * 20)
    print("♡† 𝗚𝖔𝖏𝖔 ~ #𝔬𝔣𝔣 ✞︎໋🌙 𝐔sᴇʀ𝐁ᴏᴛ v1.0 †♡")
    print("†" * 20)
    
    await client.start(phone=PHONE)
    me = await client.get_me()
    print(f"\n✅ Logged in as: {me.first_name}")
    print(f"🤖 Configured Bots: {len(DEFAULT_BOTS)}")
    print(f"📚 Loaded Powers: {len(CMD_LIST)}")
    print(f"🎭 Custom Raids: {len(custom_raid_manager.raids)}")
    print(f"🔑 Sudo Users: {len(SUDO_USERS)}")
    print("\n" + "†" * 20)
    print("⚡ 𝗚𝖔𝖏𝖔 ~ #𝔬𝔣𝔣 ✞︎໋🌙 𝐔sᴇʀ𝐁ᴏᴛ RUNNING! ⚡")
    print("†" * 20)
    print("\n📋 Type .help to summon the menu")
    print("🔥 Features:")
    print("  • Custom Raids with Rotation")
    print("  • Auto-Reply Raids")
    print("  • Spam System")
    print("  • AFK System")
    print("  • PM Assistant with Toggle (.pmp)")
    print("  • Admin Controls")
    print("  • Games & Animations")
    print("  • Bait System (Infinite Actions)")
    print("  • FlashVault (View-Once Saver)")
    print("  • GhostVault (Anti-Delete/Edit)")
    print("  • GlobalTools (Global Moderation)")
    print("  • Tagger (Bulk/User Tagging)")
    print("  • Emoji Games")
    print("  • Purge (Message Deletion)")
    print("  • Sudo (User Management)")
    print("  • Chats (Chat Management)")
    print("\n⚡ Press Ctrl+C to stop\n")
    
    try:
        inline_bot = await setup_inline_bot()
        print("✅ Inline bot started successfully!")
        print(f"💡 Try typing: @{TG_BOT_USERNAME} help")
        asyncio.create_task(inline_bot.run_until_disconnected())
    except Exception as e:
        print(f"❌ Inline bot failed to start: {e}")
        print("💡 Check your BOT_TOKEN and make sure the bot is created with @BotFather")
    
    await client.run_until_disconnected()

if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.WARNING)
        client.loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("\n\n👋 Bot stopped")
    except Exception as e:
        print(f"\n❌ Error: {e}")