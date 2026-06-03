#Else_finally Examples
try:
    print("Hello world!")
except:
    print("Error occurred!")
else:
    print("No any error")
finally:
    print("This will always execute.")


#Write a python program to divide two numbers.
#If an occurs,print "Error occurred!"
#If no error occurs, print "Division successful!"
#Always print "Program finished!" at the end of the program.
try:
    num1=10
    num2=5
    result=num1/num2
    print(result)
except:
    print("Error occurred!")
else:
    print("Division successful!")
finally:
    print("Program finished!")

#Write a python program to access an element from a list using an index.
try:
    list=[1,2,3,4,5]
    index=4
    print(list[index])
except:
    print("Error occurred!")
else:
    print("Element accessed successfully!")
finally:
    print("Program finished!")

#Write a program to open a file and read it safely.
try:
    with open("file.txt","r") as file:
        content=file.read()
        print(content)
except:
    print("Error")
else:
    print("file read successfully")
finally:
    print("Always executed")

#Write a program to remove an element from a set using remove and handle errors.

try:
    set={1,2,3,4,5}
    set.remove(3)
    print(set)
except:
    print("Error")
else:
    print("No error")
finally:
    print("Program finished!")






