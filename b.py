import time
from datetime import datetime, timedelta
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Set up your Telegram bot token
bot_token = "6766117217:AAEOz-GXkWyz7U1aFpOIw_mg5B913f_dgKY"
chat_id = "5779948934"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Bot is active. You'll receive the time every 5 minutes.")

def send_time(context: CallbackContext) -> None:
    current_time = datetime.utcnow() + timedelta(hours=6)
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S GMT+6")
    context.bot.send_message(chat_id=chat_id, text=f"Current time in GMT+6: {formatted_time}")

def main() -> None:
    updater = Updater(token=bot_token)
    dispatcher = updater.dispatcher

    # Register the /start command
    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)

    # Set up the time-sending job every 5 minutes
    job_queue = updater.job_queue
    job_queue.run_repeating(send_time, interval=300, first=0)

    # Start the bot
    updater.start_polling()

    # Run the bot until you decide to stop
    updater.idle()

if __name__ == '__main__':
    main()
  
