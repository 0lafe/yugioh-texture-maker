from PIL import Image
from download_chooser import *
from download_cards import downloadWithParams
from create_lua_file import create_lua_file
from build import build
from wand import image
import os
import shutil
from tqdm import tqdm

def clear_temp():
    shutil.rmtree('outputs/YuGiOh')

    for file in os.listdir('temp'):
        if file != '.keep':
            os.remove(f'temp/{file}')

def main():
    xdim = 4096
    ydim = 4096
    xwidth = 245
    yheight = 342

    download_params = choose_download()
    if downloadWithParams(download_params):
        return

    images = []

    files = list(os.listdir('./pics'))
    del files[0]
    files_length = len(files)
    total_images = int(files_length/176) + 1

    print('Making pngs: ')
    for index, card_index in enumerate(tqdm(range(len(files)))):
        card = files[card_index]
        current_image_index = index % 176
        if (current_image_index == 0):
            images.append(Image.new("RGBA", (xdim, ydim)))
        new_card = Image.open(f'./pics/{card}').convert("RGBA")
        new_card = new_card.resize((xwidth, yheight))
        x = int((current_image_index % 16) * xwidth)
        y = int(current_image_index / 16) * yheight
        img_index = int(index/176)
        images[img_index].paste(new_card, (x, y), new_card)

    print('Making textures: ')
    for index, image_index in enumerate(tqdm(range(len(images)))):
        aimage = images[image_index]
        aimage.save(f'temp/pack{index}.png')
        with image.Image(filename=f'temp/pack{index}.png') as img:
            img.compression = 'dxt5'
            img.save(filename=f'temp/pack{index}.dds')
        os.rename(f'temp/pack{index}.dds', f'temp/pack{index}.texture')

    create_lua_file(files_length, total_images)
    build()
    clear_temp()

main()