arr=[5,2,4,9,6,8,1,0,3,7]
for i in range(0,8):
    for j in range(0,9-i):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(arr)
