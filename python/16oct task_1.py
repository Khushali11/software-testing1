# grade of given score
# A:90-100
# B:80-89
# C:70-79
# D:60-69
# F:0-59
print("Enter the four subjects marks out of 100 :")
marks1=float(input("Enter  1 subject marks:"))
marks2=float(input("Enter  2 subject marks:"))
marks3=float(input("Enter  3 subject marks:"))
marks4=float(input("Enter  4 subject marks:"))
avg=(marks1+marks2+marks3+marks4)/4
print(avg)
print("A" if 90<= avg <=100 else "B" if 80<= avg <=89 else "C" if 70<= avg <=79 else "D" if 60<= avg <=69 else "F")
