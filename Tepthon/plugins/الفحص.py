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

#احمد - @RNRYR
#باقر - @E_7_V ولو ماشتغل بالكود بس يلا بئرة

@zedub.zed_cmd(pattern="فحص$")
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    random_media = ["https://telegra.ph/file/6fa698c2e409a2bf41bd6.mp4","https://telegra.ph/file/1131ec8fee887ddcc06bd.mp4"]
    RNRYRTM = time.strftime("%I:%M")
    RNRYRDATE = time.strftime("%Y/%m/%d")
    tgbot = Config.TG_BOT_USERNAME
    me = await event.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    delete = await event.delete()
    user = await event.client.get_entity(event.chat_id)
    my_mention=my_mention,
    telever=version.__version__,
    zdver=zedversion,
    pyver=python_version(),
    dbhealth=check_sgnirts,
    ping=ms,
    RNRYRTM=RNRYRTM,
    RNRYRDATE=RNRYRDATE,
    tgbot=tgbot,
    uptime=uptime,

    final_message = f"""
~ سۅٛࢪس تيبثۅٛن يعمݪ بنجاެح
--  --  --  --  --  --  --  --
~ اެسِمِكَ : {my_mention} .
~ اެصداެࢪ اެݪتيݪيثۅٛن : `{telever}` .
~ اެصداެࢪ اެݪسۅٛࢪس : `{zdver}` .
~ اެصداެࢪ اެݪباެيثۅٛن : `{pyver}` .
~ اެݪتاެࢪيخ : `{RNRYRDATE}` .
~ اެݪۅٛقت : `{RNRYRTM}` .
~ اެݪبۅٛت : {tgbot} .
~ ۅٛقت اެݪتشغيݪ : `{uptime}` .
~ اެݪماެݪك : {mention} .\n--  --  --  --  --  --  --  --"""
    send_new_message = await event.client.send_message(entity=event.chat_id, message=final_message, file=random.choice(random_media))
