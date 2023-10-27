# given number is prime or not
num=int(input("Enter the number:"))
if num<=1:
    print(num,"it is not a prime number.")
if num>1:
    for i in range(2,num):
        if num%i ==0:
            print(num,"it is not a prime number.")
            break
    else:
        print(num,"it is a prime number.")