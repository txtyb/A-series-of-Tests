for x in range(6):
    a=True
    if a==True:
        for i in range(50):
            print("*"*(i+1))
        if i==49:
            for j in range(50,1,-1):
                print("*"*(j-1))
        a=False
