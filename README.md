# telegramBot-Testing

how to do it
what to import:
import Final -> typing
import Update -> telegram
import Application, CommandHandler, MessageHandler, filters, ContextTypes -? telegram.ext
what to install 
pip install python-telegram-bot


we need:
token = string
bot name = string


# command
async function:
- start command(update: Udpate, context: ContextTypes.DEFAULT_TYPE):
      await update.message.reply_text("string")



# response
handle_message()
handle_response()




