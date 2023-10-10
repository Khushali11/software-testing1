# take input from user and display  it with no repeated values
list_one = input("Enter any values with repeatation:\n")
print(list(list_one))
list_two = list(set(list_one))
print(list_two)
