def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
var=int(input("enter a number:"))
print("factorial of %d= %d"%(var,factorial(var)))
print("now a single line lambda function")
var1=3;var2=5
result=lambda var1,var2: var1+var2
print(result(var1,var2))
def unique_func(x,*extras):
    print("your first argument:",x)
    print("now for extra values")
    for i in extras:
        print(i)
    return
unique_func(10)
unique_func(10,20)
unique_func(10,20,30,40,50,60,70,80,90,100)
