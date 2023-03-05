from pyrogram import Client, filters
from pyrogram.types import Message,

from asyncio import sleep

@Client.on_message(filters.command(["restart"]))
async def restart(_, message: Message):
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("<b>Heroku Veriləri Yenilənir Zəhmət Olmasa Gözləyin</b>")
        if not message.reply_to_message:
            await sleep(10)
            await wtf.edit("<b>✅Heroku Uğurla Yeniləndi</b>")
