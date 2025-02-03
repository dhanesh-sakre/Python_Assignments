# Q1: # define a function to calculate of a factorial of a number and handle all possible exceptions.

# sol1
def factorial(num):
    try:
        if type(num)!=int:
            raise TypeError
        if num<0:
            raise ValueError
        fact = 1
        for i in range(1, num+1):
            fact *= i
        return fact
    except TypeError:
        print("type of value is not valid here")
    except ValueError:
        print("invalid value")
    except:
        print("unkown error")

print(factorial(num=-9))
# ---------------------------------------------------------------------

# sol2 
def factorial(num):
    i = 1
    facto = 1
    while i <= num:
        facto *= i
        i += 1
    return facto

print(factorial(6))
# -----------------------------------------------------------------------
# sol3
def factor(num):
    if num == 1:
        return 1
    else:
        return num * factor(num-1)
    
a=factor(5)
print(a)
# ----------------------------------------------------------------------------


# Q2 : define a function to find the greatest number among 3 given data. handle all possible Exceptions.

# sol1
def great():
    try:
        print("please enter numbers")
        a, b, c = int(input()), int(input()), int(input())
        return max(a, b, c)
    except ValueError:
        print("you gave invalid value as input")
    except TypeError:
        print("the type of value is not valid")
    except:
        print("unknown exception")

maxi = great()
print(f"the greatest number among these numbers is {maxi}")
# ----------------------------------------------------------------------------

# sol2
def greater():
    try:
        print("please enter numbers")
        a, b, c = int(input()), int(input()), int(input())
        if a > b:
            if a > c:
                print(f"the greatest number is : {a}")
            else:
                print(f"the greatest number is : {c}")
        else:
            if b > c:
                print(f"the greatest number is : {b}")
            else:
                print(f"the greatest number is : {c}")
    except ValueError:
        print("value is not valid")
    except type:
        print("type of value is not valid")

greater()
# ----------------------------------------------------------------------------


# Q3 HOW MANY "except" can be used with try block?
# ans: multiple time

# ----------------------------------------------------------------------------

# Q4  # Q3 HOW MANY "else" can be used with try block?
# ans: one time

# ----------------------------------------------------------------------------

# Q5 CAN WE WRITE try block without except block?
# ans: yes, but finally keyword(along with it's block of code) should be written in this case

try:
    num = input("enter a number: ")
    print(num)
finally:
    print("we are in the finally block.")
print("end")
# ----------------------------------------------------------------------------



