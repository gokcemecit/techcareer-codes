def median(list1,list2):
    if len(list1) > len(list2):
        list1, list2 = list2, list1
    while len(list1) > 1 and len(list2) > 1:
        if len(list1) > len(list2):
            list1, list2 = list2, list1
        list1Mid=len(list1)//2
        list2Mid=len(list2)//2
       
        if(list1[list1Mid]<list2[list2Mid]):    
            list1=list1[list1Mid:]
            list2=list2[:list2Mid]
        else:
            list1=list1[:list1Mid]
            list2=list2[list2Mid:]
    

    totalLength=len(list1)+len(list2)
    merged=sorted(list1+list2)
    median=0
    if(totalLength%2==0):
        medianIndexUpper=totalLength//2
        medianIndexLower=medianIndexUpper-1
        
        median=(merged[medianIndexLower]+merged[medianIndexUpper])/2
    else:
        medianIndex=totalLength//2
        median=merged[medianIndex]

    return median
        

    
list1=[1,3]
list2=[2]

print(median(list1,list2))

list3=[1,2,3]
list4=[4,5,6]

print(median(list3,list4))


