
from telebot import types


def kb_joke_handler(voteP: str = 0, voteN: str = 0,totalVotes: str = 0, base_source_joke: str = ""):
    kb = types.InlineKeyboardMarkup()
    votesP = "👆 {0}".format(voteP)
    votesN = "👇 {0}".format(voteN)
    totalVote = "(ToT)/~~~ {0}".format(totalVotes)
    source_joke = base_source_joke
    if(source_joke == ""):
        button_voteP = types.InlineKeyboardButton(
            text = votesP,
            callback_data="qwerty1"
        )
        button_voteN = types.InlineKeyboardButton(
            text = votesN,
            callback_data="qwerty2"
        )
        button_total_vote = types.InlineKeyboardButton(
            text = totalVote,
            callback_data="qwerty3"
        )
    else:
        button_voteP = types.InlineKeyboardButton(
            text = votesP,
            url=source_joke
        )
        button_voteN = types.InlineKeyboardButton(
            text = votesN,
            url=source_joke
        )
        button_total_vote = types.InlineKeyboardButton(
            text = totalVote,
            url=source_joke
        )
    kb.row(button_voteP, button_total_vote, button_voteN)
    return kb