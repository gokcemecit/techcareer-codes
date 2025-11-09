def reversingString(string):
    length=len(string)
    reversedString=""
    for i in range(length-1,-1,-1):
        reversedString+=string[i]
    return reversedString

text="hello"
print(reversingString(text))