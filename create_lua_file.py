
def create_lua_file(quantity, files):
    with open('assets/main.lua', 'r') as file:
        data = file.readlines()

    data[17] = f"    local max_cards = {quantity}"
    imports = ''
    for i in range(files):
        imports += f"BLTAssetManager:CreateEntry(\"units/menu/menu_scene/pack{i}\", \"texture\", ModPath..\"assets/units/menu/menu_scene/pack{i}.texture\", nil)\n"
    data[2] = imports

    with open('temp/main.lua', 'w') as file:
        file.writelines( data )
