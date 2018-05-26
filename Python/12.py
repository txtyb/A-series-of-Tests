def fibo():
     a=1
     b=1
     for i in range(10):
          a,b=b,a+b
          yield a
     return
print(1)
b=fibo()

for i in range(11):
     print(next(b))
'''for j in fibo():
     
     print(j)'''
