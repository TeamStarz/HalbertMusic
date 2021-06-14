from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgIAAxkBAAEKL_1gt842-B5SnR5eHrlBsfTviEt2GwACrAsAAt_YUUnNC_qAE0qWKR8E")
    await message.reply_text(
        f"""<b>Hello {message.from_user.first_name}!</b>

__Aku Adalah Zeed Music Bot, Bot Sumber Terbuka Yang Memungkinkan Anda Untuk Mengunduh Maupun Memutar Musik di Obrolan Suara Grup Telegram Anda.__
┈──────────────────────┈
➠ Invite __[Assistance](https://t.me/Zeed_RobotAss)__ Masuk Kedalam Grup Anda.\n ➠ Untuk Info, dan Panduan Selengkapnya Tekan Tombol Panduan di Bawah, Terima kasih! Have Fun!!\n\n➥ Dikelola Oleh @Reeeeeezy
        """,
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "Panduan", url="https://t.me/ZeedGoodBoys/14")
                  ],[
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/Rezy_IsBack"
                    ),
                    InlineKeyboardButton(
                        "Group Music", url="https://t.me/ZeeedMusic") 
                  ],[
                    InlineKeyboardButton(
                        "Instagram", url="https://www.instagram.com/ridhoalfahrezi._"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""'Zeed - Music' **Sedang Online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Music", url="https://t.me/ZeeedMusic"
                    ),
                    InlineKeyboardButton(
                        "Rezy 🇲🇨", url="https://t.me/Reeeeeezy"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""'Zeed - Musik' **Sedang Online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Instagram", url="https://www.instagram.com/ridhoalfahrezi._") 
                ],[
                    InlineKeyboardButton(
                        "Group Music", url="https://t.me/ZeeedMusic"
                    )
                ]
            ]
        )
   )
