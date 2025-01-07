import tkinter as tk
from tkinter import messagebox

# Function to calculate grade based on average marks
def calculate_grade(average):
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

# Function to calculate results
def calculate():
    try:
        if not subjects:
            raise ValueError("Please add at least one subject!")
        
        # Get marks for all subjects
        marks = []
        for entry in subject_entries.values():
            marks.append(float(entry.get()))
        
        if any(mark < 0 or mark > 100 for mark in marks):
            raise ValueError("Marks must be between 0 and 100.")
        
        # Calculate total, average, and grade
        total_marks = sum(marks)
        average_marks = total_marks / len(marks)
        grade = calculate_grade(average_marks)
        
        # Display results
        result_text.set(
            f"Total Marks: {total_marks}\n"
            f"Average Marks: {average_marks:.2f}\n"
            f"Grade: {grade}"
        )
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Function to reset the calculator
def reset():
    global subjects, subject_entries
    for widget in subject_frame.winfo_children():
        widget.destroy()
    subjects = []
    subject_entries = {}
    result_text.set("")

# Function to add a new subject dynamically
def add_subject():
    global subjects, subject_entries
    subject_name = subject_name_var.get().strip()
    if not subject_name:
        messagebox.showerror("Error", "Subject name cannot be empty!")
        return
    if subject_name in subjects:
        messagebox.showerror("Error", f"Subject '{subject_name}' already exists!")
        return
    
    # Add the subject to the list and display input fields
    subjects.append(subject_name)
    label = tk.Label(subject_frame, text=f"{subject_name} Marks:", font=("Arial", 12), bg="#f5f5f5")
    label.pack(anchor="w", pady=5)
    entry = tk.Entry(subject_frame, font=("Arial", 12), width=10, relief="solid", bd=1)
    entry.pack(anchor="w", pady=5)
    subject_entries[subject_name] = entry

    subject_name_var.set("") 

# Initialize main window
root = tk.Tk()
root.title("Grade Calculator")
root.geometry("500x600")
root.configure(bg="#f5f5f5")

# Title
tk.Label(
    root, text="Grade Calculator", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white"
).pack(fill="x", pady=10)

# Subject Input Section
subject_name_var = tk.StringVar()
subject_input_frame = tk.Frame(root, bg="#f5f5f5")
subject_input_frame.pack(pady=10)

tk.Label(subject_input_frame, text="Subject Name:", font=("Arial", 12), bg="#f5f5f5").grid(row=0, column=0, padx=10)
subject_input = tk.Entry(subject_input_frame, textvariable=subject_name_var, font=("Arial", 12), width=15, relief="solid", bd=1)
subject_input.grid(row=0, column=1, padx=10)
add_subject_btn = tk.Button(
    subject_input_frame, text="Add Subject", command=add_subject, font=("Arial", 10), bg="#2196F3", fg="white"
)
add_subject_btn.grid(row=0, column=2, padx=10)

# Subject Marks Section
subject_frame = tk.Frame(root, bg="#f5f5f5")
subject_frame.pack(pady=20)

# Buttons
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=20)

tk.Button(
    button_frame, text="Calculate", command=calculate, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=20
).grid(row=0, column=0, padx=10)

tk.Button(
    button_frame, text="Reset", command=reset, font=("Arial", 12, "bold"), bg="#f44336", fg="white", padx=20
).grid(row=0, column=1, padx=10)

# Results Section
result_text = tk.StringVar()
tk.Label(
    root, textvariable=result_text, font=("Arial", 14, "bold"), fg="#3f51b5", bg="#f5f5f5", justify="center"
).pack(pady=20)

# Footer
tk.Label(
    root, text="Created by Riyaz", font=("Arial", 10), bg="#f5f5f5", fg="#555"
).pack(side="bottom", pady=10)

# Initialize subject data
subjects = []
subject_entries = {}

# Run the application
root.mainloop()
