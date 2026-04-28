#Tuple built in methods
#index()
t=(10,20,40,30)
print(t.index(20))

#count()
t=("Hello world")
print(t.count("l"))

#Built in functions
#all()
t1=(True, True, True, False)
print(all(t1))

#any()
t=(10,30,20,50)
print(any(t))

#len()
t1=("a","b","c","d")
print(len(t1))

#max()
t2=(10,30,60,40,100)
print(max(t2))

#min()
t2=(10,30,60,40,100)
print(min(t2))

#sum()
t1=(1,2,3,4,5)
print(sum(t1))

#sorted()
sort=("b","d","e","i","a")
print(sorted(sort))

#tuple()
sort=["b","d","e","i","a"]
print(tuple(sort))

#Write a program to find the index of any element in a tuple. 
sample=(10,20,40,60)
print(sample.index(40))

#Write a program to determine how many times Mumbai appears in a tuple.
city=("Pune","Mumbai","Solapur","Kolhapur","Mumbai") 
print(city.count("Mumbai"))

#Write a program to find the length of a tuple. 
city=("Pune","Mumbai","Solapur","Kolhapur","Mumbai") 
print(len(city))

#Write a program to find the maximum element of a tuple.
t=(10,20,70,100,200,600,20)
print(max(t)) 

#Write a program to find the sum of all elements in a tuple. 
t=(10,20,70,100,200,600,20)
print(sum(t))

#Write a program to convert a list into a tuple. 
t=[20,40,60,10]
print(tuple(t))
 
#Combine Two Lists and Convert to a Tuple
t1=[10,20,30,40]
t2=["a","b","c","d"]
t3=t1+t2
print(t3)
print(tuple(t3))