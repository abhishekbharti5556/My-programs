#Print all Prime Numbers in an Interval
lower=int(input("Enter the Lower number:"))
upper=int(input("Enter the upper number:"))
for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if num % i ==0 :
                break
        else:
            print(num)