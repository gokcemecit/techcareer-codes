def reversingString(string):
    length=len(string)
    reversedString=""
    for i in range(length-1,-1,-1):
        reversedString+=string[i]
    return reversedString

def PalindromControl(string):
    newString=""
    for ch in string:
        if ch!=" ":
            newString+=ch.lower()

    reversedString=reversingString(newString)

    if(reversedString==newString):
        return True
    else:
        return False
        
    




print(PalindromControl("hello"))
print(PalindromControl("A man a plan a canal Panama"))





