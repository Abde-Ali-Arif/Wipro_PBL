n = int(input("Enter number of items: "))
d = {}

for i in range(n):
    k = input("Enter key: ")
    v = int(input("Enter value: "))
    d[k] = v

x = input("Enter key to search: ")

if x in d:
    print("Key exists")
else:
    print("Key does not exist")