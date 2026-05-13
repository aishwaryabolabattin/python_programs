#pass examples
for i in range(5):
    if i==3:
        pass
    print(i)

#Write a python program that iterates through numbers from 0 to 10. fro each number, print it only if it is odd.
for i in range(0,11):
    if i % 2 != 0:
        pass
        print(i)

#Write a program that iterates through a set of numbers {1,2,3,4,5}.
#Print all the elements except the number 3. when the value is 3, do nothing using the pass statement inside the if condition.

set={1,2,3,4,5}
for i in set:
    if i==3:
        pass
    else:
        print(i)