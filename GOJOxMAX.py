import asyncio
import random
import os
from playwright.async_api import async_playwright

# ================== COLOR SUPPORT ==================
try:
    from colorama import init, Fore
    init(autoreset=True)
except ImportError:
    class Fore:
        MAGENTA = CYAN = WHITE = LIGHTYELLOW_EX = RED = GREEN = YELLOW = RESET = ''

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def professional_banner():
    clear()
    banner = f"""{Fore.MAGENTA}╔════════════════════════════════════════════════════════════════════════════╗
{Fore.CYAN}║ 💛👑 𝐆𝐎𝐉𝐎~x~ᗰᗩ᙭ 𓂃Ꮆ۝Ꮆ ࣪˖⚜️𓂃˖ ࣪⊹♱ • P Y S P A M 💛👑 ║  Msg - @Rdp_ruler (Dm for queries my tg)
{Fore.MAGENTA}╚════════════════════════════════════════════════════════════════════════════╝
{Fore.WHITE} SPAMigV2 • {Fore.LIGHTYELLOW_EX} DEVELOPED BY : {Fore.RED}𝐆𝐎𝐉𝐎~x~ᗰᗩ᙭ 𓂃Ꮆ۝Ꮆ ࣪˖⚜️𓂃˖ ࣪⊹♱{Fore.LIGHTYELLOW_EX}
{Fore.RED} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{Fore.CYAN} STATUS │ {Fore.GREEN}● HARI GOD SCRIPT IS ACTIVE!{Fore.CYAN}
{Fore.CYAN} MODE   │ {Fore.YELLOW}FAST SPAM FIXED STRIKES {Fore.CYAN}
{Fore.CYAN} VERSION│ {Fore.WHITE}2.0{Fore.CYAN}
{Fore.CYAN} POWER  │ {Fore.MAGENTA}MULTI ENGINE BACKGROUND MODE {Fore.CYAN}
{Fore.RED} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{Fore.RESET}"""
    print(banner)

# ================== YOUR STRIKES ==================
STRIKES = [
    "『#HATER〆#』 𐙚࣪ 𝐀ᴘɴɪ 𝐌ᴀ ᴋɪ 𝐂ꪊᴅᴀɪ 𝕯ᴇᴋʜ ❤‍🔥༆",
    "『#HATER〆#』 𐙚࣪𝐀ᴘɴɪ 𝐌ᴀ ᴄʜᴜᴛ ᴘᴇ 𝐆ᴜsᴊᴀ 🌪༆",
    "『#HATER〆#』 𐙚࣪ 𝐀ᴘɴɪ 𝐌ᴀ ᴋɪ 𝐂ꪊᴅᴀɪ 𝕯ᴇᴋʜ 🌙༆",
    "『#HATER〆#』 𐙚࣪ 𝐓ᴇʀɪ ᴍᴀ 𝐑ᴀɴᴅɪ 🌪༆",
    "『#HATER〆#』 𐙚࣪ 𝐓ᴇʀɪ ᴍᴀ 𝐇ɪᴊɪᴅɪ 🌙༆"
]

INVISIBLE = "⠀\n" * 100

async def send_combined_message(page, text):
    try:
        selectors = [
            'div[aria-label="Message"][contenteditable="true"]',
            'div[role="textbox"][contenteditable="true"]',
            'div[contenteditable="true"]'
        ]

        box = None
        for sel in selectors:
            box = await page.query_selector(sel)
            if box:
                break

        if not box:
            await page.click('div[role="main"]', timeout=5000)
            await asyncio.sleep(0.8)
            box = await page.wait_for_selector('div[contenteditable="true"]', timeout=8000)

        if not box:
            return False

        full_msg = INVISIBLE + text

        await box.click()
        await box.fill(full_msg)
        await page.keyboard.press("Enter")

        print(f'𝐆𝐎𝐉𝐎~x~ᗰᗩ᙭ 𓂃Ꮆ۝Ꮆ ࣪˖⚜️𓂃˖ ࣪⊹♱ sent "{text}"')
        
        await asyncio.sleep(0.08)
        return True

    except:
        return False

async def spam_cycle(page, hater_name, delay):
    # Replace ONLY the word "HATER" 
    strikes = [s.replace("HATER", hater_name) for s in STRIKES]
    
    print(f"🚀 Background Engine Running | Hater: {hater_name} | Delay: {delay}s\n")

    while True:
        for strike in strikes:
            await send_combined_message(page, strike)
            await asyncio.sleep(delay)

        await asyncio.sleep(0.05)

async def main():
    professional_banner()

    print("=== Ultra Fast Background Instagram Spam ===\n")

    sessionid = input("Enter your Instagram sessionid: ").strip()
    gc_url = input("Enter Group Chat URL: ").strip()
    
    hater_name = input("Enter Hater Name: ").strip() or "HATER"

    try:
        delay = float(input("Enter delay (0.1 - 2.0 | default 0.2 for ultra fast): ") or "0.2")
        if delay < 0.05:
            delay = 0.1
    except:
        delay = 0.2

    try:
        engines = int(input("Enter number of engines (3-5 recommended): ") or "4")
        engines = max(1, min(8, engines))
    except:
        engines = 4

    # After engine input - show thank you message
    print(f"\n{Fore.GREEN}Ty for using hari py!~{Fore.RESET}\n")
    
    print(f"{Fore.GREEN}Launching {engines} background engines (Hidden Mode)...{Fore.RESET}")
    print(f"{Fore.CYAN}Press Ctrl + C to stop\n{Fore.RESET}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=['--no-sandbox', '--disable-blink-features=AutomationControlled']
        )

        tasks = []
        for i in range(engines):
            context = await browser.new_context()
            await context.add_cookies([{
                'name': 'sessionid',
                'value': sessionid,
                'domain': '.instagram.com',
                'path': '/',
                'httpOnly': True,
                'secure': True
            }])

            page = await context.new_page()
            await page.goto(gc_url, wait_until="domcontentloaded", timeout=60000)
            await asyncio.sleep(7)

            print(f"Engine {i+1} started in background")
            tasks.append(spam_cycle(page, hater_name, delay))

        try:
            await asyncio.gather(*tasks)
        except asyncio.CancelledError:
            print(f"\n{Fore.RED}🛑 Stopping all background engines...{Fore.RESET}")
        finally:
            await browser.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Script stopped by user (Ctrl+C). Goodbye!{Fore.RESET}")
