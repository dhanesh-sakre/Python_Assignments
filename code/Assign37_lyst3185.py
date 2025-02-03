def printN(n):
    if n>0:
        printN(n-1)
        print(n)
def printNReverse(n):
    if n>0:
        print(n)
        printNReverse(n-1)

def printNOdd(n):
    if n>0:
        printNOdd(n-1)
        print(2*n-1)
    
def printNOddReverse(n):
    if n>0:
        print(2*n-1)
        printNOddReverse(n-1)
    
def printMySirG(n):
    if n>0:
        print("MySirG")
        printMySirG(n-1)
        