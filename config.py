## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BACXB6roqxOZHdeH7Fl2ZllveNZ3vdbLqY778srJvgeN0wL9T94S_Vn43ALlaY5utgaGkOWCJAubKuxnuO1iU7r_3S24QSUDUP9ZVlvG-KlqNIFjFYVhkxH5A6Meh26tiLiLP8OxYPAjwu6JqGklJjz-SWKU5_-UF2T0jDi6j92iOmAd3rh_33SGNhVL7bMB-Gy1ewgyHOo9h3Izh1nfdZDxb6DKHP-XsBlq-MmrCrBBJx7V3YNA91dWtYw5BI6E_8Wmr0iQEQM4essXsYm95WDEC_EJrBjCXoRpzjuDrSy9q1kpBHCoN1aDdAK2TZ7RBlv1sENjgZDVkuVBZYwjNi3UAAAAAVrFDwcA")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "6189663454:AAGBt36qMRDxwD4khyDk2UJgecEpxSy4gus")
BOT_NAME = getenv("BOT_NAME", "Umk")

API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Cloner:Cloner@cluster0.cgc6t.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Eslam")
OWNER_USERNAME = getenv("OWNER_USERNAME", "K_3_4")
ALIVE_NAME = getenv("ALIVE_NAME", "Eslam")
BOT_USERNAME = getenv("BOT_USERNAME", "DFG7BOT")
OWNER_ID = getenv("OWNER_ID", "5768130077")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "FBFFCB")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "F_I_K0")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "GG7GW")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5768130077").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/EF-YY/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
