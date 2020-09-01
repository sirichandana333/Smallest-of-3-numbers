#LCM of 2 numbers
x=float(input("enter first number: "))
y=float(input("enter second number: "))
#logic begins here
if(x>y):
    greater=x
else:
    greater=y
while(1):
        if((greater%x==0) and (greater%y==0)):
            LCM=greater
            break
        greater+=1
#display result
print("LCM is ",LCM)
