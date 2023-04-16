from telethon import TelegramClient, events

API_ID = 29918051
API_HASH = "793e62b1b2aefe53f84976d38215959e"
bot_token = "5746131579:AAEL2ySw1sVRwsFdqekn9L4QO6mix6do9zE"

elnur = TelegramClient('elnur', API_ID, API_HASH).start(bot_token=bot_token)

# Bot-a /start komandası göndərildikdə cavab verəcək funksiya
@elnur.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    await event.respond('Salam!')

# Telegram-a qoşuluruq
with client:
    elnur.loop.run_until_complete(client.send_message('me', '/start'))
    elnurr.run_until_disconnected()
