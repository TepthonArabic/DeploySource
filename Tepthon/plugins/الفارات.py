# Tepthon
# Copyright (C) 2022 TepthonArabic . All Rights Reserved
#
# This file is a part of < https://github.com/Tepthon-Arabic/TepthonAr/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Tepthon-Arabic/TepthonAr/blob/web/LICENSE/>.

""" وصـف الملـف : اوامـر إضـافة الفـارات باللغـة العربيـة كـاملة ولا حـرف انكلـش🤘 تخمـط اذكـر المصـدر يولـد
إضـافة فـارات صـورة ( الحمايـة - الفحـص - الوقتـي ) بـ امـر واحـد فقـط
حقـوق للتـاريخ : @Tepthon
@E_7_V - كتـابـة الملـف :  بـاقـر"""
#بـاقـر يولـد هههههههههههههههههههههههههه
import asyncio
import math
import os

import heroku3
import requests
import urllib3
import random
import string
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError
from telethon.utils import get_display_name
from urlextract import URLExtract

from . import zedub

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import delete_conv
from ..sql_helper.globals import addgvar, delgvar, gvarstatus

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY
from . import BOTLOG_CHATID, mention


plugin_category = "الادوات"
LOGS = logging.getLogger(__name__)

extractor = URLExtract()


BaqirVP_cmd = (
    "𓆩 [ 𝗧𝗲𝗽𝘁𝗵𝗼𝗻 𝗖𝗼𝗻𝗳𝗶𝗴 𝗩𝗮𝗿𝘀 - اوامـر الفـارات](t.me/Tepthon) 𓆪\n\n"
    "**⎉╎قائـمه اوامر تغييـر فـارات الصـور بأمـر واحـد فقـط - لـ اول مـره ع سـورس تليثـون يوزر بـوت 🦾 :** \n\n"
    "⪼ `.اضف صورة الحماية` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة الفحص` بالـرد ع صـورة او ميديـا\n"
    "⪼ قنـاة كلايـش الفحـص @Tepthon_kalaesh\n\n"
    "⪼ `.اضف صورة الوقتي` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة البوت` بالـرد ع صـورة او ميديـا لـ إضـافة صـورة ستـارت للبـوت\n\n"
    "⪼ `.اضف صورة الحظر` بالـرد ع صـورة او ميديـا لـ إضـافة صـورة لـ كليشـة الحظـر\n\n"
    "⪼ `.اضف صورة الكتم` بالـرد ع صـورة او ميديـا لـ إضـافة صـورة لـ كليشـة الكتـم\n\n"
    "⪼ `.اضف صورة البلوك` بالـرد ع صـورة او ميديـا لـ إضـافة صـورة لـ كليشـة حظـر الخـاص\n\n"
    "⪼ `.اوامر الفارات` لعـرض بقيـة اوامـر الفـارات\n\n\n"
    "**⎉╎قائـمه اوامر تغييـر كليشـة الايـدي :** \n\n"
    "⪼ `.اضف فار ايموجي الايدي` بالـرد ع الرمـز او الايموجـي\n\n"
    "⪼ `.اضف فار عنوان الايدي` بالـرد ع نـص العنـوان\n\n"
    "⪼ `.اضف فار خط الايدي` بالـرد ع الخـط او المستقيـم\n\n"
    "⪼ `.اضف كليشة الايدي` بالـرد ع الكليشـه مـن القنـاة @Tepthon_kalaesh\n\n\n"
    "**⎉╎قائـمه اوامر تغييـر بقيـة الفـارات بأمـر واحـد فقـط :** \n\n"
    "⪼ `.اضف فار كليشة الحماية` بالـرد ع الكليشـة\n"
    "⪼ `.اضف فار كليشة البلوك` بالـرد ع الكليشـة لتغييـر كليشة الحظر خاص\n"
    "⪼ قنـاة كلايـش حمايـة الخـاص @Tepthon_kalaesh\n\n"
    "⪼ `.اضف فار كليشة الفحص` بالـرد ع الكليشـة\n"
    "⪼ قنـاة كلايـش الفحـص @Tepthon_kalaesh\n\n"
    "⪼ `.اضف فار كليشة البوت` بالـرد ع الكليشـة لـ إضـافة كليشـة ستـارت\n\n"
    "⪼ `.اضف فار زر الستارت` بالـرد ع يوزرك او يوزر قناتك لـ إضـافة زر الستـارت\n\n"
    "⪼ `.اضف فار رمز الوقتي` بالـرد ع رمـز\n\n"
    "⪼ `.اضف فار زخرفة الوقتي` بالـرد ع ارقـام الزغـرفه\n\n"
    "⪼ `.اضف فار البايو الوقتي` بالـرد ع البـايـو\n\n"
    "⪼ `.اضف فار اسم المستخدم` بالـرد ع اسـم\n\n"
    "⪼ `.اضف فار كروب الرسائل` بالـرد ع ايدي الكـروب\n\n"
    "⪼ `.اضف فار كروب السجل` بالـرد ع ايدي الكـروب\n\n"
    "⪼ `.اضف فار ايديي` بالـرد ع ايدي حسـابك\n\n"
    "⪼ `.اضف فار نقطة الاوامر` بالـرد ع الـرمز الجديـد\n\n"
    "⪼ `.اضف فار نوم الترحيب` بالـرد ع رقـم الساعة لبداية نوم الترحيب المؤقت\n\n"
    "⪼ `.اضف فار ثواني لانهائي` بالـرد ع رقـم لعـدد الثوانـي الفاصـله بيـن كل عمليـة تجميـع فـي الامـر لانهائـي\n\n"
    "⪼ `.اضف فار رسائل الحماية` بالـرد ع رقـم لعدد رسائل تحذيـرات حماية الخاص\n\n\n"
    "⪼ `.جلب فار` + اسـم الفـار\n\n"
    "⪼ `.حذف فار` + اسـم الفـار\n\n"
    "⪼ `.رفع مطور` بالـرد ع الشخـص لرفعـه مطـور تحكـم كامـل بالاوامـر\n\n"
    "⪼ `.حذف فار المطورين`\n\n"
    "⪼ `.الوقت` لـ عـرض قائمـة اوامـر تغييـر الوقت حسب دولتك\n\n"
    "\n𓆩 [𝗧𝗲𝗽𝘁𝗵𝗼𝗻 𝗩𝗮𝗿𝘀 - قنـاة الفـارات](t.me/Tepthone1) 𓆪"
)


BaqirTZ_cmd = (
    "𓆩 [𝗧𝗲𝗽𝘁𝗵𝗼𝗻 𝗖𝗼𝗻𝗳𝗶𝗴 - اوامـر الوقت](t.me/Tepthon) 𓆪\n\n"
    "**⎉╎قائـمه اوامر تغييـر المنطقـة الزمنيـة للوقـت 🌐:** \n\n"
    "⪼ `.وقت اليمن` \n\n"
    "⪼ `.وقت العراق` \n\n"
    "⪼ `.وقت السعودية` \n\n"
    "⪼ `.وقت سوريا` \n\n"
    "⪼ `.وقت مصر` \n\n"
    "⪼ `.وقت السودان` \n\n"
    "⪼ `.وقت ليبيا` \n\n"
    "⪼ `.وقت الامارات` \n\n"
    "⪼ `.وقت ايران` \n\n"
    "⪼ `.وقت الجزائر` \n\n"
    "⪼ `.وقت المغرب` \n\n"
    "⪼ `.وقت تركيا` \n\n"
    "⪼ `.وقت ماليزيا` \n\n"
    "⪼ `.وقت روسيا` \n\n"
    "⪼ `.وقت ايطاليا` \n\n"
    "⪼ `.وقت امريكا` \n\n"
    "⪼ `.وقت المانيا` \n\n"
    "🛃 سيتـم إضـافة المزيـد من الدول قريبـًـا\n\n"
    "\n𓆩 [𝗧𝗲𝗽𝘁𝗵𝗼𝗻 𝗩𝗮𝗿𝘀 - قنـاة الفـارات](t.me/Tepthone1) 𓆪"
)


# Copyright (C) 2022 Tepthon . All Rights Reserved
@zedub.zed_cmd(pattern=r"اضف فار (.*)")
async def variable(event):
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    vinfo = reply.text
    rep = await edit_or_reply(event, "**⎉╎جـاري إضـافة الفـار إلـى بـوتك ...**")
    # All Rights Reserved for "Tepthon" "باقر"
    if input_str == "كليشة الفحص" or input_str == "كليشه الفحص":
        variable = "ALIVE_TEMPLATE"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_TEMPLATE") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.فحص` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.فحص` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("ALIVE_TEMPLATE", vinfo)
    elif input_str == "كليشة الحماية" or input_str == "كليشه الحمايه" or input_str == "كليشه الحماية" or input_str == "كليشة الحمايه":
        variable = "pmpermit_txt"
        await asyncio.sleep(1.5)
        if gvarstatus("pmpermit_txt") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.الحمايه تفعيل` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.الحمايه تفعيل` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("pmpermit_txt", vinfo)
    elif input_str == "كليشة الايدي" or input_str == "كليشه الايدي":
        variable = "RID_TEMPLATE"
        await asyncio.sleep(1.5)
        if gvarstatus("RID_TEMPLATE") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.ايدي` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.ايدي` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("RID_TEMPLATE", vinfo)
    elif input_str == "كليشة البوت" or input_str == "كليشه البوت" or input_str == "ستارت البوت" or input_str == "كليشة الستارت" or input_str == "كليشه الستارت" or input_str == "كليشة البدء":
        variable = "START_TEXT"
        await asyncio.sleep(1.5)
        if gvarstatus("START_TEXT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الآن قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("START_TEXT", vinfo)
    elif input_str == "زر البوت" or input_str == "زر الستارت" or input_str == "زر ستارت":
        variable = "START_BUTUN"
        await asyncio.sleep(1.5)
        if not vinfo.startswith("@"):
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع يـوزر فقـط**")
        vinfo = vinfo.zedlace("@", "")
        if gvarstatus("START_TEXT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎رابـط زر كليشـة الستـارت الجـديـد** \nhttps://t.me/{} \n\n**⎉╎الآن قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎رابـط زر كليشـة الستـارت الجـديـد** \nhttps://t.me/{} \n\n**⎉╎الآن قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("START_BUTUN", vinfo)
    elif input_str == "كليشة التوديع" or input_str == "كليشه التوديع" or input_str == "كليشة البلوك" or input_str == "كليشه البلوك":
        variable = "pmblock"
        await asyncio.sleep(1.5)
        if gvarstatus("pmblock") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ تفعيـل حماية الخاص عبر الأمر ↶** ( `الحماية تفعيل` ) **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ تفعيـل حماية الخاص عبر الأمر ↶** ( `الحماية تفعيل` ) **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("pmblock", vinfo)
    elif input_str == "رمز الوقتي" or input_str == "رمز الاسم الوقتي":
        variable = "CUSTOM_ALIVE_EMREP"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_EMREP") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الـرمـز الجـديـد** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.الاسم تلقائي` **لـ التحقـق مـن الـرمز . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎الـرمـز المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.الاسم تلقائي` **لـ التحقـق مـن الـرمز . .**".format(input_str, vinfo))
    elif input_str == "البايو" or input_str == "البايو الوقتي" or input_str == "النبذه" or input_str == "البايو تلقائي":
        variable = "DEFAULT_BIO"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_BIO") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎البـايـو الجـديـد** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.البايو تلقائي` **لـ التحقـق مـن البايـو . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضـافه {} بنجـاح ☑️**\n**⎉╎البـايـو المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.البايو تلقائي` **لـ التحقـق مـن البايـو . .**".format(input_str, vinfo))
    elif input_str == "التحقق" or input_str == "كود التحقق" or input_str == "التحقق بخطوتين" or input_str == "تحقق":
        variable = "TG_2STEP_VERIFICATION_CODE"
        await asyncio.sleep(1.5)
        if gvarstatus("TG_2STEP_VERIFICATION_CODE") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎كـود التحـقق بخطـوتيـن** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.تحويل ملكية` **ثم معـرف الشخـص داخـل الكـروب او القنـاة . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎كـود التحـقق بخطـوتيـن** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.تحويل ملكية` **ثم معـرف الشخـص داخـل الكـروب او القنـاة . .**".format(input_str, vinfo))
    elif input_str == "كاشف الاباحي" or input_str == "كشف الاباحي":
        variable = "DEEP_API"
        await asyncio.sleep(1.5)
        if gvarstatus("DEEP_API") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر توكـن {} بنجـاح ☑️**\n**⎉╎التوكـن الجـديـد** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.قفل الاباحي` **لـ تفعيـل كاشـف الاباحي . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة توكـن {} بنجـاح ☑️**\n**⎉╎التوكـن المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.قفل الاباحي` **لـ تفعيـل كاشـف الاباحي . .**".format(input_str, vinfo))
    elif input_str == "ايموجي الايدي" or input_str == "ايموجي ايدي" or input_str == "رمز الايدي" or input_str == "رمز ايدي" or input_str == "الرمز ايدي":
        variable = "CUSTOM_ALIVE_EMOJI"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_EMOJI") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        addgvar("CUSTOM_ALIVE_EMOJI", vinfo)
    elif input_str == "عنوان الايدي" or input_str == "عنوان ايدي":
        variable = "CUSTOM_ALIVE_TEXT"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_TEXT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        addgvar("CUSTOM_ALIVE_TEXT", vinfo)
    elif input_str == "خط الايدي" or input_str == "خط ايدي" or input_str == "خطوط الايدي" or input_str == "خط ايدي":
        variable = "CUSTOM_ALIVE_FONT"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_FONT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        addgvar("CUSTOM_ALIVE_FONT", vinfo)
    elif input_str == "اشتراك الخاص" or input_str == "اشتراك خاص":
        variable = "Custom_Pm_Channel"
        await asyncio.sleep(1.5)
        if gvarstatus("Custom_Pm_Channel") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.اشتراك خاص`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.اشتراك خاص`".format(input_str, vinfo))
        delgvar("Custom_Pm_Channel")
        addgvar("Custom_Pm_Channel", vinfo)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#قنـاة_الاشتـراك_الاجبـاري_للخـاص\
                        \n**- القنـاة {input_str} تم إضافتهـا في قاعده البيانات ..بنجـاح ✓**",
            )
    elif input_str == "اشتراك كروب" or input_str == "اشتراك الكروب":
        variable = "Custom_G_Channel"
        await asyncio.sleep(1.5)
        if gvarstatus("Custom_G_Channel") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.اشتراك كروب`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.اشتراك كروب`".format(input_str, vinfo))
        delgvar("Custom_G_Channel")
        addgvar("Custom_G_Channel", vinfo)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#قنـاة_الاشتـراك_الاجبـاري_للكـروب\
                        \n**- القنـاة {input_str} تم إضافتهـا في قاعده البيانات ..بنجـاح ✓**",
            )
    elif input_str == "زاجل" or input_str == "قائمة زاجل" or input_str == "قائمه زاجل" or input_str == "يوزرات":
        variable = "ZAGL_Rep"
        await asyncio.sleep(1.5)
        if gvarstatus("ZAGL_Rep") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎اليـوزرات المضـافة** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.زاجل` **بالـرد ع نـص او ميديـا بنـص . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎اليـوزرات المضـافة** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.زاجل` **بالـرد ع نـص او ميديـا بنـص . .**".format(input_str, vinfo))
    elif input_str == "سوبر" or input_str == "قائمة السوبر" or input_str == "قائمه السوبر" or input_str == "السوبرات" or input_str == "السوبر":
        variable = "Super_Id"
        await asyncio.sleep(1.5)
        if not vinfo.startswith("-100"):
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع ارقـام ايديات المجموعات التي تبدأ ب 100- فقـط ؟!**\n**⎉╎قم بالذهاب لمجموعات السوبر التي تريد النشر فيها وكتابة الأمر (.الايدي) ثم خذ ايدي المجموعة وهكذا لبقية المجموعات**")
        if gvarstatus("Super_Id") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎الايديات المضـافة** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** (`.سوبر` + عدد الثواني + عدد مرات التكرار)**بالـرد ع نـص او ميديـا بنـص . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الايديات المضـافة** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** (`.سوبر` + عدد الثواني + عدد مرات التكرار)**بالـرد ع نـص او ميديـا بنـص . .**".format(input_str, vinfo))
    elif input_str == "بوت التجميع" or input_str == "بوت النقاط" or input_str == "النجميع" or input_str == "النقاط":
        variable = "R_Point"
        await asyncio.sleep(1.5)
        if gvarstatus("R_Point") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎البـوت المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.تجميع` **لـ البـدء بتجميـع النقـاط من البـوت الجـديـد . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضـافه {} بنجـاح ☑️**\n**⎉╎البـوت المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.تجميع` **لـ البـدء بتجميـع النقـاط من البـوت الجـديـد . .**".format(input_str, vinfo))
    elif input_str == "اسم المستخدم" or input_str == "الاسم":
        variable = "ALIVE_NAME"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_NAME") is not None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        addgvar(variable, vinfo)

    elif input_str == "رسائل الحماية" or input_str == "رسائل الحمايه" or input_str == "رسائل الخاص" or input_str == "رسائل حماية الخاص" or input_str == "عدد التحذيرات":
        variable = "MAX_FLOOD_IN_PMS"
        await asyncio.sleep(1.5)
        if vinfo.isdigit():
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع رقـم فقـط ؟!**")
        addgvar("MAX_FLOOD_IN_PMS", vinfo)

    elif input_str == "كود تيرمكس" or input_str == "كود السيشن" or input_str == "كود سيشن":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "STRING_SESSION"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo

    elif input_str == "كروب الرسائل" or input_str == "كروب التخزين" or input_str == "كروب الخاص":
        variable = "PM_LOGGER_GROUP_ID"
        await asyncio.sleep(1.5)
        if gvarstatus("PM_LOGGER_GROUP_ID") is not None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        addgvar("PM_LOGGER_GROUP_ID", vinfo)
    elif input_str == "السجل" or input_str == "كروب السجل":
        variable = "PRIVATE_GROUP_BOT_API_ID"
        await asyncio.sleep(1.5)
        if gvarstatus("PRIVATE_GROUP_BOT_API_ID") is not None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        addgvar("PRIVATE_GROUP_BOT_API_ID", vinfo)
    elif input_str == "السجل 2" or input_str == "كروب السجل 2":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "PRIVATE_GROUP_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "قناة السجل" or input_str == "قناة السجلات":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "PRIVATE_CHANNEL_BOT_API_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "قناة الملفات" or input_str == "قناة الإضافات":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "PLUGIN_CHANNEL"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "ايديي" or input_str == "ايدي الحساب":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "OWNER_ID"
        await asyncio.sleep(1.5)
        if vinfo.isdigit():
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع رقـم فقـط ؟!**")
        heroku_var[variable] = vinfo
    elif input_str == "نقطة الاوامر" or input_str == "نقطه الاوامر":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "COMMAND_HAND_LER"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "التوكن" or input_str == "توكن البوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TG_BOT_TOKEN"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "معرف البوت" or input_str == "معرف بوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TG_BOT_USERNAME"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "الريبو" or input_str == "السورس":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه ريندر 🔄**")
        variable = "UPSTREAM_REPO"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "توكن المكافح" or input_str == "كود المكافح" or input_str == "مكافح التخريب" or input_str == "مكافح التفليش":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "SPAMWATCH_API"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "توكن الذكاء" or input_str == "مفتاح الذكاء" or input_str == "الذكاء":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "OPENAI_API_KEY"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "ايقاف الترحيب" or input_str == "نوم الترحيب":
        variable = "TIME_STOP"
        await asyncio.sleep(1.5)
        if vinfo.isdigit():
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع رقـم فقـط ؟!**")
        addgvar("TIME_STOP", vinfo)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#فتـرة_الايقـاف_المـؤقت_للترحيب\
                        \n**- تم إضافة الفتـرة من الساعة {vinfo} إلى الساعة 6 صباحـًـا .. بنجـاح ✓**",
            )
    elif input_str == "ثواني لانهائي" or input_str == "ثواني التجميع" or input_str == "عدد لانهائي":
        variable = "SEC_LAN"
        await asyncio.sleep(1.5)
        if vinfo.isdigit():
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎الثوانـي الجـديـدة** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.لانهائي` **+ اسم بوت التجميـع لـ البـدء بالتجميـع اللانهائـي . .**".format(input_str, vinfo))
        else:
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع رقـم فقـط ؟!**")
        addgvar(variable, vinfo)
    elif ("صورة" in input_str) or ("صوره" in input_str):
        return await zed.edit("**⎉╎لـ إضافة صور الكلايش ..**\n**⎉╎استخدم الأمر (اضف) مباشرة بدون كلمة فار**")
    else:
        if input_str:
            return await zed.edit("**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))
        return await edit_or_reply(event, "**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))


# Copyright (C) 2022 TepthonArabic . All Rights Reserved
@zedub.zed_cmd(pattern="حذف فار(?:\\s|$)([\\s\\S]*)")
async def variable(event):
    input_str = event.text[9:]
    if (input_str == "من" or input_str == "إلى" or input_str == "الترحيب") or "رسائلي" in input_str or "رسائله" in input_str:
        return
    rep = await edit_or_reply(event, "**⎉╎جـاري حـذف الفـار مـن بـوتك 🚮...**")
    # All Rights Reserved for "Tepthon" "باقر"
    if input_str == "كليشة الفحص" or input_str == "كليشه الفحص":
        variable = gvarstatus("ALIVE_TEMPLATE")
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_TEMPLATE") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("ALIVE_TEMPLATE")
        
    elif input_str == "كليشة الحماية" or input_str == "كليشه الحمايه" or input_str == "كليشه الحماية" or input_str == "كليشة الحمايه":
        variable = gvarstatus("pmpermit_txt")
        await asyncio.sleep(1.5)
        if gvarstatus("pmpermit_txt") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("pmpermit_txt")

    elif input_str == "كليشة البوت" or input_str == "كليشه البوت":
        variable = gvarstatus("START_TEXT")
        await asyncio.sleep(1.5)
        if gvarstatus("START_TEXT") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("START_TEXT")

    elif input_str == "زر البوت" or input_str == "زر الستارت" or input_str == "زر ستارت":
        variable = gvarstatus("START_BUTUN")
        await asyncio.sleep(1.5)
        if gvarstatus("START_BUTUN") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("START_BUTUN")

    elif input_str == "كليشة التوديع" or input_str == "كليشه التوديع" or input_str == "كليشة البلوك" or input_str == "كليشه البلوك":
        variable = gvarstatus("pmblock")
        await asyncio.sleep(1.5)
        if gvarstatus("pmblock") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت زد ثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("pmblock")

    elif input_str == "كليشة الايدي" or input_str == "كليشه الايدي":
        variable = "RID_TEMPLATE"
        await asyncio.sleep(1.5)
        if gvarstatus("RID_TEMPLATE") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("RID_TEMPLATE")

    elif input_str == "صورة الفحص" or input_str == "صوره الفحص":
        variable = "ALIVE_PIC"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_PIC") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("ALIVE_PIC")

    elif input_str == "صورة الاوامر" or input_str == "صوره الاوامر":
        variable = "CMD_PIC"
        await asyncio.sleep(1.5)
        if gvarstatus("CMD_PIC") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("CMD_PIC")

    elif input_str == "صورة السورس" or input_str == "صوره السورس":
        variable = "ALIVE_PIC"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_PIC") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("ALIVE_PIC")

    elif input_str == "صورة الكتم" or input_str == "صوره الكتم":
        variable = "PC_MUTE"
        await asyncio.sleep(1.5)
        if gvarstatus("PC_MUTE") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("PC_MUTE")

    elif input_str == "صورة الحظر" or input_str == "صوره الحظر":
        variable = "PC_BANE"
        await asyncio.sleep(1.5)
        if gvarstatus("PC_BANE") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("PC_BANE")

    elif input_str == "صورة البلوك" or input_str == "صوره البلوك":
        variable = "PC_BLOCK"
        await asyncio.sleep(1.5)
        if gvarstatus("PC_BLOCK") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("PC_BLOCK")

    elif input_str == "صورة البوت" or input_str == "صوره البوت" or input_str == "صورة الستارت" or input_str == "صوره الستارت" or input_str == "صورة ستارت" or input_str == "صوره ستارت":
        variable = "BOT_START_PIC"
        await asyncio.sleep(1.5)
        if gvarstatus("BOT_START_PIC") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("BOT_START_PIC")

    elif input_str == "صورة الحماية" or input_str == "صوره الحمايه" or input_str == "صورة الحمايه" or input_str == "صوره الحماية":
        variable = "pmpermit_pic"
        await asyncio.sleep(1.5)
        if gvarstatus("pmpermit_pic") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        delgvar("pmpermit_pic")
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))

    elif input_str == "صورة الوقتي" or input_str == "صوره الوقتي":
        variable = gvarstatus("DIGITAL_PIC")
        await asyncio.sleep(1.5)
        if gvarstatus("DIGITAL_PIC") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("DIGITAL_PIC")

    elif input_str == "رمز الوقتي" or input_str == "رمز الاسم الوقتي":
        variable = "CUSTOM_ALIVE_EMREP"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_EMREP") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        delgvar("CUSTOM_ALIVE_EMREP")
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
    elif input_str == "زخرفه الوقتي" or input_str == "زخرفة الوقتي":
        variable = "BA_FN"
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        delgvar(variable)
    elif input_str == "رسائل الحماية" or input_str == "رسائل الحمايه" or input_str == "رسائل الخاص" or input_str == "رسائل حماية الخاص" or input_str == "عدد التحذيرات":
        variable = "MAX_FLOOD_IN_PMS"
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        delgvar(variable)
    elif input_str == "البايو" or input_str == "البايو الوقتي" or input_str == "النبذه الوقتيه":
        variable = "DEFAULT_BIO"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_BIO") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        delgvar("DEFAULT_BIO")
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
    elif input_str == "اسم المستخدم" or input_str == "الاسم":
        variable = "ALIVE_NAME"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_NAME") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        delgvar(variable)
    elif input_str == "كروب الرسائل" or input_str == "كروب التخزين" or input_str == "كروب الخاص":
        variable = "PM_LOGGER_GROUP_ID"
        await asyncio.sleep(1.5)
        if gvarstatus("PM_LOGGER_GROUP_ID") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        delgvar(variable)

    elif input_str == "السجل" or input_str == "كروب السجل":
        variable = "PRIVATE_GROUP_BOT_API_ID"
        await asyncio.sleep(1.5)
        if gvarstatus("PRIVATE_GROUP_BOT_API_ID") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        delgvar(variable)

    elif input_str == "السجل 2" or input_str == "كروب السجل 2":
        variable = "PRIVATE_GROUP_ID"
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "قناة السجل" or input_str == "قناة السجلات":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "PRIVATE_CHANNEL_BOT_API_ID"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "قناة الملفات" or input_str == "قناة الإضافات":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "PLUGIN_CHANNEL"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "التحقق" or input_str == "كود التحقق":
        variable = "TG_2STEP_VERIFICATION_CODE"
        await asyncio.sleep(1.5)
        if gvarstatus("TG_2STEP_VERIFICATION_CODE") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        delgvar("TG_2STEP_VERIFICATION_CODE")
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))

    elif input_str == "ايديي" or input_str == "ايدي الحساب":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "OWNER_ID"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "نقطة الاوامر" or input_str == "نقطه الاوامر":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه ريندر 🔄**")
        variable = "COMMAND_HAND_LER"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "التوكن" or input_str == "توكن البوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TG_BOT_TOKEN"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "معرف البوت" or input_str == "معرف بوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TG_BOT_USERNAME"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "الريبو" or input_str == "السورس":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "UPSTREAM_REPO"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "اسمي التلقائي" or input_str == "الاسم التلقاائي":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "AUTONAME"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]
    elif input_str == "ايموجي الايدي" or input_str == "ايموجي ايدي" or input_str == "رمز الايدي" or input_str == "رمز ايدي" or input_str == "الرمز ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_EMOJI")
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("CUSTOM_ALIVE_EMOJI")
    elif input_str == "عنوان الايدي" or input_str == "عنوان ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_TEXT")
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("CUSTOM_ALIVE_TEXT")
    elif input_str == "خط الايدي" or input_str == "خط ايدي" or input_str == "خطوط الايدي" or input_str == "خط ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_FONT")
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("CUSTOM_ALIVE_FONT")
    elif input_str == "كاشف الاباحي" or input_str == "كشف الاباحي":
        variable = gvarstatus("DEEP_API")
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("DEEP_API")
    elif input_str == "ايقاف الترحيب" or input_str == "نوم الترحيب":
        variable = "TIME_STOP"
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("TIME_STOP")
    elif input_str == "ثواني لانهائي" or input_str == "ثواني التجميع" or input_str == "عدد لانهائي":
        variable = "SEC_LAN"
        await asyncio.sleep(1.5)
        if gvarstatus("SEC_LAN") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("SEC_LAN")
    else:
        if input_str:
            return await zed.edit("**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))
        return await edit_or_reply(event, "**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))


# Copyright (C) 2022 TepthonArabic . All Rights Reserved
@zedub.zed_cmd(pattern="جلب فار(?:\\s|$)([\\s\\S]*)")
async def custom_rep(event):
    input_str = event.text[9:]
    rep = await edit_or_reply(event, "**⎉╎جــاري جلـب معلـومـات الفــار 🛂. . .**")
    if (input_str == "كليشة الحماية" or input_str == "كليشة الحمايه" or input_str == "كليشه الحماية" or input_str == "كليشه الحمايه"):
        variable = gvarstatus("pmpermit_txt")
        if variable is None:
            await zed.edit("**⎉╎فـار كليشـة الحمايـة غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكليشـة استخـدم الامـر : ↶**\n `.اضف فار كليشة الحماية` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))
            
    elif input_str == "كليشة الفحص" or input_str == "كليشه الفحص":
        variable = gvarstatus("ALIVE_TEMPLATE")
        if variable is None:
            await zed.edit("**⎉╎فـار كليشـة الفحص غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكليشـة استخـدم الامـر : ↶**\n `.اضف فار كليشة الفحص` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "كليشة البوت" or input_str == "كليشه البوت":
        variable = gvarstatus("START_TEXT")
        if variable is None:
            await zed.edit("**⎉╎فـار كليشـة البـوت غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكليشـة استخـدم الامـر : ↶**\n `.اضف فار كليشة البوت` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "زر البوت" or input_str == "زر الستارت" or input_str == "زر ستارت":
        variable = gvarstatus("START_BUTUN")
        if variable is None:
            await zed.edit("**⎉╎فـار زر كليشـة ستـارت البـوت غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع يـوزرك او يـوزر قناتـك استخـدم الامـر : ↶**\n `.اضف فار زر الستارت` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n https://t.me/{}\n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "كليشة التوديع" or input_str == "كليشه التوديع" or input_str == "كليشة البلوك" or input_str == "كليشه البلوك":
        variable = gvarstatus("pmblock")
        if variable is None:
            await zed.edit("**⎉╎فـار كليشـة الحظـر غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكليشـة استخـدم الامـر : ↶**\n `.اضف فار كليشة الحظر` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "رمز الوقتي" or input_str == "رمز الاسم الوقتي":
        variable = gvarstatus("CUSTOM_ALIVE_EMREP")
        if variable is None:
            await zed.edit("**⎉╎فـار رمـز الوقتـي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز استخـدم الامـر : ↶**\n `.اضف فار رمز الوقتي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "التحقق" or input_str == "كود التحقق":
        variable = gvarstatus("TG_2STEP_VERIFICATION_CODE")
        if variable is None:
            await zed.edit("**⎉╎فـار التحقق بخطوتين غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز استخـدم الامـر : ↶**\n `.اضف فار التحقق`  **بالـرد ع كـود التحـقق**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "كاشف الاباحي" or input_str == "كشف الاباحي":
        variable = gvarstatus("DEEP_API")
        if variable is None:
            await zed.edit("**⎉╎فـار كشـف الاباحي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكـود استخـدم الامـر : ↶**\n `.اضف فار كاشف الاباحي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "البايو" or input_str == "البايو الوقتي" or input_str == "النبذه" or input_str == "البايو تلقائي":
        variable = gvarstatus("DEFAULT_BIO")
        if variable is None:
            await zed.edit("**⎉╎فـار البايـو الوقتـي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع نـص استخـدم الامـر : ↶**\n `.اضف فار البايو` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "اسم المستخدم" or input_str == "الاسم":
        variable = gvarstatus("ALIVE_NAME")
        if gvarstatus("ALIVE_NAME") is None:
            await zed.edit("**⎉╎فـار اسـم المستخـدم غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الاسم استخـدم الامـر : ↶**\n `.اضف فار اسم المستخدم` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "كود تيرمكس" or input_str == "كود السيشن" or input_str == "كود سيشن":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "STRING_SESSION"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار اسـم المستخـدم غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الاسم استخـدم الامـر : ↶**\n `.اضف فار اسم المستخدم` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "ايديي" or input_str == "ايدي الحساب":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "OWNER_ID"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار ايـدي الحسـاب غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الايـدي فقـط استخـدم الامـر : ↶**\n `.اضف فار ايدي الحساب` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "نقطة الاوامر" or input_str == "نقطه الاوامر":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "COMMAND_HAND_LER"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار نقطـة الاوامـر غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز فقـط استخـدم الامـر : ↶**\n `.اضف فار نقطة الاوامر` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "التوكن" or input_str == "توكن البوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TG_BOT_TOKEN"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار توكـن البـوت غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع التوكـن فقـط استخـدم الامـر : ↶**\n `.اضف فار التوكن` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "معرف البوت" or input_str == "معرف بوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "APP_USERNAME"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار معرف البوت غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع المعرف استخـدم الامـر : ↶**\n `.اضف فار معرف البوت` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "الريبو" or input_str == "السورس":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "UPSTREAM_REPO"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار الريبـو غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع رابط السورس الرسمي استخـدم الامـر : ↶**\n `.اضف فار الريبو` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "اسمي التلقائي" or input_str == "الاسم التلقاائي":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "AUTONAME"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار الاسـم التلقائي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الاسم استخـدم الامـر : ↶**\n `.اضف فار اسمي التلقائي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الحماية" or input_str == "صوره الحمايه" or input_str == "صورة الحمايه" or input_str == "صوره الحماية":
        variable = gvarstatus("pmpermit_pic")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الحمايـة غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الحماية` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الوقتي" or input_str == "صوره الوقتي":
        variable = gvarstatus("DIGITAL_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الوقتـي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الوقتي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الفحص" or input_str == "صوره الفحص":
        variable = gvarstatus("ALIVE_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الفحص غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الفحص` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة البوت" or input_str == "صوره البوت" or input_str == "صورة الستارت" or input_str == "صوره الستارت" or input_str == "صورة ستارت" or input_str == "صوره ستارت":
        variable = gvarstatus("BOT_START_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة ستـارت البـوت غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة البوت` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الاوامر" or input_str == "صوره الاوامر":
        variable = gvarstatus("CMD_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الاوامـر غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الاوامر` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة السورس" or input_str == "صوره السورس":
        variable = gvarstatus("ALIVE_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة السـورس غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة السورس` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الكتم" or input_str == "صوره الكتم":
        variable = gvarstatus("PC_MUTE")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الكتم غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الكتم` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الحظر" or input_str == "صوره الحظر":
        variable = gvarstatus("PC_BANE")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الحظر غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الحظر` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة البلوك" or input_str == "صوره البلوك":
        variable = gvarstatus("PC_BLOCK")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة البلوك غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة البلوك` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "زخرفة الوقتي" or input_str == "زخرفه الوقتي":
        variable = gvarstatus("NA_FN")
        if variable is None:
            await zed.edit("**⎉╎فـار زخرفـة الاسـم الوقتي غيـر موجـود ❌**\n**⎉╎لـ إضـافته فقـط استخـدم الامـر : ↶**\n `.الوقتي 1` إلـى `.الوقتي 14` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "رسائل الحماية" or input_str == "رسائل الحمايه" or input_str == "رسائل الخاص" or input_str == "رسائل حماية الخاص" or input_str == "عدد التحذيرات":
        variable = gvarstatus("MAX_FLOOD_IN_PMS")
        if variable is None:
            await zed.edit("**⎉╎فـار رسـائل الحمايـة غيـر موجـود ❌**\n**⎉╎لـ إضـافته فقـط استخـدم الامـر : ↶**\n `.اضف فار رسائل الحماية` بالـرد ع عـدد فقـط \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "زخرفة الوقتية" or input_str == "زخرفه الوقتيه" or input_str == "زخرفة الوقتيه" or input_str == "زخرفه الوقتية":
        variable = gvarstatus("DEFAULT_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار زخرفـة الصـورة الوقتيـة غيـر موجـود ❌**\n**⎉╎لـ إضـافته فقـط استخـدم الامـر : ↶**\n `.وقتي 1` إلـى `.وقتي 17` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "الوقت" or input_str == "الساعه" or input_str == "المنطقه الزمنيه":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TZ"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار المنطقـة الزمنيــــة غيـر موجـود ❌**\n**⎉╎لـ إضـافته فقـط استخـدم الامـر : ↶**\n `.وقت` واسـم الدولـة \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "كليشة الايدي" or input_str == "كليشه الايدي":
        variable = gvarstatus("RID_TEMPLATE")
        if variable is None:
            await zed.edit("**⎉╎فـار ايموجي/رمز الايدي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكليشـة من هنا ( @Tepthon_kalaesh ) استخـدم الامـر : ↶**\n `.اضف كليشة الايدي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "ايموجي الايدي" or input_str == "ايموجي ايدي" or input_str == "رمز الايدي" or input_str == "رمز ايدي" or input_str == "الرمز ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_EMOJI")
        if variable is None:
            await zed.edit("**⎉╎فـار ايموجي/رمز الايدي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز استخـدم الامـر : ↶**\n `.اضف فار رمز الايدي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))
            
    elif input_str == "عنوان الايدي" or input_str == "عنوان ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_TEXT")
        if variable is None:
            await zed.edit("**⎉╎فـار نص عنـوان كليشـة الايـدي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز استخـدم الامـر : ↶**\n `.اضف فار عنوان الايدي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "خط الايدي" or input_str == "خط ايدي" or input_str == "خطوط الايدي" or input_str == "خط ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_FONT")
        if variable is None:
            await zed.edit("**⎉╎فـار خطـوط كليشـة الايـدي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز استخـدم الامـر : ↶**\n `.اضف فار خطوط الايدي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "لاعب 1":
        variable = gvarstatus("R_AK")
        if gvarstatus("R_AK") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "لاعب 2":
        variable = gvarstatus("R_A2K")
        if gvarstatus("R_A2K") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "لاعب 3":
        variable = gvarstatus("R_A3K")
        if gvarstatus("R_A3K") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "لاعب 4":
        variable = gvarstatus("R_A4K")
        if gvarstatus("R_A4K") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "لاعب 5":
        variable = gvarstatus("R_A5K")
        if gvarstatus("R_A5K") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "توكن المكافح" or input_str == "كود المكافح" or input_str == "مكافح التخريب" or input_str == "مكافح التفليش":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "SPAMWATCH_API"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار توكـن المكـافح غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "اشتراك خاص" or input_str == "اشتراك الخاص" or input_str == "قناة الاشتراك" or input_str == "الاشتراك":
        variable = gvarstatus("Custom_Pm_Channel")
        if gvarstatus("Custom_Pm_Channel") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "اشتراك كروب" or input_str == "اشتراك الكروب" or input_str == "قناة الاشتراك" or input_str == "الاشتراك":
        variable = gvarstatus("Custom_G_Channel")
        if gvarstatus("Custom_G_Channel") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "االهمسه":
        variable = gvarstatus("hmsa_id")
        if gvarstatus("hmsa_id") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "ثواني لانهائي" or input_str == "ثواني التجميع" or input_str == "عدد لانهائي":
        variable = gvarstatus("SEC_LAN")
        if gvarstatus("SEC_LAN") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    else:
        if input_str:
            return await zed.edit("**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))
        return await edit_or_reply(event, "**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))


# Copyright (C) 2022 TepthonArabic . All Rights Reserved
@zedub.zed_cmd(pattern="وقت(?:\\s|$)([\\s\\S]*)")
async def variable(event):
    input_str = event.text[5:]
    viraq = "Asia/Baghdad"
    vmsr = "Africa/Cairo"
    vdubai = "Asia/Dubai"
    vturk = "Europe/Istanbul"
    valgiers = "Africa/Algiers"
    vmoroco = "Africa/Casablanca"
    viran = "Asia/Tehran"
    vsudan = "Africa/Khartoum"
    vitaly = "Europe/Rome"
    vrusia = "Europe/Moscow"
    vamerica = "America/Washington"
    vmalaysia = "Asia/Kuala_Lumpur"
    vdeutschland = "Europe/Berlin"
    rep = await edit_or_reply(event, "**⎉╎جـاري إعــداد المنطقـة الزمنيــــة لـ تيبثـون 🌐...**")
    # All Rights Reserved for "Tepthon" "باقر"
    if input_str == "العراق" or input_str == "اليمن" or input_str == "سوريا" or input_str == "السعودية" or input_str == "لبنان" or input_str == "الاردن":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", viraq)
    elif input_str == "مصر" or input_str == "ليبيا" or input_str == "القاهرة":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", vmsr)
    elif input_str == "دبي" or input_str == "الامارات" or input_str == "عمان" or input_str == "مسقط":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", vdubai)
    elif input_str == "تركيا" or input_str == "اسطنبول" or input_str == "انقرة":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", vturk)
    elif input_str == "تونس" or input_str == "الجزائر":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", valgiers)
    elif input_str == "المغرب" or input_str == "موريتانيا" or input_str == "الدار البيضاء":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", vmoroco)        
    elif input_str == "ايران" or input_str == "طهران":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", viran)
    elif input_str == "السودان":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "Africa/Khartoum")
    elif input_str == "ايطاليا":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "Europe/Rome")
    elif input_str == "روسيا":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "Europe/Moscow")
    elif input_str == "امريكا":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "America/Washington")
    elif input_str == "ماليزيا":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "Asia/Kuala_Lumpur")
    elif input_str == "المانيا":
        variable = "TZ"
        await asyncio.slepp(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "Europe/Berlin")

                
@zedub.zed_cmd(pattern="اضف صورة (الفحص|فحص) ?(.*)")
async def alive_Tepthon(event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        zedevent = await event.edit("**⎉╎ جـار رفع الـصورة إلى أمر الفحص**")
        try:
            baqir = await event.client.download_media(reply)
            if baqir.endswith((".webp")):
                resize_image(baqir)
            with open(baqir, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("ALIVE_PIC", url)
                await zedevent.edit(f"**⎉╎ تم إضافة الصورة إلى الفحص ✓ **")
            else:
                await zedevent.edit(f"**⎉╎ حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(baqir)
        except Exception as exc:
            await event.edit(f"**خـطأ : **\n`{exc}`")
            if os.path.exists(baqir):
                os.remove(baqir)
    else:
        await event.edit("**⎉╎ يُرجى الرد على الصورة لطفًا**")


@zedub.zed_cmd(pattern="اضف صورة (الحمايه|الحماية) ?(.*)")
async def Tepthon(event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        zedevent = await event.edit("**⎉╎ جـار رفع الـصورة إلى أمر الحماية**")
        try:
            baqir = await event.client.download_media(reply)
            if baqir.endswith((".webp")):
                resize_image(baqir)
            with open(baqir, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("pmpermit_pic", url)
                await zedevent.edit(f"**⎉╎ تم إضافة الصورة إلى الحماية ✓ **")
            else:
                await zedevent.edit(f"**⎉╎ حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(baqir)
        except Exception as exc:
            await event.edit(f"**خـطأ : **\n`{exc}`")
            if os.path.exists(baqir):
                os.remove(baqir)
    else:
        await event.edit("**⎉╎ يُرجى الرد على الصورة لطفًا**")


@zedub.zed_cmd(pattern="اضف صورة (الاوامر|اللوحة) ?(.*)")
async def Tepthon(event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        zedevent = await event.edit("**⎉╎ جـار رفع الـصورة إلى أمر لوحة الاوامر**")
        try:
            baqir = await event.client.download_media(reply)
            if baqir.endswith((".webp")):
                resize_image(baqir)
            with open(baqir, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("CMD_PIC", url)
                await zedevent.edit(f"**⎉╎ تم إضافة الصورة إلى لوحة الاوامر ✓ **")
            else:
                await zedevent.edit(f"**⎉╎ حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(baqir)
        except Exception as exc:
            await event.edit(f"**خـطأ : **\n`{exc}`")
            if os.path.exists(baqir):
                os.remove(baqir)
    else:
        await event.edit("**⎉╎ يُرجى الرد على الصورة لطفًا**")


@zedub.zed_cmd(pattern="اضف صورة (البوت|بوت) ?(.*)")
async def Tepthon(event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        zedevent = await event.edit("**⎉╎ جـار رفع الـصورة إلى أمر البوت**")
        try:
            baqir = await event.client.download_media(reply)
            if baqir.endswith((".webp")):
                resize_image(baqir)
            with open(baqir, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("BOT_START_PIC", url)
                await zedevent.edit(f"**⎉╎ تم إضافة الصورة إلى البوت ✓ **")
            else:
                await zedevent.edit(f"**⎉╎ حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(baqir)
        except Exception as exc:
            await event.edit(f"**خـطأ : **\n`{exc}`")
            if os.path.exists(baqir):
                os.remove(baqir)
    else:
        await event.edit("**⎉╎ يُرجى الرد على الصورة لطفًا**")


@zedub.zed_cmd(pattern="اضف صورة (الوقتي|التلقائي|وقتي|البروفايل) ?(.*)")
async def Tepthon(event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        zedevent = await event.edit("**⎉╎ جـار رفع الـصورة إلى أمر الصورة الوقتية**")
        try:
            baqir = await event.client.download_media(reply)
            if baqir.endswith((".webp")):
                resize_image(baqir)
            with open(baqir, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("DIGITAL_PIC", url)
                await zedevent.edit(f"**⎉╎ تم إضافة الصورة إلى امر الصورة الوقتية ✓ **")
            else:
                await zedevent.edit(f"**⎉╎ حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(baqir)
        except Exception as exc:
            await event.edit(f"**خـطأ : **\n`{exc}`")
            if os.path.exists(baqir):
                os.remove(baqir)
    else:
        await event.edit("**⎉╎ يُرجى الرد على الصورة لطفًا**")




# Copyright (C) 2022 Tepthon . All Rights Reserved
@zedub.zed_cmd(pattern="اوامر الفارات")
async def cmd(baqir):
    await edit_or_reply(baqir, BaqirVP_cmd)

@zedub.zed_cmd(pattern="الفارات")
async def cmd(baqir):
    await edit_or_reply(baqir, BaqirVP_cmd)
# Tepthon
# Copyright (C) 2022 TepthonArabic . All Rights Reserved
#
# This file is a part of < https://github.com/Tepthon-Arabic/TepthonAr/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Tepthon-Arabic/TepthonAr/blob/web/LICENSE/>.

""" وصـف الملـف : اوامـر إضـافة الفـارات باللغـة العربيـة كـاملة ولا حـرف انكلـش🤘 تخمـط اذكـر المصـدر يولـد
إضـافة فـارات صـورة ( الحمايـة - الفحـص - الوقتـي ) بـ امـر واحـد فقـط
حقـوق للتـاريخ : @Tepthon
@E_7_V - كتـابـة الملـف :  بـاقـر"""
#بـاقـر يولـد هههههههههههههههههههههههههه
import asyncio
import math
import os

import heroku3
import requests
import urllib3
import random
import string
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError
from telethon.utils import get_display_name
from urlextract import URLExtract

from . import zedub

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import delete_conv
from ..sql_helper.globals import addgvar, delgvar, gvarstatus

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY
from . import BOTLOG_CHATID, mention


plugin_category = "الادوات"
LOGS = logging.getLogger(__name__)

extractor = URLExtract()


BaqirVP_cmd = (
    "𓆩 [ 𝗧𝗲𝗽𝘁𝗵𝗼𝗻 𝗖𝗼𝗻𝗳𝗶𝗴 𝗩𝗮𝗿𝘀 - اوامـر الفـارات](t.me/Tepthon) 𓆪\n\n"
    "**⎉╎قائـمه اوامر تغييـر فـارات الصـور بأمـر واحـد فقـط - لـ اول مـره ع سـورس تليثـون يوزر بـوت 🦾 :** \n\n"
    "⪼ `.اضف صورة الحماية` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة الفحص` بالـرد ع صـورة او ميديـا\n"
    "⪼ قنـاة كلايـش الفحـص @Tepthon_kalaesh\n\n"
    "⪼ `.اضف صورة الوقتي` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة البوت` بالـرد ع صـورة او ميديـا لـ إضـافة صـورة ستـارت للبـوت\n\n"
    "⪼ `.اضف صورة الحظر` بالـرد ع صـورة او ميديـا لـ إضـافة صـورة لـ كليشـة الحظـر\n\n"
    "⪼ `.اضف صورة الكتم` بالـرد ع صـورة او ميديـا لـ إضـافة صـورة لـ كليشـة الكتـم\n\n"
    "⪼ `.اضف صورة البلوك` بالـرد ع صـورة او ميديـا لـ إضـافة صـورة لـ كليشـة حظـر الخـاص\n\n"
    "⪼ `.اوامر الفارات` لعـرض بقيـة اوامـر الفـارات\n\n\n"
    "**⎉╎قائـمه اوامر تغييـر كليشـة الايـدي :** \n\n"
    "⪼ `.اضف فار ايموجي الايدي` بالـرد ع الرمـز او الايموجـي\n\n"
    "⪼ `.اضف فار عنوان الايدي` بالـرد ع نـص العنـوان\n\n"
    "⪼ `.اضف فار خط الايدي` بالـرد ع الخـط او المستقيـم\n\n"
    "⪼ `.اضف كليشة الايدي` بالـرد ع الكليشـه مـن القنـاة @Tepthon_kalaesh\n\n\n"
    "**⎉╎قائـمه اوامر تغييـر بقيـة الفـارات بأمـر واحـد فقـط :** \n\n"
    "⪼ `.اضف فار كليشة الحماية` بالـرد ع الكليشـة\n"
    "⪼ `.اضف فار كليشة البلوك` بالـرد ع الكليشـة لتغييـر كليشة الحظر خاص\n"
    "⪼ قنـاة كلايـش حمايـة الخـاص @Tepthon_kalaesh\n\n"
    "⪼ `.اضف فار كليشة الفحص` بالـرد ع الكليشـة\n"
    "⪼ قنـاة كلايـش الفحـص @Tepthon_kalaesh\n\n"
    "⪼ `.اضف فار كليشة البوت` بالـرد ع الكليشـة لـ إضـافة كليشـة ستـارت\n\n"
    "⪼ `.اضف فار زر الستارت` بالـرد ع يوزرك او يوزر قناتك لـ إضـافة زر الستـارت\n\n"
    "⪼ `.اضف فار رمز الوقتي` بالـرد ع رمـز\n\n"
    "⪼ `.اضف فار زخرفة الوقتي` بالـرد ع ارقـام الزغـرفه\n\n"
    "⪼ `.اضف فار البايو الوقتي` بالـرد ع البـايـو\n\n"
    "⪼ `.اضف فار اسم المستخدم` بالـرد ع اسـم\n\n"
    "⪼ `.اضف فار كروب الرسائل` بالـرد ع ايدي الكـروب\n\n"
    "⪼ `.اضف فار كروب السجل` بالـرد ع ايدي الكـروب\n\n"
    "⪼ `.اضف فار ايديي` بالـرد ع ايدي حسـابك\n\n"
    "⪼ `.اضف فار نقطة الاوامر` بالـرد ع الـرمز الجديـد\n\n"
    "⪼ `.اضف فار نوم الترحيب` بالـرد ع رقـم الساعة لبداية نوم الترحيب المؤقت\n\n"
    "⪼ `.اضف فار ثواني لانهائي` بالـرد ع رقـم لعـدد الثوانـي الفاصـله بيـن كل عمليـة تجميـع فـي الامـر لانهائـي\n\n"
    "⪼ `.اضف فار رسائل الحماية` بالـرد ع رقـم لعدد رسائل تحذيـرات حماية الخاص\n\n\n"
    "⪼ `.جلب فار` + اسـم الفـار\n\n"
    "⪼ `.حذف فار` + اسـم الفـار\n\n"
    "⪼ `.رفع مطور` بالـرد ع الشخـص لرفعـه مطـور تحكـم كامـل بالاوامـر\n\n"
    "⪼ `.حذف فار المطورين`\n\n"
    "⪼ `.الوقت` لـ عـرض قائمـة اوامـر تغييـر الوقت حسب دولتك\n\n"
    "\n𓆩 [𝗧𝗲𝗽𝘁𝗵𝗼𝗻 𝗩𝗮𝗿𝘀 - قنـاة الفـارات](t.me/Tepthone1) 𓆪"
)


BaqirTZ_cmd = (
    "𓆩 [𝗧𝗲𝗽𝘁𝗵𝗼𝗻 𝗖𝗼𝗻𝗳𝗶𝗴 - اوامـر الوقت](t.me/Tepthon) 𓆪\n\n"
    "**⎉╎قائـمه اوامر تغييـر المنطقـة الزمنيـة للوقـت 🌐:** \n\n"
    "⪼ `.وقت اليمن` \n\n"
    "⪼ `.وقت العراق` \n\n"
    "⪼ `.وقت السعودية` \n\n"
    "⪼ `.وقت سوريا` \n\n"
    "⪼ `.وقت مصر` \n\n"
    "⪼ `.وقت السودان` \n\n"
    "⪼ `.وقت ليبيا` \n\n"
    "⪼ `.وقت الامارات` \n\n"
    "⪼ `.وقت ايران` \n\n"
    "⪼ `.وقت الجزائر` \n\n"
    "⪼ `.وقت المغرب` \n\n"
    "⪼ `.وقت تركيا` \n\n"
    "⪼ `.وقت ماليزيا` \n\n"
    "⪼ `.وقت روسيا` \n\n"
    "⪼ `.وقت ايطاليا` \n\n"
    "⪼ `.وقت امريكا` \n\n"
    "⪼ `.وقت المانيا` \n\n"
    "🛃 سيتـم إضـافة المزيـد من الدول قريبـًـا\n\n"
    "\n𓆩 [𝗧𝗲𝗽𝘁𝗵𝗼𝗻 𝗩𝗮𝗿𝘀 - قنـاة الفـارات](t.me/Tepthone1) 𓆪"
)


# Copyright (C) 2022 Tepthon . All Rights Reserved
@zedub.zed_cmd(pattern=r"اضف فار (.*)")
async def variable(event):
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    vinfo = reply.text
    rep = await edit_or_reply(event, "**⎉╎جـاري إضـافة الفـار إلـى بـوتك ...**")
    # All Rights Reserved for "Tepthon" "باقر"
    if input_str == "كليشة الفحص" or input_str == "كليشه الفحص":
        variable = "ALIVE_TEMPLATE"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_TEMPLATE") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.فحص` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.فحص` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("ALIVE_TEMPLATE", vinfo)
    elif input_str == "كليشة الحماية" or input_str == "كليشه الحمايه" or input_str == "كليشه الحماية" or input_str == "كليشة الحمايه":
        variable = "pmpermit_txt"
        await asyncio.sleep(1.5)
        if gvarstatus("pmpermit_txt") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.الحمايه تفعيل` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.الحمايه تفعيل` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("pmpermit_txt", vinfo)
    elif input_str == "كليشة الايدي" or input_str == "كليشه الايدي":
        variable = "RID_TEMPLATE"
        await asyncio.sleep(1.5)
        if gvarstatus("RID_TEMPLATE") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.ايدي` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.ايدي` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("RID_TEMPLATE", vinfo)
    elif input_str == "كليشة البوت" or input_str == "كليشه البوت" or input_str == "ستارت البوت" or input_str == "كليشة الستارت" or input_str == "كليشه الستارت" or input_str == "كليشة البدء":
        variable = "START_TEXT"
        await asyncio.sleep(1.5)
        if gvarstatus("START_TEXT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الآن قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("START_TEXT", vinfo)
    elif input_str == "زر البوت" or input_str == "زر الستارت" or input_str == "زر ستارت":
        variable = "START_BUTUN"
        await asyncio.sleep(1.5)
        if not vinfo.startswith("@"):
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع يـوزر فقـط**")
        vinfo = vinfo.zedlace("@", "")
        if gvarstatus("START_TEXT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎رابـط زر كليشـة الستـارت الجـديـد** \nhttps://t.me/{} \n\n**⎉╎الآن قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎رابـط زر كليشـة الستـارت الجـديـد** \nhttps://t.me/{} \n\n**⎉╎الآن قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("START_BUTUN", vinfo)
    elif input_str == "كليشة التوديع" or input_str == "كليشه التوديع" or input_str == "كليشة البلوك" or input_str == "كليشه البلوك":
        variable = "pmblock"
        await asyncio.sleep(1.5)
        if gvarstatus("pmblock") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ تفعيـل حماية الخاص عبر الأمر ↶** ( `الحماية تفعيل` ) **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ تفعيـل حماية الخاص عبر الأمر ↶** ( `الحماية تفعيل` ) **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("pmblock", vinfo)
    elif input_str == "رمز الوقتي" or input_str == "رمز الاسم الوقتي":
        variable = "CUSTOM_ALIVE_EMREP"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_EMREP") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الـرمـز الجـديـد** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.الاسم تلقائي` **لـ التحقـق مـن الـرمز . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎الـرمـز المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.الاسم تلقائي` **لـ التحقـق مـن الـرمز . .**".format(input_str, vinfo))
    elif input_str == "البايو" or input_str == "البايو الوقتي" or input_str == "النبذه" or input_str == "البايو تلقائي":
        variable = "DEFAULT_BIO"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_BIO") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎البـايـو الجـديـد** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.البايو تلقائي` **لـ التحقـق مـن البايـو . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضـافه {} بنجـاح ☑️**\n**⎉╎البـايـو المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.البايو تلقائي` **لـ التحقـق مـن البايـو . .**".format(input_str, vinfo))
    elif input_str == "التحقق" or input_str == "كود التحقق" or input_str == "التحقق بخطوتين" or input_str == "تحقق":
        variable = "TG_2STEP_VERIFICATION_CODE"
        await asyncio.sleep(1.5)
        if gvarstatus("TG_2STEP_VERIFICATION_CODE") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎كـود التحـقق بخطـوتيـن** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.تحويل ملكية` **ثم معـرف الشخـص داخـل الكـروب او القنـاة . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎كـود التحـقق بخطـوتيـن** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.تحويل ملكية` **ثم معـرف الشخـص داخـل الكـروب او القنـاة . .**".format(input_str, vinfo))
    elif input_str == "كاشف الاباحي" or input_str == "كشف الاباحي":
        variable = "DEEP_API"
        await asyncio.sleep(1.5)
        if gvarstatus("DEEP_API") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر توكـن {} بنجـاح ☑️**\n**⎉╎التوكـن الجـديـد** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.قفل الاباحي` **لـ تفعيـل كاشـف الاباحي . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة توكـن {} بنجـاح ☑️**\n**⎉╎التوكـن المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.قفل الاباحي` **لـ تفعيـل كاشـف الاباحي . .**".format(input_str, vinfo))
    elif input_str == "ايموجي الايدي" or input_str == "ايموجي ايدي" or input_str == "رمز الايدي" or input_str == "رمز ايدي" or input_str == "الرمز ايدي":
        variable = "CUSTOM_ALIVE_EMOJI"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_EMOJI") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        addgvar("CUSTOM_ALIVE_EMOJI", vinfo)
    elif input_str == "عنوان الايدي" or input_str == "عنوان ايدي":
        variable = "CUSTOM_ALIVE_TEXT"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_TEXT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        addgvar("CUSTOM_ALIVE_TEXT", vinfo)
    elif input_str == "خط الايدي" or input_str == "خط ايدي" or input_str == "خطوط الايدي" or input_str == "خط ايدي":
        variable = "CUSTOM_ALIVE_FONT"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_FONT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        addgvar("CUSTOM_ALIVE_FONT", vinfo)
    elif input_str == "اشتراك الخاص" or input_str == "اشتراك خاص":
        variable = "Custom_Pm_Channel"
        await asyncio.sleep(1.5)
        if gvarstatus("Custom_Pm_Channel") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.اشتراك خاص`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.اشتراك خاص`".format(input_str, vinfo))
        delgvar("Custom_Pm_Channel")
        addgvar("Custom_Pm_Channel", vinfo)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#قنـاة_الاشتـراك_الاجبـاري_للخـاص\
                        \n**- القنـاة {input_str} تم إضافتهـا في قاعده البيانات ..بنجـاح ✓**",
            )
    elif input_str == "اشتراك كروب" or input_str == "اشتراك الكروب":
        variable = "Custom_G_Channel"
        await asyncio.sleep(1.5)
        if gvarstatus("Custom_G_Channel") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.اشتراك كروب`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.اشتراك كروب`".format(input_str, vinfo))
        delgvar("Custom_G_Channel")
        addgvar("Custom_G_Channel", vinfo)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#قنـاة_الاشتـراك_الاجبـاري_للكـروب\
                        \n**- القنـاة {input_str} تم إضافتهـا في قاعده البيانات ..بنجـاح ✓**",
            )
    elif input_str == "زاجل" or input_str == "قائمة زاجل" or input_str == "قائمه زاجل" or input_str == "يوزرات":
        variable = "ZAGL_Rep"
        await asyncio.sleep(1.5)
        if gvarstatus("ZAGL_Rep") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎اليـوزرات المضـافة** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.زاجل` **بالـرد ع نـص او ميديـا بنـص . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎اليـوزرات المضـافة** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.زاجل` **بالـرد ع نـص او ميديـا بنـص . .**".format(input_str, vinfo))
    elif input_str == "سوبر" or input_str == "قائمة السوبر" or input_str == "قائمه السوبر" or input_str == "السوبرات" or input_str == "السوبر":
        variable = "Super_Id"
        await asyncio.sleep(1.5)
        if not vinfo.startswith("-100"):
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع ارقـام ايديات المجموعات التي تبدأ ب 100- فقـط ؟!**\n**⎉╎قم بالذهاب لمجموعات السوبر التي تريد النشر فيها وكتابة الأمر (.الايدي) ثم خذ ايدي المجموعة وهكذا لبقية المجموعات**")
        if gvarstatus("Super_Id") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎الايديات المضـافة** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** (`.سوبر` + عدد الثواني + عدد مرات التكرار)**بالـرد ع نـص او ميديـا بنـص . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الايديات المضـافة** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** (`.سوبر` + عدد الثواني + عدد مرات التكرار)**بالـرد ع نـص او ميديـا بنـص . .**".format(input_str, vinfo))
    elif input_str == "بوت التجميع" or input_str == "بوت النقاط" or input_str == "النجميع" or input_str == "النقاط":
        variable = "R_Point"
        await asyncio.sleep(1.5)
        if gvarstatus("R_Point") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎البـوت المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.تجميع` **لـ البـدء بتجميـع النقـاط من البـوت الجـديـد . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضـافه {} بنجـاح ☑️**\n**⎉╎البـوت المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.تجميع` **لـ البـدء بتجميـع النقـاط من البـوت الجـديـد . .**".format(input_str, vinfo))
    elif input_str == "اسم المستخدم" or input_str == "الاسم":
        variable = "ALIVE_NAME"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_NAME") is not None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        addgvar(variable, vinfo)

    elif input_str == "رسائل الحماية" or input_str == "رسائل الحمايه" or input_str == "رسائل الخاص" or input_str == "رسائل حماية الخاص" or input_str == "عدد التحذيرات":
        variable = "MAX_FLOOD_IN_PMS"
        await asyncio.sleep(1.5)
        if vinfo.isdigit():
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع رقـم فقـط ؟!**")
        addgvar("MAX_FLOOD_IN_PMS", vinfo)

    elif input_str == "كود تيرمكس" or input_str == "كود السيشن" or input_str == "كود سيشن":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "STRING_SESSION"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo

    elif input_str == "كروب الرسائل" or input_str == "كروب التخزين" or input_str == "كروب الخاص":
        variable = "PM_LOGGER_GROUP_ID"
        await asyncio.sleep(1.5)
        if gvarstatus("PM_LOGGER_GROUP_ID") is not None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        addgvar("PM_LOGGER_GROUP_ID", vinfo)
    elif input_str == "السجل" or input_str == "كروب السجل":
        variable = "PRIVATE_GROUP_BOT_API_ID"
        await asyncio.sleep(1.5)
        if gvarstatus("PRIVATE_GROUP_BOT_API_ID") is not None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        addgvar("PRIVATE_GROUP_BOT_API_ID", vinfo)
    elif input_str == "السجل 2" or input_str == "كروب السجل 2":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "PRIVATE_GROUP_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "قناة السجل" or input_str == "قناة السجلات":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "PRIVATE_CHANNEL_BOT_API_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "قناة الملفات" or input_str == "قناة الإضافات":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "PLUGIN_CHANNEL"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "ايديي" or input_str == "ايدي الحساب":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "OWNER_ID"
        await asyncio.sleep(1.5)
        if vinfo.isdigit():
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع رقـم فقـط ؟!**")
        heroku_var[variable] = vinfo
    elif input_str == "نقطة الاوامر" or input_str == "نقطه الاوامر":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "COMMAND_HAND_LER"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "التوكن" or input_str == "توكن البوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TG_BOT_TOKEN"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "معرف البوت" or input_str == "معرف بوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TG_BOT_USERNAME"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "الريبو" or input_str == "السورس":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه ريندر 🔄**")
        variable = "UPSTREAM_REPO"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "توكن المكافح" or input_str == "كود المكافح" or input_str == "مكافح التخريب" or input_str == "مكافح التفليش":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "SPAMWATCH_API"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "توكن الذكاء" or input_str == "مفتاح الذكاء" or input_str == "الذكاء":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "OPENAI_API_KEY"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "ايقاف الترحيب" or input_str == "نوم الترحيب":
        variable = "TIME_STOP"
        await asyncio.sleep(1.5)
        if vinfo.isdigit():
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع رقـم فقـط ؟!**")
        addgvar("TIME_STOP", vinfo)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#فتـرة_الايقـاف_المـؤقت_للترحيب\
                        \n**- تم إضافة الفتـرة من الساعة {vinfo} إلى الساعة 6 صباحـًـا .. بنجـاح ✓**",
            )
    elif input_str == "ثواني لانهائي" or input_str == "ثواني التجميع" or input_str == "عدد لانهائي":
        variable = "SEC_LAN"
        await asyncio.sleep(1.5)
        if vinfo.isdigit():
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎الثوانـي الجـديـدة** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.لانهائي` **+ اسم بوت التجميـع لـ البـدء بالتجميـع اللانهائـي . .**".format(input_str, vinfo))
        else:
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع رقـم فقـط ؟!**")
        addgvar(variable, vinfo)
    elif ("صورة" in input_str) or ("صوره" in input_str):
        return await zed.edit("**⎉╎لـ إضافة صور الكلايش ..**\n**⎉╎استخدم الأمر (اضف) مباشرة بدون كلمة فار**")
    else:
        if input_str:
            return await zed.edit("**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))
        return await edit_or_reply(event, "**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))


# Copyright (C) 2022 TepthonArabic . All Rights Reserved
@zedub.zed_cmd(pattern="حذف فار(?:\\s|$)([\\s\\S]*)")
async def variable(event):
    input_str = event.text[9:]
    if (input_str == "من" or input_str == "إلى" or input_str == "الترحيب") or "رسائلي" in input_str or "رسائله" in input_str:
        return
    rep = await edit_or_reply(event, "**⎉╎جـاري حـذف الفـار مـن بـوتك 🚮...**")
    # All Rights Reserved for "Tepthon" "باقر"
    if input_str == "كليشة الفحص" or input_str == "كليشه الفحص":
        variable = gvarstatus("ALIVE_TEMPLATE")
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_TEMPLATE") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("ALIVE_TEMPLATE")
        
    elif input_str == "كليشة الحماية" or input_str == "كليشه الحمايه" or input_str == "كليشه الحماية" or input_str == "كليشة الحمايه":
        variable = gvarstatus("pmpermit_txt")
        await asyncio.sleep(1.5)
        if gvarstatus("pmpermit_txt") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("pmpermit_txt")

    elif input_str == "كليشة البوت" or input_str == "كليشه البوت":
        variable = gvarstatus("START_TEXT")
        await asyncio.sleep(1.5)
        if gvarstatus("START_TEXT") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("START_TEXT")

    elif input_str == "زر البوت" or input_str == "زر الستارت" or input_str == "زر ستارت":
        variable = gvarstatus("START_BUTUN")
        await asyncio.sleep(1.5)
        if gvarstatus("START_BUTUN") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("START_BUTUN")

    elif input_str == "كليشة التوديع" or input_str == "كليشه التوديع" or input_str == "كليشة البلوك" or input_str == "كليشه البلوك":
        variable = gvarstatus("pmblock")
        await asyncio.sleep(1.5)
        if gvarstatus("pmblock") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت زد ثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("pmblock")

    elif input_str == "كليشة الايدي" or input_str == "كليشه الايدي":
        variable = "RID_TEMPLATE"
        await asyncio.sleep(1.5)
        if gvarstatus("RID_TEMPLATE") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("RID_TEMPLATE")

    elif input_str == "صورة الفحص" or input_str == "صوره الفحص":
        variable = "ALIVE_PIC"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_PIC") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("ALIVE_PIC")

    elif input_str == "صورة الاوامر" or input_str == "صوره الاوامر":
        variable = "CMD_PIC"
        await asyncio.sleep(1.5)
        if gvarstatus("CMD_PIC") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("CMD_PIC")

    elif input_str == "صورة السورس" or input_str == "صوره السورس":
        variable = "ALIVE_PIC"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_PIC") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("ALIVE_PIC")

    elif input_str == "صورة الكتم" or input_str == "صوره الكتم":
        variable = "PC_MUTE"
        await asyncio.sleep(1.5)
        if gvarstatus("PC_MUTE") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("PC_MUTE")

    elif input_str == "صورة الحظر" or input_str == "صوره الحظر":
        variable = "PC_BANE"
        await asyncio.sleep(1.5)
        if gvarstatus("PC_BANE") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("PC_BANE")

    elif input_str == "صورة البلوك" or input_str == "صوره البلوك":
        variable = "PC_BLOCK"
        await asyncio.sleep(1.5)
        if gvarstatus("PC_BLOCK") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("PC_BLOCK")

    elif input_str == "صورة البوت" or input_str == "صوره البوت" or input_str == "صورة الستارت" or input_str == "صوره الستارت" or input_str == "صورة ستارت" or input_str == "صوره ستارت":
        variable = "BOT_START_PIC"
        await asyncio.sleep(1.5)
        if gvarstatus("BOT_START_PIC") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("BOT_START_PIC")

    elif input_str == "صورة الحماية" or input_str == "صوره الحمايه" or input_str == "صورة الحمايه" or input_str == "صوره الحماية":
        variable = "pmpermit_pic"
        await asyncio.sleep(1.5)
        if gvarstatus("pmpermit_pic") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        delgvar("pmpermit_pic")
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))

    elif input_str == "صورة الوقتي" or input_str == "صوره الوقتي":
        variable = gvarstatus("DIGITAL_PIC")
        await asyncio.sleep(1.5)
        if gvarstatus("DIGITAL_PIC") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("DIGITAL_PIC")

    elif input_str == "رمز الوقتي" or input_str == "رمز الاسم الوقتي":
        variable = "CUSTOM_ALIVE_EMREP"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_EMREP") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        delgvar("CUSTOM_ALIVE_EMREP")
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
    elif input_str == "زخرفه الوقتي" or input_str == "زخرفة الوقتي":
        variable = "BA_FN"
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        delgvar(variable)
    elif input_str == "رسائل الحماية" or input_str == "رسائل الحمايه" or input_str == "رسائل الخاص" or input_str == "رسائل حماية الخاص" or input_str == "عدد التحذيرات":
        variable = "MAX_FLOOD_IN_PMS"
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        delgvar(variable)
    elif input_str == "البايو" or input_str == "البايو الوقتي" or input_str == "النبذه الوقتيه":
        variable = "DEFAULT_BIO"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_BIO") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        delgvar("DEFAULT_BIO")
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
    elif input_str == "اسم المستخدم" or input_str == "الاسم":
        variable = "ALIVE_NAME"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_NAME") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        delgvar(variable)
    elif input_str == "كروب الرسائل" or input_str == "كروب التخزين" or input_str == "كروب الخاص":
        variable = "PM_LOGGER_GROUP_ID"
        await asyncio.sleep(1.5)
        if gvarstatus("PM_LOGGER_GROUP_ID") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        delgvar(variable)

    elif input_str == "السجل" or input_str == "كروب السجل":
        variable = "PRIVATE_GROUP_BOT_API_ID"
        await asyncio.sleep(1.5)
        if gvarstatus("PRIVATE_GROUP_BOT_API_ID") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        delgvar(variable)

    elif input_str == "السجل 2" or input_str == "كروب السجل 2":
        variable = "PRIVATE_GROUP_ID"
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "قناة السجل" or input_str == "قناة السجلات":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "PRIVATE_CHANNEL_BOT_API_ID"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "قناة الملفات" or input_str == "قناة الإضافات":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "PLUGIN_CHANNEL"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "التحقق" or input_str == "كود التحقق":
        variable = "TG_2STEP_VERIFICATION_CODE"
        await asyncio.sleep(1.5)
        if gvarstatus("TG_2STEP_VERIFICATION_CODE") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        delgvar("TG_2STEP_VERIFICATION_CODE")
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))

    elif input_str == "ايديي" or input_str == "ايدي الحساب":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "OWNER_ID"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "نقطة الاوامر" or input_str == "نقطه الاوامر":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه ريندر 🔄**")
        variable = "COMMAND_HAND_LER"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "التوكن" or input_str == "توكن البوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TG_BOT_TOKEN"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "معرف البوت" or input_str == "معرف بوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TG_BOT_USERNAME"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "الريبو" or input_str == "السورس":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "UPSTREAM_REPO"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "اسمي التلقائي" or input_str == "الاسم التلقاائي":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "AUTONAME"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]
    elif input_str == "ايموجي الايدي" or input_str == "ايموجي ايدي" or input_str == "رمز الايدي" or input_str == "رمز ايدي" or input_str == "الرمز ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_EMOJI")
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("CUSTOM_ALIVE_EMOJI")
    elif input_str == "عنوان الايدي" or input_str == "عنوان ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_TEXT")
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("CUSTOM_ALIVE_TEXT")
    elif input_str == "خط الايدي" or input_str == "خط ايدي" or input_str == "خطوط الايدي" or input_str == "خط ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_FONT")
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("CUSTOM_ALIVE_FONT")
    elif input_str == "كاشف الاباحي" or input_str == "كشف الاباحي":
        variable = gvarstatus("DEEP_API")
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("DEEP_API")
    elif input_str == "ايقاف الترحيب" or input_str == "نوم الترحيب":
        variable = "TIME_STOP"
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("TIME_STOP")
    elif input_str == "ثواني لانهائي" or input_str == "ثواني التجميع" or input_str == "عدد لانهائي":
        variable = "SEC_LAN"
        await asyncio.sleep(1.5)
        if gvarstatus("SEC_LAN") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("SEC_LAN")
    else:
        if input_str:
            return await zed.edit("**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))
        return await edit_or_reply(event, "**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))


# Copyright (C) 2022 TepthonArabic . All Rights Reserved
@zedub.zed_cmd(pattern="جلب فار(?:\\s|$)([\\s\\S]*)")
async def custom_rep(event):
    input_str = event.text[9:]
    rep = await edit_or_reply(event, "**⎉╎جــاري جلـب معلـومـات الفــار 🛂. . .**")
    if (input_str == "كليشة الحماية" or input_str == "كليشة الحمايه" or input_str == "كليشه الحماية" or input_str == "كليشه الحمايه"):
        variable = gvarstatus("pmpermit_txt")
        if variable is None:
            await zed.edit("**⎉╎فـار كليشـة الحمايـة غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكليشـة استخـدم الامـر : ↶**\n `.اضف فار كليشة الحماية` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))
            
    elif input_str == "كليشة الفحص" or input_str == "كليشه الفحص":
        variable = gvarstatus("ALIVE_TEMPLATE")
        if variable is None:
            await zed.edit("**⎉╎فـار كليشـة الفحص غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكليشـة استخـدم الامـر : ↶**\n `.اضف فار كليشة الفحص` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "كليشة البوت" or input_str == "كليشه البوت":
        variable = gvarstatus("START_TEXT")
        if variable is None:
            await zed.edit("**⎉╎فـار كليشـة البـوت غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكليشـة استخـدم الامـر : ↶**\n `.اضف فار كليشة البوت` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "زر البوت" or input_str == "زر الستارت" or input_str == "زر ستارت":
        variable = gvarstatus("START_BUTUN")
        if variable is None:
            await zed.edit("**⎉╎فـار زر كليشـة ستـارت البـوت غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع يـوزرك او يـوزر قناتـك استخـدم الامـر : ↶**\n `.اضف فار زر الستارت` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n https://t.me/{}\n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "كليشة التوديع" or input_str == "كليشه التوديع" or input_str == "كليشة البلوك" or input_str == "كليشه البلوك":
        variable = gvarstatus("pmblock")
        if variable is None:
            await zed.edit("**⎉╎فـار كليشـة الحظـر غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكليشـة استخـدم الامـر : ↶**\n `.اضف فار كليشة الحظر` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "رمز الوقتي" or input_str == "رمز الاسم الوقتي":
        variable = gvarstatus("CUSTOM_ALIVE_EMREP")
        if variable is None:
            await zed.edit("**⎉╎فـار رمـز الوقتـي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز استخـدم الامـر : ↶**\n `.اضف فار رمز الوقتي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "التحقق" or input_str == "كود التحقق":
        variable = gvarstatus("TG_2STEP_VERIFICATION_CODE")
        if variable is None:
            await zed.edit("**⎉╎فـار التحقق بخطوتين غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز استخـدم الامـر : ↶**\n `.اضف فار التحقق`  **بالـرد ع كـود التحـقق**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "كاشف الاباحي" or input_str == "كشف الاباحي":
        variable = gvarstatus("DEEP_API")
        if variable is None:
            await zed.edit("**⎉╎فـار كشـف الاباحي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكـود استخـدم الامـر : ↶**\n `.اضف فار كاشف الاباحي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "البايو" or input_str == "البايو الوقتي" or input_str == "النبذه" or input_str == "البايو تلقائي":
        variable = gvarstatus("DEFAULT_BIO")
        if variable is None:
            await zed.edit("**⎉╎فـار البايـو الوقتـي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع نـص استخـدم الامـر : ↶**\n `.اضف فار البايو` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "اسم المستخدم" or input_str == "الاسم":
        variable = gvarstatus("ALIVE_NAME")
        if gvarstatus("ALIVE_NAME") is None:
            await zed.edit("**⎉╎فـار اسـم المستخـدم غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الاسم استخـدم الامـر : ↶**\n `.اضف فار اسم المستخدم` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "كود تيرمكس" or input_str == "كود السيشن" or input_str == "كود سيشن":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "STRING_SESSION"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار اسـم المستخـدم غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الاسم استخـدم الامـر : ↶**\n `.اضف فار اسم المستخدم` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "ايديي" or input_str == "ايدي الحساب":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "OWNER_ID"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار ايـدي الحسـاب غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الايـدي فقـط استخـدم الامـر : ↶**\n `.اضف فار ايدي الحساب` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "نقطة الاوامر" or input_str == "نقطه الاوامر":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "COMMAND_HAND_LER"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار نقطـة الاوامـر غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز فقـط استخـدم الامـر : ↶**\n `.اضف فار نقطة الاوامر` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "التوكن" or input_str == "توكن البوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TG_BOT_TOKEN"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار توكـن البـوت غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع التوكـن فقـط استخـدم الامـر : ↶**\n `.اضف فار التوكن` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "معرف البوت" or input_str == "معرف بوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "APP_USERNAME"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار معرف البوت غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع المعرف استخـدم الامـر : ↶**\n `.اضف فار معرف البوت` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "الريبو" or input_str == "السورس":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "UPSTREAM_REPO"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار الريبـو غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع رابط السورس الرسمي استخـدم الامـر : ↶**\n `.اضف فار الريبو` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "اسمي التلقائي" or input_str == "الاسم التلقاائي":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "AUTONAME"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار الاسـم التلقائي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الاسم استخـدم الامـر : ↶**\n `.اضف فار اسمي التلقائي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الحماية" or input_str == "صوره الحمايه" or input_str == "صورة الحمايه" or input_str == "صوره الحماية":
        variable = gvarstatus("pmpermit_pic")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الحمايـة غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الحماية` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الوقتي" or input_str == "صوره الوقتي":
        variable = gvarstatus("DIGITAL_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الوقتـي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الوقتي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الفحص" or input_str == "صوره الفحص":
        variable = gvarstatus("ALIVE_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الفحص غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الفحص` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة البوت" or input_str == "صوره البوت" or input_str == "صورة الستارت" or input_str == "صوره الستارت" or input_str == "صورة ستارت" or input_str == "صوره ستارت":
        variable = gvarstatus("BOT_START_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة ستـارت البـوت غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة البوت` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الاوامر" or input_str == "صوره الاوامر":
        variable = gvarstatus("CMD_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الاوامـر غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الاوامر` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة السورس" or input_str == "صوره السورس":
        variable = gvarstatus("ALIVE_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة السـورس غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة السورس` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الكتم" or input_str == "صوره الكتم":
        variable = gvarstatus("PC_MUTE")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الكتم غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الكتم` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الحظر" or input_str == "صوره الحظر":
        variable = gvarstatus("PC_BANE")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الحظر غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الحظر` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة البلوك" or input_str == "صوره البلوك":
        variable = gvarstatus("PC_BLOCK")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة البلوك غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة البلوك` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "زخرفة الوقتي" or input_str == "زخرفه الوقتي":
        variable = gvarstatus("NA_FN")
        if variable is None:
            await zed.edit("**⎉╎فـار زخرفـة الاسـم الوقتي غيـر موجـود ❌**\n**⎉╎لـ إضـافته فقـط استخـدم الامـر : ↶**\n `.الوقتي 1` إلـى `.الوقتي 14` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "رسائل الحماية" or input_str == "رسائل الحمايه" or input_str == "رسائل الخاص" or input_str == "رسائل حماية الخاص" or input_str == "عدد التحذيرات":
        variable = gvarstatus("MAX_FLOOD_IN_PMS")
        if variable is None:
            await zed.edit("**⎉╎فـار رسـائل الحمايـة غيـر موجـود ❌**\n**⎉╎لـ إضـافته فقـط استخـدم الامـر : ↶**\n `.اضف فار رسائل الحماية` بالـرد ع عـدد فقـط \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "زخرفة الوقتية" or input_str == "زخرفه الوقتيه" or input_str == "زخرفة الوقتيه" or input_str == "زخرفه الوقتية":
        variable = gvarstatus("DEFAULT_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار زخرفـة الصـورة الوقتيـة غيـر موجـود ❌**\n**⎉╎لـ إضـافته فقـط استخـدم الامـر : ↶**\n `.وقتي 1` إلـى `.وقتي 17` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "الوقت" or input_str == "الساعه" or input_str == "المنطقه الزمنيه":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TZ"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار المنطقـة الزمنيــــة غيـر موجـود ❌**\n**⎉╎لـ إضـافته فقـط استخـدم الامـر : ↶**\n `.وقت` واسـم الدولـة \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "كليشة الايدي" or input_str == "كليشه الايدي":
        variable = gvarstatus("RID_TEMPLATE")
        if variable is None:
            await zed.edit("**⎉╎فـار ايموجي/رمز الايدي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكليشـة من هنا ( @Tepthon_kalaesh ) استخـدم الامـر : ↶**\n `.اضف كليشة الايدي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "ايموجي الايدي" or input_str == "ايموجي ايدي" or input_str == "رمز الايدي" or input_str == "رمز ايدي" or input_str == "الرمز ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_EMOJI")
        if variable is None:
            await zed.edit("**⎉╎فـار ايموجي/رمز الايدي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز استخـدم الامـر : ↶**\n `.اضف فار رمز الايدي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))
            
    elif input_str == "عنوان الايدي" or input_str == "عنوان ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_TEXT")
        if variable is None:
            await zed.edit("**⎉╎فـار نص عنـوان كليشـة الايـدي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز استخـدم الامـر : ↶**\n `.اضف فار عنوان الايدي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "خط الايدي" or input_str == "خط ايدي" or input_str == "خطوط الايدي" or input_str == "خط ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_FONT")
        if variable is None:
            await zed.edit("**⎉╎فـار خطـوط كليشـة الايـدي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز استخـدم الامـر : ↶**\n `.اضف فار خطوط الايدي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "لاعب 1":
        variable = gvarstatus("R_AK")
        if gvarstatus("R_AK") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "لاعب 2":
        variable = gvarstatus("R_A2K")
        if gvarstatus("R_A2K") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "لاعب 3":
        variable = gvarstatus("R_A3K")
        if gvarstatus("R_A3K") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "لاعب 4":
        variable = gvarstatus("R_A4K")
        if gvarstatus("R_A4K") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "لاعب 5":
        variable = gvarstatus("R_A5K")
        if gvarstatus("R_A5K") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "توكن المكافح" or input_str == "كود المكافح" or input_str == "مكافح التخريب" or input_str == "مكافح التفليش":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "SPAMWATCH_API"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار توكـن المكـافح غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "اشتراك خاص" or input_str == "اشتراك الخاص" or input_str == "قناة الاشتراك" or input_str == "الاشتراك":
        variable = gvarstatus("Custom_Pm_Channel")
        if gvarstatus("Custom_Pm_Channel") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "اشتراك كروب" or input_str == "اشتراك الكروب" or input_str == "قناة الاشتراك" or input_str == "الاشتراك":
        variable = gvarstatus("Custom_G_Channel")
        if gvarstatus("Custom_G_Channel") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "االهمسه":
        variable = gvarstatus("hmsa_id")
        if gvarstatus("hmsa_id") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "ثواني لانهائي" or input_str == "ثواني التجميع" or input_str == "عدد لانهائي":
        variable = gvarstatus("SEC_LAN")
        if gvarstatus("SEC_LAN") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    else:
        if input_str:
            return await zed.edit("**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))
        return await edit_or_reply(event, "**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))


# Copyright (C) 2022 TepthonArabic . All Rights Reserved
@zedub.zed_cmd(pattern="وقت(?:\\s|$)([\\s\\S]*)")
async def variable(event):
    input_str = event.text[5:]
    viraq = "Asia/Baghdad"
    vmsr = "Africa/Cairo"
    vdubai = "Asia/Dubai"
    vturk = "Europe/Istanbul"
    valgiers = "Africa/Algiers"
    vmoroco = "Africa/Casablanca"
    viran = "Asia/Tehran"
    vsudan = "Africa/Khartoum"
    vitaly = "Europe/Rome"
    vrusia = "Europe/Moscow"
    vamerica = "America/Washington"
    vmalaysia = "Asia/Kuala_Lumpur"
    vdeutschland = "Europe/Berlin"
    rep = await edit_or_reply(event, "**⎉╎جـاري إعــداد المنطقـة الزمنيــــة لـ تيبثـون 🌐...**")
    # All Rights Reserved for "Tepthon" "باقر"
    if input_str == "العراق" or input_str == "اليمن" or input_str == "سوريا" or input_str == "السعودية" or input_str == "لبنان" or input_str == "الاردن":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", viraq)
    elif input_str == "مصر" or input_str == "ليبيا" or input_str == "القاهرة":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", vmsr)
    elif input_str == "دبي" or input_str == "الامارات" or input_str == "عمان" or input_str == "مسقط":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", vdubai)
    elif input_str == "تركيا" or input_str == "اسطنبول" or input_str == "انقرة":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", vturk)
    elif input_str == "تونس" or input_str == "الجزائر":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", valgiers)
    elif input_str == "المغرب" or input_str == "موريتانيا" or input_str == "الدار البيضاء":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", vmoroco)        
    elif input_str == "ايران" or input_str == "طهران":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", viran)
    elif input_str == "السودان":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "Africa/Khartoum")
    elif input_str == "ايطاليا":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "Europe/Rome")
    elif input_str == "روسيا":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "Europe/Moscow")
    elif input_str == "امريكا":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "America/Washington")
    elif input_str == "ماليزيا":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "Asia/Kuala_Lumpur")
    elif input_str == "المانيا":
        variable = "TZ"
        await asyncio.slepp(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "Europe/Berlin")

                
@zedub.zed_cmd(pattern="اضف صورة (الفحص|فحص) ?(.*)")
async def alive_Tepthon(event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        zedevent = await event.edit("**⎉╎ جـار رفع الـصورة إلى أمر الفحص**")
        try:
            baqir = await event.client.download_media(reply)
            if baqir.endswith((".webp")):
                resize_image(baqir)
            with open(baqir, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("ALIVE_PIC", url)
                await zedevent.edit(f"**⎉╎ تم إضافة الصورة إلى الفحص ✓ **")
            else:
                await zedevent.edit(f"**⎉╎ حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(baqir)
        except Exception as exc:
            await event.edit(f"**خـطأ : **\n`{exc}`")
            if os.path.exists(baqir):
                os.remove(baqir)
    else:
        await event.edit("**⎉╎ يُرجى الرد على الصورة لطفًا**")


@zedub.zed_cmd(pattern="اضف صورة (الحمايه|الحماية) ?(.*)")
async def Tepthon(event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        zedevent = await event.edit("**⎉╎ جـار رفع الـصورة إلى أمر الحماية**")
        try:
            baqir = await event.client.download_media(reply)
            if baqir.endswith((".webp")):
                resize_image(baqir)
            with open(baqir, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("pmpermit_pic", url)
                await zedevent.edit(f"**⎉╎ تم إضافة الصورة إلى الحماية ✓ **")
            else:
                await zedevent.edit(f"**⎉╎ حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(baqir)
        except Exception as exc:
            await event.edit(f"**خـطأ : **\n`{exc}`")
            if os.path.exists(baqir):
                os.remove(baqir)
    else:
        await event.edit("**⎉╎ يُرجى الرد على الصورة لطفًا**")


@zedub.zed_cmd(pattern="اضف صورة (الاوامر|اللوحة) ?(.*)")
async def Tepthon(event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        zedevent = await event.edit("**⎉╎ جـار رفع الـصورة إلى أمر لوحة الاوامر**")
        try:
            baqir = await event.client.download_media(reply)
            if baqir.endswith((".webp")):
                resize_image(baqir)
            with open(baqir, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("CMD_PIC", url)
                await zedevent.edit(f"**⎉╎ تم إضافة الصورة إلى لوحة الاوامر ✓ **")
            else:
                await zedevent.edit(f"**⎉╎ حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(baqir)
        except Exception as exc:
            await event.edit(f"**خـطأ : **\n`{exc}`")
            if os.path.exists(baqir):
                os.remove(baqir)
    else:
        await event.edit("**⎉╎ يُرجى الرد على الصورة لطفًا**")


@zedub.zed_cmd(pattern="اضف صورة (البوت|بوت) ?(.*)")
async def Tepthon(event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        zedevent = await event.edit("**⎉╎ جـار رفع الـصورة إلى أمر البوت**")
        try:
            baqir = await event.client.download_media(reply)
            if baqir.endswith((".webp")):
                resize_image(baqir)
            with open(baqir, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("BOT_START_PIC", url)
                await zedevent.edit(f"**⎉╎ تم إضافة الصورة إلى البوت ✓ **")
            else:
                await zedevent.edit(f"**⎉╎ حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(baqir)
        except Exception as exc:
            await event.edit(f"**خـطأ : **\n`{exc}`")
            if os.path.exists(baqir):
                os.remove(baqir)
    else:
        await event.edit("**⎉╎ يُرجى الرد على الصورة لطفًا**")


@zedub.zed_cmd(pattern="اضف صورة (الوقتي|التلقائي|وقتي|البروفايل) ?(.*)")
async def Tepthon(event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        zedevent = await event.edit("**⎉╎ جـار رفع الـصورة إلى أمر الصورة الوقتية**")
        try:
            baqir = await event.client.download_media(reply)
            if baqir.endswith((".webp")):
                resize_image(baqir)
            with open(baqir, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("DIGITAL_PIC", url)
                await zedevent.edit(f"**⎉╎ تم إضافة الصورة إلى امر الصورة الوقتية ✓ **")
            else:
                await zedevent.edit(f"**⎉╎ حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(baqir)
        except Exception as exc:
            await event.edit(f"**خـطأ : **\n`{exc}`")
            if os.path.exists(baqir):
                os.remove(baqir)
    else:
        await event.edit("**⎉╎ يُرجى الرد على الصورة لطفًا**")




# Copyright (C) 2022 Tepthon . All Rights Reserved
@zedub.zed_cmd(pattern="اوامر الفارات")
async def cmd(baqir):
    await edit_or_reply(baqir, BaqirVP_cmd)

@zedub.zed_cmd(pattern="الفارات")
async def cmd(baqir):
    await edit_or_reply(baqir, BaqirVP_cmd)

@zedub.zed_cmd(pattern="اوامر الوقت")
async def cmd(baqir):
    await edit_or_reply(baqir, BaqirTZ_cmd)

@zedub.zed_cmd(pattern="الوقت")
async def cmd(baqir):
    await edit_or_rep# Tepthon
# Copyright (C) 2022 TepthonArabic . All Rights Reserved
#
# This file is a part of < https://github.com/Tepthon-Arabic/TepthonAr/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Tepthon-Arabic/TepthonAr/blob/web/LICENSE/>.

""" وصـف الملـف : اوامـر إضـافة الفـارات باللغـة العربيـة كـاملة ولا حـرف انكلـش🤘 تخمـط اذكـر المصـدر يولـد
إضـافة فـارات صـورة ( الحمايـة - الفحـص - الوقتـي ) بـ امـر واحـد فقـط
حقـوق للتـاريخ : @Tepthon
@E_7_V - كتـابـة الملـف :  بـاقـر"""
#بـاقـر يولـد هههههههههههههههههههههههههه
import asyncio
import math
import os

import heroku3
import requests
import urllib3
import random
import string
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError
from telethon.utils import get_display_name
from urlextract import URLExtract

from . import zedub

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import delete_conv
from ..sql_helper.globals import addgvar, delgvar, gvarstatus

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY
from . import BOTLOG_CHATID, mention


plugin_category = "الادوات"
LOGS = logging.getLogger(__name__)

extractor = URLExtract()


BaqirVP_cmd = (
    "𓆩 [ 𝗧𝗲𝗽𝘁𝗵𝗼𝗻 𝗖𝗼𝗻𝗳𝗶𝗴 𝗩𝗮𝗿𝘀 - اوامـر الفـارات](t.me/Tepthon) 𓆪\n\n"
    "**⎉╎قائـمه اوامر تغييـر فـارات الصـور بأمـر واحـد فقـط - لـ اول مـره ع سـورس تليثـون يوزر بـوت 🦾 :** \n\n"
    "⪼ `.اضف صورة الحماية` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة الفحص` بالـرد ع صـورة او ميديـا\n"
    "⪼ قنـاة كلايـش الفحـص @Tepthon_kalaesh\n\n"
    "⪼ `.اضف صورة الوقتي` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة البوت` بالـرد ع صـورة او ميديـا لـ إضـافة صـورة ستـارت للبـوت\n\n"
    "⪼ `.اضف صورة الحظر` بالـرد ع صـورة او ميديـا لـ إضـافة صـورة لـ كليشـة الحظـر\n\n"
    "⪼ `.اضف صورة الكتم` بالـرد ع صـورة او ميديـا لـ إضـافة صـورة لـ كليشـة الكتـم\n\n"
    "⪼ `.اضف صورة البلوك` بالـرد ع صـورة او ميديـا لـ إضـافة صـورة لـ كليشـة حظـر الخـاص\n\n"
    "⪼ `.اوامر الفارات` لعـرض بقيـة اوامـر الفـارات\n\n\n"
    "**⎉╎قائـمه اوامر تغييـر كليشـة الايـدي :** \n\n"
    "⪼ `.اضف فار ايموجي الايدي` بالـرد ع الرمـز او الايموجـي\n\n"
    "⪼ `.اضف فار عنوان الايدي` بالـرد ع نـص العنـوان\n\n"
    "⪼ `.اضف فار خط الايدي` بالـرد ع الخـط او المستقيـم\n\n"
    "⪼ `.اضف كليشة الايدي` بالـرد ع الكليشـه مـن القنـاة @Tepthon_kalaesh\n\n\n"
    "**⎉╎قائـمه اوامر تغييـر بقيـة الفـارات بأمـر واحـد فقـط :** \n\n"
    "⪼ `.اضف فار كليشة الحماية` بالـرد ع الكليشـة\n"
    "⪼ `.اضف فار كليشة البلوك` بالـرد ع الكليشـة لتغييـر كليشة الحظر خاص\n"
    "⪼ قنـاة كلايـش حمايـة الخـاص @Tepthon_kalaesh\n\n"
    "⪼ `.اضف فار كليشة الفحص` بالـرد ع الكليشـة\n"
    "⪼ قنـاة كلايـش الفحـص @Tepthon_kalaesh\n\n"
    "⪼ `.اضف فار كليشة البوت` بالـرد ع الكليشـة لـ إضـافة كليشـة ستـارت\n\n"
    "⪼ `.اضف فار زر الستارت` بالـرد ع يوزرك او يوزر قناتك لـ إضـافة زر الستـارت\n\n"
    "⪼ `.اضف فار رمز الوقتي` بالـرد ع رمـز\n\n"
    "⪼ `.اضف فار زخرفة الوقتي` بالـرد ع ارقـام الزغـرفه\n\n"
    "⪼ `.اضف فار البايو الوقتي` بالـرد ع البـايـو\n\n"
    "⪼ `.اضف فار اسم المستخدم` بالـرد ع اسـم\n\n"
    "⪼ `.اضف فار كروب الرسائل` بالـرد ع ايدي الكـروب\n\n"
    "⪼ `.اضف فار كروب السجل` بالـرد ع ايدي الكـروب\n\n"
    "⪼ `.اضف فار ايديي` بالـرد ع ايدي حسـابك\n\n"
    "⪼ `.اضف فار نقطة الاوامر` بالـرد ع الـرمز الجديـد\n\n"
    "⪼ `.اضف فار نوم الترحيب` بالـرد ع رقـم الساعة لبداية نوم الترحيب المؤقت\n\n"
    "⪼ `.اضف فار ثواني لانهائي` بالـرد ع رقـم لعـدد الثوانـي الفاصـله بيـن كل عمليـة تجميـع فـي الامـر لانهائـي\n\n"
    "⪼ `.اضف فار رسائل الحماية` بالـرد ع رقـم لعدد رسائل تحذيـرات حماية الخاص\n\n\n"
    "⪼ `.جلب فار` + اسـم الفـار\n\n"
    "⪼ `.حذف فار` + اسـم الفـار\n\n"
    "⪼ `.رفع مطور` بالـرد ع الشخـص لرفعـه مطـور تحكـم كامـل بالاوامـر\n\n"
    "⪼ `.حذف فار المطورين`\n\n"
    "⪼ `.الوقت` لـ عـرض قائمـة اوامـر تغييـر الوقت حسب دولتك\n\n"
    "\n𓆩 [𝗧𝗲𝗽𝘁𝗵𝗼𝗻 𝗩𝗮𝗿𝘀 - قنـاة الفـارات](t.me/Tepthone1) 𓆪"
)


BaqirTZ_cmd = (
    "𓆩 [𝗧𝗲𝗽𝘁𝗵𝗼𝗻 𝗖𝗼𝗻𝗳𝗶𝗴 - اوامـر الوقت](t.me/Tepthon) 𓆪\n\n"
    "**⎉╎قائـمه اوامر تغييـر المنطقـة الزمنيـة للوقـت 🌐:** \n\n"
    "⪼ `.وقت اليمن` \n\n"
    "⪼ `.وقت العراق` \n\n"
    "⪼ `.وقت السعودية` \n\n"
    "⪼ `.وقت سوريا` \n\n"
    "⪼ `.وقت مصر` \n\n"
    "⪼ `.وقت السودان` \n\n"
    "⪼ `.وقت ليبيا` \n\n"
    "⪼ `.وقت الامارات` \n\n"
    "⪼ `.وقت ايران` \n\n"
    "⪼ `.وقت الجزائر` \n\n"
    "⪼ `.وقت المغرب` \n\n"
    "⪼ `.وقت تركيا` \n\n"
    "⪼ `.وقت ماليزيا` \n\n"
    "⪼ `.وقت روسيا` \n\n"
    "⪼ `.وقت ايطاليا` \n\n"
    "⪼ `.وقت امريكا` \n\n"
    "⪼ `.وقت المانيا` \n\n"
    "🛃 سيتـم إضـافة المزيـد من الدول قريبـًـا\n\n"
    "\n𓆩 [𝗧𝗲𝗽𝘁𝗵𝗼𝗻 𝗩𝗮𝗿𝘀 - قنـاة الفـارات](t.me/Tepthone1) 𓆪"
)


# Copyright (C) 2022 Tepthon . All Rights Reserved
@zedub.zed_cmd(pattern=r"اضف فار (.*)")
async def variable(event):
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    vinfo = reply.text
    rep = await edit_or_reply(event, "**⎉╎جـاري إضـافة الفـار إلـى بـوتك ...**")
    # All Rights Reserved for "Tepthon" "باقر"
    if input_str == "كليشة الفحص" or input_str == "كليشه الفحص":
        variable = "ALIVE_TEMPLATE"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_TEMPLATE") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.فحص` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.فحص` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("ALIVE_TEMPLATE", vinfo)
    elif input_str == "كليشة الحماية" or input_str == "كليشه الحمايه" or input_str == "كليشه الحماية" or input_str == "كليشة الحمايه":
        variable = "pmpermit_txt"
        await asyncio.sleep(1.5)
        if gvarstatus("pmpermit_txt") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.الحمايه تفعيل` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.الحمايه تفعيل` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("pmpermit_txt", vinfo)
    elif input_str == "كليشة الايدي" or input_str == "كليشه الايدي":
        variable = "RID_TEMPLATE"
        await asyncio.sleep(1.5)
        if gvarstatus("RID_TEMPLATE") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.ايدي` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.ايدي` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("RID_TEMPLATE", vinfo)
    elif input_str == "كليشة البوت" or input_str == "كليشه البوت" or input_str == "ستارت البوت" or input_str == "كليشة الستارت" or input_str == "كليشه الستارت" or input_str == "كليشة البدء":
        variable = "START_TEXT"
        await asyncio.sleep(1.5)
        if gvarstatus("START_TEXT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الآن قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("START_TEXT", vinfo)
    elif input_str == "زر البوت" or input_str == "زر الستارت" or input_str == "زر ستارت":
        variable = "START_BUTUN"
        await asyncio.sleep(1.5)
        if not vinfo.startswith("@"):
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع يـوزر فقـط**")
        vinfo = vinfo.zedlace("@", "")
        if gvarstatus("START_TEXT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎رابـط زر كليشـة الستـارت الجـديـد** \nhttps://t.me/{} \n\n**⎉╎الآن قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎رابـط زر كليشـة الستـارت الجـديـد** \nhttps://t.me/{} \n\n**⎉╎الآن قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("START_BUTUN", vinfo)
    elif input_str == "كليشة التوديع" or input_str == "كليشه التوديع" or input_str == "كليشة البلوك" or input_str == "كليشه البلوك":
        variable = "pmblock"
        await asyncio.sleep(1.5)
        if gvarstatus("pmblock") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ تفعيـل حماية الخاص عبر الأمر ↶** ( `الحماية تفعيل` ) **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ تفعيـل حماية الخاص عبر الأمر ↶** ( `الحماية تفعيل` ) **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("pmblock", vinfo)
    elif input_str == "رمز الوقتي" or input_str == "رمز الاسم الوقتي":
        variable = "CUSTOM_ALIVE_EMREP"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_EMREP") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الـرمـز الجـديـد** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.الاسم تلقائي` **لـ التحقـق مـن الـرمز . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎الـرمـز المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.الاسم تلقائي` **لـ التحقـق مـن الـرمز . .**".format(input_str, vinfo))
    elif input_str == "البايو" or input_str == "البايو الوقتي" or input_str == "النبذه" or input_str == "البايو تلقائي":
        variable = "DEFAULT_BIO"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_BIO") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎البـايـو الجـديـد** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.البايو تلقائي` **لـ التحقـق مـن البايـو . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضـافه {} بنجـاح ☑️**\n**⎉╎البـايـو المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.البايو تلقائي` **لـ التحقـق مـن البايـو . .**".format(input_str, vinfo))
    elif input_str == "التحقق" or input_str == "كود التحقق" or input_str == "التحقق بخطوتين" or input_str == "تحقق":
        variable = "TG_2STEP_VERIFICATION_CODE"
        await asyncio.sleep(1.5)
        if gvarstatus("TG_2STEP_VERIFICATION_CODE") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎كـود التحـقق بخطـوتيـن** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.تحويل ملكية` **ثم معـرف الشخـص داخـل الكـروب او القنـاة . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎كـود التحـقق بخطـوتيـن** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.تحويل ملكية` **ثم معـرف الشخـص داخـل الكـروب او القنـاة . .**".format(input_str, vinfo))
    elif input_str == "كاشف الاباحي" or input_str == "كشف الاباحي":
        variable = "DEEP_API"
        await asyncio.sleep(1.5)
        if gvarstatus("DEEP_API") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر توكـن {} بنجـاح ☑️**\n**⎉╎التوكـن الجـديـد** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.قفل الاباحي` **لـ تفعيـل كاشـف الاباحي . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة توكـن {} بنجـاح ☑️**\n**⎉╎التوكـن المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.قفل الاباحي` **لـ تفعيـل كاشـف الاباحي . .**".format(input_str, vinfo))
    elif input_str == "ايموجي الايدي" or input_str == "ايموجي ايدي" or input_str == "رمز الايدي" or input_str == "رمز ايدي" or input_str == "الرمز ايدي":
        variable = "CUSTOM_ALIVE_EMOJI"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_EMOJI") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        addgvar("CUSTOM_ALIVE_EMOJI", vinfo)
    elif input_str == "عنوان الايدي" or input_str == "عنوان ايدي":
        variable = "CUSTOM_ALIVE_TEXT"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_TEXT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        addgvar("CUSTOM_ALIVE_TEXT", vinfo)
    elif input_str == "خط الايدي" or input_str == "خط ايدي" or input_str == "خطوط الايدي" or input_str == "خط ايدي":
        variable = "CUSTOM_ALIVE_FONT"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_FONT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        addgvar("CUSTOM_ALIVE_FONT", vinfo)
    elif input_str == "اشتراك الخاص" or input_str == "اشتراك خاص":
        variable = "Custom_Pm_Channel"
        await asyncio.sleep(1.5)
        if gvarstatus("Custom_Pm_Channel") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.اشتراك خاص`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.اشتراك خاص`".format(input_str, vinfo))
        delgvar("Custom_Pm_Channel")
        addgvar("Custom_Pm_Channel", vinfo)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#قنـاة_الاشتـراك_الاجبـاري_للخـاص\
                        \n**- القنـاة {input_str} تم إضافتهـا في قاعده البيانات ..بنجـاح ✓**",
            )
    elif input_str == "اشتراك كروب" or input_str == "اشتراك الكروب":
        variable = "Custom_G_Channel"
        await asyncio.sleep(1.5)
        if gvarstatus("Custom_G_Channel") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.اشتراك كروب`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.اشتراك كروب`".format(input_str, vinfo))
        delgvar("Custom_G_Channel")
        addgvar("Custom_G_Channel", vinfo)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#قنـاة_الاشتـراك_الاجبـاري_للكـروب\
                        \n**- القنـاة {input_str} تم إضافتهـا في قاعده البيانات ..بنجـاح ✓**",
            )
    elif input_str == "زاجل" or input_str == "قائمة زاجل" or input_str == "قائمه زاجل" or input_str == "يوزرات":
        variable = "ZAGL_Rep"
        await asyncio.sleep(1.5)
        if gvarstatus("ZAGL_Rep") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎اليـوزرات المضـافة** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.زاجل` **بالـرد ع نـص او ميديـا بنـص . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎اليـوزرات المضـافة** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.زاجل` **بالـرد ع نـص او ميديـا بنـص . .**".format(input_str, vinfo))
    elif input_str == "سوبر" or input_str == "قائمة السوبر" or input_str == "قائمه السوبر" or input_str == "السوبرات" or input_str == "السوبر":
        variable = "Super_Id"
        await asyncio.sleep(1.5)
        if not vinfo.startswith("-100"):
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع ارقـام ايديات المجموعات التي تبدأ ب 100- فقـط ؟!**\n**⎉╎قم بالذهاب لمجموعات السوبر التي تريد النشر فيها وكتابة الأمر (.الايدي) ثم خذ ايدي المجموعة وهكذا لبقية المجموعات**")
        if gvarstatus("Super_Id") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎الايديات المضـافة** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** (`.سوبر` + عدد الثواني + عدد مرات التكرار)**بالـرد ع نـص او ميديـا بنـص . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الايديات المضـافة** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** (`.سوبر` + عدد الثواني + عدد مرات التكرار)**بالـرد ع نـص او ميديـا بنـص . .**".format(input_str, vinfo))
    elif input_str == "بوت التجميع" or input_str == "بوت النقاط" or input_str == "النجميع" or input_str == "النقاط":
        variable = "R_Point"
        await asyncio.sleep(1.5)
        if gvarstatus("R_Point") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎البـوت المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.تجميع` **لـ البـدء بتجميـع النقـاط من البـوت الجـديـد . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضـافه {} بنجـاح ☑️**\n**⎉╎البـوت المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.تجميع` **لـ البـدء بتجميـع النقـاط من البـوت الجـديـد . .**".format(input_str, vinfo))
    elif input_str == "اسم المستخدم" or input_str == "الاسم":
        variable = "ALIVE_NAME"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_NAME") is not None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        addgvar(variable, vinfo)

    elif input_str == "رسائل الحماية" or input_str == "رسائل الحمايه" or input_str == "رسائل الخاص" or input_str == "رسائل حماية الخاص" or input_str == "عدد التحذيرات":
        variable = "MAX_FLOOD_IN_PMS"
        await asyncio.sleep(1.5)
        if vinfo.isdigit():
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع رقـم فقـط ؟!**")
        addgvar("MAX_FLOOD_IN_PMS", vinfo)

    elif input_str == "كود تيرمكس" or input_str == "كود السيشن" or input_str == "كود سيشن":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "STRING_SESSION"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo

    elif input_str == "كروب الرسائل" or input_str == "كروب التخزين" or input_str == "كروب الخاص":
        variable = "PM_LOGGER_GROUP_ID"
        await asyncio.sleep(1.5)
        if gvarstatus("PM_LOGGER_GROUP_ID") is not None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        addgvar("PM_LOGGER_GROUP_ID", vinfo)
    elif input_str == "السجل" or input_str == "كروب السجل":
        variable = "PRIVATE_GROUP_BOT_API_ID"
        await asyncio.sleep(1.5)
        if gvarstatus("PRIVATE_GROUP_BOT_API_ID") is not None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        addgvar("PRIVATE_GROUP_BOT_API_ID", vinfo)
    elif input_str == "السجل 2" or input_str == "كروب السجل 2":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "PRIVATE_GROUP_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "قناة السجل" or input_str == "قناة السجلات":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "PRIVATE_CHANNEL_BOT_API_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "قناة الملفات" or input_str == "قناة الإضافات":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "PLUGIN_CHANNEL"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "ايديي" or input_str == "ايدي الحساب":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "OWNER_ID"
        await asyncio.sleep(1.5)
        if vinfo.isdigit():
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع رقـم فقـط ؟!**")
        heroku_var[variable] = vinfo
    elif input_str == "نقطة الاوامر" or input_str == "نقطه الاوامر":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "COMMAND_HAND_LER"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "التوكن" or input_str == "توكن البوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TG_BOT_TOKEN"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "معرف البوت" or input_str == "معرف بوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TG_BOT_USERNAME"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "الريبو" or input_str == "السورس":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه ريندر 🔄**")
        variable = "UPSTREAM_REPO"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "توكن المكافح" or input_str == "كود المكافح" or input_str == "مكافح التخريب" or input_str == "مكافح التفليش":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "SPAMWATCH_API"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "توكن الذكاء" or input_str == "مفتاح الذكاء" or input_str == "الذكاء":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "OPENAI_API_KEY"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "ايقاف الترحيب" or input_str == "نوم الترحيب":
        variable = "TIME_STOP"
        await asyncio.sleep(1.5)
        if vinfo.isdigit():
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع رقـم فقـط ؟!**")
        addgvar("TIME_STOP", vinfo)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#فتـرة_الايقـاف_المـؤقت_للترحيب\
                        \n**- تم إضافة الفتـرة من الساعة {vinfo} إلى الساعة 6 صباحـًـا .. بنجـاح ✓**",
            )
    elif input_str == "ثواني لانهائي" or input_str == "ثواني التجميع" or input_str == "عدد لانهائي":
        variable = "SEC_LAN"
        await asyncio.sleep(1.5)
        if vinfo.isdigit():
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎الثوانـي الجـديـدة** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.لانهائي` **+ اسم بوت التجميـع لـ البـدء بالتجميـع اللانهائـي . .**".format(input_str, vinfo))
        else:
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع رقـم فقـط ؟!**")
        addgvar(variable, vinfo)
    elif ("صورة" in input_str) or ("صوره" in input_str):
        return await zed.edit("**⎉╎لـ إضافة صور الكلايش ..**\n**⎉╎استخدم الأمر (اضف) مباشرة بدون كلمة فار**")
    else:
        if input_str:
            return await zed.edit("**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))
        return await edit_or_reply(event, "**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))


# Copyright (C) 2022 TepthonArabic . All Rights Reserved
@zedub.zed_cmd(pattern="حذف فار(?:\\s|$)([\\s\\S]*)")
async def variable(event):
    input_str = event.text[9:]
    if (input_str == "من" or input_str == "إلى" or input_str == "الترحيب") or "رسائلي" in input_str or "رسائله" in input_str:
        return
    rep = await edit_or_reply(event, "**⎉╎جـاري حـذف الفـار مـن بـوتك 🚮...**")
    # All Rights Reserved for "Tepthon" "باقر"
    if input_str == "كليشة الفحص" or input_str == "كليشه الفحص":
        variable = gvarstatus("ALIVE_TEMPLATE")
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_TEMPLATE") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("ALIVE_TEMPLATE")
        
    elif input_str == "كليشة الحماية" or input_str == "كليشه الحمايه" or input_str == "كليشه الحماية" or input_str == "كليشة الحمايه":
        variable = gvarstatus("pmpermit_txt")
        await asyncio.sleep(1.5)
        if gvarstatus("pmpermit_txt") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("pmpermit_txt")

    elif input_str == "كليشة البوت" or input_str == "كليشه البوت":
        variable = gvarstatus("START_TEXT")
        await asyncio.sleep(1.5)
        if gvarstatus("START_TEXT") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("START_TEXT")

    elif input_str == "زر البوت" or input_str == "زر الستارت" or input_str == "زر ستارت":
        variable = gvarstatus("START_BUTUN")
        await asyncio.sleep(1.5)
        if gvarstatus("START_BUTUN") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("START_BUTUN")

    elif input_str == "كليشة التوديع" or input_str == "كليشه التوديع" or input_str == "كليشة البلوك" or input_str == "كليشه البلوك":
        variable = gvarstatus("pmblock")
        await asyncio.sleep(1.5)
        if gvarstatus("pmblock") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت زد ثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("pmblock")

    elif input_str == "كليشة الايدي" or input_str == "كليشه الايدي":
        variable = "RID_TEMPLATE"
        await asyncio.sleep(1.5)
        if gvarstatus("RID_TEMPLATE") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("RID_TEMPLATE")

    elif input_str == "صورة الفحص" or input_str == "صوره الفحص":
        variable = "ALIVE_PIC"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_PIC") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("ALIVE_PIC")

    elif input_str == "صورة الاوامر" or input_str == "صوره الاوامر":
        variable = "CMD_PIC"
        await asyncio.sleep(1.5)
        if gvarstatus("CMD_PIC") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("CMD_PIC")

    elif input_str == "صورة السورس" or input_str == "صوره السورس":
        variable = "ALIVE_PIC"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_PIC") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("ALIVE_PIC")

    elif input_str == "صورة الكتم" or input_str == "صوره الكتم":
        variable = "PC_MUTE"
        await asyncio.sleep(1.5)
        if gvarstatus("PC_MUTE") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("PC_MUTE")

    elif input_str == "صورة الحظر" or input_str == "صوره الحظر":
        variable = "PC_BANE"
        await asyncio.sleep(1.5)
        if gvarstatus("PC_BANE") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("PC_BANE")

    elif input_str == "صورة البلوك" or input_str == "صوره البلوك":
        variable = "PC_BLOCK"
        await asyncio.sleep(1.5)
        if gvarstatus("PC_BLOCK") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("PC_BLOCK")

    elif input_str == "صورة البوت" or input_str == "صوره البوت" or input_str == "صورة الستارت" or input_str == "صوره الستارت" or input_str == "صورة ستارت" or input_str == "صوره ستارت":
        variable = "BOT_START_PIC"
        await asyncio.sleep(1.5)
        if gvarstatus("BOT_START_PIC") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("BOT_START_PIC")

    elif input_str == "صورة الحماية" or input_str == "صوره الحمايه" or input_str == "صورة الحمايه" or input_str == "صوره الحماية":
        variable = "pmpermit_pic"
        await asyncio.sleep(1.5)
        if gvarstatus("pmpermit_pic") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        delgvar("pmpermit_pic")
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))

    elif input_str == "صورة الوقتي" or input_str == "صوره الوقتي":
        variable = gvarstatus("DIGITAL_PIC")
        await asyncio.sleep(1.5)
        if gvarstatus("DIGITAL_PIC") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("DIGITAL_PIC")

    elif input_str == "رمز الوقتي" or input_str == "رمز الاسم الوقتي":
        variable = "CUSTOM_ALIVE_EMREP"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_EMREP") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        delgvar("CUSTOM_ALIVE_EMREP")
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
    elif input_str == "زخرفه الوقتي" or input_str == "زخرفة الوقتي":
        variable = "BA_FN"
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        delgvar(variable)
    elif input_str == "رسائل الحماية" or input_str == "رسائل الحمايه" or input_str == "رسائل الخاص" or input_str == "رسائل حماية الخاص" or input_str == "عدد التحذيرات":
        variable = "MAX_FLOOD_IN_PMS"
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        delgvar(variable)
    elif input_str == "البايو" or input_str == "البايو الوقتي" or input_str == "النبذه الوقتيه":
        variable = "DEFAULT_BIO"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_BIO") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        delgvar("DEFAULT_BIO")
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
    elif input_str == "اسم المستخدم" or input_str == "الاسم":
        variable = "ALIVE_NAME"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_NAME") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        delgvar(variable)
    elif input_str == "كروب الرسائل" or input_str == "كروب التخزين" or input_str == "كروب الخاص":
        variable = "PM_LOGGER_GROUP_ID"
        await asyncio.sleep(1.5)
        if gvarstatus("PM_LOGGER_GROUP_ID") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        delgvar(variable)

    elif input_str == "السجل" or input_str == "كروب السجل":
        variable = "PRIVATE_GROUP_BOT_API_ID"
        await asyncio.sleep(1.5)
        if gvarstatus("PRIVATE_GROUP_BOT_API_ID") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        delgvar(variable)

    elif input_str == "السجل 2" or input_str == "كروب السجل 2":
        variable = "PRIVATE_GROUP_ID"
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "قناة السجل" or input_str == "قناة السجلات":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "PRIVATE_CHANNEL_BOT_API_ID"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "قناة الملفات" or input_str == "قناة الإضافات":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "PLUGIN_CHANNEL"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "التحقق" or input_str == "كود التحقق":
        variable = "TG_2STEP_VERIFICATION_CODE"
        await asyncio.sleep(1.5)
        if gvarstatus("TG_2STEP_VERIFICATION_CODE") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        delgvar("TG_2STEP_VERIFICATION_CODE")
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))

    elif input_str == "ايديي" or input_str == "ايدي الحساب":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "OWNER_ID"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "نقطة الاوامر" or input_str == "نقطه الاوامر":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه ريندر 🔄**")
        variable = "COMMAND_HAND_LER"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "التوكن" or input_str == "توكن البوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TG_BOT_TOKEN"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "معرف البوت" or input_str == "معرف بوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TG_BOT_USERNAME"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "الريبو" or input_str == "السورس":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "UPSTREAM_REPO"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "اسمي التلقائي" or input_str == "الاسم التلقاائي":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "AUTONAME"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]
    elif input_str == "ايموجي الايدي" or input_str == "ايموجي ايدي" or input_str == "رمز الايدي" or input_str == "رمز ايدي" or input_str == "الرمز ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_EMOJI")
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("CUSTOM_ALIVE_EMOJI")
    elif input_str == "عنوان الايدي" or input_str == "عنوان ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_TEXT")
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("CUSTOM_ALIVE_TEXT")
    elif input_str == "خط الايدي" or input_str == "خط ايدي" or input_str == "خطوط الايدي" or input_str == "خط ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_FONT")
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("CUSTOM_ALIVE_FONT")
    elif input_str == "كاشف الاباحي" or input_str == "كشف الاباحي":
        variable = gvarstatus("DEEP_API")
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("DEEP_API")
    elif input_str == "ايقاف الترحيب" or input_str == "نوم الترحيب":
        variable = "TIME_STOP"
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("TIME_STOP")
    elif input_str == "ثواني لانهائي" or input_str == "ثواني التجميع" or input_str == "عدد لانهائي":
        variable = "SEC_LAN"
        await asyncio.sleep(1.5)
        if gvarstatus("SEC_LAN") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("SEC_LAN")
    else:
        if input_str:
            return await zed.edit("**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))
        return await edit_or_reply(event, "**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))


# Copyright (C) 2022 TepthonArabic . All Rights Reserved
@zedub.zed_cmd(pattern="جلب فار(?:\\s|$)([\\s\\S]*)")
async def custom_rep(event):
    input_str = event.text[9:]
    rep = await edit_or_reply(event, "**⎉╎جــاري جلـب معلـومـات الفــار 🛂. . .**")
    if (input_str == "كليشة الحماية" or input_str == "كليشة الحمايه" or input_str == "كليشه الحماية" or input_str == "كليشه الحمايه"):
        variable = gvarstatus("pmpermit_txt")
        if variable is None:
            await zed.edit("**⎉╎فـار كليشـة الحمايـة غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكليشـة استخـدم الامـر : ↶**\n `.اضف فار كليشة الحماية` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))
            
    elif input_str == "كليشة الفحص" or input_str == "كليشه الفحص":
        variable = gvarstatus("ALIVE_TEMPLATE")
        if variable is None:
            await zed.edit("**⎉╎فـار كليشـة الفحص غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكليشـة استخـدم الامـر : ↶**\n `.اضف فار كليشة الفحص` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "كليشة البوت" or input_str == "كليشه البوت":
        variable = gvarstatus("START_TEXT")
        if variable is None:
            await zed.edit("**⎉╎فـار كليشـة البـوت غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكليشـة استخـدم الامـر : ↶**\n `.اضف فار كليشة البوت` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "زر البوت" or input_str == "زر الستارت" or input_str == "زر ستارت":
        variable = gvarstatus("START_BUTUN")
        if variable is None:
            await zed.edit("**⎉╎فـار زر كليشـة ستـارت البـوت غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع يـوزرك او يـوزر قناتـك استخـدم الامـر : ↶**\n `.اضف فار زر الستارت` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n https://t.me/{}\n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "كليشة التوديع" or input_str == "كليشه التوديع" or input_str == "كليشة البلوك" or input_str == "كليشه البلوك":
        variable = gvarstatus("pmblock")
        if variable is None:
            await zed.edit("**⎉╎فـار كليشـة الحظـر غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكليشـة استخـدم الامـر : ↶**\n `.اضف فار كليشة الحظر` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "رمز الوقتي" or input_str == "رمز الاسم الوقتي":
        variable = gvarstatus("CUSTOM_ALIVE_EMREP")
        if variable is None:
            await zed.edit("**⎉╎فـار رمـز الوقتـي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز استخـدم الامـر : ↶**\n `.اضف فار رمز الوقتي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "التحقق" or input_str == "كود التحقق":
        variable = gvarstatus("TG_2STEP_VERIFICATION_CODE")
        if variable is None:
            await zed.edit("**⎉╎فـار التحقق بخطوتين غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز استخـدم الامـر : ↶**\n `.اضف فار التحقق`  **بالـرد ع كـود التحـقق**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "كاشف الاباحي" or input_str == "كشف الاباحي":
        variable = gvarstatus("DEEP_API")
        if variable is None:
            await zed.edit("**⎉╎فـار كشـف الاباحي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكـود استخـدم الامـر : ↶**\n `.اضف فار كاشف الاباحي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "البايو" or input_str == "البايو الوقتي" or input_str == "النبذه" or input_str == "البايو تلقائي":
        variable = gvarstatus("DEFAULT_BIO")
        if variable is None:
            await zed.edit("**⎉╎فـار البايـو الوقتـي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع نـص استخـدم الامـر : ↶**\n `.اضف فار البايو` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "اسم المستخدم" or input_str == "الاسم":
        variable = gvarstatus("ALIVE_NAME")
        if gvarstatus("ALIVE_NAME") is None:
            await zed.edit("**⎉╎فـار اسـم المستخـدم غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الاسم استخـدم الامـر : ↶**\n `.اضف فار اسم المستخدم` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "كود تيرمكس" or input_str == "كود السيشن" or input_str == "كود سيشن":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "STRING_SESSION"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار اسـم المستخـدم غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الاسم استخـدم الامـر : ↶**\n `.اضف فار اسم المستخدم` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "ايديي" or input_str == "ايدي الحساب":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "OWNER_ID"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار ايـدي الحسـاب غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الايـدي فقـط استخـدم الامـر : ↶**\n `.اضف فار ايدي الحساب` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "نقطة الاوامر" or input_str == "نقطه الاوامر":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "COMMAND_HAND_LER"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار نقطـة الاوامـر غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز فقـط استخـدم الامـر : ↶**\n `.اضف فار نقطة الاوامر` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "التوكن" or input_str == "توكن البوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TG_BOT_TOKEN"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار توكـن البـوت غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع التوكـن فقـط استخـدم الامـر : ↶**\n `.اضف فار التوكن` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "معرف البوت" or input_str == "معرف بوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "APP_USERNAME"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار معرف البوت غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع المعرف استخـدم الامـر : ↶**\n `.اضف فار معرف البوت` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "الريبو" or input_str == "السورس":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "UPSTREAM_REPO"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار الريبـو غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع رابط السورس الرسمي استخـدم الامـر : ↶**\n `.اضف فار الريبو` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "اسمي التلقائي" or input_str == "الاسم التلقاائي":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "AUTONAME"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار الاسـم التلقائي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الاسم استخـدم الامـر : ↶**\n `.اضف فار اسمي التلقائي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الحماية" or input_str == "صوره الحمايه" or input_str == "صورة الحمايه" or input_str == "صوره الحماية":
        variable = gvarstatus("pmpermit_pic")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الحمايـة غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الحماية` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الوقتي" or input_str == "صوره الوقتي":
        variable = gvarstatus("DIGITAL_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الوقتـي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الوقتي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الفحص" or input_str == "صوره الفحص":
        variable = gvarstatus("ALIVE_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الفحص غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الفحص` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة البوت" or input_str == "صوره البوت" or input_str == "صورة الستارت" or input_str == "صوره الستارت" or input_str == "صورة ستارت" or input_str == "صوره ستارت":
        variable = gvarstatus("BOT_START_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة ستـارت البـوت غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة البوت` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الاوامر" or input_str == "صوره الاوامر":
        variable = gvarstatus("CMD_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الاوامـر غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الاوامر` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة السورس" or input_str == "صوره السورس":
        variable = gvarstatus("ALIVE_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة السـورس غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة السورس` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الكتم" or input_str == "صوره الكتم":
        variable = gvarstatus("PC_MUTE")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الكتم غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الكتم` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الحظر" or input_str == "صوره الحظر":
        variable = gvarstatus("PC_BANE")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الحظر غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الحظر` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة البلوك" or input_str == "صوره البلوك":
        variable = gvarstatus("PC_BLOCK")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة البلوك غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة البلوك` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "زخرفة الوقتي" or input_str == "زخرفه الوقتي":
        variable = gvarstatus("NA_FN")
        if variable is None:
            await zed.edit("**⎉╎فـار زخرفـة الاسـم الوقتي غيـر موجـود ❌**\n**⎉╎لـ إضـافته فقـط استخـدم الامـر : ↶**\n `.الوقتي 1` إلـى `.الوقتي 14` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "رسائل الحماية" or input_str == "رسائل الحمايه" or input_str == "رسائل الخاص" or input_str == "رسائل حماية الخاص" or input_str == "عدد التحذيرات":
        variable = gvarstatus("MAX_FLOOD_IN_PMS")
        if variable is None:
            await zed.edit("**⎉╎فـار رسـائل الحمايـة غيـر موجـود ❌**\n**⎉╎لـ إضـافته فقـط استخـدم الامـر : ↶**\n `.اضف فار رسائل الحماية` بالـرد ع عـدد فقـط \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "زخرفة الوقتية" or input_str == "زخرفه الوقتيه" or input_str == "زخرفة الوقتيه" or input_str == "زخرفه الوقتية":
        variable = gvarstatus("DEFAULT_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار زخرفـة الصـورة الوقتيـة غيـر موجـود ❌**\n**⎉╎لـ إضـافته فقـط استخـدم الامـر : ↶**\n `.وقتي 1` إلـى `.وقتي 17` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "الوقت" or input_str == "الساعه" or input_str == "المنطقه الزمنيه":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TZ"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار المنطقـة الزمنيــــة غيـر موجـود ❌**\n**⎉╎لـ إضـافته فقـط استخـدم الامـر : ↶**\n `.وقت` واسـم الدولـة \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "كليشة الايدي" or input_str == "كليشه الايدي":
        variable = gvarstatus("RID_TEMPLATE")
        if variable is None:
            await zed.edit("**⎉╎فـار ايموجي/رمز الايدي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكليشـة من هنا ( @Tepthon_kalaesh ) استخـدم الامـر : ↶**\n `.اضف كليشة الايدي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "ايموجي الايدي" or input_str == "ايموجي ايدي" or input_str == "رمز الايدي" or input_str == "رمز ايدي" or input_str == "الرمز ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_EMOJI")
        if variable is None:
            await zed.edit("**⎉╎فـار ايموجي/رمز الايدي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز استخـدم الامـر : ↶**\n `.اضف فار رمز الايدي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))
            
    elif input_str == "عنوان الايدي" or input_str == "عنوان ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_TEXT")
        if variable is None:
            await zed.edit("**⎉╎فـار نص عنـوان كليشـة الايـدي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز استخـدم الامـر : ↶**\n `.اضف فار عنوان الايدي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "خط الايدي" or input_str == "خط ايدي" or input_str == "خطوط الايدي" or input_str == "خط ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_FONT")
        if variable is None:
            await zed.edit("**⎉╎فـار خطـوط كليشـة الايـدي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز استخـدم الامـر : ↶**\n `.اضف فار خطوط الايدي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "لاعب 1":
        variable = gvarstatus("R_AK")
        if gvarstatus("R_AK") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "لاعب 2":
        variable = gvarstatus("R_A2K")
        if gvarstatus("R_A2K") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "لاعب 3":
        variable = gvarstatus("R_A3K")
        if gvarstatus("R_A3K") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "لاعب 4":
        variable = gvarstatus("R_A4K")
        if gvarstatus("R_A4K") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "لاعب 5":
        variable = gvarstatus("R_A5K")
        if gvarstatus("R_A5K") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "توكن المكافح" or input_str == "كود المكافح" or input_str == "مكافح التخريب" or input_str == "مكافح التفليش":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "SPAMWATCH_API"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار توكـن المكـافح غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "اشتراك خاص" or input_str == "اشتراك الخاص" or input_str == "قناة الاشتراك" or input_str == "الاشتراك":
        variable = gvarstatus("Custom_Pm_Channel")
        if gvarstatus("Custom_Pm_Channel") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "اشتراك كروب" or input_str == "اشتراك الكروب" or input_str == "قناة الاشتراك" or input_str == "الاشتراك":
        variable = gvarstatus("Custom_G_Channel")
        if gvarstatus("Custom_G_Channel") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "االهمسه":
        variable = gvarstatus("hmsa_id")
        if gvarstatus("hmsa_id") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "ثواني لانهائي" or input_str == "ثواني التجميع" or input_str == "عدد لانهائي":
        variable = gvarstatus("SEC_LAN")
        if gvarstatus("SEC_LAN") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    else:
        if input_str:
            return await zed.edit("**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))
        return await edit_or_reply(event, "**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))


# Copyright (C) 2022 TepthonArabic . All Rights Reserved
@zedub.zed_cmd(pattern="وقت(?:\\s|$)([\\s\\S]*)")
async def variable(event):
    input_str = event.text[5:]
    viraq = "Asia/Baghdad"
    vmsr = "Africa/Cairo"
    vdubai = "Asia/Dubai"
    vturk = "Europe/Istanbul"
    valgiers = "Africa/Algiers"
    vmoroco = "Africa/Casablanca"
    viran = "Asia/Tehran"
    vsudan = "Africa/Khartoum"
    vitaly = "Europe/Rome"
    vrusia = "Europe/Moscow"
    vamerica = "America/Washington"
    vmalaysia = "Asia/Kuala_Lumpur"
    vdeutschland = "Europe/Berlin"
    rep = await edit_or_reply(event, "**⎉╎جـاري إعــداد المنطقـة الزمنيــــة لـ تيبثـون 🌐...**")
    # All Rights Reserved for "Tepthon" "باقر"
    if input_str == "العراق" or input_str == "اليمن" or input_str == "سوريا" or input_str == "السعودية" or input_str == "لبنان" or input_str == "الاردن":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", viraq)
    elif input_str == "مصر" or input_str == "ليبيا" or input_str == "القاهرة":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", vmsr)
    elif input_str == "دبي" or input_str == "الامارات" or input_str == "عمان" or input_str == "مسقط":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", vdubai)
    elif input_str == "تركيا" or input_str == "اسطنبول" or input_str == "انقرة":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", vturk)
    elif input_str == "تونس" or input_str == "الجزائر":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", valgiers)
    elif input_str == "المغرب" or input_str == "موريتانيا" or input_str == "الدار البيضاء":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", vmoroco)        
    elif input_str == "ايران" or input_str == "طهران":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", viran)
    elif input_str == "السودان":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "Africa/Khartoum")
    elif input_str == "ايطاليا":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "Europe/Rome")
    elif input_str == "روسيا":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "Europe/Moscow")
    elif input_str == "امريكا":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "America/Washington")
    elif input_str == "ماليزيا":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "Asia/Kuala_Lumpur")
    elif input_str == "المانيا":
        variable = "TZ"
        await asyncio.slepp(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "Europe/Berlin")

                
@zedub.zed_cmd(pattern="اضف صورة (الفحص|فحص) ?(.*)")
async def alive_Tepthon(event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        zedevent = await event.edit("**⎉╎ جـار رفع الـصورة إلى أمر الفحص**")
        try:
            baqir = await event.client.download_media(reply)
            if baqir.endswith((".webp")):
                resize_image(baqir)
            with open(baqir, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("ALIVE_PIC", url)
                await zedevent.edit(f"**⎉╎ تم إضافة الصورة إلى الفحص ✓ **")
            else:
                await zedevent.edit(f"**⎉╎ حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(baqir)
        except Exception as exc:
            await event.edit(f"**خـطأ : **\n`{exc}`")
            if os.path.exists(baqir):
                os.remove(baqir)
    else:
        await event.edit("**⎉╎ يُرجى الرد على الصورة لطفًا**")


@zedub.zed_cmd(pattern="اضف صورة (الحمايه|الحماية) ?(.*)")
async def Tepthon(event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        zedevent = await event.edit("**⎉╎ جـار رفع الـصورة إلى أمر الحماية**")
        try:
            baqir = await event.client.download_media(reply)
            if baqir.endswith((".webp")):
                resize_image(baqir)
            with open(baqir, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("pmpermit_pic", url)
                await zedevent.edit(f"**⎉╎ تم إضافة الصورة إلى الحماية ✓ **")
            else:
                await zedevent.edit(f"**⎉╎ حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(baqir)
        except Exception as exc:
            await event.edit(f"**خـطأ : **\n`{exc}`")
            if os.path.exists(baqir):
                os.remove(baqir)
    else:
        await event.edit("**⎉╎ يُرجى الرد على الصورة لطفًا**")


@zedub.zed_cmd(pattern="اضف صورة (الاوامر|اللوحة) ?(.*)")
async def Tepthon(event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        zedevent = await event.edit("**⎉╎ جـار رفع الـصورة إلى أمر لوحة الاوامر**")
        try:
            baqir = await event.client.download_media(reply)
            if baqir.endswith((".webp")):
                resize_image(baqir)
            with open(baqir, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("CMD_PIC", url)
                await zedevent.edit(f"**⎉╎ تم إضافة الصورة إلى لوحة الاوامر ✓ **")
            else:
                await zedevent.edit(f"**⎉╎ حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(baqir)
        except Exception as exc:
            await event.edit(f"**خـطأ : **\n`{exc}`")
            if os.path.exists(baqir):
                os.remove(baqir)
    else:
        await event.edit("**⎉╎ يُرجى الرد على الصورة لطفًا**")


@zedub.zed_cmd(pattern="اضف صورة (البوت|بوت) ?(.*)")
async def Tepthon(event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        zedevent = await event.edit("**⎉╎ جـار رفع الـصورة إلى أمر البوت**")
        try:
            baqir = await event.client.download_media(reply)
            if baqir.endswith((".webp")):
                resize_image(baqir)
            with open(baqir, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("BOT_START_PIC", url)
                await zedevent.edit(f"**⎉╎ تم إضافة الصورة إلى البوت ✓ **")
            else:
                await zedevent.edit(f"**⎉╎ حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(baqir)
        except Exception as exc:
            await event.edit(f"**خـطأ : **\n`{exc}`")
            if os.path.exists(baqir):
                os.remove(baqir)
    else:
        await event.edit("**⎉╎ يُرجى الرد على الصورة لطفًا**")


@zedub.zed_cmd(pattern="اضف صورة (الوقتي|التلقائي|وقتي|البروفايل) ?(.*)")
async def Tepthon(event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        zedevent = await event.edit("**⎉╎ جـار رفع الـصورة إلى أمر الصورة الوقتية**")
        try:
            baqir = await event.client.download_media(reply)
            if baqir.endswith((".webp")):
                resize_image(baqir)
            with open(baqir, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("DIGITAL_PIC", url)
                await zedevent.edit(f"**⎉╎ تم إضافة الصورة إلى امر الصورة الوقتية ✓ **")
            else:
                await zedevent.edit(f"**⎉╎ حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(baqir)
        except Exception as exc:
            await event.edit(f"**خـطأ : **\n`{exc}`")
            if os.path.exists(baqir):
                os.remove(baqir)
    else:
        await event.edit("**⎉╎ يُرجى الرد على الصورة لطفًا**")




# Copyright (C) 2022 Tepthon . All Rights Reserved
@zedub.zed_cmd(pattern="اوامر الفارات")
async def cmd(baqir):
    await edit_or_reply(baqir, BaqirVP_cmd)

@zedub.zed_cmd(pattern="الفارات")
async def cmd(baqir):
    await edit_or_reply(baqir, BaqirVP_cmd)
# Tepthon
# Copyright (C) 2022 TepthonArabic . All Rights Reserved
#
# This file is a part of < https://github.com/Tepthon-Arabic/TepthonAr/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Tepthon-Arabic/TepthonAr/blob/web/LICENSE/>.

""" وصـف الملـف : اوامـر إضـافة الفـارات باللغـة العربيـة كـاملة ولا حـرف انكلـش🤘 تخمـط اذكـر المصـدر يولـد
إضـافة فـارات صـورة ( الحمايـة - الفحـص - الوقتـي ) بـ امـر واحـد فقـط
حقـوق للتـاريخ : @Tepthon
@E_7_V - كتـابـة الملـف :  بـاقـر"""
#بـاقـر يولـد هههههههههههههههههههههههههه
import asyncio
import math
import os

import heroku3
import requests
import urllib3
import random
import string
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError
from telethon.utils import get_display_name
from urlextract import URLExtract

from . import zedub

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import delete_conv
from ..sql_helper.globals import addgvar, delgvar, gvarstatus

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY
from . import BOTLOG_CHATID, mention


plugin_category = "الادوات"
LOGS = logging.getLogger(__name__)

extractor = URLExtract()


BaqirVP_cmd = (
    "𓆩 [ 𝗧𝗲𝗽𝘁𝗵𝗼𝗻 𝗖𝗼𝗻𝗳𝗶𝗴 𝗩𝗮𝗿𝘀 - اوامـر الفـارات](t.me/Tepthon) 𓆪\n\n"
    "**⎉╎قائـمه اوامر تغييـر فـارات الصـور بأمـر واحـد فقـط - لـ اول مـره ع سـورس تليثـون يوزر بـوت 🦾 :** \n\n"
    "⪼ `.اضف صورة الحماية` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة الفحص` بالـرد ع صـورة او ميديـا\n"
    "⪼ قنـاة كلايـش الفحـص @Tepthon_kalaesh\n\n"
    "⪼ `.اضف صورة الوقتي` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة البوت` بالـرد ع صـورة او ميديـا لـ إضـافة صـورة ستـارت للبـوت\n\n"
    "⪼ `.اضف صورة الحظر` بالـرد ع صـورة او ميديـا لـ إضـافة صـورة لـ كليشـة الحظـر\n\n"
    "⪼ `.اضف صورة الكتم` بالـرد ع صـورة او ميديـا لـ إضـافة صـورة لـ كليشـة الكتـم\n\n"
    "⪼ `.اضف صورة البلوك` بالـرد ع صـورة او ميديـا لـ إضـافة صـورة لـ كليشـة حظـر الخـاص\n\n"
    "⪼ `.اوامر الفارات` لعـرض بقيـة اوامـر الفـارات\n\n\n"
    "**⎉╎قائـمه اوامر تغييـر كليشـة الايـدي :** \n\n"
    "⪼ `.اضف فار ايموجي الايدي` بالـرد ع الرمـز او الايموجـي\n\n"
    "⪼ `.اضف فار عنوان الايدي` بالـرد ع نـص العنـوان\n\n"
    "⪼ `.اضف فار خط الايدي` بالـرد ع الخـط او المستقيـم\n\n"
    "⪼ `.اضف كليشة الايدي` بالـرد ع الكليشـه مـن القنـاة @Tepthon_kalaesh\n\n\n"
    "**⎉╎قائـمه اوامر تغييـر بقيـة الفـارات بأمـر واحـد فقـط :** \n\n"
    "⪼ `.اضف فار كليشة الحماية` بالـرد ع الكليشـة\n"
    "⪼ `.اضف فار كليشة البلوك` بالـرد ع الكليشـة لتغييـر كليشة الحظر خاص\n"
    "⪼ قنـاة كلايـش حمايـة الخـاص @Tepthon_kalaesh\n\n"
    "⪼ `.اضف فار كليشة الفحص` بالـرد ع الكليشـة\n"
    "⪼ قنـاة كلايـش الفحـص @Tepthon_kalaesh\n\n"
    "⪼ `.اضف فار كليشة البوت` بالـرد ع الكليشـة لـ إضـافة كليشـة ستـارت\n\n"
    "⪼ `.اضف فار زر الستارت` بالـرد ع يوزرك او يوزر قناتك لـ إضـافة زر الستـارت\n\n"
    "⪼ `.اضف فار رمز الوقتي` بالـرد ع رمـز\n\n"
    "⪼ `.اضف فار زخرفة الوقتي` بالـرد ع ارقـام الزغـرفه\n\n"
    "⪼ `.اضف فار البايو الوقتي` بالـرد ع البـايـو\n\n"
    "⪼ `.اضف فار اسم المستخدم` بالـرد ع اسـم\n\n"
    "⪼ `.اضف فار كروب الرسائل` بالـرد ع ايدي الكـروب\n\n"
    "⪼ `.اضف فار كروب السجل` بالـرد ع ايدي الكـروب\n\n"
    "⪼ `.اضف فار ايديي` بالـرد ع ايدي حسـابك\n\n"
    "⪼ `.اضف فار نقطة الاوامر` بالـرد ع الـرمز الجديـد\n\n"
    "⪼ `.اضف فار نوم الترحيب` بالـرد ع رقـم الساعة لبداية نوم الترحيب المؤقت\n\n"
    "⪼ `.اضف فار ثواني لانهائي` بالـرد ع رقـم لعـدد الثوانـي الفاصـله بيـن كل عمليـة تجميـع فـي الامـر لانهائـي\n\n"
    "⪼ `.اضف فار رسائل الحماية` بالـرد ع رقـم لعدد رسائل تحذيـرات حماية الخاص\n\n\n"
    "⪼ `.جلب فار` + اسـم الفـار\n\n"
    "⪼ `.حذف فار` + اسـم الفـار\n\n"
    "⪼ `.رفع مطور` بالـرد ع الشخـص لرفعـه مطـور تحكـم كامـل بالاوامـر\n\n"
    "⪼ `.حذف فار المطورين`\n\n"
    "⪼ `.الوقت` لـ عـرض قائمـة اوامـر تغييـر الوقت حسب دولتك\n\n"
    "\n𓆩 [𝗧𝗲𝗽𝘁𝗵𝗼𝗻 𝗩𝗮𝗿𝘀 - قنـاة الفـارات](t.me/Tepthone1) 𓆪"
)


BaqirTZ_cmd = (
    "𓆩 [𝗧𝗲𝗽𝘁𝗵𝗼𝗻 𝗖𝗼𝗻𝗳𝗶𝗴 - اوامـر الوقت](t.me/Tepthon) 𓆪\n\n"
    "**⎉╎قائـمه اوامر تغييـر المنطقـة الزمنيـة للوقـت 🌐:** \n\n"
    "⪼ `.وقت اليمن` \n\n"
    "⪼ `.وقت العراق` \n\n"
    "⪼ `.وقت السعودية` \n\n"
    "⪼ `.وقت سوريا` \n\n"
    "⪼ `.وقت مصر` \n\n"
    "⪼ `.وقت السودان` \n\n"
    "⪼ `.وقت ليبيا` \n\n"
    "⪼ `.وقت الامارات` \n\n"
    "⪼ `.وقت ايران` \n\n"
    "⪼ `.وقت الجزائر` \n\n"
    "⪼ `.وقت المغرب` \n\n"
    "⪼ `.وقت تركيا` \n\n"
    "⪼ `.وقت ماليزيا` \n\n"
    "⪼ `.وقت روسيا` \n\n"
    "⪼ `.وقت ايطاليا` \n\n"
    "⪼ `.وقت امريكا` \n\n"
    "⪼ `.وقت المانيا` \n\n"
    "🛃 سيتـم إضـافة المزيـد من الدول قريبـًـا\n\n"
    "\n𓆩 [𝗧𝗲𝗽𝘁𝗵𝗼𝗻 𝗩𝗮𝗿𝘀 - قنـاة الفـارات](t.me/Tepthone1) 𓆪"
)


# Copyright (C) 2022 Tepthon . All Rights Reserved
@zedub.zed_cmd(pattern=r"اضف فار (.*)")
async def variable(event):
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    vinfo = reply.text
    rep = await edit_or_reply(event, "**⎉╎جـاري إضـافة الفـار إلـى بـوتك ...**")
    # All Rights Reserved for "Tepthon" "باقر"
    if input_str == "كليشة الفحص" or input_str == "كليشه الفحص":
        variable = "ALIVE_TEMPLATE"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_TEMPLATE") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.فحص` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.فحص` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("ALIVE_TEMPLATE", vinfo)
    elif input_str == "كليشة الحماية" or input_str == "كليشه الحمايه" or input_str == "كليشه الحماية" or input_str == "كليشة الحمايه":
        variable = "pmpermit_txt"
        await asyncio.sleep(1.5)
        if gvarstatus("pmpermit_txt") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.الحمايه تفعيل` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.الحمايه تفعيل` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("pmpermit_txt", vinfo)
    elif input_str == "كليشة الايدي" or input_str == "كليشه الايدي":
        variable = "RID_TEMPLATE"
        await asyncio.sleep(1.5)
        if gvarstatus("RID_TEMPLATE") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.ايدي` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.ايدي` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("RID_TEMPLATE", vinfo)
    elif input_str == "كليشة البوت" or input_str == "كليشه البوت" or input_str == "ستارت البوت" or input_str == "كليشة الستارت" or input_str == "كليشه الستارت" or input_str == "كليشة البدء":
        variable = "START_TEXT"
        await asyncio.sleep(1.5)
        if gvarstatus("START_TEXT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الآن قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("START_TEXT", vinfo)
    elif input_str == "زر البوت" or input_str == "زر الستارت" or input_str == "زر ستارت":
        variable = "START_BUTUN"
        await asyncio.sleep(1.5)
        if not vinfo.startswith("@"):
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع يـوزر فقـط**")
        vinfo = vinfo.zedlace("@", "")
        if gvarstatus("START_TEXT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎رابـط زر كليشـة الستـارت الجـديـد** \nhttps://t.me/{} \n\n**⎉╎الآن قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎رابـط زر كليشـة الستـارت الجـديـد** \nhttps://t.me/{} \n\n**⎉╎الآن قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("START_BUTUN", vinfo)
    elif input_str == "كليشة التوديع" or input_str == "كليشه التوديع" or input_str == "كليشة البلوك" or input_str == "كليشه البلوك":
        variable = "pmblock"
        await asyncio.sleep(1.5)
        if gvarstatus("pmblock") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ تفعيـل حماية الخاص عبر الأمر ↶** ( `الحماية تفعيل` ) **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ تفعيـل حماية الخاص عبر الأمر ↶** ( `الحماية تفعيل` ) **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("pmblock", vinfo)
    elif input_str == "رمز الوقتي" or input_str == "رمز الاسم الوقتي":
        variable = "CUSTOM_ALIVE_EMREP"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_EMREP") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الـرمـز الجـديـد** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.الاسم تلقائي` **لـ التحقـق مـن الـرمز . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎الـرمـز المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.الاسم تلقائي` **لـ التحقـق مـن الـرمز . .**".format(input_str, vinfo))
    elif input_str == "البايو" or input_str == "البايو الوقتي" or input_str == "النبذه" or input_str == "البايو تلقائي":
        variable = "DEFAULT_BIO"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_BIO") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎البـايـو الجـديـد** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.البايو تلقائي` **لـ التحقـق مـن البايـو . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضـافه {} بنجـاح ☑️**\n**⎉╎البـايـو المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.البايو تلقائي` **لـ التحقـق مـن البايـو . .**".format(input_str, vinfo))
    elif input_str == "التحقق" or input_str == "كود التحقق" or input_str == "التحقق بخطوتين" or input_str == "تحقق":
        variable = "TG_2STEP_VERIFICATION_CODE"
        await asyncio.sleep(1.5)
        if gvarstatus("TG_2STEP_VERIFICATION_CODE") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎كـود التحـقق بخطـوتيـن** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.تحويل ملكية` **ثم معـرف الشخـص داخـل الكـروب او القنـاة . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎كـود التحـقق بخطـوتيـن** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.تحويل ملكية` **ثم معـرف الشخـص داخـل الكـروب او القنـاة . .**".format(input_str, vinfo))
    elif input_str == "كاشف الاباحي" or input_str == "كشف الاباحي":
        variable = "DEEP_API"
        await asyncio.sleep(1.5)
        if gvarstatus("DEEP_API") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر توكـن {} بنجـاح ☑️**\n**⎉╎التوكـن الجـديـد** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.قفل الاباحي` **لـ تفعيـل كاشـف الاباحي . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة توكـن {} بنجـاح ☑️**\n**⎉╎التوكـن المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.قفل الاباحي` **لـ تفعيـل كاشـف الاباحي . .**".format(input_str, vinfo))
    elif input_str == "ايموجي الايدي" or input_str == "ايموجي ايدي" or input_str == "رمز الايدي" or input_str == "رمز ايدي" or input_str == "الرمز ايدي":
        variable = "CUSTOM_ALIVE_EMOJI"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_EMOJI") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        addgvar("CUSTOM_ALIVE_EMOJI", vinfo)
    elif input_str == "عنوان الايدي" or input_str == "عنوان ايدي":
        variable = "CUSTOM_ALIVE_TEXT"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_TEXT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        addgvar("CUSTOM_ALIVE_TEXT", vinfo)
    elif input_str == "خط الايدي" or input_str == "خط ايدي" or input_str == "خطوط الايدي" or input_str == "خط ايدي":
        variable = "CUSTOM_ALIVE_FONT"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_FONT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        addgvar("CUSTOM_ALIVE_FONT", vinfo)
    elif input_str == "اشتراك الخاص" or input_str == "اشتراك خاص":
        variable = "Custom_Pm_Channel"
        await asyncio.sleep(1.5)
        if gvarstatus("Custom_Pm_Channel") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.اشتراك خاص`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.اشتراك خاص`".format(input_str, vinfo))
        delgvar("Custom_Pm_Channel")
        addgvar("Custom_Pm_Channel", vinfo)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#قنـاة_الاشتـراك_الاجبـاري_للخـاص\
                        \n**- القنـاة {input_str} تم إضافتهـا في قاعده البيانات ..بنجـاح ✓**",
            )
    elif input_str == "اشتراك كروب" or input_str == "اشتراك الكروب":
        variable = "Custom_G_Channel"
        await asyncio.sleep(1.5)
        if gvarstatus("Custom_G_Channel") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.اشتراك كروب`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.اشتراك كروب`".format(input_str, vinfo))
        delgvar("Custom_G_Channel")
        addgvar("Custom_G_Channel", vinfo)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#قنـاة_الاشتـراك_الاجبـاري_للكـروب\
                        \n**- القنـاة {input_str} تم إضافتهـا في قاعده البيانات ..بنجـاح ✓**",
            )
    elif input_str == "زاجل" or input_str == "قائمة زاجل" or input_str == "قائمه زاجل" or input_str == "يوزرات":
        variable = "ZAGL_Rep"
        await asyncio.sleep(1.5)
        if gvarstatus("ZAGL_Rep") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎اليـوزرات المضـافة** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.زاجل` **بالـرد ع نـص او ميديـا بنـص . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎اليـوزرات المضـافة** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.زاجل` **بالـرد ع نـص او ميديـا بنـص . .**".format(input_str, vinfo))
    elif input_str == "سوبر" or input_str == "قائمة السوبر" or input_str == "قائمه السوبر" or input_str == "السوبرات" or input_str == "السوبر":
        variable = "Super_Id"
        await asyncio.sleep(1.5)
        if not vinfo.startswith("-100"):
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع ارقـام ايديات المجموعات التي تبدأ ب 100- فقـط ؟!**\n**⎉╎قم بالذهاب لمجموعات السوبر التي تريد النشر فيها وكتابة الأمر (.الايدي) ثم خذ ايدي المجموعة وهكذا لبقية المجموعات**")
        if gvarstatus("Super_Id") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎الايديات المضـافة** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** (`.سوبر` + عدد الثواني + عدد مرات التكرار)**بالـرد ع نـص او ميديـا بنـص . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الايديات المضـافة** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** (`.سوبر` + عدد الثواني + عدد مرات التكرار)**بالـرد ع نـص او ميديـا بنـص . .**".format(input_str, vinfo))
    elif input_str == "بوت التجميع" or input_str == "بوت النقاط" or input_str == "النجميع" or input_str == "النقاط":
        variable = "R_Point"
        await asyncio.sleep(1.5)
        if gvarstatus("R_Point") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎البـوت المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.تجميع` **لـ البـدء بتجميـع النقـاط من البـوت الجـديـد . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضـافه {} بنجـاح ☑️**\n**⎉╎البـوت المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.تجميع` **لـ البـدء بتجميـع النقـاط من البـوت الجـديـد . .**".format(input_str, vinfo))
    elif input_str == "اسم المستخدم" or input_str == "الاسم":
        variable = "ALIVE_NAME"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_NAME") is not None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        addgvar(variable, vinfo)

    elif input_str == "رسائل الحماية" or input_str == "رسائل الحمايه" or input_str == "رسائل الخاص" or input_str == "رسائل حماية الخاص" or input_str == "عدد التحذيرات":
        variable = "MAX_FLOOD_IN_PMS"
        await asyncio.sleep(1.5)
        if vinfo.isdigit():
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع رقـم فقـط ؟!**")
        addgvar("MAX_FLOOD_IN_PMS", vinfo)

    elif input_str == "كود تيرمكس" or input_str == "كود السيشن" or input_str == "كود سيشن":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "STRING_SESSION"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo

    elif input_str == "كروب الرسائل" or input_str == "كروب التخزين" or input_str == "كروب الخاص":
        variable = "PM_LOGGER_GROUP_ID"
        await asyncio.sleep(1.5)
        if gvarstatus("PM_LOGGER_GROUP_ID") is not None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        addgvar("PM_LOGGER_GROUP_ID", vinfo)
    elif input_str == "السجل" or input_str == "كروب السجل":
        variable = "PRIVATE_GROUP_BOT_API_ID"
        await asyncio.sleep(1.5)
        if gvarstatus("PRIVATE_GROUP_BOT_API_ID") is not None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        addgvar("PRIVATE_GROUP_BOT_API_ID", vinfo)
    elif input_str == "السجل 2" or input_str == "كروب السجل 2":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "PRIVATE_GROUP_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "قناة السجل" or input_str == "قناة السجلات":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "PRIVATE_CHANNEL_BOT_API_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "قناة الملفات" or input_str == "قناة الإضافات":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "PLUGIN_CHANNEL"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "ايديي" or input_str == "ايدي الحساب":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "OWNER_ID"
        await asyncio.sleep(1.5)
        if vinfo.isdigit():
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع رقـم فقـط ؟!**")
        heroku_var[variable] = vinfo
    elif input_str == "نقطة الاوامر" or input_str == "نقطه الاوامر":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "COMMAND_HAND_LER"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "التوكن" or input_str == "توكن البوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TG_BOT_TOKEN"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "معرف البوت" or input_str == "معرف بوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TG_BOT_USERNAME"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "الريبو" or input_str == "السورس":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه ريندر 🔄**")
        variable = "UPSTREAM_REPO"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "توكن المكافح" or input_str == "كود المكافح" or input_str == "مكافح التخريب" or input_str == "مكافح التفليش":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "SPAMWATCH_API"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "توكن الذكاء" or input_str == "مفتاح الذكاء" or input_str == "الذكاء":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "OPENAI_API_KEY"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "ايقاف الترحيب" or input_str == "نوم الترحيب":
        variable = "TIME_STOP"
        await asyncio.sleep(1.5)
        if vinfo.isdigit():
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, vinfo))
        else:
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع رقـم فقـط ؟!**")
        addgvar("TIME_STOP", vinfo)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#فتـرة_الايقـاف_المـؤقت_للترحيب\
                        \n**- تم إضافة الفتـرة من الساعة {vinfo} إلى الساعة 6 صباحـًـا .. بنجـاح ✓**",
            )
    elif input_str == "ثواني لانهائي" or input_str == "ثواني التجميع" or input_str == "عدد لانهائي":
        variable = "SEC_LAN"
        await asyncio.sleep(1.5)
        if vinfo.isdigit():
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎الثوانـي الجـديـدة** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.لانهائي` **+ اسم بوت التجميـع لـ البـدء بالتجميـع اللانهائـي . .**".format(input_str, vinfo))
        else:
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع رقـم فقـط ؟!**")
        addgvar(variable, vinfo)
    elif ("صورة" in input_str) or ("صوره" in input_str):
        return await zed.edit("**⎉╎لـ إضافة صور الكلايش ..**\n**⎉╎استخدم الأمر (اضف) مباشرة بدون كلمة فار**")
    else:
        if input_str:
            return await zed.edit("**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))
        return await edit_or_reply(event, "**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))


# Copyright (C) 2022 TepthonArabic . All Rights Reserved
@zedub.zed_cmd(pattern="حذف فار(?:\\s|$)([\\s\\S]*)")
async def variable(event):
    input_str = event.text[9:]
    if (input_str == "من" or input_str == "إلى" or input_str == "الترحيب") or "رسائلي" in input_str or "رسائله" in input_str:
        return
    rep = await edit_or_reply(event, "**⎉╎جـاري حـذف الفـار مـن بـوتك 🚮...**")
    # All Rights Reserved for "Tepthon" "باقر"
    if input_str == "كليشة الفحص" or input_str == "كليشه الفحص":
        variable = gvarstatus("ALIVE_TEMPLATE")
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_TEMPLATE") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("ALIVE_TEMPLATE")
        
    elif input_str == "كليشة الحماية" or input_str == "كليشه الحمايه" or input_str == "كليشه الحماية" or input_str == "كليشة الحمايه":
        variable = gvarstatus("pmpermit_txt")
        await asyncio.sleep(1.5)
        if gvarstatus("pmpermit_txt") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("pmpermit_txt")

    elif input_str == "كليشة البوت" or input_str == "كليشه البوت":
        variable = gvarstatus("START_TEXT")
        await asyncio.sleep(1.5)
        if gvarstatus("START_TEXT") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("START_TEXT")

    elif input_str == "زر البوت" or input_str == "زر الستارت" or input_str == "زر ستارت":
        variable = gvarstatus("START_BUTUN")
        await asyncio.sleep(1.5)
        if gvarstatus("START_BUTUN") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("START_BUTUN")

    elif input_str == "كليشة التوديع" or input_str == "كليشه التوديع" or input_str == "كليشة البلوك" or input_str == "كليشه البلوك":
        variable = gvarstatus("pmblock")
        await asyncio.sleep(1.5)
        if gvarstatus("pmblock") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت زد ثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("pmblock")

    elif input_str == "كليشة الايدي" or input_str == "كليشه الايدي":
        variable = "RID_TEMPLATE"
        await asyncio.sleep(1.5)
        if gvarstatus("RID_TEMPLATE") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("RID_TEMPLATE")

    elif input_str == "صورة الفحص" or input_str == "صوره الفحص":
        variable = "ALIVE_PIC"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_PIC") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("ALIVE_PIC")

    elif input_str == "صورة الاوامر" or input_str == "صوره الاوامر":
        variable = "CMD_PIC"
        await asyncio.sleep(1.5)
        if gvarstatus("CMD_PIC") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("CMD_PIC")

    elif input_str == "صورة السورس" or input_str == "صوره السورس":
        variable = "ALIVE_PIC"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_PIC") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("ALIVE_PIC")

    elif input_str == "صورة الكتم" or input_str == "صوره الكتم":
        variable = "PC_MUTE"
        await asyncio.sleep(1.5)
        if gvarstatus("PC_MUTE") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("PC_MUTE")

    elif input_str == "صورة الحظر" or input_str == "صوره الحظر":
        variable = "PC_BANE"
        await asyncio.sleep(1.5)
        if gvarstatus("PC_BANE") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("PC_BANE")

    elif input_str == "صورة البلوك" or input_str == "صوره البلوك":
        variable = "PC_BLOCK"
        await asyncio.sleep(1.5)
        if gvarstatus("PC_BLOCK") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("PC_BLOCK")

    elif input_str == "صورة البوت" or input_str == "صوره البوت" or input_str == "صورة الستارت" or input_str == "صوره الستارت" or input_str == "صورة ستارت" or input_str == "صوره ستارت":
        variable = "BOT_START_PIC"
        await asyncio.sleep(1.5)
        if gvarstatus("BOT_START_PIC") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("BOT_START_PIC")

    elif input_str == "صورة الحماية" or input_str == "صوره الحمايه" or input_str == "صورة الحمايه" or input_str == "صوره الحماية":
        variable = "pmpermit_pic"
        await asyncio.sleep(1.5)
        if gvarstatus("pmpermit_pic") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        delgvar("pmpermit_pic")
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))

    elif input_str == "صورة الوقتي" or input_str == "صوره الوقتي":
        variable = gvarstatus("DIGITAL_PIC")
        await asyncio.sleep(1.5)
        if gvarstatus("DIGITAL_PIC") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, variable))
        delgvar("DIGITAL_PIC")

    elif input_str == "رمز الوقتي" or input_str == "رمز الاسم الوقتي":
        variable = "CUSTOM_ALIVE_EMREP"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_EMREP") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        delgvar("CUSTOM_ALIVE_EMREP")
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
    elif input_str == "زخرفه الوقتي" or input_str == "زخرفة الوقتي":
        variable = "BA_FN"
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        delgvar(variable)
    elif input_str == "رسائل الحماية" or input_str == "رسائل الحمايه" or input_str == "رسائل الخاص" or input_str == "رسائل حماية الخاص" or input_str == "عدد التحذيرات":
        variable = "MAX_FLOOD_IN_PMS"
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        delgvar(variable)
    elif input_str == "البايو" or input_str == "البايو الوقتي" or input_str == "النبذه الوقتيه":
        variable = "DEFAULT_BIO"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_BIO") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        delgvar("DEFAULT_BIO")
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
    elif input_str == "اسم المستخدم" or input_str == "الاسم":
        variable = "ALIVE_NAME"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_NAME") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        delgvar(variable)
    elif input_str == "كروب الرسائل" or input_str == "كروب التخزين" or input_str == "كروب الخاص":
        variable = "PM_LOGGER_GROUP_ID"
        await asyncio.sleep(1.5)
        if gvarstatus("PM_LOGGER_GROUP_ID") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        delgvar(variable)

    elif input_str == "السجل" or input_str == "كروب السجل":
        variable = "PRIVATE_GROUP_BOT_API_ID"
        await asyncio.sleep(1.5)
        if gvarstatus("PRIVATE_GROUP_BOT_API_ID") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        delgvar(variable)

    elif input_str == "السجل 2" or input_str == "كروب السجل 2":
        variable = "PRIVATE_GROUP_ID"
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "قناة السجل" or input_str == "قناة السجلات":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "PRIVATE_CHANNEL_BOT_API_ID"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "قناة الملفات" or input_str == "قناة الإضافات":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "PLUGIN_CHANNEL"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "التحقق" or input_str == "كود التحقق":
        variable = "TG_2STEP_VERIFICATION_CODE"
        await asyncio.sleep(1.5)
        if gvarstatus("TG_2STEP_VERIFICATION_CODE") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        delgvar("TG_2STEP_VERIFICATION_CODE")
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))

    elif input_str == "ايديي" or input_str == "ايدي الحساب":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "OWNER_ID"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "نقطة الاوامر" or input_str == "نقطه الاوامر":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه ريندر 🔄**")
        variable = "COMMAND_HAND_LER"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "التوكن" or input_str == "توكن البوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TG_BOT_TOKEN"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "معرف البوت" or input_str == "معرف بوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TG_BOT_USERNAME"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "الريبو" or input_str == "السورس":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "UPSTREAM_REPO"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "اسمي التلقائي" or input_str == "الاسم التلقاائي":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "AUTONAME"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]
    elif input_str == "ايموجي الايدي" or input_str == "ايموجي ايدي" or input_str == "رمز الايدي" or input_str == "رمز ايدي" or input_str == "الرمز ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_EMOJI")
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("CUSTOM_ALIVE_EMOJI")
    elif input_str == "عنوان الايدي" or input_str == "عنوان ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_TEXT")
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("CUSTOM_ALIVE_TEXT")
    elif input_str == "خط الايدي" or input_str == "خط ايدي" or input_str == "خطوط الايدي" or input_str == "خط ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_FONT")
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("CUSTOM_ALIVE_FONT")
    elif input_str == "كاشف الاباحي" or input_str == "كشف الاباحي":
        variable = gvarstatus("DEEP_API")
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("DEEP_API")
    elif input_str == "ايقاف الترحيب" or input_str == "نوم الترحيب":
        variable = "TIME_STOP"
        await asyncio.sleep(1.5)
        if variable is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("TIME_STOP")
    elif input_str == "ثواني لانهائي" or input_str == "ثواني التجميع" or input_str == "عدد لانهائي":
        variable = "SEC_LAN"
        await asyncio.sleep(1.5)
        if gvarstatus("SEC_LAN") is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. مطـوري الغالـي 🥰، أنت لم تقم بإضافة فار {} أصلًا؟؟!...**".format(input_str))
        await zed.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("SEC_LAN")
    else:
        if input_str:
            return await zed.edit("**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))
        return await edit_or_reply(event, "**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))


# Copyright (C) 2022 TepthonArabic . All Rights Reserved
@zedub.zed_cmd(pattern="جلب فار(?:\\s|$)([\\s\\S]*)")
async def custom_rep(event):
    input_str = event.text[9:]
    rep = await edit_or_reply(event, "**⎉╎جــاري جلـب معلـومـات الفــار 🛂. . .**")
    if (input_str == "كليشة الحماية" or input_str == "كليشة الحمايه" or input_str == "كليشه الحماية" or input_str == "كليشه الحمايه"):
        variable = gvarstatus("pmpermit_txt")
        if variable is None:
            await zed.edit("**⎉╎فـار كليشـة الحمايـة غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكليشـة استخـدم الامـر : ↶**\n `.اضف فار كليشة الحماية` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))
            
    elif input_str == "كليشة الفحص" or input_str == "كليشه الفحص":
        variable = gvarstatus("ALIVE_TEMPLATE")
        if variable is None:
            await zed.edit("**⎉╎فـار كليشـة الفحص غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكليشـة استخـدم الامـر : ↶**\n `.اضف فار كليشة الفحص` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "كليشة البوت" or input_str == "كليشه البوت":
        variable = gvarstatus("START_TEXT")
        if variable is None:
            await zed.edit("**⎉╎فـار كليشـة البـوت غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكليشـة استخـدم الامـر : ↶**\n `.اضف فار كليشة البوت` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "زر البوت" or input_str == "زر الستارت" or input_str == "زر ستارت":
        variable = gvarstatus("START_BUTUN")
        if variable is None:
            await zed.edit("**⎉╎فـار زر كليشـة ستـارت البـوت غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع يـوزرك او يـوزر قناتـك استخـدم الامـر : ↶**\n `.اضف فار زر الستارت` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n https://t.me/{}\n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "كليشة التوديع" or input_str == "كليشه التوديع" or input_str == "كليشة البلوك" or input_str == "كليشه البلوك":
        variable = gvarstatus("pmblock")
        if variable is None:
            await zed.edit("**⎉╎فـار كليشـة الحظـر غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكليشـة استخـدم الامـر : ↶**\n `.اضف فار كليشة الحظر` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "رمز الوقتي" or input_str == "رمز الاسم الوقتي":
        variable = gvarstatus("CUSTOM_ALIVE_EMREP")
        if variable is None:
            await zed.edit("**⎉╎فـار رمـز الوقتـي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز استخـدم الامـر : ↶**\n `.اضف فار رمز الوقتي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "التحقق" or input_str == "كود التحقق":
        variable = gvarstatus("TG_2STEP_VERIFICATION_CODE")
        if variable is None:
            await zed.edit("**⎉╎فـار التحقق بخطوتين غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز استخـدم الامـر : ↶**\n `.اضف فار التحقق`  **بالـرد ع كـود التحـقق**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "كاشف الاباحي" or input_str == "كشف الاباحي":
        variable = gvarstatus("DEEP_API")
        if variable is None:
            await zed.edit("**⎉╎فـار كشـف الاباحي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكـود استخـدم الامـر : ↶**\n `.اضف فار كاشف الاباحي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "البايو" or input_str == "البايو الوقتي" or input_str == "النبذه" or input_str == "البايو تلقائي":
        variable = gvarstatus("DEFAULT_BIO")
        if variable is None:
            await zed.edit("**⎉╎فـار البايـو الوقتـي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع نـص استخـدم الامـر : ↶**\n `.اضف فار البايو` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "اسم المستخدم" or input_str == "الاسم":
        variable = gvarstatus("ALIVE_NAME")
        if gvarstatus("ALIVE_NAME") is None:
            await zed.edit("**⎉╎فـار اسـم المستخـدم غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الاسم استخـدم الامـر : ↶**\n `.اضف فار اسم المستخدم` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "كود تيرمكس" or input_str == "كود السيشن" or input_str == "كود سيشن":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "STRING_SESSION"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار اسـم المستخـدم غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الاسم استخـدم الامـر : ↶**\n `.اضف فار اسم المستخدم` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "ايديي" or input_str == "ايدي الحساب":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "OWNER_ID"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار ايـدي الحسـاب غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الايـدي فقـط استخـدم الامـر : ↶**\n `.اضف فار ايدي الحساب` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "نقطة الاوامر" or input_str == "نقطه الاوامر":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "COMMAND_HAND_LER"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار نقطـة الاوامـر غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز فقـط استخـدم الامـر : ↶**\n `.اضف فار نقطة الاوامر` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "التوكن" or input_str == "توكن البوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TG_BOT_TOKEN"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار توكـن البـوت غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع التوكـن فقـط استخـدم الامـر : ↶**\n `.اضف فار التوكن` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "معرف البوت" or input_str == "معرف بوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "APP_USERNAME"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار معرف البوت غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع المعرف استخـدم الامـر : ↶**\n `.اضف فار معرف البوت` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "الريبو" or input_str == "السورس":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "UPSTREAM_REPO"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار الريبـو غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع رابط السورس الرسمي استخـدم الامـر : ↶**\n `.اضف فار الريبو` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "اسمي التلقائي" or input_str == "الاسم التلقاائي":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "AUTONAME"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار الاسـم التلقائي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الاسم استخـدم الامـر : ↶**\n `.اضف فار اسمي التلقائي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الحماية" or input_str == "صوره الحمايه" or input_str == "صورة الحمايه" or input_str == "صوره الحماية":
        variable = gvarstatus("pmpermit_pic")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الحمايـة غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الحماية` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الوقتي" or input_str == "صوره الوقتي":
        variable = gvarstatus("DIGITAL_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الوقتـي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الوقتي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الفحص" or input_str == "صوره الفحص":
        variable = gvarstatus("ALIVE_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الفحص غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الفحص` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة البوت" or input_str == "صوره البوت" or input_str == "صورة الستارت" or input_str == "صوره الستارت" or input_str == "صورة ستارت" or input_str == "صوره ستارت":
        variable = gvarstatus("BOT_START_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة ستـارت البـوت غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة البوت` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الاوامر" or input_str == "صوره الاوامر":
        variable = gvarstatus("CMD_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الاوامـر غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الاوامر` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة السورس" or input_str == "صوره السورس":
        variable = gvarstatus("ALIVE_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة السـورس غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة السورس` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الكتم" or input_str == "صوره الكتم":
        variable = gvarstatus("PC_MUTE")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الكتم غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الكتم` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة الحظر" or input_str == "صوره الحظر":
        variable = gvarstatus("PC_BANE")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة الحظر غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة الحظر` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "صورة البلوك" or input_str == "صوره البلوك":
        variable = gvarstatus("PC_BLOCK")
        if variable is None:
            await zed.edit("**⎉╎فـار صـورة البلوك غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع صـورة فقـط استخـدم الامـر : ↶**\n `.اضف صورة البلوك` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "زخرفة الوقتي" or input_str == "زخرفه الوقتي":
        variable = gvarstatus("NA_FN")
        if variable is None:
            await zed.edit("**⎉╎فـار زخرفـة الاسـم الوقتي غيـر موجـود ❌**\n**⎉╎لـ إضـافته فقـط استخـدم الامـر : ↶**\n `.الوقتي 1` إلـى `.الوقتي 14` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "رسائل الحماية" or input_str == "رسائل الحمايه" or input_str == "رسائل الخاص" or input_str == "رسائل حماية الخاص" or input_str == "عدد التحذيرات":
        variable = gvarstatus("MAX_FLOOD_IN_PMS")
        if variable is None:
            await zed.edit("**⎉╎فـار رسـائل الحمايـة غيـر موجـود ❌**\n**⎉╎لـ إضـافته فقـط استخـدم الامـر : ↶**\n `.اضف فار رسائل الحماية` بالـرد ع عـدد فقـط \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "زخرفة الوقتية" or input_str == "زخرفه الوقتيه" or input_str == "زخرفة الوقتيه" or input_str == "زخرفه الوقتية":
        variable = gvarstatus("DEFAULT_PIC")
        if variable is None:
            await zed.edit("**⎉╎فـار زخرفـة الصـورة الوقتيـة غيـر موجـود ❌**\n**⎉╎لـ إضـافته فقـط استخـدم الامـر : ↶**\n `.وقتي 1` إلـى `.وقتي 17` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "الوقت" or input_str == "الساعه" or input_str == "المنطقه الزمنيه":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "TZ"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار المنطقـة الزمنيــــة غيـر موجـود ❌**\n**⎉╎لـ إضـافته فقـط استخـدم الامـر : ↶**\n `.وقت` واسـم الدولـة \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "كليشة الايدي" or input_str == "كليشه الايدي":
        variable = gvarstatus("RID_TEMPLATE")
        if variable is None:
            await zed.edit("**⎉╎فـار ايموجي/رمز الايدي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الكليشـة من هنا ( @Tepthon_kalaesh ) استخـدم الامـر : ↶**\n `.اضف كليشة الايدي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "ايموجي الايدي" or input_str == "ايموجي ايدي" or input_str == "رمز الايدي" or input_str == "رمز ايدي" or input_str == "الرمز ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_EMOJI")
        if variable is None:
            await zed.edit("**⎉╎فـار ايموجي/رمز الايدي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز استخـدم الامـر : ↶**\n `.اضف فار رمز الايدي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))
            
    elif input_str == "عنوان الايدي" or input_str == "عنوان ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_TEXT")
        if variable is None:
            await zed.edit("**⎉╎فـار نص عنـوان كليشـة الايـدي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز استخـدم الامـر : ↶**\n `.اضف فار عنوان الايدي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "خط الايدي" or input_str == "خط ايدي" or input_str == "خطوط الايدي" or input_str == "خط ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_FONT")
        if variable is None:
            await zed.edit("**⎉╎فـار خطـوط كليشـة الايـدي غيـر موجـود ❌**\n**⎉╎لـ إضـافته بالـرد ع الرمـز استخـدم الامـر : ↶**\n `.اضف فار خطوط الايدي` \n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "لاعب 1":
        variable = gvarstatus("R_AK")
        if gvarstatus("R_AK") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "لاعب 2":
        variable = gvarstatus("R_A2K")
        if gvarstatus("R_A2K") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "لاعب 3":
        variable = gvarstatus("R_A3K")
        if gvarstatus("R_A3K") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "لاعب 4":
        variable = gvarstatus("R_A4K")
        if gvarstatus("R_A4K") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "لاعب 5":
        variable = gvarstatus("R_A5K")
        if gvarstatus("R_A5K") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "توكن المكافح" or input_str == "كود المكافح" or input_str == "مكافح التخريب" or input_str == "مكافح التفليش":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "**⎉╎عـذراً .. عـزيـزي ⚠️**\n**⎉╎هـذا الفـار لا يعمـل الآن ✖️**\n**⎉╎سـوف يتم تحديثه لاحقاً ع منصه سكالينجو 🔄**")
        variable = "SPAMWATCH_API"
        if variable not in heroku_var:
            await zed.edit("**⎉╎فـار توكـن المكـافح غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "اشتراك خاص" or input_str == "اشتراك الخاص" or input_str == "قناة الاشتراك" or input_str == "الاشتراك":
        variable = gvarstatus("Custom_Pm_Channel")
        if gvarstatus("Custom_Pm_Channel") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "اشتراك كروب" or input_str == "اشتراك الكروب" or input_str == "قناة الاشتراك" or input_str == "الاشتراك":
        variable = gvarstatus("Custom_G_Channel")
        if gvarstatus("Custom_G_Channel") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "االهمسه":
        variable = gvarstatus("hmsa_id")
        if gvarstatus("hmsa_id") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    elif input_str == "ثواني لانهائي" or input_str == "ثواني التجميع" or input_str == "عدد لانهائي":
        variable = gvarstatus("SEC_LAN")
        if gvarstatus("SEC_LAN") is None:
            await zed.edit("**⎉╎المتغيـر غيـر موجـود ❌**\n\n**⎉╎قنـاة السـورس : @Tepthon**")
        else:
            await zed.edit("**⎉╎المتغيـر {} موجـود ☑️**\n**⎉╎قيمـة المتغيـر : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @Tepthon**".format(input_str, variable))

    else:
        if input_str:
            return await zed.edit("**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))
        return await edit_or_reply(event, "**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))


# Copyright (C) 2022 TepthonArabic . All Rights Reserved
@zedub.zed_cmd(pattern="وقت(?:\\s|$)([\\s\\S]*)")
async def variable(event):
    input_str = event.text[5:]
    viraq = "Asia/Baghdad"
    vmsr = "Africa/Cairo"
    vdubai = "Asia/Dubai"
    vturk = "Europe/Istanbul"
    valgiers = "Africa/Algiers"
    vmoroco = "Africa/Casablanca"
    viran = "Asia/Tehran"
    vsudan = "Africa/Khartoum"
    vitaly = "Europe/Rome"
    vrusia = "Europe/Moscow"
    vamerica = "America/Washington"
    vmalaysia = "Asia/Kuala_Lumpur"
    vdeutschland = "Europe/Berlin"
    rep = await edit_or_reply(event, "**⎉╎جـاري إعــداد المنطقـة الزمنيــــة لـ تيبثـون 🌐...**")
    # All Rights Reserved for "Tepthon" "باقر"
    if input_str == "العراق" or input_str == "اليمن" or input_str == "سوريا" or input_str == "السعودية" or input_str == "لبنان" or input_str == "الاردن":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}` \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", viraq)
    elif input_str == "مصر" or input_str == "ليبيا" or input_str == "القاهرة":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", vmsr)
    elif input_str == "دبي" or input_str == "الامارات" or input_str == "عمان" or input_str == "مسقط":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", vdubai)
    elif input_str == "تركيا" or input_str == "اسطنبول" or input_str == "انقرة":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", vturk)
    elif input_str == "تونس" or input_str == "الجزائر":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", valgiers)
    elif input_str == "المغرب" or input_str == "موريتانيا" or input_str == "الدار البيضاء":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", vmoroco)        
    elif input_str == "ايران" or input_str == "طهران":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", viran)
    elif input_str == "السودان":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "Africa/Khartoum")
    elif input_str == "ايطاليا":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "Europe/Rome")
    elif input_str == "روسيا":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "Europe/Moscow")
    elif input_str == "امريكا":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "America/Washington")
    elif input_str == "ماليزيا":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "Asia/Kuala_Lumpur")
    elif input_str == "المانيا":
        variable = "TZ"
        await asyncio.slepp(1.5)
        if gvarstatus("TZ") is not None:
            await zed.edit("**⎉╎تم تغييـر المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المتغير : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**⎉╎تم إضـافـة المنطقـة الزمنيــــة .. بنجـاح ☑️**\n**⎉╎المضـاف إليـــه : ↶**\n دولـة `{}`  \n**⎉╎يتم الآن إعــادة تشغيـل بـوت تيبثـون يستغـرق الأمر 2-1 دقيقـة ⏰ ▬▭ ...**".format(input_str))
        addgvar("TZ", "Europe/Berlin")

                
@zedub.zed_cmd(pattern="اضف صورة (الفحص|فحص) ?(.*)")
async def alive_Tepthon(event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        zedevent = await event.edit("**⎉╎ جـار رفع الـصورة إلى أمر الفحص**")
        try:
            baqir = await event.client.download_media(reply)
            if baqir.endswith((".webp")):
                resize_image(baqir)
            with open(baqir, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("ALIVE_PIC", url)
                await zedevent.edit(f"**⎉╎ تم إضافة الصورة إلى الفحص ✓ **")
            else:
                await zedevent.edit(f"**⎉╎ حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(baqir)
        except Exception as exc:
            await event.edit(f"**خـطأ : **\n`{exc}`")
            if os.path.exists(baqir):
                os.remove(baqir)
    else:
        await event.edit("**⎉╎ يُرجى الرد على الصورة لطفًا**")


@zedub.zed_cmd(pattern="اضف صورة (الحمايه|الحماية) ?(.*)")
async def Tepthon(event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        zedevent = await event.edit("**⎉╎ جـار رفع الـصورة إلى أمر الحماية**")
        try:
            baqir = await event.client.download_media(reply)
            if baqir.endswith((".webp")):
                resize_image(baqir)
            with open(baqir, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("pmpermit_pic", url)
                await zedevent.edit(f"**⎉╎ تم إضافة الصورة إلى الحماية ✓ **")
            else:
                await zedevent.edit(f"**⎉╎ حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(baqir)
        except Exception as exc:
            await event.edit(f"**خـطأ : **\n`{exc}`")
            if os.path.exists(baqir):
                os.remove(baqir)
    else:
        await event.edit("**⎉╎ يُرجى الرد على الصورة لطفًا**")


@zedub.zed_cmd(pattern="اضف صورة (الاوامر|اللوحة) ?(.*)")
async def Tepthon(event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        zedevent = await event.edit("**⎉╎ جـار رفع الـصورة إلى أمر لوحة الاوامر**")
        try:
            baqir = await event.client.download_media(reply)
            if baqir.endswith((".webp")):
                resize_image(baqir)
            with open(baqir, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("CMD_PIC", url)
                await zedevent.edit(f"**⎉╎ تم إضافة الصورة إلى لوحة الاوامر ✓ **")
            else:
                await zedevent.edit(f"**⎉╎ حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(baqir)
        except Exception as exc:
            await event.edit(f"**خـطأ : **\n`{exc}`")
            if os.path.exists(baqir):
                os.remove(baqir)
    else:
        await event.edit("**⎉╎ يُرجى الرد على الصورة لطفًا**")


@zedub.zed_cmd(pattern="اضف صورة (البوت|بوت) ?(.*)")
async def Tepthon(event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        zedevent = await event.edit("**⎉╎ جـار رفع الـصورة إلى أمر البوت**")
        try:
            baqir = await event.client.download_media(reply)
            if baqir.endswith((".webp")):
                resize_image(baqir)
            with open(baqir, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("BOT_START_PIC", url)
                await zedevent.edit(f"**⎉╎ تم إضافة الصورة إلى البوت ✓ **")
            else:
                await zedevent.edit(f"**⎉╎ حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(baqir)
        except Exception as exc:
            await event.edit(f"**خـطأ : **\n`{exc}`")
            if os.path.exists(baqir):
                os.remove(baqir)
    else:
        await event.edit("**⎉╎ يُرجى الرد على الصورة لطفًا**")


@zedub.zed_cmd(pattern="اضف صورة (الوقتي|التلقائي|وقتي|البروفايل) ?(.*)")
async def Tepthon(event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        zedevent = await event.edit("**⎉╎ جـار رفع الـصورة إلى أمر الصورة الوقتية**")
        try:
            baqir = await event.client.download_media(reply)
            if baqir.endswith((".webp")):
                resize_image(baqir)
            with open(baqir, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("DIGITAL_PIC", url)
                await zedevent.edit(f"**⎉╎ تم إضافة الصورة إلى امر الصورة الوقتية ✓ **")
            else:
                await zedevent.edit(f"**⎉╎ حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(baqir)
        except Exception as exc:
            await event.edit(f"**خـطأ : **\n`{exc}`")
            if os.path.exists(baqir):
                os.remove(baqir)
    else:
        await event.edit("**⎉╎ يُرجى الرد على الصورة لطفًا**")




# Copyright (C) 2022 Tepthon . All Rights Reserved
@zedub.zed_cmd(pattern="اوامر الفارات")
async def cmd(baqir):
    await edit_or_reply(baqir, BaqirVP_cmd)

@zedub.zed_cmd(pattern="الفارات")
async def cmd(baqir):
    await edit_or_reply(baqir, BaqirVP_cmd)

@zedub.zed_cmd(pattern="اوامر الوقت")
async def cmd(baqir):
    await edit_or_reply(baqir, BaqirTZ_cmd)

@zedub.zed_cmd(pattern="الوقت")
async def cmd(baqir):
    await edit_or_reply(baqir, BaqirTZ_cmd)

@zedub.zed_cmd(pattern="اوامر الوقت")
async def cmd(baqir):
    await edit_or_reply(baqir, BaqirTZ_cmd)

@zedub.zed_cmd(pattern="الوقت")
async def cmd(baqir):
    await edit_or_reply(baqir, BaqirTZ_cmd)
ly(baqir, BaqirTZ_cmd)

@zedub.zed_cmd(pattern="اوامر الوقت")
async def cmd(baqir):
    await edit_or_reply(baqir, BaqirTZ_cmd)

@zedub.zed_cmd(pattern="الوقت")
async def cmd(baqir):
    await edit_or_reply(baqir, BaqirTZ_cmd)
