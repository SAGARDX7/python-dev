inp=input().split(" ")
T=int(inp[0])
R=int(inp[1])
G=int(inp[2])
B=int(inp[3])
r=g=b=False
red=green=blue=0
yellow=cyan=magenta=white=0
black=1
for i in range(1,T):
    if i%R==0:
        r=~r
    if i%G==0:
        g=~g
    if i%B==0:
        b=~b
    if r and b and g:
        white=white+1
    elif r and ~g and b:
        magenta=magenta+1
    elif ~r and g and b:
        cyan=cyan+1
    elif r and g and ~b:
        yellow=yellow+1
    elif ~r and ~g and b:
        blue=blue+1
    elif ~r and g and ~b:
        green=green+1
    elif r and ~g and ~b:
        red=red+1
    else:
        black=black+1
print("%d %d %d %d %d %d %d %d" % (red,green,blue,yellow,cyan,magenta,white,black))
