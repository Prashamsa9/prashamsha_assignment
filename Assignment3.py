import functools

# Decorator to log function activity
def log_activity(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with args: {args} kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

student_records = []

# Function to add student data using *args and **kwargs
@log_activity
def add_student(name, age, *grades, **additional_info):
    student = {
        "name": name,
        "age": age,
        "grades": list(grades),
    }
    student.update(additional_info)
    student_records.append(student)

# Function to calculate average and determine pass/fail status
@log_activity
def calculate_results():
    for student in student_records:
        grades = student.get("grades", [])
        if grades:
            average = sum(grades) / len(grades)
            student["average"] = round(average, 2)
            student["status"] = "Pass" if average >= 50 else "Fail"
        else:
            student["average"] = None
            student["status"] = "No grades available"

# Function to display student records
@log_activity
def display_records():
    for student in student_records:
        print("-" * 30)
        for key, value in student.items():
            print(f"{key.capitalize()}: {value}")


add_student("Mounika", 20, 85, 90, 88, major="Computer Science")
add_student("Chinni", 22, 45, 50, 55, major="Mathematics")
add_student("Alisha", 21, 70, 65, major="Physics")
add_student("Mahi", 23, major="History")  # No grades

calculate_results()
display_records()