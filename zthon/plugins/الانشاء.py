from telethon.tl import functions

from .. import zedub
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..utils.tools import create_supergroup

plugin_category = "الادوات"


@zedub.zed_cmd(
    pattern="انشاء (مجموعة|خارقة|قناة) ([\s\S]*)",
    command=("انشاء", plugin_category),
    info={
        "header": "لـ إنشـاء (مجموعة خارقة/مجموعة/قناة) باستخـدام البـوت",
        "امر اضافي": {
            "خارقة": "لـ إنشـاء مجمـوعـة خـارقـه",
            "مجموعة": "لـ إنشـاء مجمـوعـة",
            "قناة": "لـ إنشـاء قنـاة",
        },
        "الاستخـدام": "{tr}إنشاء (خارقة/مجموعة/قناة) + اسـم (القنـاة/المـجمـوعـة)",
        "مثــال": "{tr}إنشاء قناة تيبثون",
    },
)
async def _(event):
    "لـ إنشـاء (مجموعة خارقة/مجموعة/قناة) باستخـدام البـوت"
    type_of_group = event.pattern_match.group(1)
    group_name = event.pattern_match.group(2)
    if type_of_group == "قناة":
        descript = "**𓆰 هـذه القنـاة تم إنشائها بواسطـة .. تيبـثـون™**"
    else:
        descript = "**𓆰 هـذا الـمـجمـوعـة تم إنشائها بواسطـة .. تيبـثـون™**"
    if type_of_group == "مجموعة":
        try:
            result = await event.client(
                functions.messages.CreateChatRequest(
                    users=[Config.TG_BOT_USERNAME],
                    # Not enough users (to create a chat, for example)
                    # Telegram, no longer allows creating a chat with ourselves
                    title=group_name,
                )
            )
            created_chat_id = result.chats[0].id
            result = await event.client(
                functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                )
            )
            await edit_or_reply(
                event, f"**𓆰 المـجمـوعـة `{group_name}` تم إنشـائه.. بنجـاح✓** \n**𓆰 الرابـط** {result.link}"
            )
        except Exception as e:
            await edit_delete(event, f"**- خطـأ :**\n{str(e)}")
    elif type_of_group == "قناة":
        try:
            r = await event.client(
                functions.channels.CreateChannelRequest(
                    title=group_name,
                    about=descript,
                    megagroup=False,
                )
            )
            created_chat_id = r.chats[0].id
            result = await event.client(
                functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                )
            )
            await edit_or_reply(
                event,
                f"**𓆰 القنـاة `{group_name}` تم إنشائـها .. بنجـاح✓** \n**𓆰 الرابـط** {result.link}",
            )
        except Exception as e:
            await edit_delete(event, f"**- خطـأ :**\n{e}")
    elif type_of_group == "خارقة":
        answer = await create_supergroup(
            group_name, event.client, Config.TG_BOT_USERNAME, descript
        )
        if answer[0] != "error":
            await edit_or_reply(
                event,
                f"**𓆰 المـجمـوعـة الخـارقـة `{group_name}` تم إنشـائه.. بنجـاح✓** \n**𓆰 الرابـط** {answer[0].link}",
            )
        else:
            await edit_delete(event, f"**- خطـأ :**\n{answer[1]}")
    else:
        await edit_delete(event, "**- عـذراً .. قم باستخـدام الامـر بشكـل صحيـح ...**")
