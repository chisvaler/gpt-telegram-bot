import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

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
