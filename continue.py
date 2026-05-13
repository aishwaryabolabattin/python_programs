#continue examples
for i in range(10):
    if i== 5:
        continue
    print(i)

#Print number from 1 to 10 skip number 5
for i in range(1,11):
    if i==5:
        continue
    print(i)

#Skip a specific item in the list and the list is
city=["Pune","Satara","Vardha","Nagar"]
for i in city:
    if i=="Vardha":
        continue
    print(i)

#Print only the odd number from 1 to 10.
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)

#Skip a specific character in a string
word="Hello World"
for w in word:
    if w=="l":
        continue
    print(w)