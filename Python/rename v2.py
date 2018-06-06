import os,time,shutil
start=time.clock()
path1 = '/storage/emulated/0/Android/data/tv.danmaku.bili/download'
sum1 = 0
paths=list()

def search(path,word):
    for filename in os.listdir(path):
        fp=os.path.join(path,filename)
        if os.path.isfile(fp)==True and word==filename:
            paths.append(fp)
        if os.path.isdir(fp)==True:
            search(fp,word)

search(path1,'entry.json')
#print(paths)
for perpath1 in paths:
    with open(perpath1) as f:
        #print(f)
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
            print('读取到的名字'+'：'+name)
            a=os.path.join((os.path.split(perpath1))[0],'lua.flv.bili2api.3')
            #print(os.path.join((os.path.split(perpath1))[0],'lua.flv.bili2api.3'))
            os.rename(os.path.join(a,'0.blv'),os.path.join(a,name+'.mp4'))
            #paths=list()
            #search(path1,'0.blv')
            #for perpath2 in paths:
                #os.rename(perpath2)
            sum1+= 1
            print(name+'重命名成功')
            shutil.copyfile(os.path.join(a,name+'.mp4'),os.path.join('/storage/emulated/0/Download',name+'.mp4'))
            print(name+'已复制')

shutil.rmtree('/storage/emulated/0/Android/data/tv.danmaku.bili/download')
print('已删除')
end=time.clock()
print('总共处理了%s个文件\n程序耗时%.4s秒'%(sum1,end-start))
