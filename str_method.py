'''class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
s1=Student('Bhagya',101,95)
s2=Student('MAdhu',102,50)
print(s1)
print(s2)
In the above case,whenever we directly try to print the object,internally __str__ will get called whose default implementation returns the 
string format :
    __main__.Student object at 0x000002377EF46100
In order to get meaningful string representation of the object,we have to override __str__()method in our class'''

class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def __str__(self):
        return 	'Name:{},Roll no:{},Marks:{}'.format(self.name,self.rollno,self.marks)
s1=Student('Bhagya',101,95)
s2=Student('MAdhu',102,50)
print(s1)
print(s2)
    


