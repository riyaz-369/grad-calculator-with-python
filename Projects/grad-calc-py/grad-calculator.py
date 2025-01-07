# Grade Calculator

def calculate_grade(average):
    """Function to calculate grade based on average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

def main():
    print("Welcome to the Grade Calculator!")
    
    # Get the number of subjects
    try:
        num_subjects = int(input("Enter the number of subjects: "))
        if num_subjects <= 0:
            print("Number of subjects must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Input subject names and marks
    subjects = {}
    for i in range(num_subjects):
        subject_name = input(f"Enter the name of subject {i+1}: ")
        try:
            marks = float(input(f"Enter marks for {subject_name}: "))
            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100. Try again.")
                return
            subjects[subject_name] = marks
        except ValueError:
            print("Invalid marks. Please enter a number.")
            return
    
    # Calculate total, average, and grade
    total_marks = sum(subjects.values())
    average_marks = total_marks / num_subjects
    grade = calculate_grade(average_marks)

    # Display results
    print("\n--- Result ---")
    for subject, mark in subjects.items():
        print(f"{subject}: {mark} marks")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
