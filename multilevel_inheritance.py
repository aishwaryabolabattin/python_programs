class Parent:
    def show(self):
        print("this is parent class")
class Mother(Parent):
    def display(self):
        print("This is mother class")
class Child(Mother):
    def show1(self):
        print("This is child class")

c=Child()
c.display()
c.show()
c.show1()

#Create a class Grandparent with a method show_gp() to display "I am Grandparent" Create class Parent that inherits from Grandparent and has a method show_p() to display
#"I am Parent" Create class Child that inherits fro Parent and has method show_c() to display "I am Child" Create an object of the child class and call all three methods.
class Grandparent:
    def show_gp(self):
        print("I am Grandparent")
class Parent(Grandparent):
    def show_p(self):
        print("I am parent")
class Child(Parent):
    def show_c(self):
        print("I am Child")
c=Child()
c.show_gp()
c.show_p()
c.show_c()

#Create a class School with a method show_School() to display "This is a School", Create a class Teacher thet inherits from School and has a method show_teacher() to
#display "  This is a Teacher", Create a class Student that inherits from Teacher and has a method show_student() to display "This is a Student" Create an object of the Student class and call all three methods.
class School:
    def show_school(self):
        print("This is a SChool")
class Teacher(School):
    def show_teacher(self):
        print("This is a Teacher")
class Student(Teacher):
    def show_student(self):
        print("This is a student")
s=Student()
s.show_school()
s.show_teacher()
s.show_student()

#Create a class Vehicle with a method show_vehicle() to display "This is a Vehicle", Create a class Car that inherits from Vehicle and has a method show_car() to display "This is a Car", Create a class SportsCar that inherits from Car and has a method show_sportscar() to display "This is a Sports Car" Create an object of the SportsCar class and call all three methods.
class Vehicle:
    def show_vehicle(self):
        print("This is a vehicle")
class Car(Vehicle):
    def show_car(self):
        print("This is a car")
class SportsCar(Car):
    def show_sportscar(self):
        print("This is a SPortsCar")
s=SportsCar()
s.show_vehicle()
s.show_car()
s.show_sportscar()


    
