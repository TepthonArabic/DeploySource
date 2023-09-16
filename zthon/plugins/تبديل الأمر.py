```
import os
import shutil
from asyncio import sleep
import random

from telethon import events

from Zara import zedub
from Zara.core.logger import logging
from ..Config import Config
from ..core.managers import edit_or_reply, edit_delete
from ..helpers import reply_id, get_user_from_event
from . import BOTLOG, BOTLOG_CHATID
plugin_category = "تبديل الامر"
LOGS = logging.getLogger(__name__)

async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj
########################  ZThon Userbot ~ By: Zelzal (@zzzzl1l)  ########################
@zedub.zed_cmd(pattern="تبديل الامر")
async def _(zed):
await edit_or_reply (zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗧𝗘𝗣𝗧𝗛𝗢𝗡 - 𝘿𝙀𝙇𝙀𝙏𝙀](t.me/Tepthon)

 def switch_values(a, b):
    temp = a
    a = b
    b = temp

    return a, b

x = 5
y = 10

print(f"قبل التبديل: x = {x}, y = {y}")

x, y = switch_values(x, y)

print(f"بعد التبديل: x = {x}, y = {y}")