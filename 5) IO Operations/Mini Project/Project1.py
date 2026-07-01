import re

# Read file
file = open("Sample.txt", "r")
lines = file.readlines()
file.close()

# 1. Calculate Meeting Time
num_lines = len(lines)

if num_lines > 12:
    meeting_time = f"{num_lines - 12} PM"
else:
    meeting_time = f"{num_lines} AM"

# Read full content
file = open("Sample.txt", "r")
content = file.read().lower()
file.close()

# Extract words
words = re.findall(r"\b\w+\b", content)

# Count frequency of every word
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Find the word with maximum frequency
meeting_place = ""
max_count = 0

for word in freq:
    if freq[word] > max_count:
        max_count = freq[word]
        meeting_place = word

# Output
print("Meeting time:", meeting_time)
print("Meeting place:", meeting_place,"street")