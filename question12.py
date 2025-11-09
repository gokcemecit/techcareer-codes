def palindrom(string):
    longestPolindrom=""
    
    for i in range(len(string)):
        singleCentered=""
        right=i
        left=i
        while(left >= 0 and right < len(string) and string[right]==string[left]):
           
            right=right+1
            left=left-1
            singleCentered=string[left+1:right]

        doublyCentered=""
        right=i+1
        left=i
        while(left >= 0 and right < len(string) and string[right]==string[left]):
           
            right=right+1
            left=left-1
            doublyCentered=string[left+1:right]

    if(len(doublyCentered)>len(singleCentered)):
        longestPolindrom=doublyCentered
    else:
        longestPolindrom=singleCentered

        

            


        
