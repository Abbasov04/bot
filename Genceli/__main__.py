from telethon import TelegramClient, events

api_id = 29918051  # API ID-nizi burada daxil edin
api_hash = '793e62b1b2aefe53f84976d38215959e'  # API HASH-nizi burada daxil edin
bot_token = '5746131579:AAEL2ySw1sVRwsFdqekn9L4QO6mix6do9zE'  # Botunuzun tokeni burada daxil edin

elnur = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

@elnur.on(events.NewMessage(pattern='/hello'))
async def handler(event):
    await event.respond('Hello, World!')

if __name__ == '__main__':
    elnur.run_until_disconnected()
