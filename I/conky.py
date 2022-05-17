
from shutil import copyfile
copyfile('./conky.desktop', '/etc/xdg/autostart/conky.desktop')

with open('/etc/conky/conky.conf', 'r') as paper:

    text = paper.readlines()
    pass

for l, t in enumerate(text):

    if("alignment" in t):

        key, value = t.split("=")
        value = " 'top_right',\n"
        update = key + '=' + value
        text[l] = update
        break

    if("own_window_argb_visual" in t):

        key, value = t.split("=")
        value = " 'true',\n"
        update = key + '=' + value
        text[l] = update
        break

    if("own_window_argb_value" in t):

        key, value = t.split("=")
        value = " '0',\n"
        update = key + '=' + value
        text[l] = update
        break
        
    pass

with open('/etc/conky/conky.conf', 'w') as paper:

    paper.writelines(text)
    pass
