# Owner: @ElnurGenCeLi  
# Band@edalet_22akodu
# Bu Reponu Başqasına Satan Peysərdi
# Öz Adına Çıxartma!


from telethon import Button
from telethon import events
from telethon import errors
from telethon import TelegramClient
import random, os, logging, asyncio
from asyncio import sleep
from time import time
from telethon.tl.types import ChannelParticipantsBots
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.sessions import StringSession
from os import remove
from telethon.tl.functions.users import GetFullUserRequest
from telethon.sync import types
from datetime import datetime 
from telethon.errors.rpcerrorlist import PeerFloodError


logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)


# config 
API_ID = 21236884 
API_HASH = "2e526fe32b1177ba7ce3d552640ab854"
bot_token = "6565277854:AAHUD19Rf3VEBe7ZtDvUxxGEKPG0LswTy64"


anlik_calisan = []
tekli_calisan = []
rxyzdev_tagTot = []

grup_sayi = []
user_sayi = []

isleyen = []

#Client i silmə !
elnur = TelegramClient('elnur', API_ID, API_HASH).start(bot_token=bot_token)


SUDO_USERS = 6960862388
SUDO = [6960862388]
OWNER_ID = 6960862388 
OWNER = [6960862388]
OWNER_USERNAME = "xSanalKrayzen"
OWNERNAME = "𝐒𝐚𝐧𝐚𝐥 #κʀɑⲩⲍ૯ⲛ"
SUPPORT_KANAL = "KrayzenResmi"
log_qrup = -1002057111740
BOT_USERNAME = "KrayzenTaggerBot"
BOT_NAME = "Krayzen🫅"

__python__ = "3.11.1"
__telethon__ = "1.27.0"
__version__ = "v2"
gruplar = []













SUDO_USERS = set()


@elnur.on(events.NewMessage(pattern='/addsudo'))
async def sudoadd(event):
    try:
        await event.delete()
    except:
        pass

    if not event.reply_to_msg_id:
        if len(event.text.split()) != 2:
            return await event.respond(
                "İstifadəçinin mesajına cavab verin və ya istifadəçi adı/istifadəçi ID-si yazın"
            )

        user = await client(GetFullUserRequest(event.text.split()[1]))
        if int(user.user.id) in SUDO_USERS:
            return await event.respond(f"{user.user.first_name} artıq botun sudo istifadəçisidir 👨🏻‍💻")

        try:
            SUDO_USERS.add(int(user.user.id))
            await event.respond(f"{user.user.first_name} sudo istifadəçi təyin edildi ✅")
        except:
            return await event.respond("Sudo istifadəçi əlavə etmək alınmadı ❌")

    else:
        msg = await event.get_reply_message()
        if msg.sender_id in SUDO_USERS:
            return await event.respond(f"{msg.sender.first_name} artıq sudo istifadəçisidir ✅")

        try:
            SUDO_USERS.add(msg.sender_id)
            await event.respond(f"{msg.sender.first_name} sudo istifadəçi təyin edildi ✅")
        except:
            return await event.respond("Sudo istifadəçi əlavə etmək alınmadı ❌")


    


@elnur.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_group:
    await event.reply(f"**[{BOT_NAME}](http://t.me/{BOT_USERNAME})'un Əmrlər üçün?.Bot'a daxil olub.**",
    buttons=(
              
		      [Button.url('Kanal📣', f'https://t.me/{SUPPORT_KANAL}'),
		      
		      Button.url('Sahib 🫅', f'https://t.me/{OWNER_USERNAME}')]
                    ),
                    link_preview=False
                   )
  if event.is_private:
    async for usr in elnur.iter_participants(event.chat_id):
     ad = f"{usr.first_name} "
     idd = f"{usr.id} "
     profil = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await elnur.send_message(log_qrup, f"ℹ️ **Yeni istifadəçi -**\n- {profil}\n- {idd}")
    await event.respond("**Salam mən qrupunuzdakı bütün üzvləri tağ edə bilərəm 👀\n\n Ətraflı məlumat üçün Əmrlər bölməsinə daxil olun ✅**",
            buttons=(
              
		      [
		        Button.url('Məni Qurupa əlavə et❤️', f'http://t.me/{BOT_USERNAME}?startgroup=a'),
		        ],[
		        Button.inline("Əmrlər❤️", data="helpdata"),
		        
		        Button.url('Kanal📣', f'http://t.me/{SUPPORT_KANAL}'),
		        ],[
		        Button.url('Bot Sahibi🧑🏻‍💻', f'http://t.me/{OWNER_USERNAME}')
		          ],
                    ),
                    link_preview=False
                   )
    

@elnur.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    await event.edit(f"**Salam mən qrupunuzdakı bütün üzvləri tağ edə bilərəm 👀\n\n Ətraflı məlumat üçün Əmrlər bölməsinə daxil olun ✅**",
            buttons=(
              
		      [
		        Button.url('Məni Qurupa əlavə et❤️', f'http://t.me/{BOT_USERNAME}?startgroup=a'),
		        ],[
		        Button.inline("Əmrlər❤️", data="helpdata"),
		        
		        Button.url('Kanal📣', f'http://t.me/{SUPPORT_KANAL}'),
		        ],[
		        Button.url('Bot Sahibi🧑🏻‍💻', f'http://t.me/{OWNER_USERNAME}')
		          ],
                    ),
                    link_preview=False
                   )


@elnur.on(events.NewMessage(pattern="/help"))
async def help(event):
        await event.reply(f"[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Botun Əmirləri:",
        buttons=(
                      [
                       Button.inline("Hərkəs", data="hami"),
                       
                       Button.inline("Admin", data="admin"),
                      ],[
                       Button.inline("Oyun", data="oyun"),
                       
                       Button.inline("Sudo", data="sudo"),
                       ],[
                       Button.inline("Geri◀️", data="start"),
                      ],
                    ),
                    link_preview=False)


@elnur.on(events.callbackquery.CallbackQuery(data="helpdata"))
async def handler(event):
    await event.edit(f"[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Botun Əmirləri:",
        buttons=(
                      [
                       Button.inline("Hərkəs", data="hami"),
                       
                       Button.inline("Admin", data="admin"),
                      ],[
                       Button.inline("Oyun", data="oyun"),
                       
                       Button.inline("Sudo", data="sudo"),
                       ],[
                       Button.inline("Geri◀️", data="start"),
                      ],
                    ),
                    link_preview=False)


@elnur.on(events.callbackquery.CallbackQuery(data="hami"))
async def handler(event):
    await event.edit(f"**[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Botun Əmirləri:\n\n/🔹start - Botu Başlat.\n🔹/help - Əmrlərə Bax.\n🔹/sudolist - Bot-un Sudo İstifadəçilərini yoxlayın.\n🔹/chatmesaj - ON - OFF.\n🔹/banda - Qrupunda Olan Silinmiş Hesaplar.\n🔹/ship - Qrubda Cütlük Seçər.\n🔹/bots - Qrubdaki Botları Göstərir.\n🔹/admins - Qrubdaki Adminləri Göstərir.\n🔹/id - Qrub Və User ID Göstərir.**",
      buttons=(
                      [
                       Button.inline("Geri", data="helpdata")
                      ],
                    ),
                    link_preview=False)


@elnur.on(events.callbackquery.CallbackQuery(data="admin"))
async def handler(event):
    await event.edit(f"**[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Botun Əmirləri:\n\n🔹/sil - Reply Atdığı Mesaji Silər.\n🔹/purge - Reply Atılmış Söhbətləri Silər.\n🔹/tag - Qrubda Userləri 5- Li Tağ Edər.\n🔹/tektag - Qrubda Userləri Tək-Tək Tağ Edər.\n🔹/adtag - Qrubda Userləri Qəribə Adlarlar Tağ Edər.\n🔹/mafia - Mafia Oyunun Rolları İlə Tağ Elə.\n🔹/btag - Bayrağlar İlə Tağ Elə.\n🔹/cancel - Tağ Prosesini Dayandırar.**",
      buttons=(
                      [
                       Button.inline("Geri", data="helpdata")
                      ],
                    ),
                    link_preview=False)


@elnur.on(events.callbackquery.CallbackQuery(data="oyun"))
async def handler(event):
    await event.edit(f"**[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Botun Əmirləri:\n\n/🔹dc - Doğruluq Cəsarət Oyunu.**",
      buttons=(
                      [
                       Button.inline("Geri", data="helpdata")
                      ],
                    ),
                    link_preview=False)



@elnur.on(events.callbackquery.CallbackQuery(data="sudo"))
async def handler(event):
       sender = await event.get_sender()
       if sender.id in OWNER:
            await event.edit(f"**[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Botun Əmirləri:\n\n🔹/alive - Botun Sahibi Botu Aktiv Olduğuna Baxar.\n🔹/stat - Botun Sahibi Botun Neçə Qrubda Olduğuna Baxar.\n🔹/addsudo - Sudo Siyahısına Əlavə Edir.**",
      buttons=(
                      [
                       Button.inline("Geri", data="helpdata")
                      ],
                    ),
                    link_preview=False)
       elif sender.id not in OWNER:
                 await event.respond(f"{sender.id} Sən Sudo Değilsən!")


@elnur.on(events.NewMessage(pattern="^/alive ?(.*)"))
async def alive(event):
  if event.sender_id == SUDO_USERS:
    await event.delete()
    genceli = await event.reply("Ak")
    await asyncio.sleep(1.5)
    await genceli.edit("Aktiv")
    await asyncio.sleep(1.5)
    await genceli.edit("Aktivəm")
    await asyncio.sleep(1.5)
    await genceli.edit(f"╔═════════════════\n║▻ ⚡️ @{BOT_USERNAME} Aktivdir [{__version__}]\n║\n║▻ 💠 Python versiyası: {__python__}\n║▻ 💻 Telethon versiyası: {__telethon__}\n╚═════════════════")
    await asyncio.sleep(15)
    await genceli.delete()
    await event.respond("Mesajı Sildim!🍃")

@elnur.on(events.NewMessage(pattern='/sudolist'))
async def sudolist_handler(event):
    # Sudo siyahısını hazırlayırıq
    sudo_list_formatted = ''
    for sudo_id in SUDO:
        sudo = await elnur.get_entity(sudo_id)
        sudo_list_formatted += f'➤ [{sudo.first_name}](tg://user?id={sudo.id})'
    # Owner siyahısını hazırlayırıq
    owner_list_formatted = ''
    for owner_id in OWNER:
        owner = await elnur.get_entity(owner_id)
        owner_list_formatted += f'➤ [{owner.first_name}](tg://user?id={owner.id})'

    # Sudo və Owner siyahısını göndəririk
    await event.respond(f'👨🏻‍💻 Sahiblər:\n{owner_list_formatted}\n\n⭐️ Sudo İstifadəçiləri:\n{sudo_list_formatted}')
    await event.delete()


@elnur.on(events.NewMessage(pattern="^.stat ?(.*)"))
async def start(event):
    if event.sender_id == SUDO_USERS:
        await event.reply(f"📊İstatiska", buttons=(
                      [
                       Button.inline("📊 İstatiska", data="stats")
                      ],
                    ),
                    link_preview=False)


@elnur.on(events.callbackquery.CallbackQuery(data="stats"))
async def handler(event):
    await event.edit(f"📋 Toplam Qrup: `{len(grup_sayi)}`\n📈 Aktuv Qruplar: `{len(anlik_calisan)}`\n👤 İsdifadəçi Sayı: `{len(user_sayi)}`")
	              

@elnur.on(events.NewMessage(pattern='/ship'))
async def ship(event):
    chat = await event.get_chat()
    if not chat.megagroup:
        return  
    members = []
    async for member in elnur.iter_participants(chat):
        members.append(member)
    selected_members = random.sample(members, 2)
    message = f"Artık bir çiftsiniz! 🚢💕\n@{selected_members[0].username}\n@{selected_members[1].username}\n\n❤️‍🩹Sevgilərin Faizi {random.randint(10, 100)}%"
    await elnur.send_message(chat, message)
  
@elnur.on(events.NewMessage(pattern='/sil'))
async def handle_delete(event):
    chat = await event.get_chat()
    if not chat.megagroup:
        return
    if event.is_reply:
        message = await event.get_reply_message()
        await elnur.delete_messages(chat, message)
        await event.delete()

@elnur.on(events.NewMessage(incoming=True, pattern="^[!/]purge$"))
async def purge_messages(event):
    if event.is_private:
        await event.respond("ℹ️ Bu əmr qruplar üçün etibarlıdır.", parse_mode='markdown')
        return

    if not await is_group_admin(event):
        await event.respond("Bunu həyata keçirmək üçün admin olmalısınız.", parse_mode='markdown')
        return

    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.respond("Silməyə başlayacağım mesaja yanıt ver.")
        return

    messages = []
    message_id = reply_msg.id
    delete_to = event.message.id

    messages.append(event.reply_to_msg_id)
    for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await event.client.delete_messages(event.chat_id, messages)
            messages = []

    await event.client.delete_messages(event.chat_id, messages)
    time_ = time.perf_counter() - start
    text = f"✅ Təmizləmə prosesi {time_:0.2f} saniyədə tamamlandı"
    await event.respond(text, parse_mode='markdown')


async def is_group_admin(event):
    """
    Checks if the user is a group admin
    """
    try:
        user = await event.client.get_entity(event.input_chat)
        user_info = await event.client.get_participants(user, filter=ChannelParticipantsAdmins, limit=100)
        for u in user_info:
            if u.id == event.sender_id:
                return True
    except errors.rpcerrorlist.ChatAdminRequiredError:
        pass
    return False


@elnur.on(events.NewMessage(pattern='/bots'))
async def show_bots(event):
    all_users = await event.client.get_participants(event.chat_id)
    bot_list = []
    for user in all_users:
        if isinstance(user, types.User) and user.bot:
            bot_list.append(user.username)
    if bot_list:
        await event.reply(f"{len(bot_list)} bot tapıldı:\n\n@" + "\n@".join(bot_list))
    else:
        await event.reply("Bu qrupda heç bir bot yoxdur.")

@elnur.on(events.NewMessage(pattern='/admins'))
async def show_admins(event):
    chat = await event.get_chat()
    admins = await event.client.get_participants(chat, filter=types.ChannelParticipantsAdmins)
    admin_list = ""
    for admin in admins:
        admin_list += f"\n\n[{admin.username}](tg://user?id={admin.id})"
    await event.respond(f"Qrupda olan adminlər: {admin_list}")

@elnur.on(events.NewMessage(pattern="^/dc$"))
async def test(event):
    await event.reply("Salam Doğruluq Cəsarət Oyununa Xoş Gəldin", buttons=(
                      [
                      Button.inline("Doğruluq", data="dogruluq")
                      ],
                      [
                      Button.inline("Cəsarət", data="cesaret")
                      ]
                    ),
                    link_preview=False)

@elnur.on(events.callbackquery.CallbackQuery(data="dogruluq"))
async def sahib(event):
    await event.reply(f" {random.choice(d)}")

@elnur.on(events.callbackquery.CallbackQuery(data="cesaret"))
async def sahib(event):
    await event.reply(f" {random.choice(c)}")

d = (
	"Seçtiğiniz bir sosyal medya hesabınızdan çok çirkin bir fotoğrafınızı paylaşın.","Mesaj yazma bölümünüzü telefonunuzdan açın gözlerinizi kapatın ve rasgele bir kişiye körü körüne bir metin gönderin.",
	"Önümüzdeki 5 dakika boyunca söylediğin her şeyden sonra “mee” diyeceksin",
	"Önümüzdeki 5 dakika içinde birinin hayvanı olun.","İnstagramını oyunculardan birine ver. 5 dk boyunca her yere bakmak serbest.",
	"Oyundan bir kişiye serenat yap (kız ise erkeğe, erkek ise kıza)","Sonraki 3 tur boyunca şiveyle konuş.",
	"3 dakika boyunca bebek taklidi yap!","Telefonunda ki en sevmediğin fotoğrafını at","En beğendiğin fotoğrafını at",
	"Whatsapp’da 2 konuşmanı at","Özel mesajlarını ssi al ve gruba at","Whatsapp’da son konuşmanı at",
	"Bir deftere 20 kez ben çatlağım yaz ve resmini at","Telegramda son konuşmanı ss at.","Biyografine +18 bir cümle yaz; 3 Saat duracak.!",
	"Galerinin bir kısmını ss alıp at","Galerindeki 16. Fotoğrafı at.","Instagram yada telegramdan tanımadığın birine komik olmayan bir fıkra anlat.",
	"Ninni Söyleyerek Ses At","Bugununle ilgili kısa bir hikaye uydur.","Grupta ki en çok hoşuna giden karşı cinse seni seviyorum diye mesaj at.",
	"Galerindeki 16. Fotoğrafı at.","Galerindeki 30. Fotoğrafı at.","Whatsapp’da konuşduğun kişilerin ss ini at",
	"Grubun üye listesine gir ve 7. kişiye anlık at. (Grup daha az kişiyse ya da aktif sayısı azsa üstten saymaya devam et)",
	"En son konuştuğun kişiye \"Hayırlı Cumalar\" diye mesaj at.(platform farketmez)",
	"Şuan ki halini fotoğraf çekip  atar mısın?","Grupta üyeler kısmına gir 11. kişiye \"Analar neler doğuruyor bee\" diye ses at ve cevabını grupla paylaş.",
	"Profil fotoğrafına nefret ettiğin bir ünlünün resmini koy.","Kafanda yumurta kır ve fotosunu at",
	"Gruptan sevdiğin bir kişinin fotoğrafını profil resmi yap","Balkona veya pencereye cık dısardakılerın duyacagı sekılde sarkı soyle videoya al gruba at.",
	"İtiraf et: üye çalmak için kaç hesabın var?","Gruptaki 5 abazaya seni seviyorum de","İki dakika tavuk gibi davran.","Seçtiğiniz bir hayvanı taklit edin.",
	"Seçtiğin bir nesneyi yalayın ve gruba fotosunu atın.","Gruba gerçekten utanç verici bir fotoğrafını göster.",
	"Çirkin bir selfie çek ve sosyal medya uygulamalarından birinde yayınla 1.5 saat kalacak.","Bir kaşık un ye ve video ya al gruba at",
	"Hiç tanımadığın birine Kurban Bayramınızı kutlarım deyin","Sevdiğin bir kişiye \"`ben seni neden sevdim niçin sevdim niye sevdim bunların bi izahı yok gördün işte sevdim. Yaw sahi ben seni nidennn sevdim `\" de. Cevap geldiğinde grupla paylaş biz de gülelim",
	"Telegram'daki en kalabalık grubu aç ve \"`Benim adım turşu bidonu!`\" diyerek ses kaydedip en kalabalık gruba gönder.","Hemcinsin olan yakın bir arkadaşına ona aşık olduğunu söyle.","Sürahiden su iç ve fotoğraf at.",
	"En çok konuştuğun karşı cinsten arkadaşına \" `Seni çok seviyorum galiba aşık oldum`\" yaz ve tepkisini bizimle paylaş",
	"İsmini 1 saatliğine Abdül<ismin> yap. (örneğin adın Berk ise AbdülBerk yap)","İnstagram'da dm kutunu (mesajlar bölümü) ss al gruba at.",
	"Tanımadığın birisine şu cümleyi atıp sohbet başlat: \"`Aşkımızın suya düşeceğini bilseydim , balık olurdum`\"",
	"En komik fotoğrafını grupla paylaş.","Grupta üyeler kısmına gir 11. kişiye \"`Analar neler doğuruyor bee`\" diye ses at ve cevabını grupla paylaş.",
	"Tanımadığın birine şu mesajı at sonra cevabını grupla paylaş ➡️\n  \"`Bu mesaj özel bir frekansla gönderilmiştir. Zekilerde hafıza kaybı, aptallarda kısa sureli körlük ibnelerde de bir anlık gülümseme yapar!`\"",
	"@ yaz çıkan ilk kişiyi etiketle ve seni seviyorum yaz.","Tanımadığın birine \" `sanırım sana aşık oldum`\" diye mesaj at.",
	"Telegram hakkında kısmına \"`Babasının Prensesi`\" yaz 1 saat boyunca dursun.","Birine Sesli Öpücük At Ve Etiketle",
	"Telegramda son konuşmanı ss at.","🎀 ŞANSLI MESAJ🎊 Grupdan İstediğin Birinin Google/Youtube/İnstagram Arama Geçmişini İste",
	"Galerinin En Alttan 7. Fotosunu gönder",
	"Sonraki 3 tur boyunca şiveyle konuş. Farklı şivelere kayış olursa /zar Komutunu kullanarak 6 ya en cok yaklaşan oyuncu sana ceza verecek",
	"Üç çorba kaşığı acı salça (veya buna benzer bir şey) ye ve video ya al gruba at",
	"5 dakika boyunca oyundaki birinin evcil hayvanı olmasını isteyebilirsin.","Yeri yala Ve fotoğraf/videosunu gruba at",
	"/zar Komutunu kullanarak 6 ya en cok yaklaşan oyuncuya sosyal medya hesaplarından birini 5dk ver",
	"3 dakika boyunca bir ünlüyü taklit et.", "Birisi taklit edilen sanatçıyı tahmin edene kadar bir sanatçıyı taklit et",
	"Grubun ortaya koyduğu bir konu etrafında sekiz satır ve iki mısralık bir şiir yaz",
	"Oyundaki kişilerin ortak kararıyla gruptan birini öp ses atarak (ortak karar verilemezse /zar komutundan 1 e en yakın oyuncuyu öp).",
	"5 dakika boyunca oyundaki bir kişinin kölesi ol.", "Bir süpürgeyle veya paspas ile dans et ve videosunu at",
	"Gerçek aşkının kim olduğunu ilan et","Ağzını hareket ettirmeden baştan sona alfabeyi oku okurken video at", "Aklına gelen ilk kelimeyi hemen söyle.",
	"Oyundaki oyunculardan biri hakkında hikaye uydur", "15 saniye içerisinde sondan başa doğru alfabeyi oku okurken ses at", "Bir köpek gibi havla havlarken ses at",
	"Bir şarkıyı baştan sona söyle söylerken ses at","Çıktığın en kötü ve en iyi kişiyi açıkla.",
	"Bir dakika boyunca karşı cinsten biri gibi yürü.","Sevgiline atıp atabileceğin en acımasız mesajı gönder.","Oyunda yer a
