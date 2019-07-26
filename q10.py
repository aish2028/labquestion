def biggest(num1,num2,num3):
    if num1>num2 and num2>num3:
        return num1
    elif num2>num3:
        return num2
    else:
        max=num3
        return num3
num1=int(input("enter the number1:"))
num2=int(input("enter the number2:"))
num3=int(input("enter the number3:"))
print(biggest(num1,num2,num3))
