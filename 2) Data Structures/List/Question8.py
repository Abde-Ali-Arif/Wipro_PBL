n = int(input("Enter size of list: "))
a = []

for i in range(n):
    a.append(int(input("Enter number: ")))

x = int(input("Enter element to remove: "))

a.remove(x)

print(a)