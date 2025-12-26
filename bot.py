from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "TrixelAutoFilterBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🎬 Trixel Movie Group",
                    url="https://t.me/TRIXEL_MOVIE"
                )
            ],
            [
                InlineKeyboardButton(
                    "➕ Add Me To Your Group",
                    url="https://t.me/YourBotUserName?startgroup=true"
                )
            ],
            [
                InlineKeyboardButton(
                    "📸 Follow on Instagram",
                    url="https://instagram.com/your_instagram_id"
                )
            ]
        ]
    )

    await message.reply_photo(
        photo="start.jpg",   # 🔁 Or use Image URL
        caption=
        "🍿 **Welcome!** 🍿\n\n"
        "I am the filter bot of the **Trixel Movie** group 🎬.\n"
        "You can add me to your channel or group and use me.\n\n"
        "🍿 **സ്വാഗതം!** 🍿\n\n"
        "ഞാൻ **Trixel Movie 🎬 ഗ്രൂപ്പിന്റെ ഫിൽട്ടർ ബോട്ട്** ആണ്.\n"
        "നിങ്ങൾ എന്നെ നിങ്ങളുടെ Channel / Group-ൽ add ചെയ്ത്\n"
        "use ചെയ്യാവുന്നതാണ് ☺️",
        reply_markup=buttons
    )

@app.on_message(filters.text & ~filters.command)
async def auto_filter(client, message):
    text = message.text.lower()

    if "movie" in text:
        await message.reply_text("🎬 Movie Found!")
    elif "song" in text:
        await message.reply_text("🎵 Song Found!")
    else:
        await message.reply_text("❌ No Result Found.")

app.run()
