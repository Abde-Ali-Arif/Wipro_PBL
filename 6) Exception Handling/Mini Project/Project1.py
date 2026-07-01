try:
    filename = input("Enter the file name: ")

    file = open(filename, "r")

    total_items = 0
    free_items = 0
    amount = 0
    discount = 0

    for line in file:
        line = line.strip()

        # Ignore blank line
        if line == "":
            continue

        data = line.split()

        # Discount line
        if data[0].lower() == "discount":
            discount = int(data[1])

        # Free item
        elif data[1].lower() == "free":
            total_items += 1
            free_items += 1

        # Purchased item
        else:
            total_items += 1
            amount += int(data[1])

    file.close()

    final_amount = amount - discount

    print("No of items purchased:", total_items)
    print("No of free items:", free_items)
    print("Amount to pay:", amount)
    print("Discount given:", discount)
    print("Final amount paid:", final_amount)

except FileNotFoundError:
    print("File not found.")

except Exception as e:
    print("Error:", e)