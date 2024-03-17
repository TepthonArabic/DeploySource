#𝙕𝙚𝙙𝙏𝙝𝙤𝙣 ®
#الملـف حقـوق وكتابـة زلـزال الهيبـه ⤶ @zzzzl1l خاص بسـورس ⤶ 𝙕𝙚𝙙𝙏𝙝𝙤𝙣
#الملف مرفـوع ع استضـافتـي مهمـا خمطت راح تطلـع حقـــوقــي بســورســـك
#هههههههههههههههههه


import asyncio
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from Tepthon import zedub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "البحث"


ZelzalPH_cmd = (
    "**الأذكــار :**\n\n"
    "**الحمدُ لله 📿**\n\n"
    "**لا إله إلّا الله 🤍**\n\n"
    "**صلوا على النبي ♥️**\n\n"
    "**داوموا الأذكار 🥰 - سورس تيبثـون 🇵🇸🤍 .**"
)


# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@zedub.zed_cmd(pattern="اذكار")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalPH_cmd)

