K=int(input())
dislike=[]
sb=[]
for i in range(0,K):
    dislike.append(input())
N=int(input())
str=input().split(" ")
for i in range(0,N):
    flag=True
    for j in range(0,K):
        if str[i] == dislike[j]:
            flag=False
            break
    if flag:
        sb.append((str[i].upper())[0])
l=len(sb)
for i in range(0,l):
    if i>=0 and i<l-1:
        print(sb[i],end=".")
    else:
        print(sb[i],end="")
