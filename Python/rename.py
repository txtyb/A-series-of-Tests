import os
start=time.clock()
path1 = '/storage/emulated/0/Android/data/tv.danmaku.bili/download'
os.chdir(path1)
#print(os.getcwd())
sum1 = 0

names = os.listdir(os.getcwd())
#print(names)

for pername in names:
    path2 = path1 + '/' + pername
    #print(path2)
    if os.path.isdir(path2) == True:
        path2 = path2 + '/1'
        #print(path2)
        os.chdir(path2)
        with open('entry.json') as f:
            text1=f.readlines()
        #text1 = open('entry.json').readlines()
        #print(text1)
        #print(text1.find('6'))
        for part in text1:
            tar='title\":\"'
            s=part.find(tar)
            #print(part,s)
            if s !=-1:
                name = part[s+len(tar):part.find('\"',s+len(tar))]
                os.rename(path2+'/lua.flv.bili2api.3/0.blv',path2+"/lua.flv.bili2api.3/"+name+'.mp4')
                sum1+= 1
                print(name)
                
end=time.clock()
print('总共处理了'+str(sum1)+'个文件'+'程序耗时'+('%s'%(end-start))[0:6]+'秒')
