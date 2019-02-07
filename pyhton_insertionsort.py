arr=[5,2,4,9,6,8,1,0,3,7]
for i in range(1,10):
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
print(arr)
