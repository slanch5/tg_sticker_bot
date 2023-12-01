import logging
import aiogram
from aiogram import Bot, Dispatcher, types

API_TOKEN = '6402497897:AAGj1SQcbjiF0b-fP3_lDpjYtK982OAbepo'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=types.ContentType.TEXT)
async def reply_with_sticker(message: types.Message):
    sticker_id = 'CAACAgIAAxkBAAEK4BRlaeATJY5TD3pHKzJC9FC9SNRAJwACtUYAAqrDYEopnyiJs0SYwzME'  
    # Перевірка, чи користувач ввів "Доброго вечора"
    if message.text.lower() == 'доброго вечора':
        # Відправляємо стікер у відповідь
        await bot.send_sticker(message.chat.id, sticker_id)

if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)
