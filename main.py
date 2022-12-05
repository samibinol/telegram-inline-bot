from telegram.ext import *
from telegram import *
from dotenv import load_dotenv
import logging
import os


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)
logger = logging.getLogger(__name__)

load_dotenv()
token = os.getenv('TELEGRAM_API_KEY')


def start_command(update, context):
    update.message.reply_text('Hello!')


def add_sticker(update, context):
    pass


"""
def inline_query(update, context):
    query = update.inline_query.query
"""


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))

    dp.add_error_handler(error)

    updater.start_polling()


main()
