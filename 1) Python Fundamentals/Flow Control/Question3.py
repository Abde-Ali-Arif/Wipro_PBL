def lastDigit(num1,num2):
    num1=num1%10
    num2=num2%10
    if(num1 == num2): return True
    else : return False
num1=int(input("enter first number : "))
num2=int(input("enter second number : "))
print(lastDigit(num1,num2))