# TYPE CONVERSION

# Q1 write a python script to convert a int to str
x = 25663
print(x)
type(x)

y = str(x)
print(y)
type(y)


# Q2 write a python script to pritn UNICODE of m
print(ord('m'))
# 109

print(ord('a'))
# 97

# Q3 write a python script to print character representation of unicode 100
print(chr(100))
# d

# Q4 write a python script to convert str into int type. 
# also describe when a str type value is not possible to convert into int

x = '45665'
type(x)

x = int(x)
type(x)

# it is not possible to convert str into int tyep when the base value present in the str
# is not a integer numebr
x = '255.66'
x = int(x)
print(x)
# error

#Q5 how to convert int into bool value
x = 2532
print(x)
x = bool(x)
print(x)
type(x)

# every non-zero value and non-empty values is True in python