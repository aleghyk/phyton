import pickle
obj1 = {"asd": {1, 2, 3}, 123: "223", 2: 122}
s = pickle.dumps(obj1)
obj2 = pickle.loads(s)
print (obj1,"/n",obj2)
with open ("obj.pickle", "wb") as f:
    pickle.dump(obj1, f)
    obj3 = pickle.load (f)
    print obj3

