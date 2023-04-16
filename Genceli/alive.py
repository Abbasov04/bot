
# Bot-a /start komandası göndərildikdə cavab verəcək funksiya
@elnur.on(events.NewMessage(pattern='/sa'))
async def start_handler(event):
    await event.respond('Salam!')

