string1=input("enter the string")
n=string1.split()
count=0
for i in range(0,len(n)):
    if(n[i]=='day'):
            count=count+1;
print(count)
        
