#Program to Generate a Random Number
import random as rd
num1=int(input("Enter the starting range:"))
num2=int(input("Enter the ending range:"))
num=rd.randint(num1,num2)
print(num)