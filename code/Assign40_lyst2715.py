def sumOfDigits(x):
    if x!=0:
        return x%10+sumOfDigits(x//10)
    return 0
def fact(x):
    if x==0:
        return 1
    return x*fact(x-1)
def dtob(num):
    if num>0:
        dtob(num//2)
        print(num%2,end='')
def dtoo(num):
    if num>0:
        dtoo(num//8)
        print(num%8,end='')

def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def nthPrime(n):
    x=1
    while n>0:
        x+=1
        if isPrime(x):
            n-=1
    return x

def sumPrime(n):
    if n==1:
        return 2
    return sumPrime(n-1)+nthPrime(n)
print(sumPrime(4))