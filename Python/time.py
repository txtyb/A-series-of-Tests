import time

start=time.clock()
sum1=0
for i in range(1,99999999):
    sum1=sum1+i

print(sum1)
end=time.clock()
print("程序耗时%s秒"%(end-start))