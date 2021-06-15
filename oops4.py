##Update instance variables
class Test:
    def __init__(self):
        self.a=10
        self.b=20
t1=Test()
t2=Test()
t1.a=999
t1.b=888
print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)
