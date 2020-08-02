#While

#formataçao padrao
#while teste
#   declaração de codigo
#else
#   declaraçao de código

x=0
while x<10:
        print('x is currently: ',x)
        print('x is still less than 10,adding 1 to x')
        x+=1
else:
    print('Well done')

#break, continuos, pass
x=0
while x<10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('x==3')
    else:
        print('continuing')
        continue

#Exercicios

x=0
while x<=4:
    print('*'*x)
    x+=1
while x>0:
    print('*'*x)
    x-=1
    
        
