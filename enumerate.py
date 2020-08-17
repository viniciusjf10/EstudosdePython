#Enumerate
#permite enumar elementos de uma lista em uma tupla
lst=['a','b','c','d']

for number,item in enumerate(lst):
    print(number,item)
    
#é muito util para rastrear um elemento especifico

for count,item in enumerate(lst):
    if count >=2:
        break
    else:
        print(item)
        
#exercicio        

