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
from telethon.sync import types

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

@elnur.on(events.NewMessage(pattern='/bots'))
async def show_bots(event):
    all_users = await event.client.get_participants(event.chat_id)
    bot_list = []
    for user in all_users:
        if isinstance(user, types.User) and user.bot:
            bot_list.append(user.username)
    if bot_list:
        await event.reply(f"{len(bot_list)} bot tapıldı:\n\n@" + "\n".join(bot_list))
    else:
        await event.reply("Bu qrupda heç bir bot yoxdur.")

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
    await event.respond("**[ɢᴇɴᴄᴇʟɪ ᴀꜱꜱɪꜱᴛᴀɴᴛ](https://t.me/GenceliRoBot) Botun Əmirləri:\n\n/start - Botu Başlat.\n/dc - Doğruluq Cəsarət Oyunu.\n/game - Oyunlara Bax.\n/startgame - Oyunu Başlad.\n/help - Əmrlərə Bax.\n/ship - Qrubda Cütlük Seçər.\n/id - Qrub Və User ID Göstərir.\n/banda - Qrupunda Olan Silinmiş Hesaplar.\n/sil - Reply Atdığı Mesaji Silər.\n/tag - Qrubda Userləri 5- Li Tağ Edər.\n/tektag - Qrubda Userləri Tək-Tək Tağ Edər.\n/adtag - Qrubda Userləri Qəribə Adlarlar Tağ Edər.\n/mafia - Mafia Oyunun Rolları İlə Tağ Elə.\n/btag - Bayrağlar İlə Tağ Elə.\n/cancel - Tağ Prosesini Dayandırar.**")


@elnur.on(events.NewMessage(pattern='/ship'))
async def ship(event):
    chat = await event.get_chat()
    if not chat.megagroup:
        return  
    members = []
    async for member in elnur.iter_participants(chat):
        members.append(member)
    selected_members = random.sample(members, 2)
    message = f"Artık bir çiftsiniz! 🚢💕\n@{selected_members[0].username}\n@{selected_members[1].username}\n\n❤️‍🩹Sevgilərin Faizi {random.choice(ship)}{random.choice(ship)}%"
    await elnur.send_message(chat, message)
  
ship = (
"1",
"2",
"3",
"4",
"5",
"6",
"7",
"8",
"9",
"0",
)
  
@elnur.on(events.NewMessage(pattern='/sil'))
async def handle_delete(event):
    chat = await event.get_chat()
    if not chat.megagroup:
        return
    if event.is_reply:
        message = await event.get_reply_message()
        await elnur.delete_messages(chat, message)

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
      usrtxt += f"↯ - [{usr.first_name}](tg://user?id={usr.id}) \n"
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
      usrtxt += f"↯ - [{random.choice(adlar)}](tg://user?id={usr.id}) "
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
      usrtxt += f"↯ - [{random.choice(adlar)}](tg://user?id={usr.id}) "
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


@elnur.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
bayrag = ['🏳️‍🌈','🏳️‍⚧️','🇦🇫','🇦🇽','🇦🇱','🇩🇿','🇦🇸','🇦🇩','🇦🇴','🇦🇮','🇦🇶','🇦🇬','🇦🇷','🇦🇲','🇦🇼','🇦🇺','🇦🇹','🇦🇿','🇧🇸','🇧🇭','🇧🇩','🇧🇧','🇧🇾','🇧🇪','🇧🇿','🇧🇯','🇧🇲','🇧🇹','🇧🇴','🇧🇦','🇧🇼','🇧🇷','🇻🇬','🇧🇳','🇧🇬','🇧🇫','🇧🇮','🇰🇭','🇨🇲','🇨🇦','🇮🇨','🇨🇻','🇧🇶','🇰🇾','🇨🇫','🇹🇩','🇮🇴','🇨🇱','🇨🇳','🇨🇽','🇨🇨','🇨🇴','🇰🇲','🇨🇬','🇨🇩','🇨🇰','🇨🇷','🇨🇮','🇭🇷','🇨🇺','🇨🇼','🇨🇾','🇨🇿','🇩🇰','🇩🇯','🇩🇲','🇩🇴','🇪🇨','🇪🇬','🇸🇻','🇬🇶','🇪🇷','🇪🇪','🇪🇹','🇸🇿','🇪🇺','🇫🇰','🇫🇴','🇫🇯','🇫🇮','🇫🇷','🇬🇫','🇵🇫','🇹🇫','🇬🇦','🇬🇲','🇬🇪','🇩🇪','🇬🇭','🇬🇮','🇬🇷','🇬🇱','🇬🇩','🇬🇵','🇬🇺','🇬🇹','🇬🇬','🇬🇳','🇬🇼','🇬🇾','🇭🇹','🇭🇳','🇭🇰','🇭🇺','🇮🇸','🇮🇳','🇮🇩','🇮🇷','🇮🇶','🇮🇪','🇮🇲','🇮🇱','🇮🇹','🇯🇲','🇯🇵','🎌','','🇯🇪','🇯🇴','🇰🇿','🇰🇪','🇰🇮','🇽🇰','🇰🇼','🇰🇬','🇱🇦','🇱🇻','🇱🇧','🇱🇸','🇱🇷','🇱🇾','🇱🇮','🇱🇹','🇱🇺','🇲🇴','🇲🇬','🇲🇼','🇲🇾','🇲🇻','🇲🇱','🇲🇹','🇲🇭','🇲🇶','🇲🇷','🇲🇺','🇾🇹','🇲🇽','🇫🇲','🇲🇩','🇲🇨','🇲🇳','🇲🇪','🇲🇸','🇲🇦','🇲🇿','🇲🇲','🇳🇦','🇳🇷','🇳🇵','🇳🇱','🇳🇨','🇳🇿','🇳🇮','🇳🇪','🇳🇬','🇳🇺','🇳🇫','🇰🇵','🇲🇰','🇲🇵','🇳🇴','🇴🇲','🇵🇰','🇵🇼','🇵🇸','🇵🇦','🇵🇬','🇵🇾','🇵🇪','🇵🇭','🇵🇳','🇵🇱','🇵🇹','🇵🇷','🇶🇦','🇷🇪','🇷🇴','🇷🇺','🇷🇼','🇼🇸','🇸🇲','🇸🇹','🇸🇦','🇸🇳','🇷🇸','🇸🇨','🇸🇱','🇸🇬','🇸🇽','🇸🇰','🇸🇮','🇬🇸','🇸🇧','🇸🇴','🇿🇦','🇰🇷','🇸🇸','🇪🇸','🇱🇰','🇧🇱','🇸🇭','🇰🇳','🇱🇨','🇵🇲','🇻🇨','🇸🇩','🇸🇪','🇸🇷','🇨🇭','🇸🇾','🇹🇼','🇹🇯','🇹🇿','🇹🇭','🇹🇱','🇹🇬','🇹🇰','🇹🇴','🇹🇹','🇹🇳','🇹🇷','🇹🇲','🇹🇨','🇹🇻','🇺🇬','🇺🇦','🇦🇪','🇬🇧','🏴󠁧󠁢󠁥󠁮󠁧󠁿','🏴󠁧󠁢󠁳󠁣󠁴󠁿','🏴󠁧󠁢󠁷󠁬󠁳󠁿','🇺🇸','🇺🇾','🇻🇮','🇺🇿','🇻🇺','🇻🇦','🇻🇪','🇻🇳','🇼🇫','🇪🇭','🇾🇪','🇿🇲','🇿🇼',]

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


@elnur.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)

print(">> Bot işləyir narahat olmayın.<<")
elnur.run_until_disconnected()
