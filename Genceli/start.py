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
bot_token = "6565277854:AAG2uqWhG9OB3zFJ3SG56Tl4LZv6JiFjyTs"


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
OWNER_USERNAME = "NatiqOwner"
OWNERNAME = "⚯ ͛: 𝙰𝚋𝚋𝚊𝚜𝚘𝚟 ✷"
SUPPORT_KANAL =  "KrayzenResmi"
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
    await event.reply(f"**Salam mən qrupunuzdakı bütün üzvləri tağ edə bilərəm 👀\n\nƏtraflı məlumat üçün Əmrlər bölməsinə daxil olun ✅**",
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
    await event.respond("**Salam mən qrupunuzdakı bütün üzvləri tağ edə bilərəm 👀\n\n Ətraflı məlumat üçün Əmrlər bölməsinə daxil olun ✅. **",
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
    await event.edit(f"[{BOT_NAME}](https://t.me/KrayzenTaggerBot) Botun Əmirləri:",
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
    await event.edit(f"**[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Botun Əmirləri:\n\n🔹/start - Botu Başlat.\n🔹/help - Əmrlərə Bax.\n🔹/sudolist - Bot-un Sudo İstifadəçilərini yoxlayın.\n🔹/chatmesaj - ON - OFF.\n🔹/banda - Qrupunda Olan Silinmiş Hesaplar.\n🔹/ship - Qrubda Cütlük Seçər.\n🔹/bots - Qrubdaki Botları Göstərir.\n🔹/admins - Qrubdaki Adminləri Göstərir.\n🔹/id - Qrub Və User ID Göstərir.**",
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
    await event.edit(f"**[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Botun Əmirləri:\n\n🔹/dc - Doğruluq Cəsarət Oyunu.**",
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
	"Bir dakika boyunca karşı cinsten biri gibi yürü.","Sevgiline atıp atabileceğin en acımasız mesajı gönder.","Oyunda yer alan her kişi hakkında bildiğin komik bir şey anlat.",
	"Ünlü restoranlardan birini ara ve menülerini öğrenirken dalga geç.","Eski bir şarkıyı aç ve onu taklit ederek söylemeye çalış söylerken ses at","1 tur boyunca farklı bir dilde konuş.",
	"Eski sevgiline mesaj at ve onu unutamadığını söyle.","2 tur boyunca “sen” kelimesini duyunca kuş gibi ses çıkart.",
	"Telefondaki tarayıcı geçmişini herkese göster.","Odadan birisi için satın alacakmış gibi iç çamaşırı araştırması yap."
)

c = (
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
	"Üç çorba kaşığı acı salça veya buna benzer",
)

@elnur.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        user = await event.get_user()
        username = f"{user.first_name}"
        Aylin = (f"{username} Xoş gəldin",
                 f"{username} Gəldi 🙄",
                 f"{username} Sənin Gəlişin Məni Sevindirdi 🫠", 
                 f"{username} Aramıza Xoş Gəldin 🙋🏻",
                 f"{username} Partimizə Xoş Gəldin🥳",
                 f"{username} Bayaqdan Səni Gözləyirəm 🤩",
                 f"{username} Xoşgəldin, Pizza gətirəcəyivi düşünürdük. 🤠",
                 f"{username} Xoşgəldin, Çıxacaqsansa indidən çıx 😒.",)
        await event.reply(f"{random.choice(mesaj)}")

    elif event.user_left: 
        user = await event.get_user() 
        username = f"{user.first_name}"
        await event.reply(f"{username} Əla Birdaha Gəlmə 🥱")

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
    mentions += f"\nSilinmiş hesaplar` = {deleted}`\n\n__• By @KrayzenResmi"
    await event.reply(mentions)


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
        return await event.respond("Əvvəlki  Mesajlara Cavab Verməyin")
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
      usrtxt += f"↯ - [{usr.first_name}](tg://user?id={usr.id}) \n"
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
      usrtxt += f"↯ - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**Tağ uğurla dayandırıldı ⛔**")
        return
      if usrnum == 5:
        await elnur.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

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
      usrtxt += f"↯ - [{usr.first_name}](tg://user?id={usr.id})"
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
      usrtxt += f"↯ - [{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Tağ uğurla dayandırıldı ⛔**")
        return
      if usrnum == 1:
        await elnur.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

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
      usrtxt += f"↯ - [{random.choice(adlar)}](tg://user?id={usr.id}) "
      if event.chat_id not in tekli_calisan:
        await event.respond("**Tağ uğurla dayandırıldı ⛔**")
        return
      if usrnum == 5:
        await elnur.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in elnur.iter_participants(event.chat_id):
      usrnum += 5
      usrtxt += f"↯ - [{random.choice(adlar)}](tg://user?id={usr.id}) "
      if event.chat_id not in tekli_calisan:
        await event.respond("**Tağ uğurla dayandırıldı ⛔**")
        return
      if usrnum == 1:
        await elnur.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

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
        return await event.respond("Əvvəlki  Mesajlara Cavab Verməyin")
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
      usrtxt += f"↯ - [{random.choice(mafia)}](tg://user?id={usr.id}) "
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
      usrtxt += f"↯ - [{random.choice(mafia)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Tağ uğurla dayandırıldı ⛔**")
        return
      if usrnum == 5:
        await elnur.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
  
bayrag = ['🏳️‍⚧️','🇦🇫','🇦🇽','🇦🇱','🇩🇿','🇦🇸','🇦🇩','🇦🇴','🇦🇮','🇦🇶','🇦🇬','🇦🇷','🇦🇼','🇦🇺','🇦🇹','🇦🇿','🇧🇸','🇧🇭','🇧🇩','🇧🇧','🇧🇾','🇧🇪','🇧🇿','🇧🇯','🇧🇲','🇧🇹','🇧🇴','🇧🇦','🇧🇼','🇧🇷','🇻🇬','🇧🇳','🇧🇬','🇧🇫','🇧🇮','🇰🇭','🇨🇲','🇨🇦','🇮🇨','🇨🇻','🇧🇶','🇰🇾','🇨🇫','🇹🇩','🇮🇴','🇨🇱','🇨🇳','🇨🇽','🇨🇨','🇨🇴','🇰🇲','🇨🇬','🇨🇩','🇨🇰','🇨🇷','🇨🇮','🇭🇷','🇨🇺','🇨🇼','🇨🇾','🇨🇿','🇩🇰','🇩🇯','🇩🇲','🇩🇴','🇪🇨','🇪🇬','🇸🇻','🇬🇶','🇪🇷','🇪🇪','🇪🇹','🇸🇿','🇪🇺','🇫🇰','🇫🇴','🇫🇯','🇫🇮','🇫🇷','🇬🇫','🇵🇫','🇹🇫','🇬🇦','🇬🇲','🇬🇪','🇩🇪','🇬🇭','🇬🇮','🇬🇷','🇬🇱','🇬🇩','🇬🇵','🇬🇺','🇬🇹','🇬🇬','🇬🇳','🇬🇼','🇬🇾','🇭🇹','🇭🇳','🇭🇰','🇭🇺','🇮🇸','🇮🇳','🇮🇩','🇮🇷','🇮🇶','🇮🇪','🇮🇲','🇮🇱','🇮🇹','🇯🇲','🇯🇵','🎌','','🇯🇪','🇯🇴','🇰🇿','🇰🇪','🇰🇮','🇽🇰','🇰🇼','🇰🇬','🇱🇦','🇱🇻','🇱🇧','🇱🇸','🇱🇷','🇱🇾','🇱🇮','🇱🇹','🇱🇺','🇲🇴','🇲🇬','🇲🇼','🇲🇾','🇲🇻','🇲🇱','🇲🇹','🇲🇭','🇲🇶','🇲🇷','🇲🇺','🇾🇹','🇲🇽','🇫🇲','🇲🇩','🇲🇨','🇲🇳','🇲🇪','🇲🇸','🇲🇦','🇲🇿','🇲🇲','🇳🇦','🇳🇷','🇳🇵','🇳🇱','🇳🇨','🇳🇿','🇳🇮','🇳🇪','🇳🇬','🇳🇺','🇳🇫','🇰🇵','🇲🇰','🇲🇵','🇳🇴','🇴🇲','🇵🇰','🇵🇼','🇵🇸','🇵🇦','🇵🇬','🇵🇾','🇵🇪','🇵🇭','🇵🇳','🇵🇱','🇵🇹','🇵🇷','🇶🇦','🇷🇪','🇷🇴','🇷🇺','🇷🇼','🇼🇸','🇸🇲','🇸🇹','🇸🇦','🇸🇳','🇷🇸','🇸🇨','🇸🇱','🇸🇬','🇸🇽','🇸🇰','🇸🇮','🇬🇸','🇸🇧','🇸🇴','🇿🇦','🇰🇷','🇸🇸','🇪🇸','🇱🇰','🇧🇱','🇸🇭','🇰🇳','🇱🇨','🇵🇲','🇻🇨','🇸🇩','🇸🇪','🇸🇷','🇨🇭','🇸🇾','🇹🇼','🇹🇯','🇹🇿','🇹🇭','🇹🇱','🇹🇬','🇹🇰','🇹🇴','🇹🇹','🇹🇳','🇹🇷','🇹🇲','🇹🇨','🇹🇻','🇺🇬','🇺🇦','🇦🇪','🇬🇧','🏴󠁧󠁢󠁥󠁮󠁧󠁿','🏴󠁧󠁢󠁳󠁣󠁴󠁿','🏴󠁧󠁢󠁷󠁬󠁳󠁿','🇺🇸','🇺🇾','🇻🇮','🇺🇿','🇻🇺','🇻🇦','🇻🇪','🇻🇳','🇼🇫','🇪🇭','🇾🇪','🇿🇲','🇿🇼',]

@elnur.on(events.NewMessage(pattern="^/btag ?(.*)"))
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
        return await event.respond("Əvvəlki  Mesajlara Cavab Verməyin")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("️️️Tağ etmək üçün səbəb yazın **Məsələn:\n/btag Gəlin Qruba**")
  else:
    return await event.respond("️️Tağ etmək üçün səbəb yazın **Məsələn:\n/btag Gəlin Qruba**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in elnur.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ - [{random.choice(bayrag)}](tg://user?id={usr.id}) "
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
      usrtxt += f"↯ - [{random.choice(bayrag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Tağ uğurla dayandırıldı ⛔**")
        return
      if usrnum == 5:
        await elnur.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@elnur.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)

@elnur.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)

@elnur.on(events.NewMessage(pattern="^/chatmesaj ?(.*)"))
async def chatbot(event):
    global isleyen
    emr = event.pattern_match.group(1)
    qrup = event.chat_id
    if emr == "ON" or emr == "on" or emr == "On":
        if qrup not in isleyen:
            isleyen.append(qrup)
            aktiv_olundu = "✅ **ChatBot bu qrupda aktiv olundu !**"
            await event.reply(aktiv_olundu)
            return
        await event.reply("⚠️ **ChatBot onsuzda aktivdir !**")
        return
    elif emr == "OFF" or emr == "off" or emr == "Off":
        if qrup in isleyen:
            isleyen.remove(qrup)
            await event.reply("⛔️ **ChatBot bu qrupda deaktiv olundu !**")
            return # aykhan026 | aykhan_s
        await event.reply("⚠️ **ChatBot onsuzda deaktivdir !**")
        return
    
    else:
        await event.reply("On və yaxud Off yazmadınız")


@elnur.on(events.NewMessage)
async def test(event):
    global isleyen
    mesaj = str(event.raw_text)
    qrup = event.chat_id
    if qrup not in isleyen:
        return
    if "test1" in mesaj or "test2" in mesaj or "test3" in mesaj:
        await event.reply("İşləyir")
    if "Kenan" in mesaj:
        await event.reply("Sahibimdi")


@elnur.on(events.NewMessage(pattern="^/testt ?(.*)"))
async def zar(event):
    mrt = await event.reply("Sudo istifadəçilərinin siyahısı əldə edilir...")
    await asyncio.sleep(2)
    await mrt.edit(f"👨🏻‍💻 Bot Sahibi:\n1➤ [{OWNERNAME}](https://t.me/{OWNER_USERNAME})")


@elnur.on(events.NewMessage)
async def send_message(event):
    now = datetime.now()
    if now.hour == 0 and now.minute == 0 and now.second == 0:
        await elnur.send_message(x, 'İyi Geceler!')

@elnur.on(events.NewMessage(pattern=f'@NatiqOwner'))
async def handler(event):
    await event.reply(random.choice(Aylin))




Aylin = (
    "Az tağ elə sahibimi😒",
    "İşi var birazdan gələcək😇",
    "Ay bala nolub mənə de o yoxdu",
    "Az tağ elədə sahibimi",
    "Sahibim burda deyil mənə deyə bilərsən👀",
    "Evdə deyil",
    "Nolub mənə deyə bilərsən",
    "Burda deyil yəqin başqa qrupdadı😂",
    "Sahibim burda olmasada qəlbi sizinlədir😌",
    "Burda yoxdur kömək üçün mənə deyə bilərsən😇",
    "🚷 Ban Olundun !\nSəbəb: Sahibimi tağ etdiyin üçün 🙄\n\nŞaka ya korkma 😂",
    "/ban çox tağ edirsən Sahibimi🙄",
    "/mute az tağ elə Sahibimi😑",
    "/warn birdə Sahibimi tağ eləsən ban verəcəm sənə!",
    "/fban Sahibimi çox tağ edirsiz!",
    "Sahibim dedi birazdan gələcəm👀",
    "Az tağ edin onu zəhmət olmasa🙄",
    "Onun başı qarışıqdı birazdan gələcək",
    "O daha qrupa gəlməyəcək onu mən əvəz edəcəyəm 🤖",
    "Nə istəyirsən ondan?",
    "Az Nolufdu Qoy Sahibim Yatsin da",
    "Sahibim Sevglisiylə Danışır\nNarahat eləmiyin!",
)

SOYUS_CAVAB = ["🤖 Mən Mesajı Sildim\n\n⛔ SƏBƏB:- Söyüş Tipli Sözlər isdifadə Elıdiyin Üçün","🚫 Söyüş Tipli Mətn Olduğu Üçün Yazılan Mesajı Sildim"]


@elnur.on(events.NewMessage(pattern='(?i)peysər+'))
@elnur.on(events.NewMessage(pattern='(?i)qəhbə+'))
@elnur.on(events.NewMessage(pattern='(?i)cındır+'))
@elnur.on(events.NewMessage(pattern='(?i)peyser+'))
@elnur.on(events.NewMessage(pattern='(?i)qehbe+'))
@elnur.on(events.NewMessage(pattern='(?i)suka+'))
@elnur.on(events.NewMessage(pattern='(?i)küçük+'))
@elnur.on(events.NewMessage(pattern='(?i)blet+'))
@elnur.on(events.NewMessage(pattern='(?i)blət+'))
@elnur.on(events.NewMessage(pattern='(?i)dalbayok+'))
@elnur.on(events.NewMessage(pattern='(?i)pidr+'))
@elnur.on(events.NewMessage(pattern='(?i)xnxx+'))
@elnur.on(events.NewMessage(pattern='(?i)porno+'))
@elnur.on(events.NewMessage(pattern='(?i)sirtiq+'))
@elnur.on(events.NewMessage(pattern='(?i)sırtıq+'))
@elnur.on(events.NewMessage(pattern='(?i)kucuy+'))
@elnur.on(events.NewMessage(pattern='(?i)küçüy+'))
@elnur.on(events.NewMessage(pattern='(?i)gic+'))
@elnur.on(events.NewMessage(pattern='(?i)sik+'))
@elnur.on(events.NewMessage(pattern='(?i)dalyok+'))
@elnur.on(events.NewMessage(pattern='(?i)oruspo+'))
@elnur.on(events.NewMessage(pattern='(?i)qehbə+'))
@elnur.on(events.NewMessage(pattern='(?i)qəhbe+'))
@elnur.on(events.NewMessage(pattern='(?i)amcıq+'))
@elnur.on(events.NewMessage(pattern='(?i)amcığ+'))
@elnur.on(events.NewMessage(pattern='(?i)amk+'))
@elnur.on(events.NewMessage(pattern='(?i)bled+'))
@elnur.on(events.NewMessage(pattern='(?i)bləd+'))
@elnur.on(events.NewMessage(pattern='(?i)cindir+'))
@elnur.on(events.NewMessage(pattern='(?i)ostur+'))
@elnur.on(events.NewMessage(pattern='(?i)dumsuy+'))
@elnur.on(events.NewMessage(pattern='(?i)dumsuk+'))
@elnur.on(events.NewMessage(pattern='(?i)slk+'))
@elnur.on(events.NewMessage(pattern='(?i)pox+'))
@elnur.on(events.NewMessage(pattern='(?i)qehbbeninnn+'))
@elnur.on(events.NewMessage(pattern='(?i)qehebe+'))
@elnur.on(events.NewMessage(pattern='(?i)qehbbeeeeee'))
@elnur.on(events.NewMessage(pattern='(?i)qehbbbeeee+'))
@elnur.on(events.NewMessage(pattern='(?i)gəhbə+'))
@elnur.on(events.NewMessage(pattern='(?i)qot+'))
@elnur.on(events.NewMessage(pattern='(?i)amcıg+'))
@elnur.on(events.NewMessage(pattern='(?i)gehbe+'))
@elnur.on(events.NewMessage(pattern='(?i)siik+'))
@elnur.on(events.NewMessage(pattern='(?i)gij+'))
@elnur.on(events.NewMessage(pattern='(?i)sg+'))
@elnur.on(events.NewMessage(pattern='(?i)qəhi+'))
@elnur.on(events.NewMessage(pattern='(?i)qehi+'))
@elnur.on(events.NewMessage(pattern='(?i)meki+'))
@elnur.on(events.NewMessage(pattern='(?i)məki+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.delete()
    await event.reply(f"{random.choice(SOYUS_CAVAB)}")

@elnur.on(events.NewMessage)
async def send_message(event):
    now = datetime.now()
    if now.hour == 8 and now.minute == 0 and now.second == 0:
        await elnur.send_message(x, 'Günaydın!')


SAHIB = OWNER_ID

@elnur.on(events.NewMessage(pattern="^.pin ?(.*)"))
async def pin(event):
    if event.sender_id == SAHIB:
        if not event.reply_to_msg_id:
            return await event.reply("🗨 Zəhmət Olmasa Bir Mesaja Yanıt Verin")
        await event.reply("📌 Sahibim Mesajınlz Pinləndi!")
        await event.client.pin_message(event.chat_id, event.reply_to_msg_id, notify=True)
    else:
        await event.reply(f"Sən {Config.BOT_NAME} Bota Sahib Deyilsən!\n⛔ Pinləməyə Çalışma.")
 

@elnur.on(events.NewMessage(pattern="^.unpin ?(.*)"))
async def unpin(event):
    if event.sender_id == SAHIB:
        if not event.reply_to_msg_id:
            return await event.reply("🗨 Zəhmət Olmasa Pinlənmiş Mesaja Yanıt Verin")
        await event.reply("Sahibim Pinlənmiş Mesaj Qaldırıldı")
        await event.client.unpin_message(event.chat_id)
    else:
        await event.reply(f"Sən {Config.BOT_NAME} Bota Sahib Deyilsən!\n⛔ UnPinləməyə Çalışma.")
	    

@elnur.on(events.NewMessage(pattern="^.soxri ?(.*)"))
async def soxri(bot: app, m: Message):
    start = time()
    replymsg = await m.reply_text("**❤ Rondom Bir Şəkil Seçilir...**")
    end = round(time() - start, 2)
    photo = random.choice(photolist)
    text = f"❤️ ** @KrayzenTaggerBot Sizin Üçün Rondom Bir Şəkil Seçdi**"
    await bot.send_photo(m.chat.id, photo=photo, caption=text)
    await replymsg.delete()

photolist = [
"https://telegra.ph/file/2af840d4b544283a5681c.jpg","https://telegra.ph/file/40da2e2c8d6845715690b.jpg","https://telegra.ph/file/35a83006ef07392cbbb02.jpg","https://telegra.ph/file/65ded72e902612fa0ecf8.jpg","https://telegra.ph/file/3164eec3577752b00c4a0.jpg","https://telegra.ph/file/de584d0f2c35ce934791c.jpg","https://telegra.ph/file/72986ec12b28c1161c0fe.jpg","https://telegra.ph/file/6e57ddb285f4a7107ef17.jpg","https://telegra.ph/file/e6613983e32c1fdbec6bc.jpg","https://telegra.ph/file/7cebaa2f536f4c9e3a04d.jpg","https://telegra.ph/file/f96d408f674dc98e11996.jpg","https://telegra.ph/file/ccd88451c6b35a41fb919.jpg","https://telegra.ph/file/18f9b0e76cb4b06e9f042.jpg","https://telegra.ph/file/f5c7fb6345ae08b0756c5.jpg","https://telegra.ph/file/25cc40e24d057db5b3510.jpg","https://telegra.ph/file/774c4807415a36d08201c.jpg","https://telegra.ph/file/06615db52698e2b5be527.jpg","https://telegra.ph/file/f602d74490ea334faa996.jpg","https://telegra.ph/file/cc7eba292d8c59426f136.jpg","https://telegra.ph/file/08fa5f7a9a913e602caae.jpg","https://telegra.ph/file/b82768ea54c1b88b761a0.jpg","https://telegra.ph/file/92902e39f863a14bf346a.jpg","https://telegra.ph/file/a09dd5667c6a156a81473.jpg","https://telegra.ph/file/d1295679bc981fd572999.jpg","https://telegra.ph/file/3d70f093b375f96fb40e5.jpg","https://telegra.ph/file/44a86e022a5f524b7174e.jpg","https://telegra.ph/file/76f8b855a22fcdc94720f.jpg","https://telegra.ph/file/5e1ef87d38881c355c694.jpg","https://telegra.ph/file/ec264472ea91541809564.jpg","https://telegra.ph/file/d20622ef559808af97eda.jpg","https://telegra.ph/file/3e7d0bbe7c7d883f752ad.jpg","https://telegra.ph/file/18b6fd691975990da488c.jpg","https://telegra.ph/file/207c46659ec65c5a9a781.jpg","https://telegra.ph/file/40918d64616279ffe3c44.jpg","https://telegra.ph/file/c2b7d80c27ef714de1a9c.jpg","https://telegra.ph/file/bd57dfc0ed53878e71c20.jpg","https://telegra.ph/file/5a6526f7da3854ecc1f15.jpg","https://telegra.ph/file/6418c9e1cb94e5640a55f.jpg","https://telegra.ph/file/1ca2b73228de65600002b.jpg","https://telegra.ph/file/66901b5512df7f6aee500.jpg","https://telegra.ph/file/55b3ae6bf7315d8aaf063.jpg","https://telegra.ph/file/720344bd1304cb85188dc.jpg","https://telegra.ph/file/ab3637e7fcb7f534a43de.jpg","https://telegra.ph/file/d92001692cad50bd020de.jpg","https://telegra.ph/file/037f8d901bcb525dded7d.jpg","https://telegra.ph/file/d3c894daa4d5d62f6006e.jpg","https://telegra.ph/file/86a3caa1f1888d09f9526.jpg","https://telegra.ph/file/578523944035c477c862f.jpg","https://telegra.ph/file/e063803deb43a02a9e353.jpg","https://telegra.ph/file/e4fd43daf77aa7c7e016b.jpg","https://telegra.ph/file/23692be820f2d86761fa2.jpg","https://telegra.ph/file/6125b4338311683b49383.jpg","https://telegra.ph/file/b047c7556e004689d81bc.jpg","https://telegra.ph/file/14826fff6f3f5266d37e9.jpg","https://telegra.ph/file/4c3b09585def5f473a426.jpg","https://telegra.ph/file/88718fc6e67e765cc2824.jpg","https://telegra.ph/file/c91546ba8ebdc5a9ee588.jpg","https://telegra.ph/file/f7e6c732fadd2d63afb11.jpg","https://telegra.ph/file/35bb823ab612c8925f7b4.jpg","https://telegra.ph/file/6cb29cdb77d62a7e81aca.jpg","https://telegra.ph/file/8bc6d95bd3de52a384d0d.jpg","https://telegra.ph/file/9f33742aab0d34d4dc357.jpg","https://telegra.ph/file/980b9a55fa1dc9f2288ac.jpg","https://telegra.ph/file/0f2b48fdd48e0bc419aff.jpg","https://telegra.ph/file/0ba309ed00aae83fb7e2d.jpg","https://telegra.ph/file/e57143440028a7c141440.jpg","https://telegra.ph/file/6c33a5a8dab4a0c4822b9.jpg","https://telegra.ph/file/666a68af2fc6ee5a429a3.jpg","https://telegra.ph/file/eee582a22fc42ed9f2286.jpg","https://telegra.ph/file/eee582a22fc42ed9f2286.jpg","https://telegra.ph/file/9066e1cedb8640e712fe8.jpg","https://telegra.ph/file/0909711f4071ab5bd6252.jpg","https://telegra.ph/file/6c2338b9c8ff62403757f.jpg","https://telegra.ph/file/a4e40d9fcb7f203d6a1ea.jpg","https://telegra.ph/file/7ee1ded692e90ec2f54e3.jpg","https://telegra.ph/file/cfd7e3b6bf3bd99e25f83.jpg","https://telegra.ph/file/7dba92c97c636e64e6561.jpg","https://telegra.ph/file/73c501102cf8c4788de9e.jpg","https://telegra.ph/file/217d3eeba0a805f35f37.jpg","https://telegra.ph/file/2a766819e0c7d6e97c1d2.jpg","https://telegra.ph/file/2cc909aff5d1e2367d0e8.jpg","https://telegra.ph/file/13fed9487f9e28f21b5b3.jpg","https://telegra.ph/file/952d66c246a6203fee602.jpg","https://telegra.ph/file/0c4658ea3174529727d9f.jpg","https://telegra.ph/file/f58e631665de14f5f58e8.jpg","https://telegra.ph/file/45a0d298852ffbee0974b.jpg","https://telegra.ph/file/c704b13ed84f55bd0dccb.jpg","https://telegra.ph/file/a39215d5e52147ab4261a.jpg","https://telegra.ph/file/fd7ef0e5773ab824936fd.jpg","https://telegra.ph/file/5b8c841fd10a423bea884.jpg","https://telegra.ph/file/19fd9f074bbc5be9d783f.jpg","https://telegra.ph/file/69f48f26de9b21b1c3fd1.jpg","https://telegra.ph/file/0d13fabfab12ee1fdc15b.jpg","https://telegra.ph/file/db1224404049c03139189.jpg","https://telegra.ph/file/73fcc5487a6abedbdb1c1.jpg","https://telegra.ph/file/34566f2222ce2ea8db41c.jpg","https://telegra.ph/file/c34a52b1b73f94f4fe2cd.jpg","https://telegra.ph/file/347265b3a372b5c133245.jpg","https://telegra.ph/file/11d45d99903d197ee4f1c.jpg","https://telegra.ph/file/8c6965aefc0c32f218d31.jpg","https://telegra.ph/file/cf2db4ae9bba24b0d4b4d.jpg","https://telegra.ph/file/4d8b2dd35c02e354305dd.jpg","https://telegra.ph/file/1249999649307f0db0ebb.jpg","https://telegra.ph/file/52361bb267d1cbb2569b4.jpg","https://telegra.ph/file/413544c4784c52a772355.jpg","https://telegra.ph/file/9c0c8e033ae1105131acf.jpg","https://telegra.ph/file/18d1a2d17fee22592c1c7.jpg","https://telegra.ph/file/dbd1c1015577dc6ddf075.jpg","https://telegra.ph/file/e9f34c716ac3ddd4b6d92.jpg","https://telegra.ph/file/727aaf87f3d210384e385.jpg","https://telegra.ph/file/a0490f7e22e70dfd2dca5.jpg","https://telegra.ph/file/5fbdb6b18b7438a0b5847.jpg","https://telegra.ph/file/b0799aa20a3728201d8d3.jpg","https://telegra.ph/file/f26df3b8b819b891ba1a4.jpg","https://telegra.ph/file/5ac106f75597dd044bc0b.jpg","https://telegra.ph/file/aa2ae5b4f866c17ed265f.jpg","https://telegra.ph/file/8728850c57f749ffb5fd8.jpg","https://telegra.ph/file/0599e692bcbc514928054.jpg","https://telegra.ph/file/a18e1053f9e5d9850bb52.jpg","https://telegra.ph/file/0d2e10583eb677a89a4ad.jpg""https://telegra.ph/file/53610699438ff6d0cc117.jpg",
"https://telegra.ph/file/ec46abdc7605a349b2deb.jpg",
"https://telegra.ph/file/ea45e7275bfbe7503846b.jpg",
"https://telegra.ph/file/9063eba2a2d11f6dae51b.jpg",
"https://telegra.ph/file/645ba1d6dcd35723e2b82.jpg", 
"https://telegra.ph/file/a7c0c07099851760ce02a.jpg"
]

#print i silmə.!
print(f">>Aktiv ... @{BOT_USERNAME} Sahib @ElnurGenCeLi .<<")
elnur.run_until_disconnected()
