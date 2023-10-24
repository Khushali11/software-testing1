# find square root using function parameter
def sqrroot(x,y):
    root= x**y
    print(x,"^",y,"=",end=' ')
    return root
srr= sqrroot(4,3)
print(srr)
# Lambda expresion for triple power
i = int(input("enter the value:"))
x= lambda a:a**3
print("Triple power of ",i)
print(x(i))