#
inputlist = ["lal", "luck", "by", "chance", "i", "am", "happy", "55", 25,56, "madam"]
print( inputlist )
y = [i if type( i ) == str else 0 for i in inputlist]
y=list(set(y))
y.remove( 0 )
print( y )
print( "number of string in the list: ", len( y ) )
z = [i if len( i ) >= 2 else 0 for i in y]
z.remove( 0 )
print( z )
print( "string length more than equal to two:", len( z ) )
f = []
for i in z:
    x = len( i )

    if i[0] == i[x - 1]:
        f.append( i )
print( f )
print("number of string who have first and last char same:",len(f))
