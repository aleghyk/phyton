class A:
    pass
a1 = A()
a2 = A()
a1.x = 42
class A:
    def f(self, x):
        print (self)
        self.x = x
a = A()
print (a)
print (a.f(42))
class A:
    def f(self):
        print ("A")
class B:
    def f(self):
        print ("B")
a = A()
a.f()
a.__class__ = B
a.f()

class D:
    def f(self):
        self._internal_dwell_tune_var = 0
        self.__secret = 0
        print ("D")

class C(D):
    pass
c = C()
c.f()
