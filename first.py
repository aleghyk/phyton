#!/usr/bin/env python
#Тестовая Программа

#Утилиты строк
print ('\tmain programm')
print ('\tStart ' * 3)
# zamena
string = 'Уругвай Парагвай Эквадор australia'
print (string.replace('Парагвай', 'Зымбабва'))

#упражнения с переменными
br = 0
ad = 12
#int (ad)
out = 1
while out == 1:
	
	ad = input ('\n\n\tTemperatura v adu')
	ad = int (ad)

	#random
	import random
	az = random.gauss (random.randint (1, 100), random.randint (1, 10)) * 1000000
	#print (az)
	#az = int (az)
	print ('\n\t', az, '\n\t', int (az))

	#matematika
	ad *= 2
#прерывание цыкла по счетчику
#--------------------------------
	br += 1
	if br == 5 and ray >= 100:
		print ('\nВсе Аблом счетчик равен ', br, 'сваливаим')
		break
#--------------------------------

	ray = int (input ("temperatura v rayu"))
	print ('temperatura v adu', ad, 'temperatura v rayu', ray)
	# вывод
	print ('Иниц'+'иалызация', '....', end=' ')
	print ('Done')
	# зумер
	print ('\a')

	# Условия
	if ad < ray:
		print ('\n\tТы шо дурак?')
		print ('\tтемпература в аду не может быть ниже', '!' * 3, end= ' ')
		print ('Эта же ад', '!!!')
	elif ad > ray:
		print ('\n\tай маладетс!!!')
		print ('\tУгадал!!!')
		out = 2
	elif ad == ray:
		print ('\n\tХм!? Так в чем же разница?')
		print ('\tНепонимаю')
	else:
		print ('Ого!! сбой')

 

input ('\n\nНажмите Enter чтобы кончить')
