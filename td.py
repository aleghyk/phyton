print("to do programm \n")
td = {}
tasks = ()
if "y" == input( "please type \"y\" if you want to continue"):
        while True:
                q1 = input ('you can add (a) show (s) task or quit (q)')
                
                if "a" == q1:
                        data = input ("please enter data")
                        task = input ('please enter task for current date')
                        tasks = tasks, task
                        td [data] = tasks
                elif "s" == q1:
                        d=input("please input date for show")
                        print(td[d])
                elif "q" ==q1:
                        break
                else:
                        print ("wrong input")
