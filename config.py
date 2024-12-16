import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "22768571"))
API_HASH = getenv("API_HASH", "7d92204d9b502be216843739f70ded0e")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "8168401477:AAG8Kjhx8ghH0BkMgzo-rCtl1bW9ZNEXKi4")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://acha:acha@cluster0.pjq3j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 960))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002410237921"))
# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7465402367"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", #ticaret
    "https://t.me/Etikettaggerbot", 
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/EtiketTaggerDuyuru") #duyuru
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/EtiketTaggerDuyuru") #gurup

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
STRING1 = getenv("STRING_SESSION", "BAGDI8IAe3VxjuN2iwMwDeUrDHbBC980Jr18oaIhzeqG5yZK7gUXEDyRASGil6grfcW9vgW8njjl21NtvlP9_xQHG0AYWd6OAApQqC0hS-IfCo_PcbfiELXc6hQNDGgUTKRj9P-fgzGPeEmHdjlRBH9-3MZtWOiV8_s6N-OR8z_Il-1470vWg6ynWC_F4LY3poB7uwCK9y-gtIxh7UYM4oFrAq1wnwOpMy-XaVM6HmgNJGTF5GCm7p8f6g8H-m1ojgNdL4YALqGakJWWi-4inVVxd5rNQvoo1albSbqln1yodL3Wwz5NhQpwoLw_4nkm61aThGiTbKM43cSn7BtHoPBKg_YErwAAAAGikPfBAA")
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
