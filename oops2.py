###ACCESS DELETE UPDATE INSTANCE VARIABLES
class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def display(self):
        print(self.a)
        print(self.b)
t=Test()
t.display()
##print(t.a)
##print(t.b)
