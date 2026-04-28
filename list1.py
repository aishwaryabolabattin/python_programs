#updating element into list
num=[10,20,30,40,50]
num[1]=100
print(num)

#Removing element into list
#remove:
num=[10,20,30,500]
num.remove(20)
print(num)

#pop:
num=[10,20,30,500]
num.pop(3)
print(num)

#del:
num=[10,20,30,500]
del num[1]
print(num)

#Nested list in python'
user=[[1,2,3,4,5],
      ["a","b","c","d","e"],
      ["sona",8.5,"true","false"]]
print(user[2][0])

#write a python program to update the element in a list. change "banana" to "mango" in the list.
fruits=["Apple","Banana"]
fruits[1]="Mango"
print(fruits)

#write a python program to remove the element 30 from the list using remove method.
a=[10,20,30,40,50]
a.remove(30)
print(a)

#Write a Python program to create a list and remove the last element.
a=[10,20,30,40,50]
a.pop()
print(a)

#Write a Python program to remove the element at index 2.
a=[1,2,3,4,5]
a.pop(2)
print(a)

#Write a program to update 20 to 25 and then remove 40 using the remove method.
a=[10,30,40,20]
a[3]=25
a.remove(40)
print(a)

#Write a Python program to create a nested list and print "Math" from the list.
user=[[1,2,3,4,5],
      ["a","b","c","d","e"],
      ["sona",8.5,"true","false"],
      ["square","fact","math","floor"]]
print(user[3][2])

#Create a list with 5 integers change the second item in the list to a new number and print the updated list.
list=[10,20,50,60,80]
list[2]=30
print(list)

#Create a list of numbers. Insert the number 100 at the Third position and print the updated list.
a=[10,20,30,50,40]
a.insert(3,100)
print(a)

#Create two lists of numbers. Concatenate both lists into a single list and print the result.
a=[10,20,40,50]
b=[1,2,3,4]
c=a+b
print(c)

#Write a Python program to create a nested list representing a 3 × 3 matrix and print element 8 from the matrix using indexing.
user=[[1,2,3],[8,9,10],[12,14,16]]
print(user[1][0])

#Write a Python program to create a nested list containing student names and their marks. Print the marks of "Amit" from the nested list.
name=[["Amit","sona","raju", "Arjun"],[80,30,100,90]]
print(name[1][0])

#Write a Python program to perform the following operations on a list:
#1.	Update the value from 30 to 35.
a=[10,20,40,30]
a[3]=35
print(a)

#2.Remove the element 50 from the list using the remove () method.
a=[10,20,30,40,50]
a.remove(50)
print(a)

#3.	Remove the last element from the list using the pop () method.
a=["a","b","c","d","e"]
a.pop()
print(a)