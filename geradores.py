#Geradores
#sao funçoes que sao suspensas e retomam a execução no ultimo ponto gerando uma 
#suspensao de estado

def gencuber(n):
    for num in range(n):
        yield num **3
for x in gencuber(10):
    print(x)


def genfibon(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b
for num in genfibon(10):
    print(num)
    
#next() e iter()
#o next acessa o proximo elemneto da sequencia
def simple_gen():
    for x in range(3):
        yield x

g=simple_gen()
print(next(g))
print(next(g))
print(next(g))

#exercicio

def gen_quad(n):
    for num in range(n):
        yield num**2

for x in gen_quad(10):
    print(x)