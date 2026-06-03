#Exception examples
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

try:
    num=int("abc")
    print(num)
except ValueError:
    print("Invalid input! Please enter a number.")

#Write a program to ask the user to enter an integer. Handle invalid input.
#try:
#   print("Integer is:",num)
#except ValueError:
  #  print("Invalid input! Please enter a valid integer.")

#Write a program to divide 10 by number entered by the user and handle division by zero error.
try:
    num=int(input("Enter a number to divide 10 by: "))
    result=10/num
    print("Result is:",result)
except ZeroDivisionError:
    print("You can't divide by zero!")

#Write a program access a list element and handle index error.
try:
    list=[1,2,3,4,5]
    print(list[4])
except IndexError:
    print("Invalid index! Please enter a valid index.")

#Write a python program to:
#Take a nnumber as input from the user(in string format)
#Convert the string to an integer 
# print the integer value
#Handle the error using try-except if the user enters invalid input

try:
    str=input("Enter a number: ")
    num=int(str)
    print(num)
except ValueError:
    print("Invalid input! Please enter a valid number.")

#Write a python program to:
#Take a number as input from the user
#Convert the integer into string using str() function
#Print the string value
#Handle error using try=except
try:
    num=int(input("Enter a number: "))
    s=str(num)
    print(s)
except ValueError:
    print("Invalid input! Please enter a valid number.")   







