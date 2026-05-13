#Break statement examples
for i in range(20):
    if i==12:
        break
    print(i)

fruits=["apple","banana","mango","orange"]
for fruit in fruits:
    if fruit=="mango":
        break
    print(fruit)

num=[10,20,40,60,-10,-3]
for item in num:
    if item<0:
        break
    print(item)

#Write a python program to print number for 1 t0 10.
#stop the loop when the number becomes 6 using the break statement
for i in range(1,11):
        if i==6:
             break
        print(i)

#Print elements of the list, but stop when "Cherry" is found.
fruits=["Apple","Banana","Cherry","Mango"]
for fruit in fruits:
     if fruit=="Cherry":
          break
     print(fruit)

#Print character of a Word until letter "t" is found.
str="silent"
for i in str:
     if i=="t":
          break
     print(i)

#