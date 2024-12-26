# Student Mark Management System

def input_students():
    """Input the number of students and their details."""
    students = []
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth (DD/MM/YYYY): ")
        students.append((student_id, name, dob))
    return students

def input_courses():
    """Input the number of courses and their details."""
    courses = []
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses.append((course_id, course_name))
    return courses

def input_marks(students, courses):
    """Input marks for students in a selected course."""
    marks = {}
    for course_id, course_name in courses:
        print(f"Course ID: {course_id}, Course Name: {course_name}")
    selected_course = input("Enter the course ID to input marks: ")

    if selected_course not in [course[0] for course in courses]:
        print("Invalid course ID!")
        return marks

    for student_id, name, _ in students:
        mark = float(input(f"Enter mark for {name} (ID: {student_id}): "))
        if selected_course not in marks:
            marks[selected_course] = {}
        marks[selected_course][student_id] = mark

    return marks

def list_courses(courses):
    """List all courses."""
    print("\nCourses:")
    for course_id, course_name in courses:
        print(f"ID: {course_id}, Name: {course_name}")

def list_students(students):
    """List all students."""
    print("\nStudents:")
    for student_id, name, dob in students:
        print(f"ID: {student_id}, Name: {name}, DoB: {dob}")

def show_student_marks(marks, students, courses):
    """Show student marks for a given course."""
    for course_id, course_name in courses:
        print(f"Course ID: {course_id}, Course Name: {course_name}")
    selected_course = input("Enter the course ID to show marks: ")

    if selected_course not in marks:
        print("No marks available for this course!")
        return

    print(f"\nMarks for Course ID: {selected_course}")
    for student_id, mark in marks[selected_course].items():
        student_name = next((name for sid, name, _ in students if sid == student_id), "Unknown")
        print(f"Student ID: {student_id}, Name: {student_name}, Mark: {mark}")

def main():
    """Main function to manage the student mark system."""
    students = input_students()
    courses = input_courses()
    marks = {}

    while True:
        print("\nOptions:")
        print("1. List students")
        print("2. List courses")
        print("3. Input marks for a course")
        print("4. Show student marks for a course")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_students(students)
        elif choice == "2":
            list_courses(courses)
        elif choice == "3":
            marks.update(input_marks(students, courses))
        elif choice == "4":
            show_student_marks(marks, students, courses)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

