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