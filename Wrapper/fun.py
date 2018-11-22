"""
lib modules

assertion = your own exception assertion example:

def some_func (some_var):
    assert some_var !=''
    some_other_func()
    some_other_var = "some_string" """


def starter (p):
    if p == '':
        print ("incorect function call /n")
        return 1
    print (str(p) + "test")
    return input("some text")
def stopper ():
    print ("stop this")

def dict_open(file, person):
    if not file or not person:
        print("somethig went wrong")
    elif not person[2]:
        print("something wrong with a person")
    else:
        print("ok")
    dict_file = open(file)
    print(dict_file.read())

