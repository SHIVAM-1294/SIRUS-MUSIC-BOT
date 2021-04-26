from pyrogram import Client, filters
from pyrogram.types import Message



@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""🛠️Commands 🛠

For all in group

/play <song name> - play song you requested

/dplay <song name> - play song you requested via deezer

/splay <song name> - play song you requested via jio saavn

/playlist - Show now playing list

/current - Show now playing

/song <song name> - download songs you want quickly

/search <query> - search videos on youtube with details

/deezer <song name> - download songs you want quickly via deezer

/saavn <song name> - download songs you want quickly via saavn

/video <song name> - download videos you want quickly

Admins only.

/player - open music player settings panel

/pause - pause song play

/resume - resume song play

/skip - play next song

/end - stop music play

/userbotjoin - invite assistant to your chat

• Inline search is also supported.""")

@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""🛠️Commands 🛠

For all in group

/play <song name> - play song you requested

/dplay <song name> - play song you requested via deezer

/splay <song name> - play song you requested via jio saavn

/playlist - Show now playing list

/current - Show now playing

/song <song name> - download songs you want quickly

/search <query> - search videos on youtube with details

/deezer <song name> - download songs you want quickly via deezer

/saavn <song name> - download songs you want quickly via saavn

/video <song name> - download videos you want quickly

Admins only.

/player - open music player settings panel

/pause - pause song play

/resume - resume song play

/skip - play next song

/end - stop music play

/userbotjoin - invite assistant to your chat

• Inline search is also supported.""")
