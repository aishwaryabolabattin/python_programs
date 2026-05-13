#Pattern examples

#Write a python program to print the following pattern.
#* * * * *
#* * * * *
#* * * * *
#* * * * *
#* * * * *

for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

#Write a python program to print the following pattern.
#*
#* *
#* * *
#* * * *
#* * * * *
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=" ")
    print()

#Write a python program to print the following pattern.
#* * * * *
#* * * *
#* * *
#* *
#*
for i in range(-1,6):
    for j in range(i,6):
        print("*", end=" ")
    print()

#Write a python program to print the following pattern.
#1 
#1 2
#1 2 3 
#1 2 3 4
#1 2 3 4 5
for i in range(1,6):
    for j in range(1, i+1):
        print(j,  end=" ")
    print()

#Write a python program to print the following pattern.
#5 4 3 2 1
#5 4 3 2
#5 4 3
#5 4 
#5
for i in range(5):
    for j in range(5,i, -1):
        print(j, end=" ")
    print()

 

