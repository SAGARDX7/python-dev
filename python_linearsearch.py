arr=list(input("input an list of elements:").split(" "))
for i in range(0,len(arr)):
    arr[i]=int(arr[i])
x=int(input("enter the element you want to search:"))
flag=0
for i in range(0,len(arr)):
    if arr[i]==x:
        flag=1
        pos=i
        break
if flag==1:
    print("element present at position no. ",pos+1)
else:
    print("element not found!")

