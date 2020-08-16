#Zip
#cria um iterador que agrega elementos 
#retorna um iterador de tuplas que contem o n elemento de cada uma das sequencias

x=[1,2,3]
y=[4,5,6]
print(list(zip(x,y)))

#nao se aconselha iterar listas de tamanhos diferentes

x=[1,2,3,4,5]
y=[1,2]
print(list(zip(x,y)))

#exercicios]

print(list(zip(range(10),[i**2 for i in range(10)])))

l1=list(range(1,11))
l2=list(range(10,0,-1))
for i1,i2 in zip (l1,l2):
    print(i1/i2)