from telegram.ext import *
import responses as res
import constants as keys
def start_command(update, context):
    update.message.reply_text('Type keys to search from Google')

def help_command(update,context):
    update.message.reply_text('Fast searching bot from Google. Hit start command to search!')

def result_from_search(update, context):
    response = res.google_search_result(update.message.text)
    for i in response:
        update.message.reply_text(i)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY,use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text,result_from_search))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

main()


