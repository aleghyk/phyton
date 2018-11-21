#create lock

import math
import fun
def lock_file():
	f=open('lock','w')
	f.write('')
	f.close()
lock_file()
