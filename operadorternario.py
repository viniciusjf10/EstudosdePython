#operadores ternarior
#se parecem com if e else porem so deve-se usar em situaçoes mais simples
import math
idade=21
if idade >=18:
    print('liberado')
else:
    print('bloqueado')
idade=15
print('liberado' if idade>=18 else "bloq")
n=16
r="par" if n%2==0 else "impar"
print(r)

#exercicios

raiz= lambda n: math.sqrt(n) if n>0 else 0
print(raiz(9))
print(raiz(-9))