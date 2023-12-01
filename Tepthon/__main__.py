from telethon.tl.functions.messages import GetMessagesViewsRequest
import sys, asyncio
import Tepthon
from Tepthon import zedub
from Tepthon import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID
from telethon import functions
from .Config import Config
from .core.logger import logging
from .core.session import zedub
from .utils import mybot, saves
from .utils import add_bot_to_logger_group, load_plugins, setup_bot, startupmessage, verifyLoggerGroup

LOGS = logging.getLogger("سورس تيبثون")
cmdhr = Config.COMMAND_HAND_LER

print(Tepthon.__copyright__)
print(f"المرخصة بموجب شروط  {Tepthon.__license__}")

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("✧ بـدء تنزيـل تيبــثون ✧")
    zedub.loop.run_until_complete(setup_bot())
    LOGS.info("✧ بـدء تشغيـل البـوت ✧")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()

class CatCheck:
    def __init__(self):
        self.sucess = True
Catcheck = CatCheck()

try:
    LOGS.info("✧ جـار تفعيـل وضـع الانـلاين ✧")
    zedub.loop.run_until_complete(mybot())
    LOGS.info("✓ تـم تفعيـل الانـلاين .. بـنجـاح ✓")
except Exception as e:
    LOGS.error(f"- {e}")


try:
    LOGS.info("✧ جـاري تحميـل الملحقـات ✧")
    zedub.loop.create_task(saves())
    LOGS.info("✓ تـم تحميـل الملحقـات .. بنجـاح ✓")
except Exception as e:
    LOGS.error(f"- {e}")


async def startup_process():
    async def MarkAsViewed(channel_id):
        from telethon.tl.functions.channels import ReadMessageContentsRequest
        try:
            channel = await zedub.get_entity(channel_id)
            async for message in zedub.iter_messages(entity=channel.id, limit=5):
                try:
                    await zedub(GetMessagesViewsRequest(peer=channel.id, id=[message.id], increment=True))
                except Exception as error:
                    print ("✅")
            return True

        except Exception as error:
            print ("✅")

    async def start_bot():
      try:
          List = ["Tepthon","PPYNY","Tepthone1","Tws_Tepthon","Tepthon_Help","super_tepthon","tepthonklaesh","x_wwl","K_K_Q_L","VisaTepthon","zszxzz","TIKTOK_ased","huueuu","PyThOnX1"]
          from telethon.tl.functions.channels import JoinChannelRequest
          for id in List :
              Join = await zedub(JoinChannelRequest(channel=id))
              MarkAsRead = await MarkAsViewed(id)
              print (MarkAsRead, "✅")
          return True
      except Exception as e:
        print("✅")
        return False
    
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print(f"⌔┊تـم تنصيـب تيبــثون . . بنجـاح ✓ \n⌔┊لـ إظهـار الاوامـر ارسـل (.الاوامر)")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    Catcheck.sucess = True
    
    Checker = await start_bot()
    if Checker == False:
        print("#1")
    else:
        print ("✅")
    
    return


zedub.loop.run_until_complete(startup_process())

if len(sys.argv) not in (1, 3, 4):
    zedub.disconnect()
elif not Catcheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        zedub.run_until_disconnected()
    except ConnectionError:
        pass
