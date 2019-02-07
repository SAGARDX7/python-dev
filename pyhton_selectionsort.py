arr=[5,2,4,9,6,8,1,0,3,7]
for i in range(0,9):
    min=arr[i]
    pos=i
    for j in range(i+1,10):
        if arr[j]<min:
            pos=j
            min=arr[j]
    temp=arr[i]
    arr[i]=arr[pos]
    arr[pos]=temp
print(arr)
