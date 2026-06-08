#1
class Child:
    def show1(self):
        print("This is child class")
class Parent(Child):
    def show(self):
        print("This is Parent class")
class Mother(Child):
    def display(self):
        print("This is Mother class")

p=Parent()
p.show()
p.show1()

m=Mother()
m.display()
m.show1()

#2
class Student:
    def show(self):
        print("This is Student class")
class Science(Student):
    def display(self):
        print("This is Science class")
class Arts(Student):
    def show1(self):
        print("This is Arts class")
s=Science()
s.show()
s.display()

a=Arts()
a.show()
a.show1()

