#1
class A:
    def a(self):
        print("This is class A")
class B(A):
    def b(self):
        print("This is class B")
class C(A):
    def c(self):
        print("This is class C")
class D(B,C):
    def d(self):
        print("This is class D")
d=D()
d.a()
d.b()
d.c()
d.d()


#2 
class Parent:
    def show(self):
        print("This is parent class")
class Child1(Parent):
    def display1(self):
        print("This is child1 class")
class Child2(Parent):
    def display2(self):
        print("This is child2 class")
class Child3(Child1,Child2):
    def display3(self):
        print("This is child3 class")
c=Child3()
c.show()
c.display1()
c.display2()
c.display3()


