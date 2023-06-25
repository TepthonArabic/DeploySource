#بسم الله الرحمن الرحيم
from telethon import events
from zthon import zedub
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..core.managers import edit_delete
from telethon import functions
from telethon.errors.rpcerrorlist import MessageIdInvalidError
@zedub.on(admin_cmd(pattern="(خط الغامق|غامق)"))
async def btext(event):
    isbold = gvarstatus("bold")
    if not isbold:
        addgvar ("bold", "on")
        await edit_delete(event, "**⪼ تـم تـفـعيل الخط الغامق بنجاح الآن**")
        return

    if isbold:
        delgvar("bold")
        await edit_delete(event, "**⪼ تـم إطفـاء الخط الغامق بنجاح الآن **")
        return

@zedub.on(admin_cmd(pattern="(رمز|خط الرمز)"))
async def btext(event):
    isramz = gvarstatus("ramz")
    if not isramz:
        addgvar ("ramz", "on")
        await edit_delete(event, "**⪼ تـم تـفـعيل خط الرمز بنجاح الآن**")
        return

    if isramz:
        delgvar("ramz")
        await edit_delete(event, "**⪼ تـم إطفـاء خط الرمز بنجاح الآن **")
        return

@zedub.on(events.NewMessage(outgoing=True))
async def reda(event):
    isbold = gvarstatus("bold")
    if isbold:
        try:
            await event.edit(f"**{event.message.message}**")
        except MessageIdInvalidError:
            pass
    isramz = gvarstatus("ramz")
    if isramz:
        try:
            await event.edit(f"`{event.message.message}`")
        except MessageIdInvalidError:
            pass
