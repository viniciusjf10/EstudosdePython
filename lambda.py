#Estudo de funçoes lambda
#funçoes lambda tem o intuito de criar funçoes anonimas e assim podemos criar
#funçoes ad hoc sem usar o def
#usa-se apenas para terefas simples

def square(num):
    result = num**2
    return result
print(square(2))

def square1(num):
    return num**2
print(square1(2))

def square3(num): return num**2
print(square3(2))

square=lambda num:num**2
print(square(2))


even=lambda x:x%2==0
print(even(3))
print(even(2))

first=lambda s:s[0]
print(first('hello'))

rev= lambda s:s[::-1]
print(rev('casa'))

#exercicios
mult=lambda x,y:x*y
print(mult(2,4))
print(mult(518978,54517))

meio = lambda x: x[round((len(x)/2)+0.1)-1]if len(x)%2==1 else ""
print(meio('php'))
print(meio('Python'))
print(meio('sql'))
