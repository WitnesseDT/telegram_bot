from telebot import TeleBot, types
from telebot import formatting
from telebot.async_telebot import AsyncTeleBot
import random
import asyncio
import default_messages, jokes, config


bot = AsyncTeleBot(config.BOT_TOKEN)


@bot.message_handler(content_types=['sticker'])
async def send_reaction_onsticker(message: types.Message):
    await bot.send_sticker(chat_id=message.chat.id, sticker=message.sticker.file_id)

@bot.message_handler(commands=['start'])
async def send_start_message(message: types.Message):
    text = default_messages.START_MSG
    await bot.reply_to(message, text)

@bot.message_handler(commands=['help'])
async def send_help_message(message: types.Message):
    text = default_messages.BOT_HELP
    await bot.reply_to(message, text)

@bot.message_handler(commands=['joke'])
async def send_joke_message(message: types.Message):
    text = jokes.get_jokesi()
    await bot.send_message(message.chat.id, formatting.hcite(text), parse_mode='HTML')

def any_query(query: types.InlineQuery):
    return True

@bot.inline_handler(func=any_query)
async def any_inline_query(query: types.InlineQuery):
    
    content = types.InputTextMessageContent(
        message_text=formatting.hcite(jokes.get_jokesi()),
        parse_mode="HTML"
    )
    result_article = types.InlineQueryResultArticle(
        id = "joke-id",
        title = "Шутка минутка",
        input_message_content = content,
        thumbnail_url = config.THUMNAIL_PHOTO_FOR_INLINE_QUERY
    )
    result = [
        result_article,
    ]
    await bot.answer_inline_query(
        inline_query_id=query.id,
        results=result,
        cache_time=4
    )

# @bot.message_handler()
# async def send_message(message: types.Message):
#     text = message.text
#     if 'привет' == text.lower():
#        text = "И тебе привет!"
#     elif 'как дела' in text.lower():
#         text = "Хорошо! А у вас как?"
#     elif 'пока' in text.lower() or 'до свидания' in text.lower():
#         text = "До новых встреч!"
#     await bot.reply_to(message, text)



if __name__ == "__main__":
    asyncio.run(bot.polling(skip_pending=True))