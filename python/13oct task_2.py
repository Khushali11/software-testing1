# find the area of circle= pi*r**2
# pi=3.14

r = int(input('Enter radius='))
print("Area of circle=", 3.14 * (r ** 2))
print("----------------------------------------")
# find > ,< ,=
x=int(input('Enter one number x:'))
y=int(input("Enter second number y:"))
print("x>y ",x>y)
print("x<y ",x<y)
print("x=y ",x==y)
print("----------------------------------------")
# use ternary operator
print("x = y" if x==y else "x>y" if x>y else "x<y")
z=int(input("Enter third number z:"))
print("Maximum of ",x,y,z,"is",sep=",")
print(x if x>y and x>z else y if y>z else z)
print("----------------------------------------")
### find square and cube of given number
numb=int(input("Enter the number :"))
print("square of ",numb,"=",numb**2)
print("cube of ",numb,"=",numb**3)