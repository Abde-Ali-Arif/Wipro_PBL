try:
    num = int(input("Enter an integer: "))
    
    # Basic prime check logic
    is_prime = True
    if num <= 1:
        is_prime = False
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
except ValueError:
    print("Error: Please enter a valid integer number only.")
