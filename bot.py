from pyrogram import Client

import re, os, random, asyncio, logging, html

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(name)

APP_ID = os.environ.get("APP_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

pbot = Client("pbot", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

print("Bot started!")
pbot.run()
