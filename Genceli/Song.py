from FallenMusic import BOT_MENTION, BOT_USERNAME, LOGGER, app
import config
from yt_dlp import YoutubeDL
import os, requests, wget, youtube_dl, time, yt_dlp
from random import randint
from urllib.parse import urlparse
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram import Client, filters
from youtube_search import YoutubeSearch
from pyrogram.handlers import MessageHandler
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
)

#### Əkmə Oğlum

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


buttons = {
  "markup_for_private": InlineKeyboardMarkup([[InlineKeyboardButton('Playlist 🎧', url=f'https://t.me/ssmusiclist')]]),
  "add_to_group": InlineKeyboardMarkup([[InlineKeyboardButton('️✨️ Qrupa əlavə et ️✨️', url=f'https://t.me/SSMusicRobot?startgroup=true')]]),
}


@app.on_message(filters.command(["song"]))
def song(client, message):

    message.delete()
    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    chutiya = "["+user_name+"](tg://user?id="+str(user_id)+")"
    
    isteyen = message.from_user.first_name 
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply(f"🔎 **Axtarılır...{query}**")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:100]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb@pastermusicbot.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)

### Oğurlamq Oğlum
        performer = f"Unknown Artist"  
        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]
        channel = results[0]["channel"]   

    except Exception as e:
        m.edit("İstədiyiniz musiqi tapılmadı 😔")
        print(str(e))
        return
    m.edit(f"🎵**{title}**")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        caption_for_logchannel = f'''
**╭───────────────**
**├▷ 🎧 Başlıq: [{title}]({link})**
**├───────────────**
**├▷ 👁‍🗨 Baxış: {views}**
**├───────────────**
**├▷ 👤 İstəyən: {isteyen}**
**├───────────────**
**├▷ 🌀 Bot:  @SSMusicRobot**
**╰───────────────**
'''
        caption_for_private = f'''
**╭───────────────**
**├▷ 🎧 Başlıq: [{title}]({link})**
**├───────────────**
**├▷ 👁‍🗨 Baxış: {views}**
**├───────────────**
**├▷ 🌀 Bot:  @SSMusicRobot**
**╰───────────────**
'''

        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        m.edit("📤 Yüklənir..")
        message.reply_audio(audio_file, caption=caption_for_private, quote=False, title=title, duration=dur, thumb=thumb_name, performer = f"SSMusicRobot", reply_markup=buttons['markup_for_private'])
        m.delete()
        app.send_audio(chat_id=-1002074288242, audio=audio_file, caption=caption_for_logchannel, performer = f"@SSMusicRobot", title=title, duration=dur, thumb=thumb_name, reply_markup=buttons['add_to_group'])
    except Exception as e:
        m.edit(f'**⚠️ Gözlənilməyən xəta yarandı.**\n**Xahiş edirəm xətanı @khalilovss sahibimə xəbərdar et!**')
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
