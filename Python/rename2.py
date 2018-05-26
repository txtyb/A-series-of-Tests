import os
path1 = '/storage/emulated/0/Android/data/tv.danmaku.bili/download'
os.chdir(path1)
print(os.getcwd())

names = os.listdir(os.getcwd())
print(names)

for pername in names:
    path2 = path1 + '/' + pername
    print(path2)
    if os.path.isdir(path2) == True:
        path2 = path2 + '/1'
        print(path2)
        os.chdir(path2)
        text1 = open('entry.json').read()
        print(text1)
        for part in text1
        if part == '"title":"':
        name =  
