# palindrom

input_str = str( input( "Enter the string:" ) )
print( input_str )
# rever =''.join(reversed(input_str))
# print( rever )

rever1 = input_str[::-1]
print( rever1 )
# rever2 = ' '
# for c in input_str:
#     rever2 = c + rever2
# print( rever2 )
if input_str == rever1:
    print( "Palindrome" )
else:
    print( "no palindrome" )
