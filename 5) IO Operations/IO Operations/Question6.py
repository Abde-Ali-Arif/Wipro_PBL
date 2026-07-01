target_word = input("Enter word to count: ")

with open("demo.txt", "r") as file:
    words = file.read().split()

print(words.count(target_word))