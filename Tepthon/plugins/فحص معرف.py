from Tepthon import zedub
from Tepthon.core.logger import logging
import re
import requests
from telethon.sync import TelegramClient, events

@zedub.zed_cmd.on(events.NewMessage(pattern='nft'))
async def checknft(event):
    try:
        chat_id = event.chat_id
        nft = event.text.split()[1]
        img = f'https://nft.fragment.com/username/{nft}.webp'
        message = await client.send_file(chat_id, img, caption=f'*Yes, this is the nft : {nft}*', parse_mode="Markdown")
        await client.send_message(chat_id, f'Yes, this is the nft : {nft}', reply_to=message)
    except:
        await event.reply(f'*Sorry, this username is not nft : {nft}*', parse_mode="Markdown")
