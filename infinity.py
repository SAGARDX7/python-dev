count=0
def A():
    global count
    count=count+1
    print("A",count)
    B()
def B():
    global count
    count=count+1
    print("B",count)
    A()
A()
