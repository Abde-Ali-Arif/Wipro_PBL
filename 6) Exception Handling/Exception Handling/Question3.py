filename = input("Enter the file name to open: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print(content.title())
except FileNotFoundError:
    print("Error: This file does not exist.")