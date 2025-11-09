def maxValue(list):
    temp=list[0]
    for i in list:
        if(i>temp):
            temp=i
        else:
            continue
    return temp


def missingElement(list):
    listSum=0
    for i in list:
        listSum=listSum+i

    num=maxValue(list)
    correctSum=(num*(num+1))/2
    return correctSum-listSum


list=[1,2,4,5]

print(missingElement(list))
