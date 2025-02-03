def printNEven(n):
    if n>0:
        printNEven(n-1)
        print(2*n)
def printNEvenReverse(n):
    if n>0:
        print(2*n)
        printNEvenReverse(n-1)
def printNSquare(n):
    if n>0:
        printNSquare(n-1)
        print(n*n)
def printNCube(n):
    if n>0:
        printNCube(n-1)
        print(n*n*n)
def rev(n):
    if n!=0:
        print(n%10)
        rev(n//10)
