list=[]
n=5
for i in range(0,n):
    x=input()
    list.append(x)
count_=0
for i in list:
    count=i.count('a')
    count_=count_+count
print(count_)

