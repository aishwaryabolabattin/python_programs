class Parent:
    def show(self):
        print("This is parent class")
class Child(Parent):
    def display(self):
        print("This is child class")
c=Child()
c.show()
c.display()

class Student:
    def show(self):
        print("This is student class")
class Teacher(Student):
    def display(self):
        print("This is teacher class")
t=Teacher()
t.show()
t.display()

#Write a python program to demonstrate single inheritance using a Person class and an Employee class .
#The Employee class should inherit from person and display name and salary.
class Person:
    def display(self):
        print("Name:Sonali")
class Employee(Person):
    def show(self):
        print("Salary:80000")
e=Employee()
e.show()
e.display()

#Write a python program using a Vehicle class and Car class.
#The Car class should inherit from Vehicle and display the vehicle name and speed.
class Vehicle:
    def show(self):
        print("Vehicle Name:Maruti")
class Car(Vehicle):
    def display(self):
        print("Speed:120km/h")
c=Car()
c.show()
c.display()

#Write a python program to demonstrate single inheritance using a Animal class and an Dog class .
#The Dog class should inherit from Animal and display eating and barking behaviour.
class Animal:
    def eat(self):
        print("Eating behaviour")
class Dog(Animal):
    def bark(self):
        print("Barking Behaviour")
d=Dog()
d.eat()
d.bark()

#Write a python program using a Student class and Result class 
#The Result class should inherit from Student and display the student name and total marks.
class Student:
    def show(self):
        print("Student Name:Sonali")
class Result(Student):
    def display(self):
        print("Total Marks:450")
r=Result()
r.show()
r.display()

#Write a python program using a Shape class and Rectangle class.
#The Rectangle class should inherit from Shape and display the length and breadth.
class Shape:
    def show(self):
        print("Shape:Rectangle")
class Rectangle(Shape):
    def display(self):
        print("Length:5")
        print("Breadth:4")
r=Rectangle()
r.show()
r.display()

#Write a python program using a Bank class and Account class.
#The Account class should inherit from Bank and display bank name and balance.
class Bank:
    def show(self):
        print("Bank name:Bank Of India")
class Account(Bank):
    def display(self):
        print("Balance:80000")
a=Account()
a.show()
a.display()


