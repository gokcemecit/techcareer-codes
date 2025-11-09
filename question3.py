def factorial(value):
    if(value==1 or value==0):
        return 1
    else:
        result=1
        for i in range(value,1,-1):
            result=result*i
        return result

x=5
print(factorial(x))
y=0
print(factorial(y))
    