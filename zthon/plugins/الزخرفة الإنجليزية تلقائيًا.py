from telethon import events

from zthon import zedub

from ..sql_helper.globals import addgvar, delgvar, gvarstatus


@zedub.zed_cmd(pattern="تفعيل الزخرفة الانجليزية")
async def zakrafaon(event):
    if not gvarstatus("enzakrafa"):
        addgvar("enzakrafa", "on")
        await edit_delete(event, "**⪼ تـم تـفعـيل الزخـرفـة الإنـجليـزيـة تلقائـيّا**")
        return
    if gvarstatus("enzakrafa"):
        await edit_delete(event, "**⪼ الزخـرفـة الإنـجـليزيـة مفـعلـة سـابـقًا**")
        return


@zedub.zed_cmd(pattern="ايقاف الزخرفة الانجليزية")
async def zakrafaoff(event):
    if not gvarstatus("enzakrafa"):
        await edit_delete(event, "*⪼ عـذرًا عـزيـزي أنـت لـم تقـم بتفعيـل الزخـرفـة الإنجلـيزية تلقـائيًا**")
        return
    if gvarstatus("enzakrafa"):
        delgvar("enzakrafa")
        await edit_delete(event, "**⪼ تـم تـعطـيل الزخرفـة الإنـجليـزيـة تلقـائيًا**")
        return


@zedub.on(events.NewMessage(outgoing=True))
async def zakrafarun(event):
    if gvarstatus("enzakrafa"):
        text = event.message.message
        uppercase_text = (
            text.replace("a", "𝗮")
            .replace("b", "𝗯")
            .replace("c", "𝗰")
            .replace("d", "𝗱")
            .replace("e", "𝗲")
            .replace("f", "𝗳")
            .replace("g", "𝗴")
            .replace("h", "𝗵")
            .replace("i", "𝗶")
            .replace("j", "𝗷")
            .replace("k", "𝗸")
            .replace("l", "𝗹")
            .replace("m", "𝗺")
            .replace("n", "𝗻")
            .replace("o", "𝗼")
            .replace("p", "𝗽")
            .replace("q", "𝗾")
            .replace("r", "𝗿")
            .replace("s", "𝘀")
            .replace("t", "𝘁")
            .replace("u", "𝘂")
            .replace("v", "𝘃")
            .replace("w", "𝘄")
            .replace("x", "𝘅")
            .replace("y", "𝘆")
            .replace("z", "𝘇")
        )
        await event.edit(uppercase_text)
@zedub.zed_cmd(pattern="زخرفة 2")
async def zakrafaon(event):
    if not gvarstatus("enzakrafatwo"):
        addgvar("enzakrafatwo", "on")
        await edit_delete(event, "**⪼ تـم تـفعـيل الزخـرفـة الإنـجليـزيـة 2**")
        return
    if gvarstatus("enzakrafatwo"):
        await edit_delete(event, "**⪼ الزخـرفـة الإنـجـليزيـة 2 مفعلة مسبقًا .**")
        return


@zedub.zed_cmd(pattern="ايقاف الزخرفة 2")
async def zakrafaoff(event):
    if not gvarstatus("enzakrafatwo"):
        await edit_delete(event, "*⪼ عـذرًا عـزيـزي أنـت لـم تقـم بتفعيـل الزخـرفـة الإنجلـيزية 2*")
        return
    if gvarstatus("enzakrafatwo"):
        delgvar("enzakrafatwo")
        await edit_delete(event, "**⪼ تـم تـعطـيل الزخرفـة الإنـجليـزية 2**")
        return


@zedub.on(events.NewMessage(outgoing=True))
async def zakrafarun(event):
    if gvarstatus("enzakrafatwo"):
        text = event.message.message
        uppercase_text = (
            text.replace("a", "ꪖ")
            .replace("b", "Ⴆ")
            .replace("c", "ᥴ")
            .replace("d", "ᦔ")
            .replace("e", "꧖")
            .replace("f", "ƒ")
            .replace("g", "ᧁ")
            .replace("h", "ꫝ")
            .replace("i", "Ꭵ")
            .replace("j", "᧒")
            .replace("k", "ƙ")
            .replace("l", "ᥣ")
            .replace("m", "᧗")
            .replace("n", "ᥒ")
            .replace("o", "᥆")
            .replace("p", "ρ")
            .replace("q", "ᑫ")
            .replace("r", "ᖇ")
            .replace("s", "᥉")
            .replace("t", "ﾋ")
            .replace("u", "ꪊ")
            .replace("v", "ꪜ ")
            .replace("w", "ꪝ")
            .replace("x", "ꪎ")
            .replace("y", "ꪗ")
            .replace("z", "ᤁ")
            .replace("H", "ꫝ")
        )
        await event.edit(uppercase_text)
        #مأخوذ_من_سورس_جمثون
