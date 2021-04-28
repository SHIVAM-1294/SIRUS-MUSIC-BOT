from pyrogram import Client, filters
from pyrogram.types import Message



@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""🛠️ 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 🛠

🔥🔥𝗙𝗢𝗥 𝗔𝗟𝗟 𝗜𝗡 𝗚𝗥𝗢𝗨𝗣🔥🔥

/play <song name> - Play Song You Requested
/dplay <song name> - play Song You Requested Via Deezer
/splay <song name> - Play Song You Requested Via Jio Saavan
/playlist - Show Now Playing List
/current - Show Now Playing
/song <song name> - Download Songs You Want Quickly
/search <query> - Search Videos On Youtube With Details
/deezer <song name> - Download Songs You Want Quickly Via Deezer
/saavn <song name> - Download Songs You Want Quickly Via Saavan
/video <song name> - Download Videoss You Want Quickly

🔥🔥𝗢𝗡𝗟𝗬 𝗙𝗢𝗥 𝗔𝗗𝗠𝗜𝗡𝗦🔥🔥

/player - Open Music Player Setting Panel
/pause - Pause Song Play
/resume - Resume Song Play
/skip - Play Next Song
/end - Stop Music Play
/userbotjoin - Invite Assistant To Your Chat

• Inline Search Is Also Supported.""")

@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""🛠️ 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 🛠

🔥🔥𝗙𝗢𝗥 𝗔𝗟𝗟 𝗜𝗡 𝗚𝗥𝗢𝗨𝗣🔥🔥

/play <song name> - Play Song You Requested
/dplay <song name> - play Song You Requested Via Deezer
/splay <song name> - Play Song You Requested Via Jio Saavan
/playlist - Show Now Playing List
/current - Show Now Playing
/song <song name> - Download Songs You Want Quickly
/search <query> - Search Videos On Youtube With Details
/deezer <song name> - Download Songs You Want Quickly Via Deezer
/saavn <song name> - Download Songs You Want Quickly Via Saavan
/video <song name> - Download Videoss You Want Quickly

🔥🔥𝗢𝗡𝗟𝗬 𝗙𝗢𝗥 𝗔𝗗𝗠𝗜𝗡𝗦🔥🔥

/player - Open Music Player Setting Panel
/pause - Pause Song Play
/resume - Resume Song Play
/skip - Play Next Song
/end - Stop Music Play
/userbotjoin - Invite Assistant To Your Chat

• Inline Search Is Also Supported.""")
