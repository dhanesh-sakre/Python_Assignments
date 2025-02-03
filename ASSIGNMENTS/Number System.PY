#Q1 write a python script to print the binary of a number

def decimal_to_binary(num):
    if num > 1:
        decimal_to_binary(num // 2)
    print(num % 2, end="")

number = int(input("please enter a number: "))
print('bibary of', number, 'is :', end=" ")
decimal_to_binary(number)

#Q2 write a python script to print decimal number of a binary number 11001110
a = 11001110
str_a = str(a)
rev = str_a[::-1]
sum=0
for i in range(0, len(str_a)):
    sum += int(rev[i])*(2**i)
print(sum)

