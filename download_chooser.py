import sys
from download_cards import downloadWithParams

def choose_download():
    params = {}
    args = sys.argv
    del args[0]
    for item in sys.argv:
        if '=' in item:
            pair = item.split('=')
            params[pair[0]] = pair[1]
        else:
            params[item] = True
    return params
