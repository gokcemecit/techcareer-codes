def rotating(list,index):
    newList=[]
    length=len(list)
    
    for i in range(index,length):
        
        newList.append(list[i])
        
    for i in range(0,index):
        newList.append(list[i])
        
    return newList
    

list=[1,2,3,4,5]
index=2

rotatedList=rotating(list,index)
print(rotatedList)