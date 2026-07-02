n = int(input("Enter size of list: "))
a = []

for i in range(n):
    a.append(int(input("Enter number: ")))

a.reverse()

print(a)