from student_module import *
from student_module import create_table

create_table()

while True:
    print("\n--- Student Management ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Name: ")
        roll_no = input("Roll No: ")
        branch = input("Branch: ")
        year = int(input("Year: "))
        add_student(name, roll_no, branch, year)

    elif choice == '2':
        get_all_students()

    elif choice == '3':
        id = int(input("Enter ID to update: "))
        name = input("New Name: ")
        roll_no = input("New Roll No: ")
        branch = input("New Branch: ")
        year = int(input("New Year: "))
        update_student(id, name, roll_no, branch, year)

    elif choice == '4':
        id = int(input("Enter ID to delete: "))
        delete_student(id)

    elif choice == '5':
        break

    else:
        print("Invalid choice!")
