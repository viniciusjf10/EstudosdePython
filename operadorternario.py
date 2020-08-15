#operadores ternarior
#se parecem com if e else porem so deve-se usar em situaçoes mais simples

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