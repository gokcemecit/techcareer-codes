def GCD(num1,num2):
    if num1>0 and num2>0:
        value=0
        if num1>num2:
            
            for i in range(1,num1,1):
                if(num1%i==0 and num2%i==0):
                    value=i

        elif num2>num1:
            for i in range(1,num2,1):
                if(num1%i==0 and num2%i==0):
                    value=i
        else:
            return num1

        return value  
    else:
        print("invalid numbers")


print(GCD(15,30))          

print(GCD(24,36))
print(GCD(7,13))
print(GCD(-7,13))
