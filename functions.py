#Functions examples
#1). simple function
def simple():
    print("Hello Good Morning")
simple()

def num():
    for i in range(1,10):
        print(i)
num()

#Print Welcome Message using thefunction and call multiple times.
def user():
    print("Welcome")
user()
user()
user()
user()
user()

#Print numbers from range(1,5) using the function.
def num():
    for i in range(1,6):
        print(i)
num()

#2). Function with parameter
def add(a,b):
    print(a+b)
add(10,30)

#Write a python function that takes two numbers as parameters and print their multiplication.
def mul(a,b):
    print(a*b)
mul(5,10)

#Write a python function that takes two numbers as parameters and print their substraction.
def sub(a,b):
    print(a-b)
sub(100,34)

#Write a function that take a number as parameter and prints its square.
def square(a):
    print(a*a)
square(5)

#Write a function that takes a number and prints wherther it is even or odd.
def a(b):
    if b%2==0:
        print("even")
    else:
        print("odd")
a(290)

#Write a function that takes length and breadth as parameters and prints the area of a rectangle.
def rect(l,b):
    print("Area of Rectangle:", l*b)
rect(10,20)

#3). Functions with Return

def add(a,b):
    return a+b
result=add(10,20)
print(result)

def sub(a,b):
    return a-b
result=sub(10,5)
print(result)

def mul(a,b):
    return a*b
result=mul(5,8)
print(result)

#Write a function that takes a number and returns its square.
def square(a):
    return a*a
result=square(10)
print(result)

#Write a function that takes a number whether it is even or odd.
def num(a):
    if a%2==0:
        return "Even"
    else:
        return "Odd"
print(num(20))

#Write a function that takes a length and breadth as parameters and returns the area of rectangle.
def rect(l,b):
    return l*b
result=rect(10,4)
print(result)

#print vs return
def func():
    print("Hello World")
def s():
    return "Hello"
func()
print(s())

#Write a python function that prints the number 25.
def n():
    print(25)
n()

#Write a python function that return the number 32.
def num():
    return 32

print(num())

#Write a python function that prints the sum of two numbers.
def sum(a,b):
    print(a+b)
sum(23,44)

#Write a python function that return the square of number.
def square(a):
    return a*a
print(square(2))

#Write a python function that print the getting message.
def n():
    print("Hello..")
n()

#Write a python function that return a getting message.
def s():
    return "Good Morning"
print(s())

#4). Default Parameter
def greek(name="sonali"):
    print("Hello",name)
greek()
greek("Sona")

#5). Keyword Argument
def info(name,age):
    print(age,name)
info(age=20, name="shruti")
