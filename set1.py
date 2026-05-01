#set methods examples
#remove()
s={10,20,30,40}
s.remove(20)
print(s)

#discard()
s={10,30,50,80}
s.discard(100)
print(s)

#pop()
s={10,30,50,80}
s.pop()
print(s)

#set operations
#Union
a={1,2,3,4,5}
b={10,20,30,40,50}
print(a|b)

#Intersection
a={1,2,3,6,4}
b={1,2,6,2,7,9}
print(a&b)

#Difference
a={1,2,3,4,5}
b={10,20,30,40,50}
print(a-b)

#Symmetric Difference
a={1,2,3,6,4}
b={1,2,6,2,7,9}
print(a^b)

#issubset()
a={1,2,3,4}
b={1,2,6,8,3,4}
print(a.issubset(b))

#issuperset()
a={1,2,3,4}
b={1,2,6,8,2}
print(a.issuperset(b))

#copy()
a={1,2,3,4}
b=a.copy()
print(b)

#clear()
a={1,2,3,4}
a.clear()
print(a)

#isdisjoint()
a={1,2,3,4,5}
b={10,20,30,40,50}
print(a.isdisjoint(b))

#frozenset()
a=frozenset([1,2,3,4,5])
print(a)

#Write program to create a set with numbers{1,2,3,4,5}
a={1,2,3,4,5}
print(a)

#How would you add the number 6 to an existing set myset={1,2,3,4,5}
myset={1,2,3,4,5}
myset.add(6)
print(myset)

#Remove an element 3 from  myset={1,2,3,4,5} using remove() method
myset={1,2,3,4,5}
myset.remove(3)
print(myset)

#Write a python program to convert [1,2,2,3,4,4,5] into set to remove duplicate values
a=[1,2,2,3,4,4,5]
print(set(a))

#write a python program to remove a random element from set{5,10,15,20}
s={5,10,15,20}
s.pop()
print(s)
 
#Write a Python program to find the union of given two sets -
P = {1, 2, 3, 4, 5, 8}
Q = {5, 6, 7, 8, 1, 3}
print(P|Q)

#Check if set1 = {1, 2, 3} is a subset of set2 = {1, 2, 3, 4, 5}
#Check if set2 is a superset of set1.
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1.issuperset(set2))

#Check whether {1,2} and {3,4} are disjoint sets using isdisjoint ().
a={1,2}
b={3,4}
print(a.isdisjoint(b))

#Create a set {7,8,9} and make a copy using copy ().
a={7,8,9}
b=a.copy()
print(b)

#Create a frozenset () with elements 1,2,3 and print it
a=frozenset([1,2,3])
print(a)

#Write a set comprehension to create a set of squares of even numbers from a given list numbers = [1, 2, 3, 4, 5, 6].
#Given set1={1,2,3} and set2={2,3,4} find the intersection of these sets.
set1={1,2,3} 
set2={2,3,4} 
set3=(set1&set2)
print(set3)

#find the difference between set1={1,2,3,4} and set2={2,3,4,6}
set1={1,2,3,4} 
set2={2,3,4,6}
print(set1-set2)

#find the symmetric  difference between set={1,2,3,4} and set2={2,3,4,6}
set={1,2,3,4} 
set2={2,3,4,6}
print(set1^set2)

#Write a python code to find the length of myset={1,2,3,4,5}
myset={1,2,3,4,5}
print(len(myset))

