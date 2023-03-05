from pyrogram import Client, filters
from pyrogram.types import Message,

from asyncio import sleep

@Client.on_message(command(["sudo"]))
async def sudo(_, message: Message):
      await message.reply_text("⭐️ Sahiblər:\n\n1➤ @ElnurGenCeLi\n2➤ @rapunzzel_z")
