#Q1
n=int(input("Enter a number"))
for e in range(1,n+1):
    print(2*e,end=' ')

#Q2
n=int(input("Enter a number"))
for e in range(1,n+1):
    print(2*e-1,end=' ')

#Q3
n=int(input("Enter a number"))
for e in range(1,n+1):
    print(e**2,end=' ')
#Q4
n=int(input("Enter a number"))
for e in range(1,n+1):
    print(e**3,end=' ')

#Q5
a=int(input("Enter starting of a range: "))
b=int(input("Enter ending of a range: "))

for x in range(a,b):
    for i in range(2,x):
        if x%i==0:
            break
    else:
        print(x,end=' ')

