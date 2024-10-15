n=int(input("enter the number of elements in the list "))
list1=[]
for x in range(0,n):
    x=int(input())
    list1.append(x);
print(list1)
list2=[x for x in list1
    if x>0]


print("list2 is",list2)
        
