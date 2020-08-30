#Numeros avançados
#convertendo em hex
print(hex(255))
#converte em binario
print(bin(255))
#elevando um numero ao outro
print(pow(2,4))
#mostrar absoluto
print(abs(-1))
#reduzir a precisao do numero
print(round(3.14159266,2))

#exercicios
lst= range(1,33)
print(lst)
for i in range (0,33):
    print(bin(i))
    
def rgb_to_hex(tup):
    if type(tup) != tuple or any([not (i>=0 and i <256)for i in tup]) or len(tup) !=3:
        raise Exception('Argument invalid')
    hex_code="#"
    for i in tup:
        hex_code += hex(round(i))[2:].zfill(2).upper()
    return hex_code

print(rgb_to_hex((255,255,255)))
print(rgb_to_hex((69,140,15)))