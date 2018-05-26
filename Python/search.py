import os,time
paths=list()

def search(path,word):
    for filename in os.listdir(path):
        fp=os.path.join(path,filename)
        if os.path.isfile(fp)==True and word==filename:
            paths.append(fp)
        if os.path.isdir(fp)==True:
            search(fp,word)

start=time.clock()            
search('/storage/emulated/0/Android/data/tv.danmaku.bili/download','entry.json')
print(paths)            
end=time.clock()

print('耗时%ss'%(end-start))
#os.rename(os.path.join((os.path.split(perpath1))[0],'lua.flv.bili2api.3','0.blv'),os.path.join((os.path.split(perpath1))[0],'lua.flv.bili2api.3')+'/'+name+'.mp4')