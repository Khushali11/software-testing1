# triangle classifier
print( "triangle   classifier:" )
side1 = float( input( "Enter side 1 length of side 1:" ) )
side2 = float( input( "Enter side 1 length of side 2:" ) )
side3 = float( input( "Enter side 1 length of side 3:" ) )
if side1 == side2 == side3:
    print( "equilateral" )
elif side1 == side2 or side2 == side3 or side1 == side3:
    print( "isosceles" )
else:
    print( "scalene" )