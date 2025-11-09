def evenNumberLister(list):
    resultList=[]
    for i in list:
        if (i%2==0):
            resultList.append(i)
        else:
            continue
    return resultList

list=[1,2,3,4,5,6,7]

print(evenNumberLister(list))
