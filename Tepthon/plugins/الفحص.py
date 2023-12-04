import random
import re
import time
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

from Tepthon import StartTime, zedub, zedversion

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import zedalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "العروض"
STATS = gvarstatus("Z_STATS") or "فحص"


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
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    zedevent = await edit_or_reply(event, "**⛥ ⤻ انتـظࢪ جـاࢪي فـحص بـ ـوت TEᑭTᕼOᑎ الخـاص بـِك   ۦ**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    random_media = ["https://telegra.ph/file/6fa698c2e409a2bf41bd6.mp4","https://telegra.ph/file/1131ec8fee887ddcc06bd.mp4"]
    RNRYRTM = time.strftime("%I:%M")
    RNRYRDATE = time.strftime("%Y/%m/%d")
    Z_EMOJI = gvarstatus("ALIVE_EMOJI") or "•"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "** سۅٛࢪس تيبثۅٛن يعمݪ بنجاެح **"
    ZED_IMG = gvarstatus("ALIVE_PIC")
    zed_caption = gvarstatus("ALIVE_TEMPLATE") or zed_temp
    caption = zed_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        Z_EMOJI=Z_EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        zdver=zedversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
        RNRYRTM=RNRYRTM,
        RNRYRDATE=RNRYRDATE,
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
--  --  --  --  --  --  --  --
{Z_EMOJI} اެصداެࢪ اެݪتيݪيثۅٛن : `{telever}` .
{Z_EMOJI} اެصداެࢪ اެݪسۅٛࢪس : `{zdver}` .
{Z_EMOJI} اެصداެࢪ اެݪباެيثۅٛن : `{pyver}` .
{Z_EMOJI} اެݪتاެࢪيخ : `{RNRYRDATE}` .
{Z_EMOJI} اެݪۅٛقت : `{RNRYRTM}` .
{Z_EMOJI} ۅٛقت اެݪتشغيݪ : `{uptime}` .
{Z_EMOJI} اެݪماެݪك : {mention} .\n--  --  --  --  --  --  --  --"""
