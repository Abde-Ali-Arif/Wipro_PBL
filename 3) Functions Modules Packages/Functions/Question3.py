a=int(input("enter a number "))

if a  == 0:
    print(1)
result=1
for i in range(1,a+1):
    result *=i
print(result)