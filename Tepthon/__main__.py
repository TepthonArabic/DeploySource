import sys
import Tepthon
from Tepthon import BOTLOG_CHATID, PM_LOGGER_GROUP_ID
from .Config import Config
from .core.logger import logging
from .core.session import zedub
from .utils import mybot, autoname, autovars
from .utils import (
    add_bot_to_logger_group,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("سورس تيبثون")

print(Tepthon.__copyright__)
print(f"المرخصة بموجب شروط  {Tepthon.__license__}")

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("⌭ جـاري تحميـل الملحقـات ⌭")
    zedub.loop.run_until_complete(autovars())
    LOGS.info("✓ تـم تحميـل الملحقـات .. بنجـاح ✓")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()

if not Config.ALIVE_NAME:
    try: #Code by T.me/E_7_V
        LOGS.info("⌭ بـدء إضافة الاسـم التلقـائـي ⌭")
        zedub.loop.run_until_complete(autoname())
        LOGS.info("✓ تـم إضافة فار الاسـم .. بـنجـاح ✓")
    except Exception as e:
        LOGS.error(f"- {e}")

try: #Code by T.me/E_7_V
    LOGS.info("⌭ بـدء تنزيـل تيـبثون ⌭")
    zedub.loop.run_until_complete(setup_bot())
    LOGS.info("⌭ بـدء تشغيل البـوت ⌭")
except Exception as e:
    LOGS.error(f"- {e}")

try:
    LOGS.info("⌭ جـار تفعيـل وضـع الانـلاين ⌭")
    zedub.loop.run_until_complete(mybot())
    LOGS.info("✓ تـم تفعيـل الانـلاين .. بـنجـاح ✓")
except Exception as e:
    LOGS.error(f"- {e}")



async def startup_process():
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
async def qruan_process():
    await verifyLoggerGroup()
    await load_plugins("vc_baqir")
    print("➖➖➖➖➖ سورس تيبثون™ ➖➖➖➖➖")
    print("تـم التنصـيب .. بنجـاح ✓")
    print(
        f"⌔┊تـم تنصيـب تيبثـون يـوزر بـوت . . بنجـاح 🧸♥️ \n\n⌔┊تحيـاتي ..  محـمد\n⌔┊قنـاة السـورس ↶.\n🌐┊@Tepthon"
    )
    print("➖➖➖➖➖ سورس تيبثون™ ➖➖➖➖➖")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    return

zedub.loop.run_until_complete(startup_process())
zedub.loop.run_until_complete(qruan_process())
if len(sys.argv) not in (1, 3, 4):
    zedub.disconnect()
else:
    try:
        zedub.run_until_disconnected()
    except ConnectionError:
        pass
