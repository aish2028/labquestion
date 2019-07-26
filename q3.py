'''sum of digits'''

tnum=num=int(input("enter the number:"))
sum=0
while num>9:
    sum=(num % 10+num//10)
    num=sum
print(f"the sum of digits of {tnum} is:{num}")