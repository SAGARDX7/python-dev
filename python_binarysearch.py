import math
arr=list(input("Enter a List:").split(" "))
for i in range(0,len(arr)):
    arr[i]=int(arr[i])
print("Before sorting the list",arr)
for i in range(1,len(arr)):
    j=i
    flag=True
    while j>=1 and flag:
        if(arr[j-1]>arr[j]):
            temp=arr[j-1]
            arr[j-1]=arr[j]
            arr[j]=temp
        else:
            flag=False
        j=j-1
print("After sorting the list",arr)
x=int(input("Enter the element you want to search:"))
flag,beg,end=0,0,len(arr)-1
while beg<=end and flag==0:
    mid=int((beg+end)/2)
    if arr[mid]==x:
        pos=mid
        flag=1
        break
    elif arr[mid]<x:
        beg=mid+1
    else:
        end=mid-1
if flag==1:
    print("Element found at position: ",pos+1)
else:
    print("Element not found")
