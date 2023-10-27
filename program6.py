#Python Program - Swap Two Variables
x=int(input("Enter the value of X:"))
y=int(input("Enter the value of Y:"))
temp=x
x=y
y=temp
print("The value of x and y is:",x,"and",y)
# with out using third variable
x=int(input("Enter the value of X:"))
y=int(input("Enter the value of Y:"))
x,y=y,x
print("The value of x and y is:",x,"and",y)