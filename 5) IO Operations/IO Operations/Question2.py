n=int(input("Enter number of lines: "))
with open("demo.txt","r") as file:
    for i in range(n):
        print(file.readline(),end="")