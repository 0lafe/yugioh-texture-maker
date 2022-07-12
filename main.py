from PIL import Image
from download_cards import *
from os import listdir
from wand import image
import os

xdim = 4096
xwidth = 245
yheight = 342

downloadGoat()

img = Image.new("RGBA", (4096, 4096))
img2 = Image.new("RGBA", (4096, 4096))
img3 = Image.new("RGBA", (4096, 4096))

for index, card in enumerate(listdir('./pics')):
    useful_index = index % 176
    new_card = Image.open(f'./pics/{card}').convert("RGBA")
    new_card = new_card.resize((xwidth, yheight))
    x = int((useful_index % 16) * xwidth)
    y = int(useful_index / 16) * yheight
    if index < 176:
        img.paste(new_card, (x, y), new_card)
    elif index < 352:
        img2.paste(new_card, (x, y), new_card)
    else:
        img3.paste(new_card, (x, y), new_card)

images = [img, img2, img3]

for index, aimage in enumerate(images):
    aimage.save(f'pack{index}.png')
    with image.Image(filename=f'pack{index}.png') as img:
        img.compression = 'dxt5'
        img.save(filename=f'pack{index}.dds')
    os.rename(f'pack{index}.dds', f'pack{index}.texture')
