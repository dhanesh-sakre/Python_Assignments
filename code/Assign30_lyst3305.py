#Q1
l1=[10,20,10,30,20,40,30,20,20,10,10]
print(set(l1))

#Q2
s1={11,32,14,15,22,67,89,100}
evenSet=set()
oddSet=set()
for e in s1:
    if e%2:
        oddSet.add(e)
    else:
        evenSet.add(e)
print(evenSet,oddSet)

#Q3
players={"Virat","Rohit","Shubhman","Hardik","Sami"}
p1=list(players)
for i in range(4):
    for j in range(i+1,5):
        print(p1[i],p1[j])

#Q4
blackHat=["A","B","C","D","E"]
redShoes=["B","D","F","G"]
for c in set(blackHat).intersection(set(redShoes)):
    print(c)

#Q5
N=int(input("Enter a number"))
s1=set()
if N>=2 and N<=12:
    for i in range(1,7):
        for j in range(1,7):
            if i+j==N:
                s1.add((i,j))

print(s1)