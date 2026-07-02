user_input = input("Enter the scores separated by spaces: ")

scores = [int(x) for x in user_input.split()]

unique_scores = set(scores)

unique_scores.remove(max(unique_scores))

runner_up = max(unique_scores)

print("Runner-up score:", runner_up)