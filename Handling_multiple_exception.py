#Handling Multiple Exceptions
try:
    num=int("abc")
except ZeroDivisionError:
    print("Division error")
except ValueError:
    print("Enter valid number!!")

#Take an integer  input from the user and divide 10 by that number. use exception handling to handle ZeroDivisionError and ValueError., and display appropriate messages.
try:
    #num=int(input("Enter a number : "))
    #result=10/num
    #print(result)
#except ZeroDivisionError:
    print("divide by zero!")
except ValueError:
    print("Enter valid number.")

#Write a python program that performs the following tasks:
#Ask the user to enter a number
#Divide 10 by the number entered by the user
#try to open a file named data.txt for reading
file=open("data.txt","w")
file.write("This is a sample file.")
file.close()
try:
    num=int(input("Enter a number: "))
    result=10/num
    print(result)
    with open("data.txt","r") as file:
        content=file.read()
        print(content)
except ZeroDivisionError:
    print("divide by zero!")
except ValueError:
    print("Enter valid number.")
except FileNotFoundError:
    print("File not found")

#Create a list [10,20,30] Ask the user for index and print the value at the index. If the index is out of rage, print "Oops! Index is out of range." if the input is not a number, print "Oops!" That is not a number."
my_list=[10,20,30]
try:
    index=int(input("Enter an index: "))
    print(my_list[index])
except IndexError:
    print("Oops! Index is out of range.")
except ValueError:
    print("Oops! That is not a number.")

#Write a python program to read a filr named file.txt and handle possible errors. Your program should:
#try to open file.txt for reading.
#If the file does not exist, catch the FileNotFoundError and print "File not found."
file=open("file.txt","w")
file.write("Hello world!")
file.close()

try:
    with open("file.txt","r") as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")

#Write a python program that demonstrate a TypeError and handle it using try-except block.  
#Assign an integer value to variable a. 
#Assign string to variable b.
#Try to add a and b
#Since python cannot add an integer and string, a TypeError will occur.
#Use a try-except block to catch the TypeError and print the message.
a=10
b="30"
try:
    result=a+b
    print(result)
except TypeError:
    print("Please check your variables.")

