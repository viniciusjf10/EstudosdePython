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