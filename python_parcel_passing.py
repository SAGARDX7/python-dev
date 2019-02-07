class node:
    def __init__(self,val):
        self.data=val
        next=None
head,temp,pointer=None,None,None
N=int(input())
S=input()
l=len(S)
for i in range(1,N+1):
    if i==1:
        head=node(i)
        pointer=head
    elif i>=2 and i<N:
        temp=node(i)
        head.next=temp
        head=temp
    else:
        temp=node(i)
        head.next=temp
        head=temp
        head.next=pointer
        pointer=head
count=N
j=0
while count!=1:
    if S[j]=='a':
        pointer=pointer.next
    elif S[j]=='b':
        pointer.next=(pointer.next).next
        count=count-1
    j=(j+1)%l
print(pointer.data)
