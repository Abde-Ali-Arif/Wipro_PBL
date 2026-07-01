text = input("Enter text to append: ")

with open("demo.txt","a") as file:
    file.write(text+"\n")