#POO
l=[1,2,3]
print(l.count(2))

print(type(1)) #verifica o tipo de dado
print(type({})) #verifica o tipo de dado
print(type([])) #verifica o tipo de dado

#criaçao de classes
class Exemplo(object):
    pass #nao faz nada
x = Exemplo() #instanciando exemplo
print(type(x))

#atributos
class Dog(object):
    def __init__(self,breed): #self é igual ao this e breed é o argumento
        self.breed = breed
sam = Dog(breed='Lab')
frank = Dog(breed='Huskie')
print(sam.breed)
print(frank.breed)

