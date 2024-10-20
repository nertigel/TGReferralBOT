import json
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums.parse_mode import ParseMode

# Load configuration from JSON file
with open('data.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

api_id = config["api_id"]
api_hash = config["api_hash"]
bot_token = config["bot_token"]
refer_to_user_id = int(config["referal_user_id"])

# Initialize the client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Load buttons from config
keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("✈️ לחץ כאן למעבר ✈️", user_id=refer_to_user_id)]
])

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("בוט מעבר", reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)

if __name__ == "__main__":
    try:
        print("Building Application...")
        app.run()
    except KeyboardInterrupt:
        print("KeyboardInterrupted by user (Ctrl+C)")

    print("Bot has been stopped!")