from bs4 import BeautifulSoup
from lxml import etree
import requests as rq
import random
from urllib.parse import unquote
from datetime import date, timedelta

xpaths = "//div[@class=\"topicbox\"]/div[@class=\"text\"]"
vote_xpath = "//div[@class=\"topicbox\"]/div[@class=\"votingbox\"]/div[@class=\"rates\"]"
url_jokesi_every_day = 'https://www.anekdot.ru/release/anekdot/day/{0}/'.format(date.today() - timedelta(days = 1))
url_jokesi_best_week = "https://www.anekdot.ru/release/anekdot/week/"

def get_every_day_jokesi():
    res = rq.get(url_jokesi_every_day)
    bs = BeautifulSoup(res.text, "html.parser")
    elements_of_joke = etree.HTML(str(bs))

    joks = ""
    voteP = 0
    voteN = 0
    votes = 0
    source_of_joke = ""

    element_joke = elements_of_joke.xpath(xpaths)
    joke_votes = elements_of_joke.xpath(vote_xpath)
    
    valuesOfElement = len(element_joke)


    valueOfElement = random.randrange(0, valuesOfElement)
    _, votes, voteP, voteN = joke_votes[valueOfElement].get('data-r').split(';')
    element_btn = joke_votes[valueOfElement].getnext()
    try:
        element_source_of_joke = element_btn.getchildren()[2]
        if(element_source_of_joke.get('data-site') != None):
            source_of_joke = unquote(element_source_of_joke.get('data-site'))
    except:
        source_of_joke = ""

    if element_joke[valueOfElement].getchildren() == []:
        jok = element_joke[valueOfElement]
        joks = jok.text
    else:
        childs = element_joke[valueOfElement].getchildren()
        joks = joks + element_joke[valueOfElement].text + '\n'
        for child in childs:
            joks = joks + child.tail + '\n'
    JOKES = [joks, voteP, voteN, votes, source_of_joke]
    return JOKES


def get_best_week_jokesi():
    res = rq.get(url_jokesi_best_week)
    bs = BeautifulSoup(res.text, "html.parser")
    elements_of_joke = etree.HTML(str(bs))

    joks = ""
    voteP = 0
    voteN = 0
    votes = 0
    source_of_joke = ""

    element_joke = elements_of_joke.xpath(xpaths)
    joke_votes = elements_of_joke.xpath(vote_xpath)
    
    valuesOfElement = len(element_joke)


    valueOfElement = random.randrange(0, valuesOfElement)
    _, votes, voteP, voteN = joke_votes[valueOfElement].get('data-r').split(';')
    element_btn = joke_votes[valueOfElement].getnext()
    try:
        element_source_of_joke = element_btn.getchildren()[2]
        if(element_source_of_joke.get('data-site') != None):
            source_of_joke = unquote(element_source_of_joke.get('data-site'))
    except:
        source_of_joke = ""

    if element_joke[valueOfElement].getchildren() == []:
        jok = element_joke[valueOfElement]
        joks = jok.text
    else:
        childs = element_joke[valueOfElement].getchildren()
        joks = joks + element_joke[valueOfElement].text + '\n'
        for child in childs:
            joks = joks + child.tail + '\n'
    JOKES = [joks, voteP, voteN, votes, source_of_joke]
    return JOKES