import os

for file in os.listdir('pics'):
    if file != '.keep':
        os.remove(f'pics/{file}')

for file in os.listdir('outputs'):
    if file != '.keep':
        os.remove(f'outputs/{file}')