import os
a=os.system('pwd')
print(a)
print(os.system('echo '+str(a)[0]))[0]
