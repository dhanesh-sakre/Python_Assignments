#Q1
n=int(input("Enter a number"))
d1={x:x**2 for x in range(1,n+1)}
print(d1)

#Q2
d1={1:'a',5:'b',3:'c',8:'d',2:'e'}
d2={}
for k in sorted(d1,reverse=True):
    d2[k]=d1[k]
print(d2)

#Q3
p=[n for n in input("Enter names separated by comma").split(',')]
player={}
for e in p:
    print("Enter for ",e)
    print("Total Matches")
    matches=int(input())
    print("Total Runs")
    runs=int(input())
    print("Half Centuries")
    hc=int(input())
    print("Centuries")
    c=int(input())
    player[e]=(matches,runs,hc,c)

#Q4
batches={'SA':230,'TB':200,'ES':100,'DM':250,'FA':190}

maxBatchSize=max(batches.values())
for k in batches:
    if batches[k]==maxBatchSize:
        print("Batch Code:",k)

#Q5
cities=["Patna","Bhopal","Pune","Chennai","Puri","Bajipur","Calicut"]
d1={}
for u in range(65,91):
    l1=[]
    for city in cities:
        if(city.startswith(chr(u))):
            l1.append(city)
    if len(l1)>0:
        d1[chr(u)]=l1
print(d1)
