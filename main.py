from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

# توکن ربات
TOKEN = os.getenv("8076208218:AAED3z9q0FsO0aHeHk5Mc4M5JiH6jJ9JrN8")

def start(update, context):
    update.message.reply_text("سلام! من یک بات پاسخ‌دهی خودکار هستم!")

def echo(update, context):
    user_message = update.message.text
    update.message.reply_text(f"شما گفتید: {user_message}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
