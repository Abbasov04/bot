from telethon import events, TelegramClient

@elnur.on(events.NewMessage(pattern='/start2'))
async def start_handler(event):
    await event.respond('Salam! Botumuzla əlaqə yaratdığınız üçün təşəkkür edirik.')
