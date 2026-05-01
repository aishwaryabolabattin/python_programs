#enumerate() function
fruits=["Apple","Banana","Orange","Mango"]
for index, fruit in enumerate(fruits):
    print(index,fruit)

fruits=["Apple","Banana","Orange","Mango"]
for _, fruit in enumerate(fruits):
    print(fruit)

#enumerate() with a custom index
employee={"Sonali","Aishu"}
for i, emp in enumerate(employee, start=5):
    print(i,emp)

#Write a python program to print student names with numbering starting from 1 using the enumerate() function.
std_name={"Atharv","SOnali","Pavan","Chintu"}
for i, std in enumerate(std_name, start=1):
    print(i,std)

#Write a python program to print each character of a string with its index using enumerate().
fruits="Python"
for index, fruit in enumerate(fruits):
    print(index,fruit)

#Write a python program to print only the elements that are present at even index position in a list.
list1=["Red","Green","Blue","White"]
for i, color in enumerate(list1):
    if i%2==0:
        print(i, list1)

#Write a python program to using enumerate() to print the values from a list while ignoring the index.
list=[10,20,40,60,100]
for _, lst in enumerate(list):
    print(lst)




    