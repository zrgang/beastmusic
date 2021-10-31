import requests
from pytgcalls import idle
from pytgcalls import PyTgCalls
from pyrogram import Client as Bot

from KennedyMusic.callsmusic import run
from KennedyMusic.config import API_ID, API_HASH, BOT_TOKEN, BG_IMAGE

response = requests.get(BG_IMAGE)
with open("./etc/foreground.png", "wb") as file:
    file.write(response.content)


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="KennedyMusic/handlers")
)

call_py = PyTgCalls(bot)

call_py.start()
idle()
