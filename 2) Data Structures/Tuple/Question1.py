n = int(input("Enter size of tuple: "))
a = []

for i in range(n):
    a.append(int(input("Enter element: ")))

t = tuple(a)

print("4th from first =", t[3])
print("4th from last =", t[-4])