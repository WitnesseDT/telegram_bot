import requests as rq


HEADERS=({
'Host': 'castlots.org',
'Origin': 'http://castlots.org',
'Referer': 'http://castlots.org/generator-komplimentov-devushke/',
'X-Requested-With': 'XMLHttpRequest'
})
url = "http://castlots.org/generator-komplimentov-devushke/generate.php"

def get_for_women_comlinemts():
    comliment_text = rq.get(url, headers=HEADERS)
    comliment = comliment_text.text
    comliment = comliment.split(':')[2].strip('}').strip('"').encode('utf-8').decode("unicode_escape")
    return comliment