# Find the factorial of any number
num=int(input("Enter a number here:"))
factorial=1
if num<0:
    print("Factorial of Negative numers does not exist.")
if num==0:
    print("Factorial of 0 is", 1)
if num>0:
    for i in range (1,num+1):
        factorial=factorial*i
    print("The Factorial of the given number is", factorial)
# 2nd method recursion
def factorial(a):
    if a==0:
        return 1
    else:
        return((a)*factorial(a-1))
num = int (input("Enter a number here:"))
result=factorial(num)
print("The Factorial of the given number is", result)