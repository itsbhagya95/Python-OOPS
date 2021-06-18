class Test:
    e=50
    def __init__(self):
        Test.a=10
    def m1(self):
        Test.b=20
    @classmethod
    def m2(cls):
        cls.c=30
        Test.d=40
    @staticmethod
    def m3():
        Test.f=60
t=Test()
t.m1()
Test.m2()
Test.m3()
print(Test.__dict__)

