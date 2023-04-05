from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()
