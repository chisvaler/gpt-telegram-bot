import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TELEGRAM_TOKEN = '6811098760:AAFG6HYkpQYAmYUKGpQONFnbGOrV7iKiIlQ'
OPENAI_API_KEY = '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'


client = openai.OpenAI(api_key=OPENAI_API_KEY)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    print(f"[ВХОД]: {user_message}")

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": user_message}
            ],
            max_tokens=300
        )
        reply = response.choices[0].message.content
        print(f"[ОТВЕТ]: {reply}")
        await update.message.reply_text(reply)

    except Exception as e:
        print(f"[ОШИБКА]: {e}")
        await update.message.reply_text(f"Ошибка: {e}")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("✅ Бот запущен! Жду сообщений в Telegram...")
app.run_polling()
