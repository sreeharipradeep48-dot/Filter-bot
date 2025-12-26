from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import API_ID, API_HASH, BOT_TOKEN, ADMINS

app = Client(
    "TrixelAutoFilterBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

FILTERS = {}


def is_admin(user_id):
    return user_id in ADMINS


# ================= START =================
@app.on_message(filters.command("start"))
async def start(client, message):

    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🎬 Trixel Movie Group", url="https://t.me/trixel_movies")],
            [InlineKeyboardButton("➕ Add Me To Your Group", url="https://t.me/@tony_stark_v3_bot?startgroup=true")],
            [InlineKeyboardButton("📸 Instagram", url="https://www.instagram.com/sreehari_._pradeep?igsh=YWMzMzRzZWx2dWFy")],
            [InlineKeyboardButton("ℹ️ About Bot", callback_data="about_bot")]
        ]
    )

    await message.reply_photo(
        photo="https://graph.org/file/62386b57bf0394d7bd917-959daf5976f788890f.jpg https://graph.org/file/45f2868f0396506971dd4-319c9643069396cfbb.jpg",
        caption=
        "🍿 **Welcome!** 🍿\n\n"
        "I am the filter bot of the **Trixel Movie** group 🎬.\n"
        "You can add me to your group and use me.\n\n"
        "🍿 **സ്വാഗതം!** 🍿\n\n"
        "ഞാൻ **Trixel Movie 🎬 ഗ്രൂപ്പിന്റെ ഫിൽട്ടർ ബോട്ട്** ആണ്.\n"
        "നിങ്ങൾ എന്നെ നിങ്ങളുടെ Group-ൽ add ചെയ്ത് use ചെയ്യാവുന്നതാണ് ☺️",
        reply_markup=buttons
    )


# ================= ABOUT =================
@app.on_callback_query(filters.regex("^about_bot$"))
async def about_bot(client, callback_query):

    about_text = (
        "╭────[ ᴍʏ ᴅᴇᴛᴀɪʟs ]────⍟\n"
        "├⍟ Mʏ Nᴀᴍᴇ : Tony Stark\n"
        "├⍟ Dᴇᴠᴇʟᴏᴘᴇʀ : Sreehari\n"
        "├⍟ Lɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ\n"
        "├⍟ Lᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ 𝟹\n"
        "├⍟ Dᴀᴛᴀʙᴀsᴇ : ᴍᴏɴɢᴏ ᴅʙ\n"
        "├⍟ Bᴏᴛ Sᴇʀᴠᴇʀ : Render\n"
        "├⍟ Bᴜɪʟᴅ Sᴛᴀᴛᴜs : ᴠ1.4 [ ꜱᴛᴀʙʟᴇ ]\n"
        "╰───────────────⍟"
    )

    await callback_query.message.reply_text(about_text)
    await callback_query.answer()


# ================= FILTER COMMANDS =================
@app.on_message(filters.command("filter"))
async def add_filter(client, message):
    if not is_admin(message.from_user.id):
        return await message.reply_text("❌ Admin only command")

    try:
        _, keyword, reply = message.text.split(" ", 2)
    except:
        return await message.reply_text("Usage:\n/filter keyword reply")

    FILTERS[keyword.lower()] = reply
    await message.reply_text(f"✅ Filter added for `{keyword}`")


@app.on_message(filters.command("del"))
async def delete_filter(client, message):
    if not is_admin(message.from_user.id):
        return await message.reply_text("❌ Admin only command")

    try:
        _, keyword = message.text.split(" ", 1)
    except:
        return await message.reply_text("Usage:\n/del keyword")

    if keyword.lower() in FILTERS:
        del FILTERS[keyword.lower()]
        await message.reply_text(f"🗑️ Filter `{keyword}` deleted")
    else:
        await message.reply_text("❌ Filter not found")


@app.on_message(filters.command("filters"))
async def list_filters(client, message):
    if not FILTERS:
        return await message.reply_text("❌ No filters added")

    text = "📂 **Available Filters:**\n\n"
    for k in FILTERS:
        text += f"• `{k}`\n"

    await message.reply_text(text)


# ================= AUTO FILTER =================
@app.on_message(filters.text & ~filters.regex("^/"))
async def auto_filter(client, message):
    text = message.text.lower()

    for keyword, reply in FILTERS.items():
        if keyword in text:
            return await message.reply_text(reply)


app.run()
