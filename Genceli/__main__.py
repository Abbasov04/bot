from telethon import TelegramClient, events
from Genceli.start import *


api_id = 29918051  # API ID-nizi burada daxil edin
api_hash = '82539501ec5d09ac20d414e377cdefd9'  # API HASH-nizi burada daxil edin
bot_token = '5597264378:AAFghbb1GYbSSKpqMeJ6a2LUMXYUb--M-Fs'  # Botunuzun tokeni burada daxil edin

elnur = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

@elnur.on(events.NewMessage(pattern='/hello'))
async def handler(event):
    await event.respond('Hello, World!')

if __name__ == '__main__':
    elnur.run_until_disconnected()
