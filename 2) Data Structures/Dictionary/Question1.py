n = int(input("Enter number of items: "))
d = {}

for i in range(n):
    k = input("Enter key: ")
    v = int(input("Enter value: "))
    d[k] = v

print("Initially Dictionary: ")
print(d)

k = input("Enter new key: ")
v = int(input("Enter new value: "))

d[k] = v

print(d)