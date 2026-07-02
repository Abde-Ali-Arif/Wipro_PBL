n = int(input("Enter number of items: "))
d = {}

for i in range(n):
    k = input("Enter key: ")
    v = int(input("Enter value: "))
    d[k] = v

s = 0

for i in d.values():
    s = s + i

print("Sum =", s)