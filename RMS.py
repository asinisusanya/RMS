def calculate_grade(presentation_marks, report_marks):
    total_marks = presentation_marks + report_marks
    if total_marks >= 76:
        return 'A'
    elif total_marks >= 66:
        return 'B'
    elif total_marks >= 56:
        return 'C'
    elif total_marks >= 41:
        return 'D'
    else:
        return 'E'


def display_student_details(students):
    print("\n{:<15} {:<20} {:<25} {:<20} {:<15} {:<10}".format(
        "Reg No", "Name", "Research Area", "Presentation Marks", "Report Marks", "Grade"))
    print("-" * 105)
    for student in students:
        print("{:<15} {:<20} {:<25} {:<20} {:<15} {:<10}".format(
            student['reg_no'], student['name'], student['research_area'],
            student['presentation_marks'], student['report_marks'], student['grade']))


def update_marks(students, reg_no, mark_type):
    for student in students:
        if student['reg_no'] == reg_no:
            new_marks = int(input(f"Enter new {mark_type} Marks: "))
            student[mark_type] = new_marks
            student['grade'] = calculate_grade(student['presentation_marks'], student['report_marks'])
            print("Marks updated successfully!")
            return
    print("Student not found!")


def main():
    students = []
    while True:
        print("\n*** Welcome to Research Management System ***")
        print("1. Enter Student Details")
        print("2. View Student Details")
        print("3. Update Presentation Marks")
        print("4. Update Report Marks")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            num_students = int(input("Enter number of students: "))
            for _ in range(num_students):
                student = {
                    'reg_no': input("Enter Registration Number: "),
                    'name': input("Enter Name: "),
                    'research_area': input("Enter Research Area: "),
                    'presentation_marks': int(input("Enter Presentation Marks: ")),
                    'report_marks': int(input("Enter Report Marks: "))
                }
                student['grade'] = calculate_grade(student['presentation_marks'], student['report_marks'])
                students.append(student)

        elif choice == 2:
            display_student_details(students)

        elif choice == 3:
            reg_no = input("Enter Student Registration Number: ")
            update_marks(students, reg_no, 'presentation_marks')

        elif choice == 4:
            reg_no = input("Enter Student Registration Number: ")
            update_marks(students, reg_no, 'report_marks')

        elif choice == 5:
            print("Exiting the system.")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()

