n1 = int(input("Enter size of first set: "))
s1 = set()

for i in range(n1):
    s1.add(int(input("Enter element: ")))

n2 = int(input("Enter size of second set: "))
s2 = set()

for i in range(n2):
    s2.add(int(input("Enter element: ")))

print(s1.intersection(s2))