import os
import shutil


def build():
    os.mkdir('outputs/YuGiOh')
    os.mkdir('outputs/YuGiOh/assets')
    os.mkdir('outputs/YuGiOh/assets/units')
    os.mkdir('outputs/YuGiOh/assets/units/menu')
    os.mkdir('outputs/YuGiOh/assets/units/menu/menu_scene')

    shutil.copyfile('assets/menu_scene/infamy_card_df.texture', 'outputs/YuGiOh/assets/units/menu/menu_scene/infamy_card_df.texture')
    shutil.copyfile('assets/menu_scene/infamy_card.object', 'outputs/YuGiOh/assets/units/menu/menu_scene/infamy_card.object')
    shutil.copyfile('assets/menu_scene/ithea.texture', 'outputs/YuGiOh/assets/units/menu/menu_scene/ithea.texture')

    files = os.listdir('temp')
    del files[0]
    del files[0]
    for file in files:
        split_tup = os.path.splitext(file)
        file_extension = split_tup[1]
        if file_extension == '.texture':
            shutil.copyfile(f'temp/{file}', f'outputs/YuGiOh/assets/units/menu/menu_scene/{file}')

    shutil.copyfile('assets/icon.dds', 'outputs/YuGiOh/icon.dds')
    shutil.copyfile('assets/mod.txt', 'outputs/YuGiOh/mod.txt')
    shutil.copyfile('temp/main.lua', 'outputs/YuGiOh/main.lua')

    shutil.make_archive('outputs/YuGiOh-Infamy-Card', 'zip', 'outputs/YuGiOh')