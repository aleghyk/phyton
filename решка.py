#!/usr/bin/env python
#Орел решка

while True:
    print ('\tПрограмма Орел-решка. \nправила просты, подбрасывается Монета указанное количество раз')
    print ('ы потом показываетс количество решек и орлов')
    import random

    print ('\nlets start\n')
    orel = 0
    resh = 0
    count = 0
    rand = 0

    count = int(input ('Enter count'))
    while count:
        count -= 1
        rand = random.randint (1,2)
        if rand == 1:
            orel +=1
            input ('Решка')
        else:
            resh +=1
            input ('Орел')

    print ('Итого решка', resh, 'раз орел', orel, 'раз')
    y = input ('Еще? Y,N')
    if y == 'N':
        break
input ('Нажмите любую клавишу')
    
