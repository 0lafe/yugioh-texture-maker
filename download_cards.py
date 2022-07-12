import json
import requests
import random


def download():
    failures = []
    f = open('cards.json')
    data = json.load(f)
    for index, cardName in enumerate(data['cards']):
        params = {'name': cardName}
        x = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php', params)
        reply = json.loads(x.text)
        if 'data' in reply:
            image_url = reply['data'][0]['card_images'][0]['image_url']
            img_data = requests.get(image_url).content
            with open(f'./pics/{str(index).zfill(4)} - {cardName}.png', 'wb') as handler:
                handler.write(img_data)
        else:
            failures.append(cardName)
    if len(failures) > 0:
        print('~~~ These Cards Failed To Download: ~~~')
        for cardName in failures:
            print(cardName)

def downloadGoat():
    x = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php?format=goat&sort=id')
    reply = json.loads(x.text)
    if 'data' in reply:
        for index, card in enumerate(reply['data'][0:500]):
            image_url = card['card_images'][0]['image_url']
            img_data = requests.get(image_url).content
            name = card['name']
            with open(f'./pics/{str(index).zfill(4)} - {name}.png', 'wb') as handler:
                handler.write(img_data)

def downloadGoatRandom():
    x = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php?format=goat&sort=id')
    reply = json.loads(x.text)
    if 'data' in reply:
        for index, card in enumerate(random.shuffle(reply['data'])[0:500]):
            image_url = card['card_images'][0]['image_url']
            img_data = requests.get(image_url).content
            name = card['name']
            with open(f'./pics/{str(index).zfill(4)} - {name}.png', 'wb') as handler:
                handler.write(img_data)