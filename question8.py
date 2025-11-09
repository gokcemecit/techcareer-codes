def isAnagram(string1,string2):
    string1=string1.lower()
    string2=string2.lower()

    string1=string1.replace(" ","")
    string2=string2.replace(" ","")


    if(sorted(string1)==sorted(string2)):
        return True
    else:
        return False
    



print(isAnagram("listen","silent"))
print(isAnagram("hello","world"))
