from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

LOVER_MUSIC_BOT_IMG= "https://telegra.ph/file/a76e3f40dcc50b7696993.jpg"

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_photo(LOVER_MUSIC_BOT_IMG)
    await message.reply_text(
        f"""**Hey, I'm  ✯𝗧𝗿𝗶𝗴𝗴𝗲𝗿𝗲𝗱𝗠𝘂𝘀𝗶𝗰𝗕𝗼𝘁✯, An Open-Source Bot That Lets You Play Music In Your Telegram Groups.For Support Join Our Group @TriggeredSupport.

 The Assistant Must Be In Your Group To Play Music In The Voice Chat Of Your Group.

 Type Or Press /help To Know My Commands**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥𝗖𝗿𝗲𝗮𝘁𝗼𝗿🔥", url="https://t.me/TriggeredOwner")
                  ],[
                    InlineKeyboardButton(
                        "🔥𝗛𝗲𝗹𝗽𝗲𝗿🔥", url="https://t.me/SHIVAMIPA"
                    ),
                    InlineKeyboardButton(
                        "💬 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗚𝗿𝗼𝘂𝗽 💬", url="https://t.me/TriggeredSupport"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "💁 𝗔𝘀𝘀𝗶𝘀𝘁𝗮𝗻𝘁 💁", url="https://t.me/TriggeredAssistant"
                    )],
                    [ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/TriggeredMusicBot?startgroup=true"
                    )],
                    [ 
                    InlineKeyboardButton(
                        "➕ TriggeredNetwork ➕", url="https://t.me/TriggeredNetwork"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**💜 Triggered Music Bot is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎙️ Support Group 🎙️", url="https://t.me/TriggeredSupport")
                ]
            ]
        )
   )

