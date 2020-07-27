#sets ou conjuntos sao usados quando desejamos nao repetiçao em um conjunto de
#dados.

x=set()
x.add(1)
print(x)
x.add(2)
print(x)
x.add(1)
print(x) #ele nao adiciona outro 1 por nao possuir elementos repetitos
l=[1,1,2,2,3,4,5,6,1,1]
set(l)
print(l)#remove repetiçoes


#Exercicios

l2=[1,2,2,33,4,4,11,22,3]
set(l2)
print(set(l2))

