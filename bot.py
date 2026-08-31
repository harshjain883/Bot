import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client("dm_button_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    await message.reply_text("👋 **Hello!**\n\nMujhe Telegram **User ID** bhejo, main DM button dunga.")

@app.on_message(filters.text & filters.private)
async def id_to_dm_button(client, message):
    text = message.text.strip()
    if not text.isdigit():
        await message.reply_text("❌ Kripya valid numeric **User ID** bhejein.")
        return

    user_id = int(text)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(text=f"Direct DM 👉 {user_id}", url=f"tg://user?id={user_id}")]
    ])
    await message.reply_text(f"👤 **Target User ID:** `{user_id}`", reply_markup=keyboard)

if __name__ == "__main__":
    app.run()
    
