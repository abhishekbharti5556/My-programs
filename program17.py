# Display the Multiplication Table
n=int(input("Enter a number here:"))
for i in range (1,11):
    print(n, "x", i, "=",n*i)
#2nd method
n=int(input("Enter a number here:"))
i=1
while i<=10:
    print(n, "x", i, "=",n*i)
    i=i+1