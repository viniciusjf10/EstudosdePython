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