# Copyright (C) 2020-2023 by TgCatUB@Github.

# This file is part of: https://github.com/TgCatUB/catuserbot
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/TgCatUB/catuserbot/blob/master/LICENSE
---------------------------------------------------------------------------------
from googletrans import LANGUAGES, Translator

from Tepthon import zedub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions.functions import getTranslate
from ..sql_helper.globals import addgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID, soft_deEmojify

plugin_category = "utils"


@zedub.zedub_cmd(
    pattern="ترجمة ([\s\S]*)",
    command=("ترجمة", plugin_category),
    info={
        "header": "لـ ترجمـة النـص إلى اللغة المطلوبة",
        "note": "انظر إلى أكواد اللغات [هُنــا](https://bit.ly/2SRQ6WU)",
        "usage": [
            "{tr}tl <language code> ; <text>",
            "{tr}tl <language codes>",
        ],
        "examples": "{tr} ترجمة ar Free Palestine",
    },
)
async def _(event):
    "**⋙ لـ ترجمـة النـص**."
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "en"
    elif ";" in input_str:
        lan, text = input_str.split(";")
    else:
        return await edit_delete(
            event, "**⋙ .ترجمة + رمز اللغة بالرد على الرسالة**", time=5
        )
    text = soft_deEmojify(text.strip())
    lan = lan.strip()
    Translator()
    try:
        translated = await getTranslate(text, dest=lan)
        after_tr_text = translated.text
        output_str = f"**⋙ تم الترجمـة {LANGUAGES[translated.src].title()} إلـى {LANGUAGES[lan].title()}**\
                \n`{after_tr_text}`"
        await edit_or_reply(event, output_str)
    except Exception as exc:
        await edit_delete(event, f"**⋙ خطـأ :**\n`{exc}`", time=5)
