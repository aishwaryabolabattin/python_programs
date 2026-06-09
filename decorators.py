#1
def Fun1():
    print("Fun1 is called...")

def Fun2(Fun1):
    print("Fun2 is called...")
    Fun1()

Fun2(Fun1)

#2
def withdraw():
    print("Withdraw is called")
withdraw()

def ATM(func1):     #Decorator function
    def inside():
        print("Welcome to ATM")
        func1()
        print("Thank You")
    return inside 

a=ATM(withdraw)
a()


def deposite():
    print("Deposite is called")
b=ATM(deposite)
b()

#3 @Decorators using Annotation
@ATM
def deposite():
    print("Deposite is called")
deposite()

@ATM
def withdraw():
    print("Withdraw is called")
withdraw()

#4
def ATM(func1):     #Decorator function
    def inside(amount):
        print("Welcome to ATM")
        func1(amount)
        print("Thank You")
    return inside 

@ATM
def withdraw(amount):
    print(f"{amount} Withdraw is called")
withdraw(50000)


#4 
def intro(fun):
    def wrapper(s):
        print("Hi..")
        fun(s)
        print("Welcome to Python")
    return wrapper
@intro
def name(name):
    print(name)
s=input("Enter your name:")
name(s)

def intro(fun):
    def wrapper(*args,**kwargs):
        print("Hi..")
        fun(*args,**kwargs)
        print("Welcome to Python")
    return wrapper
@intro
def sample(*args, **kwargs):
    for data in args:
        print(data)
    for name,value in kwargs.items():
        print(name,value)
sample(10,20,30,40,50,name="Python",version=3.10)


#5 Decorators as a scheduler
import datetime
def ScheduleTask(func):
    def wrapper():
        hour=datetime.datetime.now().hour
        if hour>=10 and hour<=18:
            func()
            print(hour)
        else:
            print("Task is not allowed at this time!!!")
    return wrapper

@ScheduleTask
def Test():
    print("Task is running...")
Test()




