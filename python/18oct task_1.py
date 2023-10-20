# fibbonacci series
num = int( input( "Enter the value for fibbonacci series:" ) )
x = list()
x.append( 0 )
x.append( 1 )
if num<=0:
    print("please enter valid input number")
elif num == 1:
    print(x[0])
elif num==2:
    print(x[0],x[1])
else:
    for i in range( 2, num ):
        x.append( x[i - 1] + x[i - 2])
    print( x )
#Factorial
print("____________________________________________________")
numb = int( input( "Enter the value for fibbonacci series:" ) )
y=1
if numb < 0:
    print("please enter valid input number")
elif num == 0:
    print( "Factorial of 0 is 1" )
else:
    print("Factorial series:")
    for i in range (1,numb+1):
        y = i*y
        print( y,  end=' ' )

