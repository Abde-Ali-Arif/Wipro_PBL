n = int(input("Enter number of items: "))
d = {}

for i in range(n):
    k = input("Enter key: ")
    v = int(input("Enter value: "))
    d[k] = v

print("Keys")
for i in d:
    print(i)

print("Values")
for i in d.values():
    print(i)

print("Keys and Values")
for i in d:
    print(i, d[i])