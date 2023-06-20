#𝙕𝙚𝙙𝙏𝙝𝙤𝙣 ®
#الملـف حقـوق وكتابـة زلـزال الهيبـه ⤶ @zzzzl1l خاص بسـورس ⤶ 𝙕𝙚𝙙𝙏𝙝𝙤𝙣
#الملف مرفـوع ع استضـافتـي مهمـا خمطت راح تطلـع حقـــوقــي بســورســـك
#هههههههههههههههههه


import asyncio
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from zthon import zedub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "البحث"


ZelzalPH_cmd = (
    "𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝗧𝗘𝗣𝗧𝗛𝗢𝗡 𝗖𝗼𝗻𝗳𝗶𝗴 📲 - كـاشـف الأرقـام العربيــة](t.me/Tepthon) 𓆪\n\n"
    "**⪼ الأمــر ↵**\n\n"
    "⪼ `.كاشف` + الرقـم مع مـفـتاح الـدولـة\n\n"
    "**⪼ الوصـف :**\n"
    "**- لجـلب معلـومـات عـن رقـم هـاتف معيـن**\n\n"
    "**⪼ مثـال :**\n\n"
    "`.كاشف اليمن 777887798` \n\n"
    "`.كاشف السعودية 555542317` \n\n"
    "`.كاشف الإمارات 43171234` \n\n"
    "**الأمـر يدعـم الـدول التـاليـة ↵** 🇾🇪🇸🇦🇦🇪🇰🇼🇶🇦🇧🇭🇴🇲 \n\n"
    "شكـرًا لاستخدام سـورس تيـبـثون\n\n"
    "\n𓆩 [𝙈𝙊𝙃𝘼𝙈𝙈𝘼𝘿](t.me/S_4_N) 𓆪"
)


@zedub.zed_cmd(
    pattern="كاشف ?(.*)",
    command=("كاشف", plugin_category),
    info={
        "header": "لـ جـلب معلـومـات عـن رقـم هـاتف معيـن .. الأمـر يدعـم الـدول التـاليـة ↵ 🇾🇪🇸🇦🇦🇪🇰🇼🇶🇦🇧🇭🇴🇲 .. سيـتم اضـافـة بقيـة الـدول العـربيـة قريبـاً",
        "الأستـخـدام": "{tr}كاشف + اسـم الدولـة + الـرقـم بـدون مفتـاح الـدولة",
    },
)
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**╮ . كـاشف الأࢪقـام الـ؏ـࢪبيـة 📲.. أࢪسـل** `.الكاشف` **للتعليـمات 𓅫╰**"
        )
    chat = "@alhber192_bot"
    zzzzl1l = await edit_or_reply(event, "**╮•⎚ جـارِ الكـشف ؏ــن الـرقـم  📲 ⌭ . . .**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1194140165)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzzzl1l.edit("**╮•⎚ تحـقق من أنـك لم تقـم بحظر البوت @alhber192_bot .. ثم اعـد استخدام الأمـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await zzzzl1l.edit("**عـذرًا مـطـوري لم أقـدر على مـعرفة نـوع الـرقـم**")
        else:
            await zzzzl1l.delete()
            await event.client.send_message(event.chat_id, response.message)



# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@zedub.zed_cmd(pattern="الكاشف")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalPH_cmd)

