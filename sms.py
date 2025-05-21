import module

# students dictonary and loadin data from json

students = {}
students = module.load_from_json(students)


# determine operation based of role id and operation id
def operation(role_id,op,students):
    if role_id == '1':
        if op == '1':
            students = module.add_student(students)
        elif op == '2':
            students = module.remove_student(students)
        elif op == '3':
            module.show_all_students(students,faculty=None)
        elif op == '4':
            module.show_specific_student(students)
        elif op == '5':
            module.show_logs()


            
    elif role_id == '2':
        faculty = input("\nEnter faculty name: ").lower()
        if op == '1':
            students = module.add_marks(students,faculty)
        if op == '2':
            module.show_all_students(students,faculty)


    elif role_id == '3' and op == '1':
        module.show_specific_student(students)
    
    else:
        print("\nInvalid option selected")


    # parsing data to json 
    module.add_to_json(students)



# fun to print menu based on role id and return role name
def sub_menu(role_id):
    sub_menu = ''
    role = ''
    
    if role_id == '1':
        print( """
        Choose an operation------->
        1. Add student 
        2. Remove student 
        3. View all students 
        4. View Specific student 
        5. View logs
        Type menu for got to main menu
        """)
        role = "counsellor"

    elif role_id ==  '2':
        print( """
        Choose an operation------->
        1. Add marks to student 
        2. view all students
        Type menu for got to main menu
        """)
        role = "faculty"
        
        
    elif role_id == '3':
        print( """
        Choose an operation------->
        1.Search student     
        Type menu for got to main menu
        """)
        role = "student"

    return role

        
menu = """

        -------MENU-------
        press 1 for Counsellor
        press 2 for Faculty
        press 3 for Student
        Exit for exit the program
===================================================
"""

print()
print("STUDENT MANAGEMENT SYSTEM".center(50,"*"))

# program start from here

while True:
    print(menu)

    role_id = input("Enter a role id : ")
    role = ""
    op = ""

    if role_id == 'exit':
        break

    elif role_id.isdigit():
        while True :
            if role_id.isdigit():
                
                print(f"\n{"".center(51,"=")}")

                role = sub_menu(role_id)
                op = input(f"\nEnter a choiche by {role.title()} : ").lower()
                if op == "menu" or op == "exit":
                    break
                else:
                    operation(role_id,op,students)
            else:
                print("Invalid input")
    else:
        print("Invalid role_id")


