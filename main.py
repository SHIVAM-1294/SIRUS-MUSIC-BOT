from pyrogram import Client as Bot

from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=1757815027:AAHGFg9x4tajC4b5jYAvkN_UuoBCe0jLtgE,
    plugins=dict(root="handlers")
)

bot.start()
run()
