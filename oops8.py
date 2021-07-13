class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print('Hi',self.name)
        print('Your marks are',self.marks)
    def grades(self):
        if self.marks>=60:
            print('Grade "A"')
        elif self.marks>=50:
            print('Grade "B"')
        elif self.marks>=35:
            print('Grade "C"')
        else:
            print('Failed')

n=int(input('Enter no of students '))
for i in range(n):
    name=input('Enter name of student')
    marks=int(input('Enter marks of student'))
    s=Student(name,marks)
    s.display()
    s.grades()
    print()
