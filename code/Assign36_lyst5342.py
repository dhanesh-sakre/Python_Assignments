def removeDuplicates(l1):
    return list(set(l1))

def freqDict(l1):
    l2=removeDuplicates(l1)
    d1={}
    for k in l2:
        d1[k]=l1.count(k)
    return d1

def extractNumbersFromText(text):
    num=[]
    for word in text.split(' '):
        for x in word.split(','):
            if type(eval(x))==int or type(eval(x))==float:
                num.append(float(x))
    return num

# l1=[3,4,7,11,2,8,9,5,17,20,31,46]
def largestSortedSubsequence(l1):
    i,j=0,0
    maxLength=-1
    while j<len(l1):
        i=j
        j=i
        while j<len(l1) and sorted(l1[i:j+1])==l1[i:j+1]:
            j+=1
        if j-i>maxLength: 
            maxLength=j-i
            startIndex=i
            endIndex=j
    return (l1[startIndex:endIndex])
def compareList(l1,l2):
    return sorted(l1)==sorted(l2)

