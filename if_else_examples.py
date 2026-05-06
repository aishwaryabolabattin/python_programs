#If-else examples

#Write a program to check if a number is within the range 10 and 50
num=int(input("Enter number:"))
if 10<= num <=50:
    print("number within 10 and 50 range")
else:
    print("number not within an 10 and 50 range")

#Write a program to check if number is dividible by 3 and 5.
num=int(input("Enter number:"))
if num%3==0 and num%5==0:
    print("number is divisible by 3 and 5")
else:
    print("number is not divisible by 3 and 5")

#Write a program to check whether number is even or odd.
num=int(input("Enter number:"))
if num%2==0:
    print("number is even")
else:
    print("number is odd")

#check whether number is positive or negative.
num=int(input("Enter number:"))
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Error")

#If marks >= 40 the pass else fail.
marks=int(input("Enter marks:"))
if marks>=40:
    print("Pass")
else:
    print("Fail")

#Check if number is greater than 100 or not.
num=int(input("Enter number:"))
if num>100:
    print("Number is greater than 100")
else:
    print("Number is not greater than 100")

#Write a program to print "Fizz" if a number is divisible by 3, "Buzz" if divisible by 5if divisible by both 3 and 5 then print "FizzBuzz" Otherwise, print the number itself.
num=int(input("Enter number:"))
if num%3==0 and num%5==0:
    print("FizzBuzz")
    
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
else:
    print("num")

