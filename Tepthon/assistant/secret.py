import json
import os
import re

from telethon.events import CallbackQuery

from Tepthon import zedub
from ..sql_helper.globals import gvarstatus


@zedub.tgbot.on(CallbackQuery(data=re.compile(b"secret_(.*)")))
async def on_plug_in_callback_query_handler(event):
    timestamp = int(event.pattern_match.group(1).decode("UTF-8"))
    uzerid = gvarstatus("hmsa_id")
    ussr = int(uzerid) if uzerid.isdigit() else uzerid
    try:
        zzz = await event.client.get_entity(ussr)
    except ValueError:
        return
    if os.path.exists("./Tepthon/secret.txt"):
        jsondata = json.load(open("./Tepthon/secret.txt"))
        try:
            message = jsondata[f"{timestamp}"]
            userid = message["userid"]
            ids = [userid, zedub.uid, zzz.id]
            if event.query.user_id in ids:
                encrypted_tcxt = message["text"]
                reply_pop_up_alert = encrypted_tcxt
            else:
                reply_pop_up_alert = "هذي الهمسة مو لك يا حلو 🤍"
        except KeyError:
            reply_pop_up_alert = "- عذرًا .. هذه الرسـالة لم تعد موجودة في سيـرفرات تيبثون"
    else:
        reply_pop_up_alert = "- عذرًا .. هذه الرسـالة لم تعد موجودة في سيـرفرات تيبثون"
    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
