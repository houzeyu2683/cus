
import os
import xml.etree.ElementTree

dictionary = {
    '桌面':"Desktop", 
    "文件":"Documents", 
    "下載":"Downloads",
    "Music":"Music",
    "Pictures":"Pictures",
    "Videos":"Videos",
}
path = "{}/.local/share/user-places.xbel".format(os.path.expanduser('~'))
tree = xml.etree.ElementTree.parse(path)
root = tree.getroot()
loop = root.findall('bookmark')
for item in loop: 

    title = item.find('title').text
    if(title in dictionary.keys()):

        e = item.attrib['href'].split('/')
        if(e[-1]!=""): 

            e[-1] = dictionary[title] 
            item.attrib['href'] = '/'.join(e) + '/'
            pass

        else:

            e[-2] = dictionary[title]
            item.attrib['href'] = '/'.join(e)
            pass

        continue        
    
    continue

tree.write(path)












#     if(item.find('title').text=='Home'): continue


#     if(item.find('title').text=='桌面'): 
        
#         e = item.attrib['href'].split('/')
#         e[-1] = "Desktop"
#         item.attrib['href'] = '/'.join(e) + '/'
#         continue

#     if(item.find('title').text=='文件'): 
        
#         e = item.attrib['href'].split('/')
#         e[-1] = "Documents"
#         item.attrib['href'] = '/'.join(e)
#         continue

#     if(item.find('title').text=='下載'): 
        
#         e = item.attrib['href'].split('/')
#         e[-2] = "Downloads"
#         item.attrib['href'] = '/'.join(e)
#         continue    

#     if(item.find('title').text=='Music'): 
        
#         e = item.attrib['href'].split('/')
#         e[-2] = "Desktop"
#         item.attrib['href'] = '/'.join(e)
#         continue

#     if(item.find('title').text=='Music'): 
        
#         e = item.attrib['href'].split('/')
#         e[-2] = "Desktop"
#         item.attrib['href'] = '/'.join(e)
#         continue

#     if(item.find('title').text=='Music'): 
        
#         e = item.attrib['href'].split('/')
#         e[-2] = "Desktop"
#         item.attrib['href'] = '/'.join(e)
#         continue

#     if(item.find('title').text=='Music'): 
        
#         e = item.attrib['href'].split('/')
#         e[-2] = "Desktop"
#         item.attrib['href'] = '/'.join(e)
#         continue    

# with open('~/.config/user-places.xbel', 'r') as paper:

#     text = paper.readlines()
#     pass

# context = []
# for _, t in enumerate(text):

#     if(("conky.config" in t) and ("{" in t)):

#         context += [t]
#         context += ["    own_window_argb_visual = true,\n"]
#         context += ["    own_window_argb_value = 0,\n"]
#         continue

#     if("alignment" in t):

#         context += ["    alignment = 'top_right',\n"]
#         continue

#     if("own_window_type" in t):

#         context += ["    own_window_type = 'dock',\n"]
#         continue

#     context += [t]
#     continue

# with open('/etc/conky/conky.conf', 'w') as paper:

#     paper.writelines(context)
#     pass
