
#Lists, Tuples, Sets, Dictionaries and Comprehensions
#[fe for e in iter if cond]
##L=[x*x for x in range(4)  if x%2==0]
##print(L)
LL=(x*x for x in range(4)  if x%2==0)
#R=next(LL)
 
Li=['a','b','c','d','a','g','g']
inddict={Li[i]:i for i in range(len(Li))}
print(inddict)

Listfunc1=[]
for i in range(4):
    def func1(e):
        return e+i
    Listfunc1.append(func1)
R=[func1(8) for func1 in Listfunc1 ]
print(R)

Listfunc2=[]
for i in range(4):
    def func2(e, iv=i):
        return e+iv
    Listfunc2.append(func2)
RR=[func1(8) for func1 in Listfunc2 ]
print(RR)
    
