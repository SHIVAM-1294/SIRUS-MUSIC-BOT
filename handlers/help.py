from pyrogram import Client, filters
from pyrogram.types import Message



@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""๐ ๏ธ ๐๐ข๐ ๐ ๐๐ก๐๐ฆย ๐ 

๐ฅ๐ฅ๐๐ข๐ฅ ๐๐๐ ๐๐ก ๐๐ฅ๐ข๐จ๐ฃ๐ฅ๐ฅ

/play <song name>ย - Play Song You Requested
/dplay <song name>ย - play Song You Requested Via Deezer
/splay <song name>ย - Play Song You Requested Via Jio Saavan
/playlistย - Show Now Playing List
/currentย - Show Now Playing
/song <song name>ย - Download Songs You Want Quickly
/search <query>ย - Search Videos On Youtube With Details
/deezer <song name>ย - Download Songs You Want Quickly Via Deezer
/saavn <song name>ย - Download Songs You Want Quickly Via Saavan
/video <song name>ย - Download Videoss You Want Quickly

๐ฅ๐ฅ๐ข๐ก๐๐ฌ ๐๐ข๐ฅ ๐๐๐ ๐๐ก๐ฆ๐ฅ๐ฅ

/playerย - Open Music Player Setting Panel
/pauseย - Pause Song Play
/resumeย - Resume Song Play
/skipย - Play Next Song
/endย - Stop Music Play
/userbotjoinย - Invite Assistant To Your Chat

โข Inline Search Is Also Supported.""")

@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""๐ ๏ธ ๐๐ข๐ ๐ ๐๐ก๐๐ฆย ๐ 

๐ฅ๐ฅ๐๐ข๐ฅ ๐๐๐ ๐๐ก ๐๐ฅ๐ข๐จ๐ฃ๐ฅ๐ฅ

/play <song name>ย - Play Song You Requested
/dplay <song name>ย - play Song You Requested Via Deezer
/splay <song name>ย - Play Song You Requested Via Jio Saavan
/playlistย - Show Now Playing List
/currentย - Show Now Playing
/song <song name>ย - Download Songs You Want Quickly
/search <query>ย - Search Videos On Youtube With Details
/deezer <song name>ย - Download Songs You Want Quickly Via Deezer
/saavn <song name>ย - Download Songs You Want Quickly Via Saavan
/video <song name>ย - Download Videoss You Want Quickly

๐ฅ๐ฅ๐ข๐ก๐๐ฌ ๐๐ข๐ฅ ๐๐๐ ๐๐ก๐ฆ๐ฅ๐ฅ

/playerย - Open Music Player Setting Panel
/pauseย - Pause Song Play
/resumeย - Resume Song Play
/skipย - Play Next Song
/endย - Stop Music Play
/userbotjoinย - Invite Assistant To Your Chat

โข Inline Search Is Also Supported.""")
