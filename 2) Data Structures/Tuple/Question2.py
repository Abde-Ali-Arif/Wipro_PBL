n = int(input("Enter size of tuple: "))
a = []

for i in range(n):
    a.append(int(input("Enter element: ")))

t = tuple(a)

x = int(input("Enter element to search: "))

if x in t:
    print("Element exists")
else:
    print("Element does not exist")