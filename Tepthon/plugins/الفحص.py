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
from ..helpers.functions import zedalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus

plugin_category = "العروض"
STATS = gvarstatus("Z_STATS") or "فحص"


@zedub.zed_cmd(pattern=f"{STATS}$")
async def zed_alive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    start = datetime.now()
    zedevent = await edit_or_reply(event, "**✦ جـاري فحـص تنصيبـك لـ 𝗧𝗘𝗣𝗧𝗛𝗢𝗡 ⌬ . .**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    if gvarstatus("z_date") is not None:
        zzd = gvarstatus("z_date")
        zzt = gvarstatus("z_time")
        zedda = f"{zzd}┊{zzt}"
    else:
        zedda = f"{bt.year}/{bt.month}/{bt.day}"
    Z_EMOJI = gvarstatus("ALIVE_EMOJI") or "✥┊"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "**بـوت تيبثـون 𝗧𝗘𝗣𝗧𝗛𝗢𝗡 يعمـل بنجـاح ☑️ ..**"
    ZED_IMG = gvarstatus("ALIVE_PIC")
    USERID = zedub.uid if Config.OWNER_ID == 0 else Config.OWNER_ID
    ALIVE_NAME = gvarstatus("ALIVE_NAME") if gvarstatus("ALIVE_NAME") else "-"
    mention = f"[{ALIVE_NAME}](tg://user?id={USERID})"
    zed_caption = gvarstatus("ALIVE_TEMPLATE") or zed_temp
    caption = zed_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        Z_EMOJI=Z_EMOJI,
        mention=mention,
        uptime=uptime,
        zedda=zzd,
        zzd=zzd,
        zzt=zzt,
        telever=version.__version__,
        tepver=tepversion,
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
            await zedevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                zedevent,
                f"**⌔∮ عـذراً عليـك الـرد ع صـوره او ميـديـا  ⪼  `.اضف صورة الفحص` <بالرد ع الصـوره او الميـديـا> ",
            )
    else:
        await edit_or_reply(
            zedevent,
            caption,
        )


zed_temp = """{ALIVE_TEXT}

**{Z_EMOJI} قاعدة البيانات :** تعمـل بـ نجـاح ♾
**{Z_EMOJI} إصـدار المكتبـة :** `{telever}`
**{Z_EMOJI} إصـدار السـورس :** `{tepver}`
**{Z_EMOJI} إصـدار بايثـون :** `{pyver}`
**{Z_EMOJI} منصـة التنصيب :** `KOYᗴᗷ`
**{Z_EMOJI} وقت التشغيل :** `{uptime}`
**{Z_EMOJI} تاريـخ التنصيب :** `{zzd}`
**{Z_EMOJI} وقت التنصيب :** `{zzt}`
**{Z_EMOJI} المسـتخـدم:** {mention}
**{Z_EMOJI} قنـاة السـورس :** [اضغـط هنـا](https://t.me/Tepthon)"""
