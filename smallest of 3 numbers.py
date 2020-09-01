#To find smallest of three numbers
num1=float(input("enter 1st number: "))
num2=float(input("enter 2nd number: "))
num3=float(input("enter 3rd number: "))
#Logic begins here
if (num1<=num2) and (num1<=num3):
    smallest=num1
elif (num2<=num1) and (num2<=num3):
    smallest=num2
else:
    smallest=num3
#displaying result
    print("the smallest number is ",smallest)
    
