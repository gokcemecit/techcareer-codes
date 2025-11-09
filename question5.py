def merging(list1,list2):
    list3=[]
    for i in list1:
        list3.append(i)
    for j in list2:
        list3.append(j)
    return list3

list1=[1,2,3]
list2=[]
print(merging(list1,list2))