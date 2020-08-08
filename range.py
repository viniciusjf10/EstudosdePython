#Estudos de range
#range gera numeros dentro de um intervalo

r=range(0,10)
print(r) #nao exibe lista
print(tuple(r))  #exibe lista

r=(range(0,20,2)) #temos um range de 0 a 20 com intervalo de 2 em 2

for i in range(0,10):
    print(i)

    
#Exercicios
for i in range (1,51):
    if i%3==0 and i%5==0:
        print(i, "-FizzBuzz")
    elif i%3==0:
        print(i, "-buzz")
    elif i%5==0:
        print(i, "-Buzz")
        
        
