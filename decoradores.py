#Estudo de decoradores
def hello (name="Rodrigo"):
    def greet ():
        return '\t This is inside te greet () function'
    def welcome ():
        return '\t This is inside the welcome() function'
    if name == "Rodrigo":
        return greet
    else:
        welcome

print(hello())


def hello ():
    return "Hi Jose!"
def other (func):
    print('Other code would go here')
    print(func())
    
print(other(hello))

def new_decorator(func):
    def wrap_func():
        print("Code would be here, before executing the func")
        func()
        print("Code her will execute after the func()")
    return wrap_func

def func_needs_decorator():
    print('This function is in need of a Decorator')
    
print(func_needs_decorator())