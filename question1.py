def maxValue(list):
    temp=list[0]
    for i in list:
        if(i>temp):
            temp=i
        else:
            continue
    return temp

list=[1,2,3,4,5]
list2=[-1,-5,-3]

print(list)
print(maxValue(list))
print(list2)
print(maxValue(list2))
