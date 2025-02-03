#Q1 wrtie a python script to take your name as an input from user and print it
name = input("enter my name: ")
print("my name is : ", name)

#Q2 write a python script to take two numbers as input and calcualte the sum of two numbers
num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))
sum = num1 + num2
print("sum of two nuimbers is : ", sum)

# Q3 write a python script to take radius as input from user and calcualte area of circle
r = float(input("enter radius of circle : "))
area = (3.14)*(r**2)
print("area of the circle is :", area)

#Q4 write a python script to calculate square of a number. take number as input from user.
num = float(input("enter a number : "))
square = num**2
print(f"the square of {num} the number is :", square)

# Q5  write a python script to take character as an input from user and
#  print unicode of that number
char = input("enter a character : ")
print(ord(char))