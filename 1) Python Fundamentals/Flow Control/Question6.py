num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    flag = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            flag = False
            break

    if flag:
        print("Prime")
    else:
        print("Not Prime")