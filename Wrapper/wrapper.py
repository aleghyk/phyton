import math
import random
import fun
import file_open

choose = input ("\nPlease make your choose! (r-random, s-stopper, d-dict, c-conf, w-while cycle)\n")

if choose == 'r':
    random_1 = random.randint (1,100)
    print(math.sqrt(random_1))

elif choose == 's':
    fun.stopper()

elif choose == 'd':
    pers = ["oleh", "alex", "alex"]
    fun.dict_open("Wrapper.cfg",pers)

elif choose == 'w':
    x = input('\nPlease enter iterations amount\n')
    i = 0

    while i <= int(x):
        i+=5
        print (i)
elif choose == 'c':
    file_open.Config_Open(input('\nPlease enter conf file name\n'))

else:
    print ('\nWrong choose\n')
    quit()


