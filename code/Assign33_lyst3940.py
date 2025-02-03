def isEven(n):
    return n%2==0

def greater(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def isLeapYear(year):
    return (year%400==0 if year%100==0 else year%4==0)

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
    