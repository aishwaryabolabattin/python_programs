#lst=[3,4,8,10,90,80]
#start=0
#end=len(lst)-1
#mid=(start+end)//2

#element=lst[mid]
#element<lst[mid]     #end=mid-1
#element>lst[mid]     #start=mid+1

#Binary Search
lst=[3,4,8,10,90,80]
def binary_Search(lst,element):
    start=0
    end=len(lst)-1
    while start<=end:
        mid=(start+end)//2
        if element==lst[mid]:
            print("Element is found")
            break
        elif element<lst[mid]:
            end=mid-1
        else:
            start=mid+1
    else:
        print("Element is not found")
element=int(input("Enter number:"))
binary_Search(lst,element)
