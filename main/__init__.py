#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("7774029", default=None, cast=int)
API_HASH = config("531dbf42d387514dc43da07db9f2dc8f", default=None)
BOT_TOKEN = config("5264031481:AAElVQQ19zSav2s1WyoFfOtFt7QXuhdrReA", default=None)
SESSION = config("AHSAVE", default=None)
FORCESUB = config("VCAM_CHANNLE", default=None)
AUTH = config("1654867043", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=AHSAVE 
    api_hash=531dbf42d387514dc43da07db9f2dc8f
    api_id=7774029

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=5264031481:AAElVQQ19zSav2s1WyoFfOtFt7QXuhdrReA
    api_id=7774029
    api_hash=531dbf42d387514dc43da07db9f2dc8f
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
