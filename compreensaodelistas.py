# topicos avançados
#compreensao de listas
#permite criar for dentro de listas

lst=[x for x in 'word']
print(lst)

lst=[x**2 for x in range(0,11)]
print(lst)

#criando um exemplo pratico

celsius=[0,10,20.1,34.5]

fahrenheit = [ ((9/5)*temp+32) for temp in celsius]
print (fahrenheit)

#exercicios
#01

lst=[x for x in range(0,31) if x%2==0]
print(lst)



#02
def vogais(s):
    return[i for i in s if i.lower()in ['a','e','i','o','u']]
print(vogais('abcde'))