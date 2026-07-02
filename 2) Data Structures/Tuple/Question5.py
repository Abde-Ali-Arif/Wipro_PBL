n = int(input("Enter number of tuples: "))
l = []

for i in range(n):
    a = []
    for j in range(3):
        a.append(int(input("Enter element: ")))
    t = tuple(a)
    l.append((t[0], t[1], 100))

print(l)