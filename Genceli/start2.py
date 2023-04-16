from telethon import TelegramClient, events

api_id = 29918051
api_hash = "793e62b1b2aefe53f84976d38215959e"
bot_token = "5746131579:AAEL2ySw1sVRwsFdqekn9L4QO6mix6do9zE"

elnur = TelegramClient('elnur', api_id, api_hash).start(bot_token=bot_token)

# Bot komutları için event handler
@elnur.on(events.NewMessage(pattern='/start2'))
async def start(event):
    await event.respond('Botunuz başarıyla başlatıldı!')

# Botu çalıştırma
elnur.start()
elnur.run_until_disconnected()
