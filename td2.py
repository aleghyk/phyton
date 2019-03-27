import pickle

def load():
    try:
        with open("todo.pickle", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

def save():
    with open("todo.pickle", "wb") as f:
        pickle.dump(tasks, f)

def add_task():
    date = input('Date?')
    task = input('Task?')
    if date not in tasks:
        tasks[date] = [task]
    else:
        tasks[date].append(task)
    save()

def list_tasks():
    date = input('Date?')
    if date in tasks:
        for number, task in enumerate(tasks[date], 1):
            print("{}. {}".format(number, task))
    else:
        print("There are no tasks on this date")

tasks = load()


while True:
    action = input("""Action: 
a - add
l - list
q - quit
?""").lower()
    if action == 'q':
        break
    elif action == 'a':
        add_task()
    elif action == 'l':
        list_tasks()
    else:
        print("Incorrect action")
