##Delete instance variables
class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
    def m1(self):
        del self.c
t1=Test()
t1.m1()
print(t1.__dict__)
t2=Test()
t2.m1()
del t2.b,t2.d
print(t2.__dict__)
