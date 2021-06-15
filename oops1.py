class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30
t1=Test() ##Adds a and b to the instance object
t1.m1() ##Adds c to the instance object
t1.d=40 ##Adds d to the instance object
print(t1.__dict__)
