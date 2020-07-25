#Estudo de strings
#strings sao escritas usando aspas simples ou aspas duplas

'hello'
"hello"
'isso tambem é uma string'

#imprimindo uma string

print("hello world 1")
print("use \n para inserir uma nova linha")

#verificando o comprimento de uma string
c=len("hello world")
print(c)

#tambem é possivel indexar strings pela posiçao
d="vinicius"
print(d[0])
print(d[1])

#para printar a partir de uma posiçao usamos:
print(d[1:]) #sera exibido inicius

print(d[:3]) #sera exibido vin

print(d[:-1]) #imprime tudo exceto a ultima letra

print (d[::1]) #pega tudo em espaço de 1 em 1
print(d[::2])#pega tudo em espaço de 2 em 2
print(d[::-1])#pega tudo em espaço de 1 em 1 mas de tras pra frente

#EXERCICIOS
#01
print(d[-1:0])
#02
p="Hello Python"
print(p[6:])
#03
z=len(p)
print(z)
