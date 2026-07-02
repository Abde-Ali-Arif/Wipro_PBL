n = int(input("Enter number of elements: "))
s = set()

for i in range(n):
    s.add(int(input("Enter element: ")))

x = int(input("Enter element to remove: "))

s.remove(x)

print(s)