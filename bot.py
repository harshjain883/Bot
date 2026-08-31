from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Telegram API credentials (my.telegram.org aur @BotFather se prapt karein)
API_ID = 35304614          # Apna API ID dalein (int)
API_HASH = "5607bebe7e0fe210300e14549ac85b92"  # Apna API Hash dalein
BOT_TOKEN = "8834143519:AAGo2LFOAwG3mApLAEKC7ZAeRqkxxKYTA_M"# Apna Bot Token dalein

app = Client("dm_button_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    await message.reply_text(
        "👋 **Hello!**\n\nMujhe koi bhi Telegram **User ID** bhejiye, main aapko direct DM link button bana kar dunga."
    )


@app.on_message(filters.text & filters.private)
async def id_to_dm_button(client, message):
    text = message.text.strip()

    # Sirf numbers check karne ke liye
    if not text.isdigit():
        await message.reply_text("❌ Kripya valid numeric **User ID** bhejein (Example: `123456789`).")
        return

    user_id = int(text)
    
    # Telegram deep link format for User ID
    dm_url = f"tg://user?id={user_id}"

    # Inline button setup
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(text=f"Direct DM 👉 {user_id}", url=dm_url)]
    ])

    await message.reply_text(
        f"👤 **Target User ID:** `{user_id}`\n\nDirect chat open karne ke liye neeche button par click karein:",
        reply_markup=keyboard
    )


if __name__ == "__main__":
    print("Bot chalu ho raha hai...")
    app.run()
  
