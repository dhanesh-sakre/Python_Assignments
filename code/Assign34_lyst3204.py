from Assign33 import isPrime
def printNOdd(n):
    for i in range(1,n+1):
        print(2*i-1,end=' ')

def printNPrime(n):
    x=2
    while n:
        if isPrime(x):
           print(x,end=' ')
           n-=1
        x+=1

def printPrimeBetween(a,b):
    for x in range(a+1,b):
        if isPrime(x):
            print(x,end=' ')

def printNfib(n):
    a,b=-1,1
    while n:
        c=a+b
        print(c,end=' ')
        a,b=b,c
        n-=1

def printAllFactors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=' ')

         