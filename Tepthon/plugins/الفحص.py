import random
import re
import time
import psutil
from datetime import datetime
from platform import python_version

import requests
from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from . import StartTime, zedub, tepversion

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import tepalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "العروض"
STATS = gvarstatus("Z_STATS") or "فحص"


@zedub.zed_cmd(pattern=f"{STATS}$")
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    start = datetime.now()
    tepevent = await edit_or_reply(event, "**✦ | جـارِ فحـص سـورس ᴛᴇᴘᴛʜᴏɴ العربي ...**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    if gvarstatus("z_date") is not None:
        zzd = gvarstatus("z_date")
        zzt = gvarstatus("z_time")
        zedda = f"{zzd}┊{zzt}"
    else:
        zedda = f"{bt.year}/{bt.month}/{bt.day}"
    Z_EMOJI = gvarstatus("ALIVE_EMOJI") or "✦┊"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "** ᴀʀᴀʙ ᴛᴇᴘᴛʜᴏɴ ѕᴏᴜʀᴄᴇ ɪѕ ᴡᴏʀᴋɪɴɢ ѕᴜᴄᴄᴇѕѕғᴜʟʟʏ - سـورس تيبثـون العربـي يعمـلُ بنجـاح **"
    ZED_IMG = gvarstatus("ALIVE_PIC")
    zed_caption = gvarstatus("ALIVE_TEMPLATE") or tep_temp
    caption = zed_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        Z_EMOJI=Z_EMOJI,
        mention=mention,
        uptime=uptime,
        zedda=zedda,
        telever=version.__version__,
        zdver=tepversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if ZED_IMG:
        ZED = [x for x in ZED_IMG.split()]
        PIC = random.choice(ZED)
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

**{Z_EMOJI} قاعدة البيانات :** تعمـل بـ نجـاح ♾
**{Z_EMOJI} إصـدار المكتبـة :** `{telever}`
**{Z_EMOJI} إصـدار السـورس :** `{zdver}`
**{Z_EMOJI} إصـدار بايثـون :** `{pyver}`
**{Z_EMOJI} وقت التشغيل :** `{uptime}`
**{Z_EMOJI} تاريـخ التنصيب :** `{zedda}`
**{Z_EMOJI} المسـتخـدم:** {mention}
**{Z_EMOJI} قنـاة السـورس :** [اضغـط هنـا](https://t.me/Tepthon)"""


@zedub.zed_cmd(
    pattern="الفحص$",
    command=("الفحص", plugin_category),
    info={
        "header": "- لـ التحـقق من ان البـوت يعمـل بنجـاح .. بخـاصيـة الانـلايـن ✓",
        "الاسـتخـدام": [
            "{tr}الفحص",
        ],
    },
)
async def amireallyialive(event):
    "A kind of showing bot details by your inline bot"
    reply_to_id = await reply_id(event)
    Z_EMOJI = gvarstatus("ALIVE_EMOJI") or "✦┊"
    zed_caption = "** ᴀʀᴀʙ ᴛᴇᴘᴛʜᴏɴ ѕᴏᴜʀᴄᴇ ɪѕ ᴡᴏʀᴋɪɴɢ ѕᴜᴄᴄᴇѕѕғᴜʟʟʏ - سـورس تيبثـون العربـي يعمـلُ بنجـاح **\n"
    zed_caption += f"**{Z_EMOJI} إصـدار التـيليثون :** `{version.__version__}\n`"
    zed_caption += f"**{Z_EMOJI} إصـدار تيبثـون :** `{tepversion}`\n"
    zed_caption += f"**{Z_EMOJI} إصـدار البـايثون :** `{python_version()}\n`"
    zed_caption += f"**{Z_EMOJI} المسـتخدم :** {mention}\n"
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, zed_caption)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


@zedub.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await tepalive(StartTime)
  #كتابـة_زلـزال_الهيبـة
    await event.answer(statstext, cache_time=0, alert=True)
