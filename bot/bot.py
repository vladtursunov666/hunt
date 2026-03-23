from __future__ import annotations

import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
WEBAPP_URL = os.getenv("TELEGRAM_WEBAPP_URL", "https://example.com")


async def start(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🚗 Открыть приложение", web_app=WebAppInfo(url=WEBAPP_URL))],
            [InlineKeyboardButton("⭐ Подписка Premium", callback_data="premium_stub")],
        ]
    )
    telegram_id = update.effective_user.id if update.effective_user else "unknown"
    if update.message:
        await update.message.reply_text(
            "Hunt Auto — аналитика авто с торгов по банкротству.\n"
            f"Ваш Telegram ID: {telegram_id}\n"
            "Откройте Mini App, чтобы посмотреть лоты, аналитику рынка и избранное.",
            reply_markup=keyboard,
        )


async def premium(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text("Premium-подписка пока в MVP как заглушка. Скоро добавим оплату и расширенные фильтры.")


async def premium_stub(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    if update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.message.reply_text(
            "Premium-подписка пока в MVP как заглушка. Сейчас доступны базовые фильтры, избранное и аналитика рынка."
        )


def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is required")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("premium", premium))
    app.add_handler(CallbackQueryHandler(premium_stub, pattern="^premium_stub$"))
    app.run_polling()


if __name__ == "__main__":
    main()
