from telegram.ext import *
from telegram import *
from dotenv import load_dotenv
import logging
import os

# Activating logging
# TODO: changing logging status with -d argument 

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)
logger = logging.getLogger(__name__)

# Loading the API Key from the ENV file

load_dotenv()
token = os.getenv('TELEGRAM_API_KEY')


# Commands 

def start_command(update, context):
    update.message.reply_text('Hello!')


def add_sticker(update, context):
    pass


# TODO: adding the inline function

"""
def inline_query(update, context):
    query = update.inline_query.query
"""


# Catch errors from python-telegram-bot

def error(update, context):
    print(f"Update {update} caused error {context.error}")


# main() function of python-telegram-bot

def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))

    dp.add_error_handler(error)

    updater.start_polling()


main()
