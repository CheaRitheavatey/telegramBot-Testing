from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [['Seller', 'Buyer']]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    await update.message.reply_text('Welcome! Are you a Seller or a Buyer?', reply_markup=reply_markup)

async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_response = update.message.text
    if user_response == 'Seller':
        await ask_business_info(update, context)
    elif user_response == 'Buyer':
        await update.message.reply_text('Thank you for your interest! Feel free to browse.')

async def ask_business_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('What is your business name?')
    # Collect more information as needed

async def main() -> None:
    application = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_response))

    try:
        await application.run_polling()
    finally:
        await application.shutdown()  # Ensure proper shutdown

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())