#compreensao de dicionarios
#criaçao rapida porem nao tao usual

p={x:x**2 for x in range(10)}
print(p)
p="Python"
g={p.index(x):x for x in p}
print(g)

#exercicio
v={x:x*x for x in range (0,31)}
print(v)