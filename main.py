from telebot import types, asyncio_filters
from telebot import formatting
from telebot.async_telebot import AsyncTeleBot

import asyncio
import default_messages as msg
import jokes, config, buttons, complinemt, memegenapi

bot = AsyncTeleBot(config.BOT_TOKEN, parse_mode="HTML")



@bot.callback_query_handler(
        func=None,
        text=asyncio_filters.TextFilter(starts_with="qwerty")
        )
async def handle_callback_query(query: types.CallbackQuery):
    bot.answer_callback_query(
        callback_query_id=query.id
    )

@bot.message_handler(commands=['start'])
async def hello_messages(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=msg.HELLO_MSG,
    )

@bot.message_handler(commands=['help'])
async def send_help_message(message: types.Message):
    text = msg.BOT_HELP
    await bot.reply_to(message, text)

@bot.message_handler(commands=['joke'])
async def send_joke_message(message: types.Message):
    text = jokes.get_every_day_jokesi()
    await bot.send_message(message.chat.id, formatting.hcite(text[0]), parse_mode='HTML')

def mems_query(query: types.InlineQuery):
    return "мем" in query.query.lower()

def anekdot_query(query: types.InlineQuery):
    return "анекдот" in query.query.lower()

def komliment_query(query: types.InlineQuery):
    return "комплимент" in query.query.lower()

def any_query(query: types.InlineQuery):
    return True



@bot.inline_handler(func=mems_query)
async def admins_inline_query(query: types.InlineQuery):
    mems_pic, _, mems_ids = memegenapi.get_meme_pic()
    content_mems_photo = []
    result_meme_photo = []
    for i in range(30):
        content_mems_photo.append(types.InputTextMessageContent(
            message_text=mems_pic[i],
            parse_mode="HTML",
        ))
        result_meme_photo.append(types.InlineQueryResultPhoto(
            id = f"{mems_ids[i]}",
            photo_url = mems_pic[i],
            thumbnail_url= mems_pic[i],
            input_message_content=content_mems_photo[i],
        ))
    result = [
    result_meme_photo,
    ]
    await bot.answer_inline_query(
        inline_query_id=query.id,
        results=result[0],
        cache_time=10,
    )
    

@bot.inline_handler(func=anekdot_query)
async def anekdot_inline_query(query: types.InlineQuery):
    joke_every_day = jokes.get_every_day_jokesi()
    joke_best_week = jokes.get_best_week_jokesi()
    kb_every_day = buttons.kb_joke_every_day_handler(joke_every_day[1], joke_every_day[2], joke_every_day[3], joke_every_day[4])
    kb_best = buttons.kb_joke_best_week_handler(joke_best_week[1], joke_best_week[2], joke_best_week[3], joke_best_week[4])
    content_joke_every_day = types.InputTextMessageContent(
        message_text=formatting.format_text(formatting.hbold("Шутейка: \n"), formatting.hcite(joke_every_day[0]),),
        parse_mode="HTML",
    )
    content_joke_best_week = types.InputTextMessageContent(
        message_text=formatting.format_text(formatting.hbold("Шутейка: \n"), formatting.hcite(joke_best_week[0]),),
        parse_mode="HTML",
    )

    result_joke_every_day_article = types.InlineQueryResultArticle(
        id = "joke-every-day-id",
        title = "Шутка минутка.",
        description = "Ежедневные шутейки.",
        input_message_content = content_joke_every_day,
        thumbnail_url = config.THUMNAIL_PHOTO_JOKE_FOR_INLINE_QUERY,
        reply_markup = kb_every_day
    ) 
    result_joke_best_week_article = types.InlineQueryResultArticle(
        id = "joke-best-week-id",
        title = "Шутка минутка.",
        description = "Лучшее за неделю.", 
        input_message_content = content_joke_best_week,
        thumbnail_url = config.THUMNAIL_PHOTO_JOKE_FOR_INLINE_QUERY,
        reply_markup = kb_best
    ) 
    result = [
        result_joke_every_day_article,
        result_joke_best_week_article
    ]

    await bot.answer_inline_query(
        inline_query_id=query.id,
        results=result,
        cache_time=2,
    )

@bot.inline_handler(func=komliment_query)
async def komliment_inline_query(query: types.InlineQuery):
    compliments = complinemt.get_for_women_comlinemts()

    content_compliment = types.InputTextMessageContent(
        message_text=formatting.format_text(formatting.hbold("Коплементарный: \n"), formatting.hcite(compliments)),
        parse_mode="HTML"
    )

    result_comliment_article = types.InlineQueryResultArticle(
        id = "complment-id",
        title = "Комплиментарный комплимент",
        input_message_content = content_compliment,
        thumbnail_url = config.THUMNAIL_PHOTO_COMLIMENT_FOR_INLINE_QUERY
    )

    result = [
        result_comliment_article,

    ]

    await bot.answer_inline_query(
        inline_query_id=query.id,
        results=result,
        cache_time=2,
    )



if __name__ == "__main__":
    asyncio.run(bot.polling(skip_pending=True))