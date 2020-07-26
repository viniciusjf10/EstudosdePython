#Estudos sobre dicionarios

my_dict={'key1':'value1','key2':'value2'}
print(my_dict['key2'])
#Dicionarios podem receber todo tipo de dados 
my_dict2={'key1':'1223','key2':'casa','key3':['item0','item1','item3']}
print(my_dict2['key3'][0])

#tambem é possivel usar metodos de formataçao
print(my_dict2['key3'][0].upper())

#metodos para dicionario

d={'key1':1,'key2':2,'key3':3}
print(d.keys())
print(d.values())
print(d.items())

#Exericios

c={'Simplekey':'hello'}
print(c.values())
c={'k1':{'k2':'hello'}}
print(c['k1']['k2'])



