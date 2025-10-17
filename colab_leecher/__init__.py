# copyright 2023 © Xron Trix | https://github.com/Xrontrix10

import asyncio, logging, json
import nest_asyncio

# IMPORTANT: Apply nest_asyncio FIRST in Colab
nest_asyncio.apply()

from pyrogram.client import Client

# Read the dictionary from the txt file
with open("/content/Telegram-Leecher/credentials.json", "r") as file:
    credentials = json.loads(file.read())

API_ID = credentials["API_ID"]
API_HASH = credentials["API_HASH"]
BOT_TOKEN = credentials["BOT_TOKEN"]
OWNER = credentials["USER_ID"]
DUMP_ID = credentials["DUMP_ID"]

logging.basicConfig(level=logging.INFO)

# Ensure event loop exists
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

colab_bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
