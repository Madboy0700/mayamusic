import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "21269322"))
API_HASH = getenv("API_HASH", "6a00b295480c9b9ceff34b43a4b92977")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7514201315:AAHX443Yipnh1T4OtElAE18dd9YBYbKkfwk")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://madboy123:madboy0707@madboy07.r1nef.mongodb.net/?retryWrites=true&w=majority&appName=madboy07")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 960))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002182187594"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7669188252"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", #ticaret
    "https://t.me/AcelyaTicaret", 
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AcelyaDuyuru") #duyuru
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/GeceExpress") #gurup

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", None)

# Time after which you're assistant account will leave chats automatically.

AUTO_LEAVE_ASSISTANT_TIME = int(

    getenv("ASSISTANT_LEAVE_TIME", "3400")

)  # Remember to give value in Seconds

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2041df9cbcd142cba804578a2cf85939")

SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "80ffd296320e49299830e80b11e3bf73")

# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 314572800))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 3221225472))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BAFEi0oAcxzDaiKAZaSDL7ujHWXq0cIxrJ1PcjBdwOdncVtYzfEejIt6We_FVAyobjoFRiyszza_2ut5S_VPawbG3ZJpNoMvm1_RjxDSHIwVWKPpmpg3Q6qHr-VBJe7GWLZ6OARTN78QFRcPLTS20pWxtH4fj9FUmr1CuVZ4S9sR9ThVgYYGViHjkkugnwK2OYnIJG1w3uEekXuDm_6vejbBu4w_MUqxlSxrXbuYdXLmFxLzUYzLPacDZ14yZ4VJbdcSSIpsBNwwFkRPY5W3eAcIp3HInKm3uRHWFvuWf8WKf-VJNx_jbYZFbUa8LxL6M6N6yKI8u-X43vHXklrHg7Z-0D8yUgAAAAHJHoacAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://camo.githubusercontent.com/916348846b424fc9431b72e7264814f8b24050baf4b71115aff855b1c8f8a43a/68747470733a2f2f74656c656772612e70682f66696c652f3336626538323061383737356630626663373733652e6a7067"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://camo.githubusercontent.com/916348846b424fc9431b72e7264814f8b24050baf4b71115aff855b1c8f8a43a/68747470733a2f2f74656c656772612e70682f66696c652f3336626538323061383737356630626663373733652e6a7067"
)
PLAYLIST_IMG_URL = "https://camo.githubusercontent.com/916348846b424fc9431b72e7264814f8b24050baf4b71115aff855b1c8f8a43a/68747470733a2f2f74656c656772612e70682f66696c652f3336626538323061383737356630626663373733652e6a7067"
STATS_IMG_URL = "https://camo.githubusercontent.com/916348846b424fc9431b72e7264814f8b24050baf4b71115aff855b1c8f8a43a/68747470733a2f2f74656c656772612e70682f66696c652f3336626538323061383737356630626663373733652e6a7067"
TELEGRAM_AUDIO_URL = "https://camo.githubusercontent.com/916348846b424fc9431b72e7264814f8b24050baf4b71115aff855b1c8f8a43a/68747470733a2f2f74656c656772612e70682f66696c652f3336626538323061383737356630626663373733652e6a7067"
TELEGRAM_VIDEO_URL = "https://camo.githubusercontent.com/916348846b424fc9431b72e7264814f8b24050baf4b71115aff855b1c8f8a43a/68747470733a2f2f74656c656772612e70682f66696c652f3336626538323061383737356630626663373733652e6a7067"
STREAM_IMG_URL = "https://camo.githubusercontent.com/916348846b424fc9431b72e7264814f8b24050baf4b71115aff855b1c8f8a43a/68747470733a2f2f74656c656772612e70682f66696c652f3336626538323061383737356630626663373733652e6a7067"
SOUNCLOUD_IMG_URL = "https://camo.githubusercontent.com/916348846b424fc9431b72e7264814f8b24050baf4b71115aff855b1c8f8a43a/68747470733a2f2f74656c656772612e70682f66696c652f3336626538323061383737356630626663373733652e6a7067"
YOUTUBE_IMG_URL = "https://camo.githubusercontent.com/916348846b424fc9431b72e7264814f8b24050baf4b71115aff855b1c8f8a43a/68747470733a2f2f74656c656772612e70682f66696c652f3336626538323061383737356630626663373733652e6a7067"
SPOTIFY_ARTIST_IMG_URL = "https://camo.githubusercontent.com/916348846b424fc9431b72e7264814f8b24050baf4b71115aff855b1c8f8a43a/68747470733a2f2f74656c656772612e70682f66696c652f3336626538323061383737356630626663373733652e6a7067"
SPOTIFY_ALBUM_IMG_URL = "https://camo.githubusercontent.com/916348846b424fc9431b72e7264814f8b24050baf4b71115aff855b1c8f8a43a/68747470733a2f2f74656c656772612e70682f66696c652f3336626538323061383737356630626663373733652e6a7067"
SPOTIFY_PLAYLIST_IMG_URL = "https://camo.githubusercontent.com/916348846b424fc9431b72e7264814f8b24050baf4b71115aff855b1c8f8a43a/68747470733a2f2f74656c656772612e70682f66696c652f3336626538323061383737356630626663373733652e6a7067"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))



if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
