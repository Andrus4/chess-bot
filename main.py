from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import asyncio
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🧠 Задача дня", callback_data='task1')],
        [InlineKeyboardButton("♟️ Дебюты", callback_data='openings')],
        [InlineKeyboardButton("📊 Ценность фигур", callback_data='value')],
        [InlineKeyboardButton("📜 Правила", callback_data='rules')],
        [InlineKeyboardButton("💡 Советы", callback_data='tips')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привет! Я бот «Шахматные основы».\nВыбери раздел:",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'task1':
        await query.message.reply_photo(
            photo="https://lichess1.org/export/fen.gif?fen=8/8/8/5Q2/8/8/5K1k/8+w+-+-+0+1&color=white&theme=blue",
            caption="🧠 Задача дня: Мат в 1 ход\n\nБелые начинают и дают мат."
        )
        await asyncio.sleep(10)
        await query.message.reply_text(
            "✅ Ответ: Ферзь на h5 — мат! (Qh5#)\n\n💡 Почему? Король чёрных загнан в угол, и ферзь контролирует все клетки вокруг. Это классический мат по краю доски."
        )

    elif query.data == 'openings':
        await query.message.reply_text(
            "♟️ Топ-8 дебютов для новичков:\n\n"
            
            "1. **Испанская партия**\n"
            "1.e4 e5 2.♘f3 ♞c6 3.♗b5\n"
            "→ Классика, учит позиционной игре.\n\n"
            
            "2. **Сицилианская защита**\n"
            "1.e4 c5\n"
            "→ Агрессивный ответ, самый популярный.\n\n"
            
            "3. **Ферзевый гамбит**\n"
            "1.d4 d5 2.c4\n"
            "→ Позиционное давление в центре.\n\n"
            
            "4. **Дебют четырёх коней**\n"
            "1.e4 e5 2.♘f3 ♞c6 3.♘c3 ♞f6\n"
            "→ Спокойное развитие, идеален для новичков!\n\n"
            
            "5. **Итальянская партия**\n"
            "1.e4 e5 2.♘f3 ♞c6 3.♗c4\n"
            "→ Быстрое давление на f7, простая тактика.\n\n"
            
            "6. **Скандинавская защита**\n"
            "1.e4 d5\n"
            "→ Просто и честно: сразу борьба за центр.\n\n"
            
            "7. **Английское начало**\n"
            "1.c4\n"
            "→ Гибкий дебют, подходит под любой стиль.\n\n"
            
            "8. **Индийская защита (Королевский гамбит)**\n"
            "1.d4 ♞f6 2.c4 g6\n"
            "→ Гипермодерный подход: контроль центра фигурами.\n\n"
            
            "💡 Совет: Выбери 1 дебют за белых и 1 за чёрных — учи глубоко!"
        )

    elif query.data == 'value':
        await query.message.reply_photo(
            photo="https://i.imgur.com/5XJmRlP.png",
            caption="📊 Ценность фигур:\n• Пешка = 1\n• Конь = 3\n• Слон = 3\n• Ладья = 5\n• Ферзь = 9\n• Король = бесценен!"
        )

    elif query.data == 'rules':
        await query.message.reply_text(
            "📜 Важные правила:\n\n"
            "• Рокировка запрещена, если король проходит через битое поле.\n"
            "• Взятие на проходе — только сразу после хода пешки на 2 клетки!\n"
            "• Пат = ничья (нет ходов, но нет шаха)."
        )

    elif query.data == 'tips':
        await query.message.reply_text(
            "💡 Советы для новичков:\n\n"
            "1. Не выводи ферзя до 5–6 хода.\n"
            "2. Контролируй центр (пешки e4/d4).\n"
            "3. Рокируйся как можно раньше!\n"
            "4. Развивай все лёгкие фигуры к 10 ходу."
        )

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()
