from Tepthon import zedub
from Tepthon.core.managers import edit_delete, edit_or_reply
from Tepthon.helpers.utils import mentionuser
from telethon import functions
from telethon.errors import ChatAdminRequiredError, UserAlreadyInvitedError
from telethon.tl.types import Channel, Chat, User

@zedub.zed_cmd(
    pattern="انضمام ?(\S+)? ?(?:-as)? ?(\S+)?",
    command=("انضمام", plugin_category),
    info={
        "header": "To join a Voice Chat.",
        "description": "To join or create and join a Voice Chat",
        "note": "You can use -as flag to join anonymously",
        "flags": {
            "-as": "To join as another chat.",
        },
        "usage": [
            "{tr}joinvc",
            "{tr}joinvc (chat_id)",
            "{tr}joinvc -as (peer_id)",
            "{tr}joinvc (chat_id) -as (peer_id)",
        ],
        "examples": [
            "{tr}joinvc",
            "{tr}joinvc -1005895485",
            "{tr}joinvc -as -1005895485",
            "{tr}joinvc -1005895485 -as -1005895485",
        ],
    },
)
async def joinVoicechat(event):
    "To join a Voice Chat."
    chat = event.pattern_match.group(1)
    joinas = event.pattern_match.group(2)

    await edit_or_reply(event, "**جار الانضمام للمكالمة الصوتية**")

    if chat and chat != "-as":
        if chat.strip("-").isnumeric():
            chat = int(chat)
    else:
        chat = event.chat_id

    if vc_player.app.active_calls:
        return await edit_delete(
            event, f"لقد انضممت بالفعل الى {vc_player.CHAT_NAME}"
        )

    try:
        vc_chat = await zedub.get_entity(chat)
    except Exception as e:
        return await edit_delete(event, f'ERROR : \n{e or "UNKNOWN CHAT"}')

    if isinstance(vc_chat, User):
        return await edit_delete(
            event, "لايمكنك استعمال اوامر القرآن على الخاص فقط في المجموعات !"
        )

    if joinas and not vc_chat.username:
        await edit_or_reply(
            event, "**لايمكنك استعمال اوامر القرآن على الخاص فقط في المجموعات !**"
        )
        joinas = False

    out = await vc_player.join_vc(vc_chat, joinas)
    await edit_delete(event, out)


@zedub.zed_cmd(
    pattern="غادر",
    command=("غادر", plugin_category),
    info={
        "header": "To leave a Voice Chat.",
        "description": "To leave a Voice Chat",
        "usage": [
            "{tr}leavevc",
        ],
        "examples": [
            "{tr}leavevc",
        ],
    },
)
async def leaveVoicechat(event):
    "To leave a Voice Chat."
    if vc_player.CHAT_ID:
        await edit_or_reply(event, "** تم مغادرة من الاتصال 🥢 **")
        chat_name = vc_player.CHAT_NAME
        await vc_player.leave_vc()
        await edit_delete(event, f"تمت المغادرة من {chat_name}")
    else:
        await edit_delete(event, "** انا لست منضم الى الاتصال 🥢**")


@zedub.zed_cmd(
    pattern="قائمة_التشغيل",
    command=("قائمة_التشغيل", plugin_category),
    info={
        "header": "To Get all playlist.",
        "description": "To Get all playlist for Voice Chat.",
        "usage": [
            "{tr}playlist",
        ],
        "examples": [
            "{tr}playlist",
        ],
    },
)
async def get_playlist(event):
    "To Get all playlist for Voice Chat."
    await edit_or_reply(event, "**جارِ جلب قائمة التشغيل**")
    playl = vc_player.PLAYLIST
    if not playl:
        await edit_delete(event, "Playlist empty", time=10)
    else:
        matrix = ""
        for num, item in enumerate(playl, 1):
            if item["stream"] == Stream.audio:
                matrix += f"{num}. 🔉  `{item['title']}`\n"
            else:
                matrix += f"{num}. 📺  `{item['title']}`\n"
        await edit_delete(event, f"**قائمة التشغيل:**\n\n{matrix}\n**-**")

def convert_youtube_link_to_name(link):
    with youtube_dl.YoutubeDL({}) as ydl:
        info = ydl.extract_info(link, download=False)
        title = info['title']
    return title

@zedub.zed_cmd(
    pattern="تشغيل ?(-f)? ?([\S ]*)?",
    command=("تشغيل", plugin_category),
    info={
        "header": "لتشغيل الوسائط كصوت على القرآن.",
        "description": "لتشغيل دفق صوتي على القرآن.",
        "flags": {
            "-f": "Force play the Audio",
        },
        "usage": [
            "{tr}play (reply to message)",
            "{tr}play (yt link)",
            "{tr}play -f (yt link)",
        ],
        "examples": [
            "{tr}play",
            "{tr}play https://www.youtube.com/watch?v=c05GBLT_Ds0",
            "{tr}play -f https://www.youtube.com/watch?v=c05GBLT_Ds0",
        ],
    },
)
async def play_audio(event):
    " لتشغيل الوسائط كصوت"
    flag = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    if input_str == "" and event.reply_to_msg_id:
        input_str = await tg_dl(event)
    if not input_str:
        return await edit_delete(
            event, "**قم بالرد على ملف صوتي او رابط يوتيوب**", time=20
        )
    if not vc_player.CHAT_ID:
        return await edit_or_reply(event, "**`قم بلانضمام للمكالمة اولاً بأستخدام أمر `انضمام")
    if not input_str:
        return await edit_or_reply(event, "No Input to play in quran")
    await edit_or_reply(event, "**يتم الان تشغيل القرآن في الاتصال**")
    if flag:
        resp = await vc_player.play_song(input_str, Stream.audio, force=True)
    else:
        resp = await vc_player.play_song(input_str, Stream.audio, force=False)
    if resp:
        await edit_delete(event, resp, time=30)
        
@zedub.zed_cmd(
    pattern="ايقاف_مؤقت",
    command=("ايقاف_مؤقت", plugin_category),
    info={
        "header": "لإيقاف البث مؤقتًا في الدردشة الصوتية.",
        "description": "لإيقاف البث مؤقتًا في الدردشة الصوتية",
        "usage": [
            "{tr}pause",
        ],
        "examples": [
            "{tr}pause",
        ],
    },
)
async def pause_stream(event):
    "To Pause a stream on Voice Chat."
    await edit_or_reply(event, "**تم ايقاف القرآن مؤقتاً ⏸**")
    res = await vc_player.pause()
    await edit_delete(event, res, time=30)


@zedub.zed_cmd(
    pattern="استمرار",
    command=("استمرار", plugin_category),
    info={
        "header": "لإيقاف البث مؤقتًا في الدردشة الصوتية.",
        "description": "لإيقاف البث مؤقتًا في الدردشة الصوتية",
        "usage": [
            "{tr}resume",
        ],
        "examples": [
            "{tr}resume",
        ],
    },
)
async def resume_stream(event):
    "To Resume a stream on Voice Chat."
    await edit_or_reply(event, "**تم استمرار القرآن الكريم ▶️**")
    res = await vc_player.resume()
    await edit_delete(event, res, time=30)


@zedub.zed_cmd(
    pattern="تخطي",
    command=("تخطي", plugin_category),
    info={
        "header": "لتخطي البث الجاري تشغيله حاليًا على الدردشة الصوتية.",
        "description": "لتخطي البث الجاري تشغيله حاليًا على الدردشة الصوتية.",
        "usage": [
            "{tr}skip",
        ],
        "examples": [
            "{tr}skip",
        ],
    },
)
async def skip_stream(event):
    "لتخطي البث الجاري تشغيله حاليًا على الدردشة الصوتية."
    await edit_or_reply(event, "**تم تخطي القرآن وتشغيل القرآن التالي**")
    res = await vc_player.skip()
    await edit_delete(event, res, time=30)


async def get_group_call(chat):
    if isinstance(chat, Channel):
        result = await zedub(functions.channels.GetFullChannelRequest(channel=chat))
    elif isinstance(chat, Chat):
        result = await zedub(functions.messages.GetFullChatRequest(chat_id=chat.id))
    return result.full_chat.call


async def chat_vc_checker(event, chat, edits=True):
    if isinstance(chat, User):
        await edit_delete(event, "**لايمكنك تشغيل القرآن في المكالمات الخاصه**")
        return None
    result = await get_group_call(chat)
    if not result:
        if edits:
            await edit_delete(event, "** لا توجد مكالمة صوتية في هذه الدردشه**")
        return None
    return result


async def parse_entity(entity):
    if entity.isnumeric():
        entity = int(entity)
    return await zedub.get_entity(entity)


@zedub.zed_cmd(pattern="تشغيل_المكالمة")
async def start_vc(event):
    vc_chat = await zedub.get_entity(event.chat_id)
    gc_call = await chat_vc_checker(event, vc_chat, False)
    if gc_call:
        return await edit_delete(
            event, "**- المكالمة الصوتية بالفعل مشغلة بهذه الدردشة**"
        )
    try:
        await zedub(
            functions.phone.CreateGroupCallRequest(
                peer=vc_chat,
                title="𝗧𝗘𝗣𝗧𝗛𝗢𝗡 𝗤𝗨𝗥𝗔𝗡",
            )
        )
        await edit_delete(event, "**- تم بنجاح تشغيل المكالمة الصوتية**")
    except ChatAdminRequiredError:
        await edit_delete(event, "**- يجب ان تكون ادمن لتشغيل المكالمة هنا**", time=20)


@zedub.zed_cmd(pattern="انهاء_المكالمة")
async def end_vc(event):
    vc_chat = await zedub.get_entity(event.chat_id)
    gc_call = await chat_vc_checker(event, vc_chat)
    if not gc_call:
        return
    try:
        await zedub(functions.phone.DiscardGroupCallRequest(call=gc_call))
        await edit_delete(event, "**- تم بنجاح انهاء المكالمة الصوتية**")
    except ChatAdminRequiredError:
        await edit_delete(
            event, "**- يجب ان تكون مشرف لأنهاء المكالمة الصوتية**", time=20
        )


@zedub.zed_cmd(pattern="دعوة ?(.*)?")
async def inv_vc(event):
    users = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    vc_chat = await zedub.get_entity(event.chat_id)
    gc_call = await chat_vc_checker(event, vc_chat)
    if not gc_call:
        return
    if not users:
        if not reply:
            return await edit_delete(
                "**- يجب عليك الرد على المستخدم او وضع معرفه مع الامر**"
            )
        users = reply.from_id
    await edit_or_reply(event, "**- تم بنجاح دعوة المستخدم**")
    entities = str(users).split(" ")
    user_list = []
    for entity in entities:
        cc = await parse_entity(entity)
        if isinstance(cc, User):
            user_list.append(cc)
    try:
        await zedub(
            functions.phone.InviteToGroupCallRequest(call=gc_call, users=user_list)
        )
        await edit_delete(event, "**- تم بنجاح دعوة المستخدمين**")
    except UserAlreadyInvitedError:
        return await edit_delete(event, "- تم دعوة المستخدم بالاصل", time=20)


@zedub.zed_cmd(pattern="معلومات_المكالمة")
async def info_vc(event):
    vc_chat = await zedub.get_entity(event.chat_id)
    gc_call = await chat_vc_checker(event, vc_chat)
    if not gc_call:
        return
    await edit_or_reply(event, "**- جار جلب معلومات المكالمة انتظر قليلا**")
    call_details = await zedub(
        functions.phone.GetGroupCallRequest(call=gc_call, limit=1)
    )
    grp_call = "**معلومات مكالمة المجموعة**\n\n"
    grp_call += f"**العنوان :** {call_details.call.title}\n"
    grp_call += f"**عدد المشاركين :** {call_details.call.participants_count}\n\n"

    if call_details.call.participants_count > 0:
        grp_call += "**المشاركون**\n"
        for user in call_details.users:
            nam = f"{user.first_name or ''} {user.last_name or ''}"
            grp_call += f"  ● {mentionuser(nam,user.id)} - `{user.id}`\n"
    await edit_or_reply(event, grp_call)


@zedub.zed_cmd(pattern="تسمية_المكالمة?(.*)?")
async def title_vc(event):
    title = event.pattern_match.group(1)
    vc_chat = await zedub.get_entity(event.chat_id)
    gc_call = await chat_vc_checker(event, vc_chat)
    if not gc_call:
        return
    if not title:
        return await edit_delete("**- يجب عليك كتابة العنوان مع الامر**")
    await zedub(functions.phone.EditGroupCallTitleRequest(call=gc_call, title=title))
    await edit_delete(event, f"- تم بنجاح تغيير اسم المكالمة الى **{title}**")
