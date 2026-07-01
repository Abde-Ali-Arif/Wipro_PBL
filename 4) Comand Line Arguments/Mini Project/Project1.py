import sys

def calculate_happiness(s1, s2, s3):
    # Split strings by hyphen and convert to sets for fast lookup
    like_set = set(s1.split('-'))
    dislike_set = set(s2.split('-'))
    numbers = s3.split('-')
    
    happiness = 0
    for num in numbers:
        if num in like_set:
            happiness += 1
        elif num in dislike_set:
            happiness -= 1
            
    return happiness

if len(sys.argv) == 4:
        print(calculate_happiness(sys.argv[1], sys.argv[2], sys.argv[3]))