d1 = {}
d2 = {}
d3 = {}

n1 = int(input("Enter number of items in first dictionary: "))
for i in range(n1):
    k = input("Enter key: ")
    v = int(input("Enter value: "))
    d1[k] = v

n2 = int(input("Enter number of items in second dictionary: "))
for i in range(n2):
    k = input("Enter key: ")
    v = int(input("Enter value: "))
    d2[k] = v

n3 = int(input("Enter number of items in third dictionary: "))
for i in range(n3):
    k = input("Enter key: ")
    v = int(input("Enter value: "))
    d3[k] = v

d = {}

d.update(d1)
d.update(d2)
d.update(d3)

print(d)