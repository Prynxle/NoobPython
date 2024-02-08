# Student Database
student_database = {}

def add_student(subj, fname, grade):
    # Check if the subject is already a key in the database
    if subj in student_database:
        student_database[subj][fname] = grade
    else:
        student_database[subj] = {fname: grade}
    print(f"Added {fname} with {grade} in {subj}.")

def display_students():
    print("\nStudent Database:")
    for subj, students in student_database.items():
        print(f"{subj}:")
        for fname, grade in students.items():
            print(f"- {fname}: {grade}")

# Main program
while True:
    print("\nOptions:")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Quit")

    choice = input("What do you want to do? ")

    if choice == '1':
        subj = input("Enter the subject: ")
        fname = input("Enter the student's name: ")
        grade = input("Enter the student's grade: ")
        add_student(subj, fname, grade)
    elif choice == '2':
        display_students()
    elif choice == '3':
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")
