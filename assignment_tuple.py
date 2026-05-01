#Write a program to concatenate two tuple.
t1=(1,2,3,4,5)
t2=(10,20,30,40,50)
t3=t1+t2
print(t3)

#Write a program to slice first three element of a tuple.
t1=(10,20,30,40,50)
print(t1[1:3])

#Write a program to delete a tuple.
#t=(1,2,3,4,5)
#del t
#print(t)

#Write a program to find a index of any element of tuple.
t2=(10,20,30,40,50)
print(t2.index(20))

#Write a program to determine how many times mumbai appears in a tuple.
city=("Pune","Mumbai","Solapur","Kolhapur","Mumbai")
print(city.count("Mumbai"))

##Write a program to find length of tuple.
city=("Pune","Mumbai","Solapur","Kolhapur","Mumbai")
print(len(city))

#Write a program to find maximum element of tuple.
t=(10,100,60,28,388)
print(max(t))

#Write a program to find sum of all tuple.
t=(10,100,60,28,388)
print(sum(t))

#Write a program to convert list into tuple.
t=[10,20,30,40,50]
print(tuple(t)) 

#Combine two lists and convert to a tuple.
t1=[10,30,50,60]
t2=[30,10,40,70]
t3=t1+t2
print(t3)
print(tuple(t3))