#Q1
l1=[2.4,21,"abc",True,50,3+4j,25]
print([e for e in l1 if type(e)==int])

#Q2
l1=[10,20,10,30,40,30,10,20,10,10]
i=0
for e in l1:
    if l1.index(e)==i:
        print(e,'  ',l1.count(e))
    i+=1

#Q3
l1=["Indore","Bhopal","Jaipur","Kanpur"]
l1.sort()
print(l1)

#Q4
l1=["Amit","Deepak","Sajal","Deepak","Arun","Amit"]
i=0
for e in l1:
    if l1.index(e)!=i:
        print('Repeated String is',e,'at index',i)
        break
    i+=1
else:
    print("All strings are distinct")

#Q5
l1=["Arun","Javed","Neeras","Gaurav","Pranav","Sahil","Paras"]
count=0
for e in l1:
    if e.endswith('s'):
        print(e)
        count+=1
print("count=",count)