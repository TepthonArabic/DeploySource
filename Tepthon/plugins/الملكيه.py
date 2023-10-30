"""امـر نقـل ملكيـة القنـاة/الكـروب
كتابـة وتطويـر الكـود لـ زلـزال الهيبـه T.ME/zzzzl1l
حقـــوق زدثـــون™ T.me/ZedThon"""

import telethon.password as pwd_mod
from telethon.tl import functions

from zthon import zedub

from ..Config import Config
from ..sql_helper.globals import gvarstatus

plugin_category = "الادوات"


@zedub.zed_cmd(
    pattern="تحويل ملكية ([\s\S]*)",
    command=("تحويل ملكية", plugin_category),
    info={
        "header": "لـ تحويـل ملكيـة القنـاة أو الكـروب",
        "الاستخـدام": "{tr}تحويل ملكية + معـرف الشخص الذي تريد نقل الملكـيـة اليـه",
    },
)
async def _(event):
    "لـ تحويـل ملكيـة القنـاة أو الكـروب"
    user_name = event.pattern_match.group(1)
    if gvarstatus("TG_2STEP_VERIFICATION_CODE") is None:
        return await edit_or_reply(event, "**𓆰قم أولًا بـ إضـافة كـود التحقق بخطوتين الخـاص بك لـ الفـارات **\n**𓆰عبـر الامـر : ↶**\n `.اضف التحقق` **بالـرد ع كـود التحقق الخـاص بك**\n\n**𓆰ثم ارسـل الامـر : ↶**\n`.تحويل ملكية` **ومعـرف الشخص**\n\n**𓆰لتحويـل ملكيـة القنـاة/الكـروب للشخـص**")
    try:
        pwd = await event.client(functions.account.GetPasswordRequest())
        my_srp_password = pwd_mod.compute_check(pwd, gvarstatus("TG_2STEP_VERIFICATION_CODE"))
        await event.client(
            functions.channels.EditCreatorRequest(
                channel=event.chat_id, user_id=user_name, password=my_srp_password
            )
        )
    except Exception as e:
        await event.edit(f"**- خطـأ :**\n`{e}`")
    else:
        await event.edit("**𓆰تم نقـل الملكـيـة .. بنجـاح✓**")
