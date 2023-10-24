# count vowels
in_string = input( 'Enter the string:' )
in_string = in_string.lower()
count = 0
for character in in_string:
    if character == 'a' or character =='e' or character =='i' or character =='o' or character =='u':
        count = count + 1

print( 'vowel=', count )
