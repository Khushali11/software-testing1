# sum of all the digit in the number
input_number = int(input( "Enter the number:" ))
sum = 0
while input_number != 0:
    digit = input_number % 10
    sum = sum + digit
    input_number //= 10
print(sum)
