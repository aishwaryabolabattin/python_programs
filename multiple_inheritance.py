class Parent:
    def show(self):
        print("this is parent class")
class Mother:
    def display(self):
        print("This is mother class")
class Child(Parent,Mother):
    def show1(self):
        print("This is child class")
c=Child()
c.show()
c.display()
c.show1()

class Parent:
    def show(self):
        print("this is parent class")
class Mother:
    def display(self):
        print("This is mother class")
class Child(Parent,Mother):
    def show1(self):
        print("This is child class")
class Child2(Child):
    def show2(self):
        print("This is child2 class")
c=Child()
c.show()
c.display()
c.show1()

c=Child2()
c.show()
c.display()
c.show2()

#Write a python program using a Techer class and Writer class The Person class inherit from both and diaplay teaching and writing skills.
class Teacher:
    def show(self):
        print("Teaching skills")
class Writer:
    def display(self):
        print("Writing skills")
class Person(Teacher,Writer):
    def show1(self):
        print("This is person class")
p=Person()
p.show()
p.display()
p.show1()

#Write a python program to demonstrate multiple inheritance using Sports class and Academic class The Student should inherit both and siplay sports and academic performance.
class Sports:
    def show(self):
        print("This is Sports class")
class Academic():
    def display(self):
        print("This is Academic class")
class Student(Sports,Academic):
    def show1(self):
        print("Both class")
s=Student()
s.show()
s.display()
s.show1()

#Write a python program using a Camera class and Phone class The SmartPhone class should inherit both and display camera and calling feature.
class Camera:
    def show(self):
        print("This is camera class")
class Phone:
    def display(self):
        print("This is phone class")
class SmartPhone(Camera,Phone):
     def show1(self):
         print("Both class")
s=SmartPhone()
s.show()
s.display()
s.show1()
   