import pickle
import os

def add_task():
    date = input('Date?')
    task = input('Task?')
    if date not in tasks:
        tasks[date] = [task]
    else:
        tasks[date].append(task)
    with open("td.pickle", "wb") as f:
        pickle.dump(tasks,f)

def load_task():
    date = input('Date?')
    if date in tasks:
        for number, task in enumerate(tasks[date], 1):
            print("{}. {}".format(number, task))
    

try:
    with open("td.pickle", "rb") as f:
        tasks = pickle.load(f)
except FileNotFoundError:
    tasks = {}

while True:
    action = input("""Action: 
a - add
l - list
q - quit
?""").lower()
    if action == 'q':
        break
    elif action == 'a':
        t1 = add_task()
    elif action == 'l':
        t2 = load_task()
    else:
        print("There are no tasks on this date")
