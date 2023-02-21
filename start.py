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
      usrnum += 5
      usrtxt += f"[{random.choice(adlar)}](tg://user?id={usr.id}) "
      if event.chat_id not in tekli_calisan:
        await event.respond("**Tağ uğurla dayandırıldı ⛔**")
        return
      if usrnum == 5:
        await elnur.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in elnur.iter_participants(event.chat_id):
      usrnum += 5
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

elnur = ('Buda kimmiş də miş miş👀😁😍','🙄👉🤲Aağil','🙄 Sən dediyim sözü elədin? 😐','Həyatımın dolması 🥲 nassın😍','Mənə niyə elə baxırsan? 🌝','İkinci planda olmaqdansa, plana daxil olmamağı seçərəm.  🎯','səni basqa qrublardada görmüsdüm ','Ac olanda sən o sən deyilsən','Niyə yalan danışırsan adamın üstündə patalok var','Həci necəsən ficuuu ','köhnə məkanın yeni sakini ','günün günnən durdun uzax de görüm haramı bəyənmədin','deyrlər ölübsən🤔','Güçlüyüm... Çünkü başka seçeneğim yok düşersem tutanım olmayacak biliyorum...🚬','gəl bir birimizi arka sokaklar bitənə qədər sevək❤️','corona belə böyüdü sən böyümədin','corona belə unduldu səni unuda bilmədim🚬','səni sevirəm sözündə neçə dənə samit var','oğlanlar niyə az yaşayır','bitkilər yaşlandıqcamı ölər yoxsa baxımsızlıqdanmı','isti havada çay içirsən hələdə','allah rəhmət eləsin','tez gəlin hədiyyəli yarışımız basladı','Benim hayelerim kelebeğin ömrü kadar yaşar 💔🥀','Çiçəklərə aşağıdan baxmağa gedirəm..➰','susмuş вir qadın üçün... вiтмiş вir adaмsan.! 🖤','𝚂ə𝚏𝚕ə𝚛𝚒𝚗𝚒 𝚞̈𝚣𝚕ə𝚛𝚒𝚗ə 𝚟𝚞𝚛𝚖𝚊𝚍𝚒𝚐̆𝚒𝚖𝚒𝚣 𝚞̈𝚌̧𝚞̈𝚗 𝚘̈𝚣𝚕𝚎𝚛𝚒𝚗𝚒 𝚚𝚞̈𝚜𝚞𝚛𝚜𝚞𝚣 𝚜𝚊𝚗𝚊𝚗 𝚒𝚗𝚜𝚊𝚗𝚕𝚊𝚛 𝚟𝚊𝚛😒','Güclü olmağa məndən daha çox ehtiyacın var, çünki haqsız olduğunu ürəyinin bir yerində bilirsən.🤙','Makiyaj və üz boyalarınıza güvənməyin. Yollar da gözəldir, lakin altından kanalizasiya keçir.👋😉','𝙸̇𝚝𝚒𝚛𝚍𝚒𝚢𝚒𝚗 𝚟𝚊𝚡𝚝𝚒 𝚚𝚊𝚢𝚝𝚊𝚛𝚊 𝚋𝚒𝚕𝚖ə𝚍𝚒𝚢𝚒𝚗 𝚔𝚒𝚖𝚒 𝚎𝚕ə𝚍𝚒𝚢𝚒𝚗 𝚙𝚒𝚜𝚕𝚒𝚢𝚒 𝚍ə 𝚑𝚎𝚌̧ 𝚟𝚊𝚡𝚝 𝚍𝚞̈𝚣ə𝚕𝚍ə 𝚋𝚒𝚕𝚖𝚎𝚢ə𝚌𝚎𝚔𝚜ən😐','𝙱𝚒𝚛𝚊𝚣 𝚒𝚗𝚜𝚊𝚗 𝚘𝚕 𝚍𝚎𝚢e𝚌ə𝚖 𝚊𝚖𝚖𝚊 𝚜ə𝚗𝚒 𝚍ə 𝚌̧ə𝚝𝚒𝚗 𝚟ə𝚣𝚒𝚢𝚢ə𝚝𝚍ə 𝚚𝚘𝚢𝚖𝚊𝚐̆ 𝚒𝚜𝚝ə𝚖𝚒𝚛ə𝚖🤧','İnsanlığa dəvət etdikdə yolu soruşan insanlar var.🔥😂','Qoyduğum şeyləri öz yerində tapa bilmirəm. Bəzilərini adam yerinə qoydum, indi gəl tap görün necə tapırsan✊','Ayə biri bunu aparsın🫢','Əgər bu həyatda öz tayını tapa bilmirsənsə üzülmə, deməli sən tayı bərabəri olmayan birisən.Qabriel Qarsia Markuez (Meksikalı yazıçı)🥲','Xoş Gəldim Nəfəs🥲','Gəlmirsən Balaca😒','Kimə Yazısan??? 🤨','Çirkin Çocuq Gəl😌','Cikolatam😍','Aaa Səndə Burdasan😳','Al Sənə Çikolata🤓👉🍫','Sevmirsən Məni?🙁 Onda Ol🙂','Haa Düz derisən?🧐','Bu Kimdir😁','Gəl Dava Edəx😁💪','Bax Sənə Nə Aldım😌👉🐒','Nə Gözəlsən🤢 Çirkin Ördək Yavrusu','Sən Kimsən🙄A Gədə👀','Gəl Sənə Sürpürüzüm var🤫','Ooo Çox Gözəlsin🤌🤐Bal','Şəxsiyə Yaz😌dünbələx','Gəl Görüm Hələ🧐 Nə demisən Mənə😬','Ayib Olsun😫 Niyə Yazmırsan😑','Bezdim Səndən🥲','Bu Neçədir✌️🙂','Nömrəni ver də Vpda yazışa🙊','👉👀 Gözün Çıxsın gəl😒','ımmm Gəl yogo yapalım🧘‍♀🤭','gəl sənə bıra süzdüm😪🍻','Ağlımı Başımdan ala şəxs😵‍💫gəl mənə doğru','Səni gördüm qızmam qalxdə🤒',) 


@elnur.on(events.NewMessage(pattern="^/rose ?(.*)"))
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
    return await event.respond("️️️Tağ etmək üçün səbəb yazın **Məsələn:\n/rose Gəlin Qruba**")
  else:
    return await event.respond("️️Tağ etmək üçün səbəb yazın **Məsələn:\n/rose Gəlin Qruba**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in elnur.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(elnur)}](tg://user?id={usr.id}) "
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
      usrtxt += f"[{random.choice(elnur)}](tg://user?id={usr.id}) "
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
  
futbol = ('Maldonado', 'Lionel Messi', 'Bobô', 'Matías Delgado', 'Márcio Nobre1', 'Rodrigo Tello', 'Federico Higuaín', 'Lamine Diatta', 'Édouard Cissé', 'Gordon Schildenfeld', 'Filip Hološko', 'Anthony Šerić', 'Tomáš Sivok', 'Tomáš Zápotočný', 'Fabian Ernst', 'Michael Fink', 'Matteo Ferrari', 'Rodrigo Tabata', 'Ricardo Quaresma', 'Roberto Hilbert', 'Guti', 'Marco Aurélio1', 'Manuel Fernandes', 'Simao Sabrosa', 'Hugo Almeida', 'Sidnei', 'Bébé', 'Júlio Alves', 'Edú', 'Julien Escudé', 'Allan McGregor', 'Dentinho', 'Mamadou Niang', 'Pedro Franco', 'Michael Eneramo', 'Atiba Hutchinson', 'Ramon Motta', 'Jermaine Jones', 'Dany Nounkeu', 'Demba Ba', 'José Sosa', 'Alexander Milošević', 'Daniel Opare', 'Duško Tošić', 'Andreas Beck', 'Luiz Rhodolfo', 'Mario Gómez', 'Denis Boyko', 'Aras Özbiliz', 'Alexis Delgado', 'Marcelo Guedes', 'Fabri', 'Adriano Correia', 'Talisca', 'Vincent Aboubakar', 'Ryan Babel', 'Matej Mitrović', 'Pepe', 'Álvaro Negredo', 'Jeremain Lens', 'Gary Medel', 'Cyle Larin', 'Vágner Love', 'Domagoj Vida', 'Enzo Roco', 'Loris Karius', 'Adem Ljajić', 'Nicolas Isimat-Mirin', 'Shinji Kagawa', 'Tyler Boyd', 'Douglas', 'Víctor Ruiz', 'Pedro Rebocho', "Georges-Kévin N'Koudou", 'Muhammed Elneni', 'Abdoulay Diaby', 'Ajdin Hasić', 'Kevin-Prince Boateng', "Fabrice N'Sakala", 'Bernard Mensah', 'Welinton', 'Francisco Montero', 'Josef de Souza', 'Valentin Rosier', 'Raşit Gezzal', 'Alex Teixeira', 'Michy Batshuayi', 'Miralem Pjanić', 'Gedson Fernandes', 'Romain Saïss', 'Mert Günok', 'Ersin Destanoğlu', 'Emre Bilgin', 'Goktug Baytekin', 'Domagoj Vida', 'Welinton', 'Douglas', 'Fabrice NSkala', 'Umut Meras', 'Francisco Montero', 'Valentin Rosier', 'Kerem Kalafat', 'Rıdvan Yılmaz', 'Serdar Saatçi', 'Serkan Emrecan Terzi', 'Aytug Batur Komec', 'Atiba Hutchinson', 'Mehmet Topal', 'Miralem Pjanic', 'Adem Ljajic', 'Alex Teixeira', 'Necip Uysal', 'Gökhan Töre', 'Rachid Ghezzal', 'Oğuzhan Özyakup', 'Georges-Kevin Nkoudou', 'Muhayer Oktay', 'Can Bozdogan', 'Berkay Vardar', 'Emirhan İlkhan', 'Emirhan Delibas', 'Demir Tiknaz', 'Jeremain Lens', 'Michy Batshuayi', 'Kenan Karaman', 'Cyle Larin', 'Güven Yalçın', 'Koray Yagci', 'Ariel Ortega', 'Robert Enke', 'Vladimir Beschastnykh', 'Ivaylo Petkov', 'Sergiy Rebrov', 'Stjepan Tomas', 'Pierre van Hooijdonk', 'Marco Aurelio', 'Fábio Luciano', 'Mert Nobre', 'Fabiano', 'Alex De Souza', 'Stephen Appiah', 'Nicolas Anelka', 'Mateja Kežman', 'Edu Dracena', 'Diego Lugano', 'Deivid', 'Roberto Carlos', 'Wederson', 'Claudio Maldonado', 'Josico', 'Daniel Güiza', 'Fábio Bilica', 'André Santos', 'Cristian Baroni', 'Miroslav Stoch', 'Issiar Dia', 'Mamadou Niang', 'Joseph Yobo', 'Emmanuel Emenike', 'Reto Ziegler', 'Henri Bienvenu', 'Moussa Sow', 'Dirk Kuyt', 'Miloš Krasić', 'Raul Meireles', 'Pierre Webó', 'Bruno Alves', 'Michal Kadlec', 'Samuel Holmén', 'Diego', 'Simon Kjær', 'Fernandão', 'Abdoulaye Ba', 'Fabiano Ribeiro', 'Nani', 'Josef de Souza', 'Robin van Persie', 'Lazar Marković', 'Aatif Chahechouhe', 'Gregory van der Wiel', 'Roman Neustädter', 'Martin Škrtel', 'Jeremain Lens', 'Oleksandr Karavayev', 'Mathieu Valbuena', 'Nebil Dirar', 'Carlos Kameni', 'Mauricio Isla', 'Elif Elmas', 'Roberto Soldado', 'Giuliano', 'Luís Neto', 'Vincent Janssen', 'André Ayew', 'Islam Slimani', 'Michael Frey', 'Diego Reyes', 'Jailson', 'Yassine Benzia', 'Victor Moses', 'Miha Zajc', 'Max Kruse', 'Allahyar Seyyadmeneş', 'Vedat Muriqi', 'Garry Rodrigues', 'Zanka', 'Adil Rami', 'Luiz Gustavo', 'Simon Falette', 'Filip Novák', 'Mame Thiam', 'José Sosa', 'Mauricio Lemos', 'Enner Valencia', 'Marcel Tisserand', 'Mbwana Samatta', 'Papiss Cissé', 'Kemal Ademi', 'Dimitris Pelkas', 'Diego Perotti', 'Attila Szalai', 'Bright Osayi-Samuel', 'Mesut Özil', 'Steven Caulker', 'Kim Min-jae', 'Diego Rossi', 'Mërgim Berisha', 'Max Meyer', 'Miguel Crespo', 'Erol Bulut', 'Saffet Akbaş', 'Tayfun Korkut', 'Elvir Bolić', 'Mustafa Doğan', 'Samuel Johnson', 'Abdullah Ercan', 'Ogün Temizkanoğlu', 'Semih Şentürk', 'Ali Güneş', 'Serhat Akın', 'Ümit Özat', 'Volkan Demirel', 'Tuncay Şanlı', 'Selçuk Şahin', 'Fabio Luciano', 'Mehmet Yozgatlı', 'Mehmet Aurelio', 'Serkan Balcı', 'Önder Turacı', 'Uğur Boral', 'Gökhan Gönül', 'Gökçek Vederson', 'Colin Kâzım Richards', 'Emre Belözoğlu', 'Mehmet Topuz', 'Bekir İrtegün', 'Caner Erkin', 'Hasan Ali Kaldırım', 'Mehmet Topal', 'Alper Potuk', 'Şener Özbayraklı', 'Ozan Tufan', 'Aykut Erçetin', 'Çağlar Birinci', 'Gökhan Zan', 'Ceyhun Gülselam', 'Aydın Yılmaz', 'Selçuk İnan', 'Johan Elmander', 'Felipe Melo', 'Dida', 'Cafu', 'Stam', 'Nesta', 'Maldini', 'Pirlo', 'Gattuso', 'Seedorf', 'Kaka', 'Shevchenko', 'Inzaghi', 'Crespo', 'Diego Altube', 'Thibaut Courtois', 'Alphonse Areola', 'Andriy Lunin', 'Lucas Canizares', 'Luis Lopez', 'Toni Fuidias', 'Diego Del Alamo', 'Luis Federico', 'Sergio Ramos', 'Raphael Varane', 'Daniel Carvajal', 'Adrian De La Fuente', 'Ferland Mendy', 'Marcelo', 'Eder Militao', 'Alvaro Odriozola', 'Victor Chust', 'Sergio Santos', 'Pablo Ramon Parra', 'Miguel Gutierrez', 'David Alaba', 'Jesus Vallejo', 'Rafa Marin', 'Mario Gila', 'Reinier', 'Marco Asensio', 'Federico Valverde', 'Brahim Diaz', 'Luka Modric', 'Toni Kroos', 'Isco', 'Carlos Casemiro', 'Lucas Vazquez', 'Martin Odegaard', 'Marvin Park', 'Sergio Arribas', 'Antonio Blanco', 'Hugo Duro', 'Eduardo Camavinga', 'Dani Ceballos', 'Peter Gonzalez', 'Karim Benzema', 'Luka Jovic', 'Eden Hazard', 'Gareth Bale', 'Vinicius Junior', 'Rodrygo', 'James Rodriguez', 'Mariano Diaz', 'Borja Mayoral', 'Oscar Aranda', 'Juan Latasa', 'Neto', 'Marc-Andre Ter Stegen', 'Inaki Pena', 'Arnau Tenas', 'Lazar Carevic', 'Jordi Alba', 'Sergi Roberto', 'Ronald Araujo', 'Samuel Umtiti', 'Nelson Semedo', 'Clement Lenglet', 'Dani Morer', 'Junior Firpo', 'Gerard Pique', 'Sergio Akieme', 'Santiago Ramos', 'Arnau Comas', 'Sergino Dest', 'Oscar Mingueza', 'Eric Garcia', 'Emerson', 'Alejandro Balde', 'Dani Alves', 'Mika Marmol', 'Sergio Busquets', 'Hiroki Abe', 'Alex Collado', 'Frenkie De Jong', 'Ivan Rakitic', 'Arturo Vidal', 'Riqui Puig', 'Guillem Jaime', 'Miralem Pjanic', 'Philippe Coutinho', 'Carles Alena', 'Konrad De La Fuente', 'Ilaix Moriba', 'Matheus Fernandes', 'Yusuf Demir', 'Nico Gonzalez', 'Abde Ezzalzouli', 'Alvaro Sanz', 'Ferran Jutgla', 'Matheus Pereira', 'Lucas De Vega', 'Estanis Pedrola', 'Adama Traore', 'Luis Suarez', 'Ousmane Dembele', 'Antoine Griezmann', 'Ansu Fati', 'Lionel Messi', 'Rey Manaj', 'Martin Braithwaite', 'Memphis Depay', 'Sergio Agüero', 'Luuk De Jong', 'Ilias Akhomach', 'Ferran Torres', 'Pierre Aubameyang', 'Albert Riera', 'Milan Baroš', 'Tomáš Ujfaluši', 'Mehmet Batdal', 'Serkan Kurtuluş', 'Yiğit Gökoğlan', 'Hakan Balta', 'Fernando Muslera', 'Semih Kaya', 'Emmanuel Eboué', 'Yekta Kurtuluş', 'Engin Baytar', 'Emre Çolak', 'Sabri Sarıoğlu', 'Servet Çetin', 'Necati Ateş', 'Ufuk Ceylan', 'Sercan Yıldırım', 'Fernando Muslera', 'Felipe Melo', 'Hamit Altıntop', 'Gökhan Zan', 'Blerim Džemaili', 'Aydın Yılmaz', 'Selçuk İnan', 'Umut Bulut', 'Wesley Sneijder', 'Bruma', 'Alex Telles', 'Burak Yılmaz', 'Sinan Gümüş', 'Goran Pandev', 'Aurélien Chedjou', 'Fernando Muslera', 'Mariano', 'Maicon', 'Serdar Aziz', 'Ahmet Çalık', 'Tolga Ciğerci', 'Yasin Öztekin', 'Selçuk İnan', 'Eren Derdiyok', 'Younès Belhanda', 'Sinan Gümüş', 'Martin Linnes', 'Ryan Donk', 'Cédric Carrasso', 'Şener Özbayraklı', 'Omar Elabdellaoui', 'Taylan Antalyalı', 'Henry Onyekuru', 'Ryan Babel', 'Radamel Falcao', 'Halil Dervişoğlu', 'Oghenekaro Etebo', 'Martin Linnes', 'Ryan Donk', 'Oğulcan Çağlayan', 'Kerem Aktürkoğlu', 'Ömer Bayram', 'Emre Akbaba', 'Cristiano Ronaldo', 'Pele', 'Maradona', 'Ronaldo', 'Thierry Henry', 'Kaka', 'Sergio Agüero', 'Xavi', 'Ruud Gullit', 'Arthur Zico', 'Lev Yashin', 'Iniesta', 'Lothar Matthäus', 'Giuseppe Meazza', 'Franz Beckenbauer', 'George Best', 'Roberto Baggio', 'Johan Cruyff', 'Luis Figo', 'Andrea Pirlo', 'Marco Van Basten', 'Zlatan Ibrahimovic', 'Sandro Mazzola', 'Ferenc Puskas', 'Zinedine Zidane', 'Alfredo Di Stéfano', 'Rio Ferdinand', 'Paolo Maldini', 'Robin van Persie', 'Iker Casillas', 'Neymar', 'Fabio Cannavaro', 'Yaya Toure', 'Edinson Cavani', 'Gabriel Batistuta', 'Thiago Silva', 'Dennis Bergkamp', 'Franck Ribery', 'Carles Puyol', 'Mesut Özil', 'Dani Alves', 'David Silva', 'Karim Benzema', 'Javier Zanetti', 'Radamel Falcao', 'Bastian Schweinsteiger', 'Gianluigi Buffon', 'Arjen Robben', 'Wayne Rooney', 'Luis Suarez', 'Mbappe', 'Juan Román Riquelme', 'Sergio Ramos', 'Muhammed Salah', 'Cesc Fabregas', 'Gerard Pique', 'Pepe', 'Didier Drogba', 'Robert Lewandowski', 'David Villa', 'Wesley Sneijder', 'Philipp Lahm', "Samuel Eto'o", 'Carlos Tevez', 'Sergio Busquets', 'Samir Nasri', 'Eden Hazard', 'Diego Forlan', 'Klaas Jan Huntelaar', 'Sabri Sarıoğlu')


@elnur.on(events.NewMessage(pattern="^/ftag ?(.*)"))
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
    return await event.respond("️️️Tağ etmək üçün səbəb yazın **Məsələn:\n/ftag Gəlin Qruba**")
  else:
    return await event.respond("️️Tağ etmək üçün səbəb yazın **Məsələn:\n/ftag Gəlin Qruba**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in elnur.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(futbol)}](tg://user?id={usr.id}) "
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
      usrtxt += f"[{random.choice(futbol)}](tg://user?id={usr.id}) "
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

mafia = (
"Sənin oyundakı rolun 👮🏼 Çavuş!",
"Sənin oyundakı rolun 🐺 Oboroten!",
"Sənin oyundakı rolun 🤓 Satqın!",
"Sənin oyundakı rolun 💃 Məşuqə!",
"Sənin oyundakı rolun 🤵🏼 Mafia!",
"Sənin oyundakı rolun 🧙‍ Maq!",
"Sənin oyundakı rolun 🤞🏼 Şanslı Vətəndaş!",
"Sənin oyundakı rolun 💣 Kamikadze!",
"Sənin oyundakı rolun 👩🏼‍💻 Jurnalist!",
"Sənin oyundakı rolun 🤹🏻 Aferist!",
"Sənin oyundakı rolun 👨🏼 Vətəndaş!",
"Sənin oyundakı rolun 🕵🏼 Komissar Kattani!",
"Sənin oyundakı rolun 🎖 Mer!",
"Sənin oyundakı rolun 🔪 Manyak!",
"Sənin oyundakı rolun 👨🏼‍⚕️️Doktor!",
"Sənin oyundakı rolun 🤵🏻 Don!",
"Sənin oyundakı rolun 🧙🏼 Bomj!",
"Sənin oyundakı rolun 👨🏼‍💼 Vəkil!",
"Sənin oyundakı rolun 🧟 Arsonist!",
"Sənin oyundakı rolun 🕴️ Qatil!",
"Sənin oyundakı rolun 🧝🏻‍♀️Şəhzadə!",
"Sənin oyundakı rolun 🧟‍♀️Cadugar!",
"Sənin oyundakı rolun 🧛🏻‍♂️Vampir!",
"Sənin oyundakı rolun 🧚🏻‍♀️Mələk!",
"Sənin oyundakı rolun 🦹🏻‍♂️BOSS!",
"Sənin oyundakı rolun 🦦Köstəbək!",
"Sənin oyundakı rolun 🦎Buqələmun!",
"Sənin oyundakı rolun 🤡Joker!",
"Sənin oyundakı rolun 🙍🏻‍♂️Məhbus!",
"Sənin oyundakı rolun 🙇🏻‍♂️Oğru!",
"Sənin oyundakı rolun 🕵️Suiqəstçi!",
"Sənin oyundakı rolun 🔮Reviver!",
"Sənin oyundakı rolun 👷🏻‍♂️Mədənçi!",
"Sənin oyundakı rolun 💂Killer!",
"Sənin oyundakı rolun 👻Ruh!",
"Sənin oyundakı rolun 👳🏻‍♂️Satıcı!",
"Sənin oyundakı rolun 👨🏻‍🦱Dedektiv!",
"Sənin oyundakı rolun  👨🏻‍🎤Specialist!",
"Sənin oyundakı rolun ⭐️General!",
"Sənin oyundakı rolun 🥷Ninja!"
)
@elnur.on(events.NewMessage(pattern="^/mafia ?(.*)"))
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
    return await event.respond("️️️Tağ etmək üçün səbəb yazın **Məsələn:\n/mafia Gəlin Qruba**")
  else:
    return await event.respond("️️Tağ etmək üçün səbəb yazın **Məsələn:\n/mafia Gəlin Qruba**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in elnur.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(mafia)}](tg://user?id={usr.id}) "
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
      usrtxt += f"[{random.choice(mafia)}](tg://user?id={usr.id}) "
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
  
bayrag = ['🏳️‍🌈','🏳️‍⚧️','🇦🇫','🇦🇽','🇦🇱','🇩🇿','🇦🇸','🇦🇩','🇦🇴','🇦🇮','🇦🇶','🇦🇬','🇦🇷','🇦🇲','🇦🇼','🇦🇺','🇦🇹','🇦🇿','🇧🇸','🇧🇭','🇧🇩','🇧🇧','🇧🇾','🇧🇪','🇧🇿','🇧🇯','🇧🇲','🇧🇹','🇧🇴','🇧🇦','🇧🇼','🇧🇷','🇻🇬','🇧🇳','🇧🇬','🇧🇫','🇧🇮','🇰🇭','🇨🇲','🇨🇦','🇮🇨','🇨🇻','🇧🇶','🇰🇾','🇨🇫','🇹🇩','🇮🇴','🇨🇱','🇨🇳','🇨🇽','🇨🇨','🇨🇴','🇰🇲','🇨🇬','🇨🇩','🇨🇰','🇨🇷','🇨🇮','🇭🇷','🇨🇺','🇨🇼','🇨🇾','🇨🇿','🇩🇰','🇩🇯','🇩🇲','🇩🇴','🇪🇨','🇪🇬','🇸🇻','🇬🇶','🇪🇷','🇪🇪','🇪🇹','🇸🇿','🇪🇺','🇫🇰','🇫🇴','🇫🇯','🇫🇮','🇫🇷','🇬🇫','🇵🇫','🇹🇫','🇬🇦','🇬🇲','🇬🇪','🇩🇪','🇬🇭','🇬🇮','🇬🇷','🇬🇱','🇬🇩','🇬🇵','🇬🇺','🇬🇹','🇬🇬','🇬🇳','🇬🇼','🇬🇾','🇭🇹','🇭🇳','🇭🇰','🇭🇺','🇮🇸','🇮🇳','🇮🇩','🇮🇷','🇮🇶','🇮🇪','🇮🇲','🇮🇱','🇮🇹','🇯🇲','🇯🇵','🎌','','🇯🇪','🇯🇴','🇰🇿','🇰🇪','🇰🇮','🇽🇰','🇰🇼','🇰🇬','🇱🇦','🇱🇻','🇱🇧','🇱🇸','🇱🇷','🇱🇾','🇱🇮','🇱🇹','🇱🇺','🇲🇴','🇲🇬','🇲🇼','🇲🇾','🇲🇻','🇲🇱','🇲🇹','🇲🇭','🇲🇶','🇲🇷','🇲🇺','🇾🇹','🇲🇽','🇫🇲','🇲🇩','🇲🇨','🇲🇳','🇲🇪','🇲🇸','🇲🇦','🇲🇿','🇲🇲','🇳🇦','🇳🇷','🇳🇵','🇳🇱','🇳🇨','🇳🇿','🇳🇮','🇳🇪','🇳🇬','🇳🇺','🇳🇫','🇰🇵','🇲🇰','🇲🇵','🇳🇴','🇴🇲','🇵🇰','🇵🇼','🇵🇸','🇵🇦','🇵🇬','🇵🇾','🇵🇪','🇵🇭','🇵🇳','🇵🇱','🇵🇹','🇵🇷','🇶🇦','🇷🇪','🇷🇴','🇷🇺','🇷🇼','🇼🇸','🇸🇲','🇸🇹','🇸🇦','🇸🇳','🇷🇸','🇸🇨','🇸🇱','🇸🇬','🇸🇽','🇸🇰','🇸🇮','🇬🇸','🇸🇧','🇸🇴','🇿🇦','🇰🇷','🇸🇸','🇪🇸','🇱🇰','🇧🇱','🇸🇭','🇰🇳','🇱🇨','🇵🇲','🇻🇨','🇸🇩','🇸🇪','🇸🇷','🇨🇭','🇸🇾','🇹🇼','🇹🇯','🇹🇿','🇹🇭','🇹🇱','🇹🇬','🇹🇰','🇹🇴','🇹🇹','🇹🇳','🇹🇷','🇹🇲','🇹🇨','🇹🇻','🇺🇬','🇺🇦','🇦🇪','🇬🇧','🏴󠁧󠁢󠁥󠁮󠁧󠁿','🏴󠁧󠁢󠁳󠁣󠁴󠁿','🏴󠁧󠁢󠁷󠁬󠁳󠁿','🇺🇸','🇺🇾','🇻🇮','🇺🇿','🇻🇺','🇻🇦','🇻🇪','🇻🇳','🇼🇫','🇪🇭','🇾🇪','🇿🇲','🇿🇼',]

@elnur.on(events.NewMessage(pattern="^/btag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr kanal və qrup üçündür!**")
  
  admins = []
  async for admin in elnur.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmr adminlər üçündür**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Əvvəlki  mesajlara cavab verməyin")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("️Tağ etmək üçün səbəb yazın ")
  else:
    return await event.respond("**Tağ etməni başlatmaq üçün səbəb yaz!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in elnur.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(bayrag)}](tg://user?id={usr.id}) "
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
      usrtxt += f"[{random.choice(bayrag)}](tg://user?id={usr.id}) "
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
