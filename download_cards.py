import json
import requests
from tqdm import tqdm

def downloadWithParams(params):
    api_reply = getRequest(params)
    return pullImage(api_reply)

def getRequest(params):
    x = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php', params)
    reply = json.loads(x.text)
    return reply

def pullImage(reply):
    if 'data' in reply:
        print('Downloading')
        for index, card_index in enumerate(tqdm(range(len(reply['data'])))):
            card = reply['data'][card_index]
            image_url = card['card_images'][0]['image_url']
            img_data = requests.get(image_url).content
            name = card['name'].replace(':', '')
            try:
                with open(f'./pics/{str(index).zfill(5)} - {name}.png', 'wb') as handler:
                    handler.write(img_data)
            except:
                with open(f'./pics/{str(index).zfill(5)} - UNNAMED.png', 'wb') as handler:
                    handler.write(img_data)
        return False
    else:
        print('Server fetch failed! Error:')
        print(reply)
        return True