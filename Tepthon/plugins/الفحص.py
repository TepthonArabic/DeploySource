import random
import re
import time
from datetime import datetime
from platform import python_version
from random import choice

import requests
from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from Tepthon import StartTime, zedub, tepversion

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import zedalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "العروض"
STATS = gvarstatus("T_STATS") or "فحص"

# @E_7_V 
file_path = "installation_date.txt"
if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    with open(file_path, "r") as file:
        installation_time = file.read().strip()
else:
    installation_time = datetime.now().strftime("%Y-%m-%d")
    with open(file_path, "w") as file:
        file.write(installation_time)

@zedub.zed_cmd(pattern=f"{STATS}$")
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    tepevent = await edit_or_reply(event, "**⛥ ⤻ انتـظࢪ جـاࢪي فـحص بـ ـوت TEᑭTᕼOᑎ الخـاص بـِك   ۦ**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    RANDOM_MEDIA = ["https://graph.org/file/6fa698c2e409a2bf41bd6.mp4", "https://graph.org/file/1131ec8fee887ddcc06bd.mp4"]
    T_EMOJI = gvarstatus("ALIVE_EMOJI") or "☼ ⤶"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "** ☼ TEᑭTᕼOᑎ ᗯOᖇKՏ ՏᑌᑕᑕEՏՏᖴᑌᒪᒪY ‌‌‏𓅓 . **"
    TEP_IMG = gvarstatus("ALIVE_PIC")
    tep_caption = gvarstatus("ALIVE_TEMPLATE") or tep_temp
    caption = tep_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        T_EMOJI=T_EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        tepver=tepversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
        Tepthon_Tare5=installation_time
    )
    if TEP_IMG:
        TEP = [x for x in TEP_IMG.split()]
        PIC = random.choice(TEP)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await tepevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                tepevent,
                f"**⌔∮ عـذراً عليـك الـرد ع صـوره او ميـديـا  ⪼  `.اضف صورة الفحص` <بالرد ع الصـوره او الميـديـا> ",
            )
    else:
        await edit_or_reply(
            tepevent,
            caption,
        )


tep_temp = """{ALIVE_TEXT}
———————⛥ ———————
**{T_EMOJI} َTEᒪETᕼOᑎ 𓋪** `{telever}`
**{T_EMOJI} TEᑭTᕼOᑎ 𓋪** `{zdver}`
**{T_EMOJI} َᑭYTᕼOᑎ 𓋪** `{pyver}`
**{T_EMOJI} ᑌᑭTIᗰE 𓋪** `{uptime}`
**{T_EMOJI} OᗯᑎEᖇ 𓋪** {mention}
**{T_EMOJI} ᗪᗩTᗴ 𓋪** {Tepthon_Tare5}"""
     send_new_message = await event.client.send_message(entity=event.chat_id, message=final_message, file=random.choice(RANDOM_MEDIA))


@zedub.zed_cmd(
    pattern="الفحص$",
    command=("الفحص", plugin_category),
    info={
        "header": "- لـ التحـقق مـن أن البـوت يعمـل بنجـاح .. بخـاصيـة الانـلايـن ✓",
        "الاسـتخـدام": [
            "{tr}الفحص",
        ],
    },
)
async def amireallyialive(event):
    "A kind of showing bot details by your inline bot"
    reply_to_id = await reply_id(event)
    T_EMOJI = gvarstatus("ALIVE_EMOJI") or "☼ ⤶"
    tep_caption = "** ☼ TEᑭTᕼOᑎ ᗯOᖇKՏ ՏᑌᑕᑕEՏՏᖴᑌᒪᒪY ‌‌‏𓅓 . **\n"
    tep_caption += f"**{T_EMOJI} َTEᒪETᕼOᑎ 𓋪** `{version.__version__}\n`"
    tep_caption += f"**{T_EMOJI} TEᑭTᕼOᑎ 𓋪 :** `{zedversion}`\n"
    tep_caption += f"**{T_EMOJI} َᑭYTᕼOᑎ 𓋪** `{python_version()}\n`"
    tep_caption += f"**{T_EMOJI} OᗯᑎEᖇ 𓋪** {mention}\n"
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, zed_caption)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


@zedub.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await zedalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
