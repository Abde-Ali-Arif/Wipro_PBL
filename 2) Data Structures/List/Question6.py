n = int(input("Enter size of list: "))
a = []

for i in range(n):
    a.append(int(input("Enter number: ")))

x = int(input("Enter new item: "))

a.insert(1, x)

print(a)