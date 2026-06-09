#1
def GenFun():
    yield "Hello"
    yield "World"
    yield "Good Morning"
for i in GenFun():
    print(i) 

#2
def GenFun():
    yield "Hello"
    yield "World"
    yield "Good Morning"
g=GenFun()
print(next(g))
print(next(g))
print(next(g))

#3 List Comprehension
list1=[10,20,30,40,500]
g=(i for i in list1)
#print(g)
next(g)

#4 Convert function into generator function
def ConvertToGen(anyList):
    for i in anyList:
        yield i
list1=[10,20,50,30,20]
g1=ConvertToGen(list1)
print(next(g1))

#5 Convert function(iterable) into iterator/generator using iter().
list1=[10,20,30,40,50]
g=iter(list1)
print(next(g))
print(next(g))
print(next(g))

#Write a generator function to generate a sequence from 20 to 30.
def GenFun():
    for i in range(20,31):
        yield i
g=GenFun()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

#Take a input start and end from user and use while loop.
def GenFun():
    start=int(input("Enter a number: "))
    end=int(input("Enter a number:"))
    while start<=end:
        yield start
        start=start+1
g=GenFun()
print(next(g))
print(next(g))

print(next(g))
print(next(g))
print(next(g))



