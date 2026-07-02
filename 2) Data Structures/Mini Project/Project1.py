# 1. Create a dictionary of people and facts
people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

# 2. Display the initial list
print("output:")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")

person=input("\nEnter person name for which you need to change fact: ")
fact=input("Enter fact that you need to change: ")
people_facts[person] = fact

nperson=input("\nEnter new person name which you want to add in dictionary: ")
nfact=input(f"Enter fact that you want to insert for the new person {nperson}: ")
people_facts[nperson] = nfact

# 5. Display the new list
print("\nNew list of people and facts:")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")