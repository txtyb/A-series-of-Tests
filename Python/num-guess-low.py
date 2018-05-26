import os
from random import randint

msg2="num:..."
print("Who are you?")
name = input()
print("Oh hello "+name)
print("Let us play a game!\n猜数"+msg2)
num = randint(1,100)
path1 = '/storage/emulated/0/Android/data/tv.danmaku.bili/download'
bingo = False
print(num)

while bingo == False:
    shuru = input("数字是？")
    b = shuru 
    
    if b=="q":
        print("quiting.....")
        exit()
    a = int(shuru)
    
    if a<num:
        print("nonono too small")
    if a>num:
        print("oh its too big")
    if a==num:
        print("bingo!")
        bingo = True

