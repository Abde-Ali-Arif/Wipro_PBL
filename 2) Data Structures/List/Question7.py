n = int(input("Enter size of list: "))
a = []

for i in range(n):
    a.append(int(input("Enter number: ")))

i = int(input("Enter index to remove: "))

a.pop(i)

print(a)