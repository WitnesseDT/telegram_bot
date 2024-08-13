from telebot import formatting

BOT_HELP = """Ты нажав хелп
Бот для приколов кык
"""

START_MSG = """Ты нажав старт"""

HELLO_MSG = formatting.format_text(
    "Приветственное сообщение от ", formatting.hbold("чудо бота\n"), "/help - для хелпа.\n/joke - для джока."
)