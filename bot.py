import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        try:
            await context.bot.send_message(
                chat_id=member.id,
                text="👋 Welcome to the group, bro! Let me know if you need anything 💪"
            )
        except Exception as e:
            print(f"Couldn't DM {member.username or member.id}: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member))
    print("✅ Bot is running...")
    app.run_polling()
