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