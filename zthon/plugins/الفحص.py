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

from zthon import StartTime, zedub, zedversion

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import zedalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "العروض"
STATS = gvarstatus("Z_STATS") or "فحص"


@zedub.zed_cmd(pattern=f"{STATS}$")
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    zedevent = await edit_or_reply(event, "**⛥ ⤻ انتـظࢪ جـاࢪي فـحص بـ ـوت TEᑭTᕼOᑎ الخـاص بـِك   ۦ**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    Z_EMOJI = gvarstatus("ALIVE_EMOJI") or " ⎉┊"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "** سُـورس TEᑭTᕼOᑎ يـَعمل بنـَجاح **"
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
**{Z_EMOJI} َِ🕊 ٍَ𝖣ٰ𝖺َ𝖳𝖺ِ𝖡𝗎َِ𝖲َ𝖾 :** ᖴِᵘ𝖭𝖼𝖳ْ𝗂𝗈ً𝖭𝗂𝖭𝗀 
**{Z_EMOJI} َِ🕊️ ٰ𝖳َ𝖾ْ𝗅ِ𝖾𝖳َ𝗁𝗈ٍ𝖭 ُ𝖵ِ𝖾𝗋𝗌ْ𝗂𝗈َ𝗇 :** `{telever}`
**{Z_EMOJI} 🕊 𝖳َ𝖾ْ𝗉𝖳َ𝗁𝗈ٍ𝖭 َ𝖵𝖾𝗋ِ𝗌ْ𝗂𝗈َِ𝖭** `{zdver}`
**{Z_EMOJI} َِ🕊 𝖯ِ𝗒َ𝖳𝗁𝗈ً𝖭 𝖵𝖾𝗋𝗌𝗂𝗈َِ𝖭 :** `{pyver}`
**{Z_EMOJI} َِ🕊 ٰ𝖴𝗉 َ𝖳ْ𝗂𝖬ِ𝖾 :** `{uptime}`
**{Z_EMOJI} • ＴＨＥ ＵＳＥＲ:** {mention} 🤍 .
**{Z_EMOJI} 𝚂OᑌᖇᑕE ᑕᕼᗩᑎᑎEᒪ :** [TEᑭTᕼOᑎ](https://t.me/Tepthon)"""


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
    Z_EMOJI = gvarstatus("ALIVE_EMOJI") or " ⎉┊"
    zed_caption = "** سُـورس TEᑭTᕼOᑎ يـَعمل بنـَجاح **\n"
    zed_caption += f"**{Z_EMOJI} َِ🕊️ ٰ𝖳َ𝖾ْ𝗅ِ𝖾𝖳َ𝗁𝗈ٍ𝖭 ُ𝖵ِ𝖾𝗋𝗌ْ𝗂𝗈َ𝗇 :** `{version.__version__}\n`"
    zed_caption += f"**{Z_EMOJI} 🕊 𝖳َ𝖾ْ𝗉𝖳َ𝗁𝗈ٍ𝖭 َ𝖵𝖾𝗋ِ𝗌ْ𝗂𝗈َِ𝖭 :** `{zedversion}`\n"
    zed_caption += f"**{Z_EMOJI} َِ🕊 𝖯ِ𝗒َ𝖳𝗁𝗈ً𝖭 𝖵𝖾𝗋𝗌𝗂𝗈َِ𝖭 :** `{python_version()}\n`"
    zed_caption += f"**{Z_EMOJI} • ＴＨＥ ＵＳＥＲ : -** {mention}\n"
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, zed_caption)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


@zedub.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await zedalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
