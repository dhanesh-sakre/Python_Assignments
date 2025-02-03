#Q1
print("Enter numbers separated by comma")
l1=[int(e) for e in input().split(" ")]
print("Sum is ",sum(l1))

#Q2
print("Enter numbers separated by comma")
l1=[int(e) for e in input().split(" ")]
print("Average is ",sum(l1)/len(l1))

#Q3
print("Enter numbers separated by comma")
l1=[int(e) for e in input().split(" ")]
l2=[e**2 for e in l1]
print(l2)

#Q4
print("Enter numbers separated by comma")
l1=[int(e) for e in input().split(" ")]
l1.sort(reverse=True)
print(l1)

#Q5
print("Enter numbers separated by comma")
l1=[int(e) for e in input().split(" ")]
l2=l1[1::2]
print(l2)
