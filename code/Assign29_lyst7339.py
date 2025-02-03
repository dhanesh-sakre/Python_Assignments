#Q1
l1=[10,20,30]
t1=tuple(l1)
print(t1,type(t1))

#Q2
t1=(10,30,20,50,40,60,70)
print(t1[::-1])

#Q3
l1=['abac','bacd','aabb','ccbaa','abc','bada','caaac']
result=[]
l1.sort()
i=0
for u in range(97,123):
    temp=[]
    flag=False
    for s in l1:
        if(s.startswith(chr(u))):
            temp.append(s)
            flag=True
    if(flag):
       result.append(tuple(temp)) 
print(result)   

#Q4
l1=[]
for e in range(65,91):
    l1.append((chr(e),e))
print(l1)

#Q5
t1=(34,56,45,12,32,71,89,60)
print("Sum is ",sum([e for e in t1 if e%2]))
