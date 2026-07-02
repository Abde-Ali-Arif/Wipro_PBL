n = int(input("Enter number of elements: "))
s = set()

for i in range(n):
    s.add(int(input("Enter element: ")))

print("Maximum =", max(s))
print("Minimum =", min(s))