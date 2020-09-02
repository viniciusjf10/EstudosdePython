#coleçoes

from collections import Counter

l=[1,2,2,2,3,5,5,4,2,1,6,7]
print(Counter(l))

print(Counter('aaaaaaadddddeufbhewnufjenfuiehnu'))

#defaultdict

from collections import defaultdict

#d={}
#d['one']
d=defaultdict(object)
d['one']
for item in d:
    print(item)

#exercicios 

print(Counter([1,1,1,1,1,1,2,2,2,2,3,4,4,4,3,3]))

#colection2
#modulos para dicionarios

print('Normal dict')
d={}
d['a']='A'
d['b']='B'
d['c']='C'

for k,v in d.items():
    print (k,v)

from collections import OrderedDict
print('OrderedDict')
d=OrderedDict()    
d['a']='A'
d['b']='B'
d['c']='C'

for k,x in d.items():
    print(k,v)
    
#igualdade de um dicionario

print('Dicionaries are equal?')
d1={}
d1['a'] ='A'
d1['b'] ='B'

d2={}
d2['b'] ='B'
d2['a'] ='A'

print(d1==d2)


d1={}
d1['b'] ='A'
d1['a'] ='B'

d2={}
d2['b'] ='B'
d2['a'] ='A'

print(d1==d2)

#namedtuple
from collections import namedtuple

Dog= namedtuple('Dog','age breed name')
sam= Dog(age=2,breed='lab',name='Sammy')
frank=Dog(age=2,breed='Shepard',name='Frank')

print(sam)

#exercicios

from collections import OrderedDict
print('OrderedDict')
d=OrderedDict()    
d['p']='P'
d['y']='Y'
d['t']='T'
d['h']='H'
d['o']='O'
d['n']='N'
for k,x in d.items():
    print(k,v)






