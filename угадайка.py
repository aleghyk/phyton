#!/usr/bin/env python

import random

#Человек загадывает число комп отгадывает
count = 1
up = 100
low = 1
des = 0
print ('Загадай число от ноля до 100')
while True :
    print ('Попытка', count)
    number = random.randint(low, up)
    print ('Это ', number, 'Больше 1, меньше 2, угадал 0')
    des = input ()
    if des == '1':
        low = number + 1
    elif des == '2':
        up = number - 1
    elif des == '0':
        break
    else :
        print ('\t\aАблом!!! неправильный ввод')
        continue
    count +=1
print ('Отгадал за ', count, 'попыток')
input ('enter to stop')
