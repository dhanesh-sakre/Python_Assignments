#Q1
n=int(input("Enter a number"))
if n>=0:
    f=1
    for i in range(1,n+1):
        f=f*i
    print("Factorial is",f)
else:
    print("Invalid value to calculate factorial")

#Q1
import math
n=int(input("Enter a number"))
f=math.factorial(n)
print("Factorial is",f)

#Q2
num=int(input("Enter a number"))
count=0
while num>0:
    num=num//10
    count+=1
print("Total digits: ",count)

#Q2
num=int(input("Enter a number"))
if num<0:
    num=-num
print("Total digits: ",len(str(num)))

#Q3
num=int(input("Enter a number"))
sum=0
while num:
    sum=sum+num%10
    num=num//10
print("Sum of digits: ",sum)

#Q3
num=int(input("Enter a number"))
if num<0:
    num=-num
print("Sum is ",sum([int(digit) for digit in str(num)]))

#Q4
num=int(input("Enter a number"))
b=''
while num:
    b=str(num%2)+b
    num=num//2
print("Binary is ",b)
"""
25 = 11001  
25%2 = 1 |  b='1'+'' ='1'  
12%2 = 0 |  b='0'+'1'='01'
6%2  = 0 |  b='0'+'01'='001'
3%2  = 1 |  b='1'+'001'='1001'
1%2  = 1 |  b='1'+'1001'='11001'
"""
#Q5
num=int(input("Enter a number"))
o=''
while num:
    o=str(num%8)+o
    num=num//8
print("Octal is ",o)
