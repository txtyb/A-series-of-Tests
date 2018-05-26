import time
start=time.clock()
sum1=0

for i in range(1,9999999):
    sum1=sum1+i
print(sum1)
end=time.clock()
#print(('%s'%(end-start))[0:4])
#second=%s%(end-start)
print('程序耗时'+('%s'%(end-start))[0:4]+'秒')
