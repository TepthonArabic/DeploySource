import base64
from yt_dlp import YoutubeDL
import contextlib
import glob
import io
import os

from ShazamAPI import Shazam
from telethon import types
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from validators.url import url

from ..core.logger import logging
from your_yt_search_module import yt_search
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import delete_conv, yt_search
from ..helpers.tools import media_type
from ..helpers.utils import reply_id
from . import zedub, song_download

plugin_category = "البحث"
LOGS = logging.getLogger(__name__)

# =========================================================== #
#                                                             Tepthon
# =========================================================== #
SONG_SEARCH_STRING = "<b>╮ جـارِ البحث ؏ـن الشيء الذي بحثت عنه... 🎧♥️╰</b>"
SONG_NOT_FOUND = "<b>⎉╎لـم أستطع إيجاد المطلـوب .. جرب البحث باستخـدام الأمر (.بحث)</b>"
SONG_SENDING_STRING = "<b>╮ جـارِ تحميـل الشيء الذي بحثت عنه... 🎧♥️╰</b>"
# =========================================================== #
#                                                           حقوق زلزال Tepthon
# =========================================================== #




def get_cookies_file():
    folder_path = f"{os.getcwd()}/rcookies"
    txt_files = glob.glob(os.path.join(folder_path, '*.txt'))
    if not txt_files:
        raise FileNotFoundError("No .txt files found in the specified folder.")
    cookie_txt_file = random.choice(txt_files)
    return cookie_txt_file

@zedub.on(events.NewMessage(pattern='بحث(320)?(?:\s|$)([\s\S]*)'))
async def song(event):
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(2):
        query = event.pattern_match.group(2)
    elif reply and reply.message:
        query = reply.message
    else:
        return await edit_or_reply(event, "⎉╎قم باضافـة الشيء المراد البحث عنه ..")

    zed = base64.b64decode("QUFBQUFGRV9vWjV5XVE5bVRtd0Y1Yw==")
    zedevent = await edit_or_reply(event, "╮ جـارِ البحث ؏ـن الشيء المطلـوب")

    # إعداد الكوكيز
    cookie_file = get_cookies_file()
    
    video_link = await yt_search(str(query), cookies=cookie_file)  # تمرير الكوكيز عند البحث
    if not url(video_link):
        return await zedevent.edit(f"⎉╎عـذراً .. لـم استطـع ايجـاد {query}")

    cmd = event.pattern_match.group(1)
    q = "320k" if cmd == "320" else "128k"

    ydl_opts = {
        "format": "best",
        "outtmpl": "%(title)s.%(ext)s",
        "cookiefile": cookie_file,
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(video_link, download=True)

            # تحقق من وجود 'title' في المعلومات المستخرجة
            if 'title' not in info or 'ext' not in info:
                return await zedevent.edit("❌ لم أتمكن من استخراج معلومات الفيديو.")

            title = info['title']
            filename = f"{title}.{info['ext']}"

            await zedevent.edit(f"࿊ تم تحميـل الفيديو: {title}\n⇜ انتظـر المعالجة جارية...")

            # إرسال الملف إلى تيليجرام
            await event.client.send_file(event.chat_id, filename, force_document=False)

            # حذف الملف بعد الإرسال
            os.remove(filename)
        except Exception as e:
            await zedevent.edit(f"خطـــأ ❌: {e}")

    await zedevent.delete()

@zedub.zed_cmd(
    pattern="ابحث(?:\ع|$)([\s\S]*)",
    command=("ابحث", plugin_category),
    info={
        "header": "To reverse search song.",
        "الوصـف": "Reverse search audio file using shazam api",
        "امـر مضـاف": {"ع": "To send the song of sazam match"},
        "الاستخـدام": [
            "{tr}ابحث بالــرد ع بصمـه او مقطـع صوتي",
            "{tr}ابحث ع بالــرد ع بصمـه او مقطـع صوتي",
        ],
    },
)
async def shazamcmd(event):
    "To reverse search song."
    reply = await event.get_reply_message()
    mediatype = await media_type(reply)
    chat = "@DeezerMusicBot"
    delete = False
    flag = event.pattern_match.group(1)
    if not reply or not mediatype or mediatype not in ["Voice", "Audio"]:
        return await edit_delete(
            event, "**- بالــرد ع مقطـع صـوتي**"
        )
    zedevent = await edit_or_reply(event, "**- جـار تحميـل المقـطع الصـوتي ...**")
    name = "zed.mp3"
    try:
        for attr in getattr(reply.document, "attributes", []):
            if isinstance(attr, types.DocumentAttributeFilename):
                name = attr.file_name
        dl = io.FileIO(name, "a")
        await event.client.fast_download_file(
            location=reply.document,
            out=dl,
        )
        dl.close()
        mp3_fileto_recognize = open(name, "rb").read()
        shazam = Shazam(mp3_fileto_recognize)
        recognize_generator = shazam.recognizeSong()
        track = next(recognize_generator)[1]["track"]
    except Exception as e:
        LOGS.error(e)
        return await edit_delete(
            zedevent, f"**- خطـأ :**\n__{e}__"
        )

    file = track["images"]["background"]
    title = track["share"]["subject"]
    slink = await yt_search(title)
    if flag == "s":
        deezer = track["hub"]["providers"][1]["actions"][0]["uri"][15:]
        async with event.client.conversation(chat) as conv:
            try:
                purgeflag = await conv.send_message("/start")
            except YouBlockedUserError:
                await zedub(unblock("DeezerMusicBot"))
                purgeflag = await conv.send_message("/start")
            await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
            await conv.send_message(deezer)
            await event.client.get_messages(chat)
            song = await event.client.get_messages(chat)
            await song[0].click(0)
            await conv.get_response()
            file = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
            delete = True
    await event.client.send_file(
        event.chat_id,
        file,
        caption=f"<b>⎉╎ المقطـع الصـوتي :</b> <code>{title}</code>\n<b>⎉╎ الرابـط : <a href = {slink}/1>YouTube</a></b>",
        reply_to=reply,
        parse_mode="html",
    )
    await zedevent.delete()
    if delete:
        await delete_conv(event, chat, purgeflag)

