#Estudo de listas

my_list = [1,2,3]
minhalista = ['string',50, 28.72, 'string']
x=len(minhalista)
print(x)

#concatenaçao de listas nao altera seu interior
print(my_list+['new item'])

#redefinindo oq ha em uma lista adiciona um termo

my_list= my_list+['adicionando um item permanentemente']
print(my_list)


#exercicio
lst=[1,2,[3,4],[5,[100,200,['ola']],23,11],1,7]
print(lst[3][1][2][0])

#listas parte2

l=[1,2,3]
l.append('adicione-me ao final')
print(l)
l.pop(0) #remove o item da posiçao 0
print(l)

#alternando listas e deixando elas em ordem alfabetica
nova_lista=['a','b','c','d','e','x']
nova_lista.reverse()
print(nova_lista)
nova_lista.sort()
print(nova_lista)


#lista aninhadas
list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9]

matrix=[list1,list2,list3]
print(matrix)
print(matrix[0])
print(matrix[0][0])

#Exercicios

vi=[5,4,3,6,1]
vi.sort()
print(vi)

