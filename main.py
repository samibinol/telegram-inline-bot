from telegram.ext import *
import telegram
import logging
import Database as db
from config import TELEGRAM_API_KEY
from ast import literal_eval

# Activating logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Commands 

def start_command(update, context):
    update.message.reply_text('Hello! This is just a test version of an inline sticker bot and in no way a finished '
                              'bot. If you have any questions, you can ask my creator @samibinol. '
                              'Thank you for understanding!')


def add_sticker(update, context):
    try:
        sid = update.message.reply_to_message.sticker.file_id
    except AttributeError:
        update.message.reply_text('Please reply to a sticker.')
    else:
        command = update.message.text
        tags = command.replace(' ', ',')[5:]
        try:
            db.add(sid, tags)
        except Exception:
            update.message.reply_text('Error adding the sticker to the database. Contact @samibinol.')
        else:
            update.message.reply_text('Added!')


# passing cached sticker to answer_inline_query with list


def inline_query(update, context):
    results = []
    query = update.inline_query.query

    if query == "":
        return

    inline_id = update.inline_query.id

    stickers = db.search(query)
    st = literal_eval(stickers)
    st1 = [i[0] for i in st]
    print(st1)

    for index, response in enumerate(st1):
        results.append(telegram.InlineQueryResultCachedSticker(index, response))

    print(results)
    update.inline_query.answer(results=results, cache_time=0)


# Catch errors from python-telegram-bot

def error(update, context):
    print(f"Update {update} caused error {context.error}")


# main() function of python-telegram-bot

def main():

    updater = Updater(TELEGRAM_API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("add", add_sticker))

    dp.add_handler(InlineQueryHandler(inline_query))

    dp.add_error_handler(error)

    updater.start_polling()


main()
