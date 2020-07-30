#Estudo de laços de repetição

l=[1,2,3,4,5,6,7,8]
for num in l:
        print(num)
print('----------------')
for num in l:
    if num % 2 == 0:
        print(num)
print('----------------')
for num in l:
    if num % 2 ==0:
        print(num)
    else:
        print('num impar')
print('----------------')
for letter in 'This is a string':
    print(letter)
print('----------------') 
tup=(1,2,3,4,5)
for t in tup:
    print(t)
print('----------------') 
l=[(2,4),(6,8),(10,12)]
for tup in  l:
    print(tup)
print
print('----------------') 
d = {'k1':1, 'k2':2, 'k3':3}
for k, v in d.items():
    print(k)
    print(v)      
print('----------------') 

#exercicios
l=[1,4,5,67,7,8,6,54,4,3,1,21,1,9,0]
for num in l:
    if num %2 ==0:
        print(num)
print('----------------')         
stri='Hello Python'
for i in stri[6:]:
    print(i)