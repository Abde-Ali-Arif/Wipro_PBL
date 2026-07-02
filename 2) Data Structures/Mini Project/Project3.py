student_records = {
    "Krishna": [67.0, 68.0, 69.0],
    "Arjun": [70.0, 98.0, 63.0],
    "Malika": [52.0, 56.0, 60.0]
}

query_name = input("Enter a name: ")

if query_name in student_records:
    marks = student_records[query_name]
    average = sum(marks) / len(marks)
    
    print(f"Average percentage mark: {average:.2f}")
else:
    print("Student not found.")