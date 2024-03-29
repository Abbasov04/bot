from telethon import TelegramClient, events
from Genceli.start import *


api_id = 14965050  # API ID-nizi burada daxil edin
api_hash = '38bab2dab10fc1b6a9ba0bf683fd7048'  # API HASH-nizi burada daxil edin
bot_token = '6565277854:AAHUD19Rf3VEBe7ZtDvUxxGEKPG0LswTy64'  # Botunuzun tokeni burada daxil edin

elnur = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

@elnur.on(events.NewMessage(pattern='/hello'))
async def handler(event):
    await event.respond('Hello, World!')

if __name__ == '__main__':
    elnur.run_until_disconnected()
