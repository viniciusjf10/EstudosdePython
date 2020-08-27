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

