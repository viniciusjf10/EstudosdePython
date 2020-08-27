#Estudo de datas

import datetime
t=datetime.time(4,20,1) #mostra a diferença entre os componentes
print(t)

print('Hour:',t.hour)
print('Minutos:',t.minute)
print('Segundos:',t.second)
print('Microsegundos:',t.microsecond)

#Dates

today = datetime.date.today()
print(today)
print('ctime',today.ctime())
print('tuple',today.timetuple())
print('ordinal',today.toordinal())
print('year:',today.year)

#operaçoes aritimeticas

d1=datetime.date(2015,3,11)
d2=d1.replace(year=2018)
print(d2)

print(d2-d1)

#exercicio

d1=datetime.date(2020,8,27)
d2=datetime.date(1991,1,1)
print(d1-d2)