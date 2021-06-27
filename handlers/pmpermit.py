from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hallo Saya Adalah **Layanan Asisten Libra Robot.**\n\n ❗️ Rules :\n   - Jangan Melakukan Spam Pesan.\n   - Jangan Spam Pemutaran Lagu.\n\n **Note :** Kirim Link Undangan Grup Atau Username Grup Jika Userbot/Asisten Tidak Dapat Bergabung Dengan Grup Anda Atau Yang Lainnya.\n   ◉ **Channel :** @Rezy_IsBack.\n   ◉ **Dikelola Oleh :** @Reeeeeezy.\n   ◉ **Instagram :** [@ridhoalfahrezi._](https://www.instagram.com/ridhoalfahrezi._)\n\n")
  return                        
