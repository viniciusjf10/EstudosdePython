#Estudo de decoradores
def hello (name="Rodrigo"):
    def greet ():
        return '\t This is inside te greet () function'
    def welcome ():
        return '\t This is inside the welcome() function'
    if name == "Rodrigo":
        return greet()
    else:
        welcome()

print(hello())

