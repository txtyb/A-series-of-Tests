class student:
     sco=[]
     @property
     def score(self,score):
         return self.score
     @score.setter
     def score(self,score):
          try:
               if 0<=int(score)<=100:
                    self.sco.append(int(score))
               else:
                    print('error')
          except ValueError:
               print('v-error')
          return 

a=student()
'''a.score=1000
a.score=100
a.score=-10'''
c=True
while c:
     b=input()
     if b=='quit' or b=='':
          c=False
     else:
          a.score=b
          print(a.sco)
     
