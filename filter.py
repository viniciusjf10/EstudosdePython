#Filter
#ela precisa de dois argumentos sendo o primeiro uma funçao e o segundo a lista
#e assim sera aplicado retornando true ou false

def even_check(num):
    if num %2 == 0:
        return True
lista1=[1,4,9,16,25]
lst=range(0,11)
print(list(filter(even_check,lista1)))
print(list(filter(lambda x:x%2==0,lst)))
