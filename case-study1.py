students = {
    "S001": {"name": "Alice", "age": 20, "courses": ["Math", "Physics"]},
    "S002": {"name": "Bob", "age": 21, "courses": ["Chemistry", "Biology"]},
    "S003": {"name": "Charlie", "age": 19, "courses": ["Math", "Computer Science"]}
}

def add_student(student_id, name, age, courses):
    students[student_id] = {"name": name, "age": age, "courses": courses}
    print(f"Student {name} added.")

def enroll_course(student_id, course_name):
    if student_id in students:
        students[student_id]["courses"].append(course_name)
        print(f"Student {students[student_id]['name']} enrolled in {course_name}.")
    else:
        print("Student not found.")

def get_student_info(student_id):
    if student_id in students:
        info = students[student_id]
        print(f"ID: {student_id}, Name: {info['name']}, Age: {info['age']}, "
              f"Courses: {', '.join(info['courses'])}")
    else:
        print("Student not found.")

add_student("S004", "David", 22, ["History"])
enroll_course("S001", "Chemistry")
get_student_info("S001")
