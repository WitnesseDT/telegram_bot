import requests as rq
import config

URL_GET_ID = "https://api.imgflip.com/get_memes"
URL_SET = "https://api.imgflip.com/caption_image"
template_id = 14859329
data = {
    'template_id' : '',
    'username' : config.USERNAME,
    'password' : config.PASSWD,
    'text0' : '',
    'text1' : '',
}

memes_urls = []
memes_name = []
memes_ids = []
def get_meme_pic():
    res = rq.get(URL_GET_ID)   
    memes_json = res.json()
    for mem in memes_json['data']['memes']:
        memes_urls.append(mem['url'])
        memes_name.append(mem['name'])
        memes_ids.append(mem['id'])
    return memes_urls, memes_name, memes_ids

