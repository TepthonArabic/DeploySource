#باقر_ريبثون
import random
import glob
import asyncio
import yt_dlp
import os
from telethon import TelegramClient, events
from yt_dlp import YoutubeDL
from Tepthon import zedub
from ..Config import Config

plugin_category = "البوت"

def get_cookies_file():
    folder_path = f"{os.getcwd()}/rcookies"
    txt_files = glob.glob(os.path.join(folder_path, '*.txt'))
    if not txt_files:
        raise FileNotFoundError("No .txt files found in the specified folder.")
    cookie_txt_file = random.choice(txt_files)
    return cookie_txt_file


@zedub.on(events.NewMessage(pattern='.بحث3 (.*)'))
async def get_song(event):
    song_name = event.pattern_match.group(1)
    await event.reply(f"جاري البحث عن المطلوب.: {song_name}...")

    # إعداد خيارات yt-dlp
    ydl_opts = {
        "format": "bestaudio/best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "writethumbnail": False,
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [
            {"key": "FFmpegVideoConvertor", "preferedformat": "mp3"},
            {"key": "FFmpegMetadata"},
            {"key": "FFmpegExtractAudio"},
        ],
        "outtmpl": "%(title)s.%(ext)s",
        "logtostderr": False,
        "quiet": True,
        "no_warnings": True,
        "cookiefile" : get_cookies_file(),
   }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f"ytsearch:{song_name}", download=True)
            title = info['entries'][0]['title']
            filename = f"{title}.mp3"

            await event.reply(f"تم العثور على المطلوب بحثه: {title}nجاري إرسال الملف...")

            # إرسال الملف إلى تيليجرام
            await zedub.send_file(event.chat_id, filename)

            # حذف الملف بعد الإرسال
            os.remove(filename)
        except Exception as e:
            await event.reply(f"حدث خطأ أثناء البحث عن المطلوب: {e}")
