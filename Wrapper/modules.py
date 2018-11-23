def list_test():
    theList = ["a","b","c"]
    print (theList)
    joinedString = ",".join(theList)
    targetList = joinedString
    print(targetList)
    targetList = filter(lambda x: len(x)>0, targetList)
    print (targetList)

def list_modif ():
    list1 = ['asd', 2, '1', 'country']
    list2 = [2,5,6,9]
    print (str(list1) + "   &    " + str(list2))
    list1.append(list2 [2])
    list2.insert( int(list1[2]), str(list2[3]))
    print (str (list1) + '    &    ' + str (list2) )

list_modif()