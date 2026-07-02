n = int(input("Enter size of list: "))
a = []

for i in range(n):
    a.append(int(input("Enter element: ")))

t = tuple(a)

print(t)