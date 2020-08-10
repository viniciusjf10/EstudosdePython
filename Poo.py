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

#criando um atributo especial para a classe

class Dog(object):
    species = "mamal"
    def __init__(self,breed,name):
         self.breed=breed
         self.name=name
sam=Dog('Lab','Sam')
print(sam.name)

class Circle (object):
    def __init__(self,radius=1): #O raio padrao para o circulo é 1
        self.radius = radius 
    def area(self):
        return self.radius *self.radius *Circle.pi
    def serRadius(self,radius):
        self.radius=radius
    def getRadius(self):
        return self.radius
    
        