theList = ["a","b","c"]
print (theList)
joinedString = ",".join(theList)
targetList = joinedString
print(targetList)
targetList = filter(lambda x: len(x)>0, targetList)

print (targetList)