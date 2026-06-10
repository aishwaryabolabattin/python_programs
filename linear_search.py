#Create a function search() to check whether the element is present or not. If element is present then display its index or position as well.
list1=[12,23,234,35,46,5,76,8,79,67]
def search(list1,element):
    if element in list1:
        print("Element Found")
        print("Index:",list1.index(element))
    else:
        print("Element not found")
search(list1,76)
search(list1,60)

#Linear Search
list1=[12,23,234,35,46,5,76,8,79,67]
def search(list1,element):
    for i in range(0, len(list1)):
        if element==list1[i]:
            print(f"{element} is found at {list1.index(element)} index")
            break
        else:
            print(f"{element } is not present in list")
element=int(input("Enter a number:"))
search(list1,element)