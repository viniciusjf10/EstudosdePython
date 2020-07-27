#Estudo sobre tuplas
#tuplas sao parecidas com listas porem as tuplas são imutaveis
#tuplas sao criadas usando parenteses e separadas por ,

t=(1,2,3)
print(len(t))
t=('one',2)
print(t)
print(t.count('one')) #mostra quantas vezes one aparece na tupla
print(t.index('one')) #mostra o indice que a palavra esta

#exercicios
l=[1,2,6,9,8,1]
print(l)
print(tuple(l))
