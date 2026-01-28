from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salom 👋\nBu 100% tekin Telegram bot.\n/help yozib ko‘r."
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message
