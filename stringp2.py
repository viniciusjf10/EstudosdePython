#Strings parte 2
#strings possuem a propriedade de imutabilidade por isso após declaradas nao 
#podem ser alteradas

s="hello world"
print(s)
#s[0]="x"
#o comando acima resulta em um erro que diz str object nao suporta item 
#assignment

#uma alternativa a isso é concatenar strings

s=s+"concatena me!"
print (s)

leter="xx yy xy"
letter=leter*10
print(letter)

print(leter.upper())
print(leter.lower())

print(leter.split()) #separa a string em espaços em branco
print(leter.split('x')) #separa a string usando a letra nos parenteses


