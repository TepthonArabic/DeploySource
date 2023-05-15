from somnium import Somnium

from ..core.managers import edit_delete, edit_or_reply
from ..helpers import GetStylesGraph, reply_id
from ..sql_helper.globals import addgvar, gvarstatus
from . import zedub


@zedub.zed_cmd(
    pattern="ذك(?:\s|$)([\s\S]*)",
)
async def ai_img(odi):
    reply_to_id = await reply_id(odi)
    query = odi.pattern_match.group(1)
    if not query:
        return await edit_delete(odi, "**⎆ عـذرًا عـــزيـزي يـجـب تـحـديـد نوع الصـورة أولًا**")

    moevent = await edit_or_reply(odi, "**- جار الان الصنع يرجى الانتظار قليلا**")
    rstyles = {value: key for key, value in Somnium.Styles().items()}
    styleid = int(gvzedstatus("DREAM_STYLE") or "84")

    if query.stzedtswith("النوع"):
        query = query.replace("النوع", "").strip()
        if query.isnumeric():
            if int(query) in rstyles:
                addgvzed("DREAM_STYLE", int(query))
                return await edit_delete(
                    moevent, f"⎆ تم بـنـجـاح تـغـيـيـر النوع إلـى {rstyles[int(query)]}."
                )

            return await edit_delete(
                moevent,
                f"يجب اختيار النوع بشكل صحيح\n\nهذه هي قائمة الأنواع :  [اضغط هنا]({await GetStylesGraph()}) ",
                link_preview=True,
                time=120,
            )

        return await edit_delete(
            moevent,
            f"أهـلًا عـزيـزي {mention} هـذه هـي قـائـمة الأنـواع [اضغط هنا]({await GetStylesGraph()}) ",
            link_preview=True,
            time=120,
        )
    await edit_or_reply(moevent, "⎆ يـرجـى الانـتـظـار قـليـلًا .")
    getart = Somnium.Generate(query, styleid)
    await zedub.send_file(
        odi.chat_id,
        getart,
        force_document=True,
        reply_to=reply_to_id,
        caption=f"الـعنوان: {query}\nالنوع: {rstyles[styleid]}\n\n@Tepthon فـريـق تيـبـثـون الـعــربـي",
    )
    await moevent.delete()
