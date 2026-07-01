with open("demo.txt", "r") as file:
    words = file.read().split()

longest_word = max(words, key=len)
print(longest_word)