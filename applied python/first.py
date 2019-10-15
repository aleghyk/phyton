import random
secret = random.randint(1, 10)
attempts = 0
while attempts < 5:
    attempts +=1
    try:
        guess = int(input ("?"))
    except ValueError:
        print ("incorect")
        continue
    if secret == guess:
        print ("OK")
        break
    if secret > guess:
        print (">")
    else:
        print ("<")
else:
    print ("you are loozer")