student_scores = {
    "Alice": [85,90,92],
    "Bob": [78,80,85],
    "Charlie": [92,88,95],
}

for student, grades in student_scores.items():
    print(f"{student}:", *grades)