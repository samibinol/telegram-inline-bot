from telegram.ext import *
from telegram import *
from dotenv import load_dotenv
import logging
import os
import Database as db

# Activating logging
# TODO: changing logging status with -d argument 

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)

# Loading the API Key from the ENV file

load_dotenv()
token = os.getenv('TELEGRAM_API_KEY')


# Commands 

def start_command(update, context):
    update.message.reply_text('Hello! This is just a test version of an inline sticker bot and in no way a finished '
                              'bot. If you have any questions, you can ask my creator @samibinol. '
                              'Thank you for understanding!')


def add_sticker(update, context):
    pass


# passing cached sticker to answer_inline_query with list


def inline_query(update, context):
    query = update.inline_query.query
    inline_id = update.inline_query.id
    stickers = db.search(query)
    if stickers != "none":
        update.inline_query.answer_inline_query(inline_id, stickers)
    else:
        pass


# Catch errors from python-telegram-bot

def error(update, context):
    print(f"Update {update} caused error {context.error}")


# main() function of python-telegram-bot

def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("add", add_sticker))

    dp.add_error_handler(error)
    
    db.authenticate()

    updater.start_polling()


main()
