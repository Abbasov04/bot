@elnur.on(events.NewMessage(pattern='/hello'))
async def hello_handler(event):
    await event.respond('Salam!')
