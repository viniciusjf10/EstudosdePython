#function
#fazer funcões é util quando um trecho de código se repete varias vezes 
def name_of_function (arg1,arg2):
    '''
    #documentaçao da funçao

    Parameters
    ----------
    arg1 : TYPE
        DESCRIPTION.
    arg2 : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    #faça a implementaçao aqui pra baixo
    
    return #coloque aqui o retorno da função

def say_hello():
    print("Hello")
    
say_hello()

def greeting(name):
    print('hello, %s' %name)
greeting('Vinicius')

#usando return

def add_num(num1,num2):
    return num1+num2
print(add_num(1,5))

def is_primo(num):
    for n in range (2,num):
        if num %2 ==0:
            print("nao é primo")
            break
        else:
            print('é primo')
            
is_primo(18)

import math
def is_prime(num):
    if num %2 ==0 and num >2:
        return False
    for i in range (3,int(math.sqrt(num))):
        if num %i==0:
            return False
    return True

print(is_prime(11))
    

#exercicios
#01
def remove_inicio(email):
    tam=len(email)
    print(tam)
    for n 
remove_inicio('viniciusouzajf@gmail.com')