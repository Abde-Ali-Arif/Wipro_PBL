n1 = int(input("Enter size of list1: "))
list1 = []

for i in range(n1):
    list1.append(int(input("Enter number: ")))

n2 = int(input("Enter size of list2: "))
list2 = []

for i in range(n2):
    list2.append(int(input("Enter number: ")))

list2 = list1 + list2

print(list2)