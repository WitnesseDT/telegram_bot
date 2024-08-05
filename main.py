from telebot import types, asyncio_filters
from telebot import formatting
from telebot.async_telebot import AsyncTeleBot

import asyncio
import default_messages, jokes, config, inlines


bot = AsyncTeleBot(config.BOT_TOKEN, parse_mode="HTML")



@bot.callback_query_handler(
        func=None,
        text=asyncio_filters.TextFilter(starts_with="qwerty")
        )
async def handle_callback_query(query: types.CallbackQuery):
    bot.answer_callback_query(
        callback_query_id=query.id
    )

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
    await bot.send_message(message.chat.id, formatting.hcite(text[0]), parse_mode='HTML')

def any_query(query: types.InlineQuery):
    return True

@bot.inline_handler(func=any_query)
async def any_inline_query(query: types.InlineQuery):

    result = [
        inlines.result_joke_article,
        inlines.result_comliment_article,
        inlines.result_dice_article,

    ]
    await bot.answer_inline_query(
        inline_query_id=query.id,
        results=result,
        cache_time=2,
        
    )

if __name__ == "__main__":
    asyncio.run(bot.polling(skip_pending=True))