T=int(input())
for i in range(0,T):
    fstr=[]
    rstr=[]
    prod=1
    flag=True
    fstr=list(input())
    l=len(fstr)
    for j in range(0,l):
        rstr.append(fstr[l-1-j])
        val=fstr[j]
        val=ord(val)-96
        prod=prod*val
    l=(int)(l/2)
    for j in range(0,l):
        if fstr[j]!=rstr[j]:
            flag=False
            break
    if flag:
        print("Palindrome")
    else:
        print(prod)
