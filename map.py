#estudo de map
#map faz com que se aplica a funçao a todos elementos da sequencia e e retorna
#uma lista com os elementos alterados

def fah(t):
    return (9/5)*t+32
def cel(t):
    return (5/9)*t-32

temp=[0,22.5,40,10]
F_temps=list(map(fah,temp))
print(F_temps)

a=[1,2,3,4]
b=[5,6,7,8]
c=[9,10,11,12]
print(list(map(lambda x,y:x+y,a,b)))
