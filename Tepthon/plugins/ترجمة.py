# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# Cat #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by Car userbot@Github.

# This file is part of: https://github.com/Tgzedub/catTepthon
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/Tgzedub/CatUserBot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

from googletrans import LANGUAGES, Translator

from Tepthon import zedub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions.functions import getTranslate
from ..sql_helper.globals import addgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID, soft_deEmojify

plugin_category = "utils"


@zedub.zed_cmd(
    pattern="ترجمة ([\s\S]*)",
    command=("ترجمة", plugin_category),
    info={
        "header": "لترجمة النص إلى اللغة المطلوبة.",
        "note": "اكتب اختصار اللغة التي تريد ترجمتهـا": [
            "{tr}tl <language code> ; <text>",
            "{tr}tl <language codes>",
        ],
        "examples": "{tr}tl te ; CatTepthon is one of the popular bot",
    },
)
async def _(event):
    "لـ ترجمـة النـص 🌐 ."
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "en"
    elif ";" in input_str:
        lan, text = input_str.split(";")
    else:
        return await edit_delete(
            event, "`.ترجمة + اختصـار اللغـة + النـص المطلوب ⚠️ .", time=5
        )
    text = soft_deEmojify(text.strip())
    lan = lan.strip()
    Translator()
    try:
        translated = await getTranslate(text, dest=lan)
        after_tr_text = translated.text
        output_str = f"**مـترجم من {LANGUAGES[translated.src].title()} إلـى {LANGUAGES[lan].title()}**\
                \n`{after_tr_text}`"
        await edit_or_reply(event, output_str)
    except Exception as exc:
        await edit_delete(event, f"**خطـأ ❌:**\n`{exc}`", time=5)


@zedub.zed_cmd(
    pattern="ترجمة2(?: |$)([\s\S]*)",
    command=("ترجمة2", plugin_category),
    info={
        "header": "لترجمة النص إلى اللغة المطلوبة.",
        "note": "for this command set lanuage by `{tr}lang trt` command.",
        "usage": [
            "{tr}trt",
            "{tr}trt <text>",
        ],
    },
)
async def translateme(trans):
    "To translate the text to required language."
    textx = await trans.get_reply_message()
    message = trans.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await edit_or_reply(
            trans, "*لـ ترجمــة النـص إلى اللغـة المطلوبـة 💪*"
        )
    trt_LANG = gvarstatus("trt_LANG") or "en"
    try:
        reply_text = await getTranslate(soft_deEmojify(message), dest=trt_LANG)
    except ValueError:
        return await edit_delete(trans, "**لغـة الوجـهة غيـر صالحة ❌ .**", time=5)
    source_lan = LANGUAGES[f"{reply_text.src.lower()}"]
    transl_lan = LANGUAGES[f"{reply_text.dest.lower()}"]
    reply_text = f"**From {source_lan.title()}({reply_text.src.lower()}) to {transl_lan.title()}({reply_text.dest.lower()}) :**\n`{reply_text.text}`"

    await edit_or_reply(trans, reply_text)
    if BOTLOG:
        await trans.client.send_message(
            BOTLOG_CHATID,
            f"`Translated some {source_lan.title()} stuff to {transl_lan.title()} just now.`",
        )


@zedub.zed_cmd(
    pattern="اللغة (ai|ترجمة2|tocr) ([\s\S]*)",
    command=("اللغة", plugin_category),
    info={
        "header": "To set language for trt/ai command.",
        "description": "Check here [Language codes](https://bit.ly/2SRQ6WU)",
        "options": {
            "trt": "default language for trt command",
            "tocr": "default language for tocr command",
            "ai": "default language for chatbot(ai)",
        },
        "usage": "{tr}lang option <language codes>",
        "examples": [
            "{tr}lang trt te",
            "{tr}lang tocr bn",
            "{tr}lang ai hi",
        ],
    },
)
async def lang(value):
    "To set language for trt comamnd."
    arg = value.pattern_match.group(2).lower()
    input_str = value.pattern_match.group(1)
    if arg not in LANGUAGES:
        return await edit_or_reply(
            value,
            f"`Invalid Language code !!`\n`رموز اللغة المتاحة لـ الترجمـة`:\n\n`{LANGUAGES}`",
        )
    LANG = LANGUAGES[arg]
    if input_str == "trt":
        addgvar("trt_LANG", arg)
        await edit_or_reply(
            value, f"**تم تغيير لغـة الترجمـة إلـى :** `{LANG.title()}`"
        )
    elif input_str == "tocr":
        addgvar("TOCR_LANG", arg)
        await edit_or_reply(
            value, f"**تم تغيير لغـة الترجمـة إلـى:** `{LANG.title()}`"
        )
    else:
        addgvar("AI_LANG", arg)
        await edit_or_reply(
            value, f"**لغـة محادثة البوت تم تغييرها إلـى :** `{LANG.title()}`"
        )
    LANG = LANGUAGES[arg]

    if BOTLOG and input_str == "trt":
        await value.client.send_message(
            BOTLOG_CHATID, f"**لغة الترجمة:** `{LANG.title()}`"
        )
    if BOTLOG:
        if input_str == "tocr":
            await value.client.send_message(
                BOTLOG_CHATID,
                f"**Language for Translated Ocr changed to:** `{LANG.title()}`",
            )
        if input_str == "ai":
            await value.client.send_message(
                BOTLOG_CHATID,
                f"**Language for Chatbot is changed to:** `{LANG.title()}`",
            )
