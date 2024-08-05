
from telebot import async_telebot, types, formatting
import config, jokes, complinemt, buttons

joke = jokes.get_jokesi()
compliments = complinemt.get_for_women_comlinemts()
kb = buttons.kb_joke_handler(joke[1], joke[2], joke[3], joke[4])
dice = "🎰"

content_dice = types.InputTextMessageContent(
    message_text=dice
)

content_joke = types.InputTextMessageContent(
    message_text=formatting.format_text(formatting.hbold("Шутейка: \n"), formatting.hcite(joke[0]),),
    parse_mode="HTML",
)

content_compliment = types.InputTextMessageContent(
    message_text=formatting.format_text(formatting.hbold("Коплементарный: \n"), formatting.hcite(compliments)),
    parse_mode="HTML"
)


result_joke_article = types.InlineQueryResultArticle(
    id = "joke-id",
    title = "Шутка минутка",
    input_message_content = content_joke,
    thumbnail_url = config.THUMNAIL_PHOTO_JOKE_FOR_INLINE_QUERY,
    reply_markup = kb
    
) 
result_comliment_article = types.InlineQueryResultArticle(
    id = "complment-id",
    title = "Комплиментарный комплимент",
    input_message_content = content_compliment,
    thumbnail_url = config.THUMNAIL_PHOTO_COMLIMENT_FOR_INLINE_QUERY
)

result_dice_article = types.InlineQueryResultArticle(
    id = "dice-id",
    title = "Штука",
    input_message_content = content_dice
)