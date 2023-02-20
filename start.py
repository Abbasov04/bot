from telethon import Button
from telethon import events
from telethon import TelegramClient
import random, os, logging, asyncio
from asyncio import sleep
from telethon.tl.types import ChannelParticipantsBots
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.sessions import StringSession
from os import remove
from telethon.tl.functions.users import GetFullUserRequest


logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)


# config 
API_ID = 29918051
API_HASH = "793e62b1b2aefe53f84976d38215959e"
bot_token = "5746131579:AAEDzPqfVsHst13-AlVCxs3Z2rZqOly8fPw"


anlik_calisan = []

tekli_calisan = []


#Client 
elnur = TelegramClient('elnur', API_ID, API_HASH).start(bot_token=bot_token)

SUDO_USERS = 5317589296
log_qrup = -1001875414285
    
@elnur.on(events.NewMessage(pattern="^/start$"))
@elnur.on(events.NewMessage(pattern="^/start@GenceliRoBot$"))
async def start(event):
    await event.respond("**🚸 Salam Aleykum Mən @ElnurGenCeLi - Tərəfindən Yaradılmış Asistant Botuyam💓\n🚷 Botu Qrupda İstifadə Etmək Üçün Yetki Verilməlidi.**")

@elnur.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in elnur.iter_participants(event.chat_id):
     ad = f"{usr.first_name}"
     await event.respond(f"**🧔🏻‍♂️Sənin Adın:\n{ad}**")

@elnur.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in elnur.iter_participants(event.chat_id):
     idd = f"{usr.id} "
     await event.respond(f"**🆔Sənin ID:\n`{idd}`**")

@elnur.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in elnur.iter_participants(event.chat_id):
     profil = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await elnur.send_message(log_qrup, f"ℹ️ **Yeni istifadəçi -** {profil}")
     await event.respond(f"**👤Sənin Profilin:\n{profil}**")

@elnur.on(events.NewMessage(pattern="^/start$"))
@elnur.on(events.NewMessage(pattern="^/start@GenceliRoBot$"))
async def start(event):
    await event.respond("**Qrupa Əlavə Etmək Üçün Aşağıdaki Düyməyə Bas.❤️‍🩹**",
            buttons=(
              
		      [Button.url('Məni Qurupa əlavə et❤️', 'http://t.me/GenceliRoBot?startgroup=a')]
                    ),
                    link_preview=False
                   )

@elnur.on(events.NewMessage(pattern="^/help$"))
@elnur.on(events.NewMessage(pattern="^/help@GenceliRoBot$"))
async def start(event):
    await event.respond("**[ɢᴇɴᴄᴇʟɪ ᴀꜱꜱɪꜱᴛᴀɴᴛ](https://t.me/GenceliRoBot) Botun Əmirləri:\n\n/start - Botu Başlat\n/help - Əmrlərə Bax\n/id - Qrub Və User ID Göstərir\n/banda - Qrupunda Olan Silinmiş Hesaplar\n/tag - Qrubda Userləri 5- Li Tağ Edər\n/tektag - Qrubda Userləri Tək-Tək Tağ Edər\n/adtag - Qrubda Userləri Qəribə Adlarlar Tağ Edər\n/cancel - Tağ Prosesini Dayandırar**")
    

@elnur.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("ℹ️ Bu əmr qruplar üçün etibarlıdır.")
  
  admins = []
  async for admin in elnur.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("Bunu həyata keçirmək üçün admin olmalısınız.")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Əvvəlki  mesajlara cavab verməyin")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("️️Tağ etmək üçün səbəb yazın **Məsələn:\n/tag Gəlin Qruba**")
  else:
    return await event.respond("️Tağ etmək üçün səbəb yazın **Məsələn:\n/tag Gəlin Qruba**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in elnur.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"❤️‍🩹 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**Tağ uğurla dayandırıldı ⛔**")
        return
      if usrnum == 5:
        await elnur.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in elnur.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"❤️‍🩹 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**Tağ uğurla dayandırıldı ⛔**")
        return
      if usrnum == 5:
        await elnur.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@elnur.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)

@elnur.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("ℹ️ Bu əmr qruplar üçün etibarlıdır.")
  
  admins = []
  async for admin in elnur.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("Bunu həyata keçirmək üçün admin olmalısınız.")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Əvvəlki  Mesajlara Cavab Verməyin")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("️️Tağ etmək üçün səbəb yazın **Məsələn:\n/tektag Gəlin Qruba**")
  else:
    return await event.respond("️️Tağ etmək üçün səbəb yazın **Məsələn:\n/tektag Gəlin Qruba**")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in elnur.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**❤️‍🩹 - [{usr.first_name}](tg://user?id={usr.id}) \n**"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Tağ uğurla dayandırıldı ⛔**")
        return
      if usrnum == 1:
        await elnur.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in elnur.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"❤️‍🩹 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Tağ uğurla dayandırıldı ⛔**")
        return
      if usrnum == 1:
        await elnur.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@elnur.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)

adlar = ['Üzümlü kek ✨', 'Nar çiçeği ✨', 'Papatya 🌼', 'Karanfil ✨', 'Gül 🌹', 'Ayıcık 🐻', 'Mutlu panda 🐼', 'Ay pare 🌛', 'Ballı lokma ✨', 'Lale 🌷', 'Ahtapot 🐙', 'Zambak ⚜️', 'Akasya 🌿', 'Akşam Sefası 🌛', 'Begonvil 🥀', 'Begonya 🪴', 'Bambu 🎍', 'Fesleğen 🌿', 'Kasımpatı 🌸', 'Manolya 🌾', 'Boncuk 🧿', 'Badem 🥭', 'Minnoş 🐹', 'Ponçik 🐣', 'Pofuduk 🐼', 'Unicorn 🦄', 'Karamel 🍫', 'Fındık 🌰', 'Fıstık 🥜', 'Pamuk ☁️', 'Minnoş 🥰', 'Zeytin 🫒', 'Afrodit 🧚🏻', 'Nergis ✨', 'Sümbül ☘️', 'Nilüfer ☘️', 'Menekşe ⚜️', 'Lavanta ✨', 'Gül pare 🌺', 'Reyhan 🌷', 'Kaktüs 🌵', 'Buket 💐', 'Başak 🌾', 'Kar Tanesi ❄️', 'Tospik 🐢', 'Kelebek 🦋', 'Tavşan 🐰', 'Şeker 🍬', 'Böğürtlen ☘️', 'Orkide ☘️', 'Manolya ✨', 'Ayçiçeği 🌻', 'Tweety 🐥', 'Star ✨', 'Yonca 🍀', 'Ateş böceği ✨']

@elnur.on(events.NewMessage(pattern="^/adtag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("ℹ️ Bu əmr qruplar üçün etibarlıdır.")
  
  admins = []
  async for admin in elnur.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("Bunu həyata keçirmək üçün admin olmalısınız.")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Əvvəlki  Mesajlara Cavab Verməyin")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("️️Tağ etmək üçün səbəb yazın **Məsələn:\n/adtag Gəlin Qruba**")
  else:
    return await event.respond("️️Tağ etmək üçün səbəb yazın **Məsələn:\n/adtag Gəlin Qruba**")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in elnur.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(adlar)}](tg://user?id={usr.id}) "
      if event.chat_id not in tekli_calisan:
        await event.respond("**Tağ uğurla dayandırıldı ⛔**")
        return
      if usrnum == 1:
        await elnur.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in elnur.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(adlar)}](tg://user?id={usr.id}) "
      if event.chat_id not in tekli_calisan:
        await event.respond("**Tağ uğurla dayandırıldı ⛔**")
        return
      if usrnum == 1:
        await elnur.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@elnur.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)

@elnur.on(events.NewMessage(pattern='@ElnurGenCeLi'))
@elnur.on(events.NewMessage(pattern='ElnurGenCeLi'))
async def sahib(event):
    await event.reply("🚷 Sahibimi Az Tağ Elə")

@elnur.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(random.choice(userjoin))

@elnur.on(events.ChatAction)
async def handler(event):
    if event.user_left:
        await event.reply("Əla Birdə Gəlmə")

userjoin = (

    "Xoş Gəldin Balam❤️",
    "Kimləri Görürəm🙈",
    "Sən Nə Əcəb Gəlibsən Bura?🙄",
    "Gəl Xala Qurban, Gəl Gör Nə Tapmışam😀",
)

@elnur.on(events.NewMessage(pattern="^/id ?(.*)"))
async def id(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_id = previous_message.sender_id
        chat_id = event.chat_id
        if event.is_private:
            return await event.reply(f"**Sizin Telegram id:** `{user_id}`")
        else:
            return await event.reply(f"**İstifadəçi id:** `{user_id}`\n**Qrup id:** `{chat_id}`")


    else:
        user_id = event.sender_id
        chat_id = event.chat_id
        if event.is_private:
            return await event.reply(f"**Sizin Telegram id:** `{user_id}`")
        else:
            return await event.reply(f"**İstifadəçi id:** `{user_id}`\n**Qrup id:** `{chat_id}`")


@elnur.on(events.NewMessage(pattern="^/banda ?(.*)"))
async def banda(event):
    if not event.is_group:
        return await event.reply("ℹ️ Bu əmr qruplar üçün etibarlıdır.")
    info = await event.client.get_entity(event.chat_id)
    title = info.title if info.title else "This chat"
    mentions = f'**{title}** qrupunda olan silinmiş hesaplar:\n'
    deleted = 0
    async for user in event.client.iter_participants(event.chat_id):
        if user.deleted:
            mentions += f"\nSilinmiş hesap `{user.id}`"
            deleted += 1
            await event.client.kick_participant(event.chat_id, user.id)
    mentions += f"\nSilinmiş hesaplar` = {deleted}`\n\n__• By @GenceliRoBot__"
    await event.reply(mentions)


@elnur.on(events.NewMessage(pattern='(?i)salam+'))
async def salam(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(salam)}")

salam = (
"Salam",
"Salam Kişi",
"Salam Balam",
"Salamdaa",
"Uşş balama salam",
"Salam Cənab 🫶",
"Salam Lələ 🔥",
)

@elnur.on(events.NewMessage(pattern='(?i)necəsən+'))
async def necesen(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(necesen)}")

necesen = (
"Saol",
"Həkimsən ?",
"Ə belədana 😂",
"What",
"İyyim aşkım sen ?",
"yaxşı olmağa çalışıram",
"Mən başımı buraxe sən necəsən 😂",
)

@elnur.on(events.NewMessage(pattern='(?i)sağol+'))
async def sagol(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(sagol)}")

sagol = (
"Salam Sağol",
"Hara gedsən",
"Yatıram demə🥲",
"Sağolunnn yenə gözləyəriyy🙈",
"Uşş balam Sağol",
"Sağol canım benim 🫶",
"Sağol Kişi 🔥",
)

@elnur.on(events.NewMessage(pattern='(?i)getdim+'))
async def getdim(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(getdim)}")

getdim = (
"Hara",
)

@elnur.on(events.NewMessage(pattern='(?i)gəldim+'))
async def geldim(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(geldim)}")

geldim = (
"Xoş Gəldin ❤️",
)

@elnur.on(events.NewMessage(pattern='(?i)ban+'))
async def ban(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ban)}")

ban = (
"Vəhşii",
"Həri Vəhşii",
"Vəhşi Panteramm kimə ban atdın",
"Havada ban kokusu var",
)

@elnur.on(events.NewMessage(pattern='(?i)sik+'))
@elnur.on(events.NewMessage(pattern='(?i)göt+'))
@elnur.on(events.NewMessage(pattern='(?i)amciq+'))
@elnur.on(events.NewMessage(pattern='(?i)amcig+'))
@elnur.on(events.NewMessage(pattern='(?i)amciğ+'))
@elnur.on(events.NewMessage(pattern='(?i)cındır+'))
@elnur.on(events.NewMessage(pattern='(?i)qəhbə+'))
@elnur.on(events.NewMessage(pattern='(?i)peysər+'))
@elnur.on(events.NewMessage(pattern='(?i)xnxx+'))
@elnur.on(events.NewMessage(pattern='(?i)xnxn+'))
@elnur.on(events.NewMessage(pattern='(?i)pornhub+'))
async def soyus(event: events.NewMessage.Event):
    await event.reply("Söyüş Söymə.!🚷")
    await event.delete()

print(">> Bot işləyir narahat olmayın.<<")
elnur.run_until_disconnected()
