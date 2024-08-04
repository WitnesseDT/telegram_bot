from bs4 import BeautifulSoup
from lxml import etree
import requests as rq
import random
from urllib.parse import unquote
from datetime import date, timedelta

xpaths = "//div[@class=\"topicbox\"]/div[@class=\"text\"]"
vote_xpath = "//div[@class=\"topicbox\"]/div[@class=\"votingbox\"]/div[@class=\"rates\"]"
url = 'https://www.anekdot.ru/release/anekdot/day/{0}/'.format(date.today() - timedelta(days = 1))


def get_jokesi():
    req = rq.get(url)
    bs = BeautifulSoup(req.text, "html.parser")
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
            print(f"dd {source_of_joke}")
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
    # joks = joks + "\n" + "   👆   " + voteP + "   👇   " + voteN + "   🫵   " + votes
    JOKES = [joks, voteP, voteN, votes, source_of_joke]
    return JOKES



 ###    /html/body/div[2]/div[4]/div[1]/div/div[3]/div[2]/span[2]
 ###    /html/body/div[2]/div[4]/div[1]/div/div
 ###    /html/body/div[2]/div[4]/div[1]/div[2]/div[3]/div[2]/span[2]/\

 ### "//*[@class=\"text\"]" "//*[@class=\"text\"]" //div[@class=\"text\"]

 # /html/body/div[2]/div[4]/div[1]/div[2]/div[1]