#Geradores
#sao funçoes que sao suspensas e retomam a execução no ultimo ponto gerando uma 
#suspensao de estado

def gencuber(n):
    for num in range(n):
        yield num **3
for x in gencuber(10):
    print(x)

