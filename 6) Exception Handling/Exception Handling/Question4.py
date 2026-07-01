numbers = [12, -5, 23, -8, 0, 45, -14, 89, -3, 7]

try:
    index = int(input("Enter an index (0 to 9): "))
    value = numbers[index]
    
    if value >= 0:
        print(f"The number {value} is positive.")
    else:
        print(f"The number {value} is negative.")
except (IndexError, ValueError):
    print("Error: Invalid index or input entered.")