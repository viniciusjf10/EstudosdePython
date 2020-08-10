#POO
'''
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
    def setRadius(self,radius):
        self.radius=radius
    def getRadius(self):
        return self.radius
    
c=Circle()
c.setRadius(2)
print('O raio é: ',c.getRadius())


#herança
#forma de formar novas classes usando outras ja criadas
#reutilizaçao de codigos, reduçao de complexidade

class Animal (object):
    def __init__(self):
        print("Animal Created")
    def whoAmI(self):
        print('Animal')
    def eat (self):
        print('Eating')
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    def bark(self):
        print("Woof")

d=Dog()
print(d.whoAmI())
 '''   
#exercicios
#01

class Cubos(object):
    def __init__(self,breed):
        self.breed=breed
    def volume(self):
        return self.breed**2
    def area(self):
        return (self.breed**2)*6
c=Cubos(4)
print("Area: ",c.area())
print("Volume: ",c.volume())
    
    






        