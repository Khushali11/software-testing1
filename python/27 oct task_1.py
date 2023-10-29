# find largest and smallest number in the list
x=[5,55,23,45,100,89,75,12]
print(type(x))
print("original list:",x)
x.sort()
print("sort list:",x)
x.reverse()
print("reverse list",x)
y=len(x)
print("smallest number is ",x[0], "largest number is",x[y-1])

# find sum of all  the number
count=0
for i in x:
    count=count+i
print ("sum of all the element =",count)
# multiplay all the number in the list
sum=1
for i in x:
    sum=sum*i
print ("multiply of all the element =",sum)



