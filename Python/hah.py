import time
s='sdkjfnnjdshgkjdsbgkiuh独钓会有的也好听滴'
for i in range(len(s)):
     with open('D:\\1\\'+str(i)+'.txt','w') as f:
          f.write(s[i])
a=''
for i in range(len(s)):
     with open('D:\\1\\'+str(i)+'.txt') as f:
          a+=f.read()
print(a)
time.time()%S
