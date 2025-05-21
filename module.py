import datetime
import os
import json

# add student 
def add_student(students):
        
        status = True
        while status:
            
            # validation for student id
            s_id = input(f"{"\nEnter a Serial Number".ljust(25)} : ")

            while True:
                if s_id.isdigit():
                    while True:
                        if s_id in students:
                            print(f"Student with id {s_id} already exist")
                            s_id = input(f"{"\nEnter Again".ljust(25)} : ")
                        else:
                            break
                    break

                else:
                    print("Invalid serial number")
                    s_id = input(f"{"\nEnter Again".ljust(25)} : ")
            
            
            # validation for student first name
            fname = input(f"{"Enter a First Name".ljust(25)}: ").strip()
            while True:
                if fname.isalpha() and fname != "":
                    break
                else:
                    print("invalid First name value required ")
                    fname = input(f"{"Enter again".ljust(25)}: ")
            
            
            # validation for student last name
            lname = input(f"{"Enter a Last Name".ljust(25)}: ").strip()
            while True:
                if lname.isalpha() and lname != "":
                    break
                else:
                    print("invalid Last name value required ")
                    lname = input(f"{"Enter again".ljust(25)}: ")
            


            # validation for student last name
            contact = input(f"{"Enter a Contact Number".ljust(25)}: ")
            while True:
                if contact.isdigit() and contact != "":
                    break
                else:
                    print("enter digits only value requiredd")
                    contact = input(f"{"Enter again".ljust(25)}: ")



            subject = {}
            # validation for fees and marsk
            for i in range(2):
                subj_name = input(f"{"Enter a Subject".ljust(25)}: ")

                marks = input(f"{"Enter a Marks".ljust(25)}: ")
                while True:
                    if marks.isdigit():
                        break
                    else:
                        print("invalid type")
                        marks = input(f"{"Enter again Marks".ljust(25)}: ")

                fees = input(f"{"Enter a Fees".ljust(25)}: ")
                while True:
                    if fees.isdigit():
                        break
                    else:
                        print("invalid type")
                        fees = input(f"{"Enter again Fees".ljust(25)}: ")


                subject[subj_name] = {"marks": marks, "fees": fees}
            
            # faculty enter 
            faculty = input(f"{"Enter Faculty".ljust(25)}: ").strip()


            # adding data to students dictonary
            students[s_id] = {}
            students[s_id]["fname"] = fname
            students[s_id]["lname"] = lname
            students[s_id]["contact"] = contact
            students[s_id]["subject"] = subject
            students[s_id]["faculty"] = faculty
            

            # calling log function to add logs to changelog.txt file
            log_generator(fname,s_id,"added")

            ch = input("\nEnter another student [y/n]: ").lower()
            
            if ch == 'y' or ch == 'yes':
                status = True
            else:
                status = False

        return students



# remove a student
def remove_student(students):
    name = ""
    status = True

    while status:
        s_id = input("enter a student id : ")
        if s_id.isdigit():
            # s_id = int(s_id)
            if s_id in students:
                name = students[s_id]["fname"]
                print(f"\tID : {s_id}\n\tNAME : {name}")
                ch = input(f"\nDo you want to remove  {name} [y/n]: ").lower()
                if ch == 'y' or ch == 'yes':
                    del students[s_id]
                    print(f"{name} removed")
                    
                    # calling log function to add logs to changelog.txt file
                    log_generator(name,s_id,"removed")

                else:
                    break
            else:
                print("Student not found")
        else:
            print("Invalid student_id")
        



        ch = input("\nDo you want to remove any one else [y/n]: ").lower()

        if ch == 'y' or ch == 'yes':
            status = True
        else:
            status = False
        
    return students



# show all students
def show_all_students(students,faculty):

    print("------+--------------+--------------+--------------+--------------+------------+------------+--------------+------------+------------+--------------")
    print(f"{"S.no":<5} | {"FNAME":<12} | {"LNAME":<12} | {"CONTACT":<12} | {"SUBJECT-1":<12} | {"S1-MARKS":<10} | {"S1-FEES":<10} | {"SUBJECT-2":<12} | {"S2-MARKS":<10} | {"S2-FEES":<10} | {"FACULTY":<12}")
    print("------+--------------+--------------+--------------+--------------+------------+------------+--------------+------------+------------+--------------")
    

    for key, value in students.items():
        subjects = list(students[key]['subject'].keys())

        if faculty == None:
            print(f"{key:<5} | {students[key]["fname"]:<12} | {students[key]["lname"]:<12} | {students[key]["contact"]:<12} | ",end="")

            for k in subjects:
                # remember to store this in seperate variables like fees and marks for better understanding 
                print(f"{k:<12} | {students[key]['subject'][k]['marks']:<10} | {students[key]['subject'][k]['fees']:<10} | ",end="")
            
            print(f"{students[key]["faculty"]:<12}")


        
        # show students faculty vise
        elif faculty == students[key]["faculty"]:
            print(f"{key:<5} | {students[key]["fname"]:<12} | {students[key]["lname"]:<12} | {students[key]["contact"]:<12} | ",end="")

            for k in subjects:
                # remember to store this in seperate variables like fees and marks for better understanding 
                print(f"{k:<12} | {students[key]['subject'][k]['marks']:<10} | {students[key]['subject'][k]['fees']:<10} | ",end="")
            
            print(f"{students[key]["faculty"]:<12}")
            
    print("------+--------------+--------------+--------------+--------------+------------+------------+--------------+------------+------------+--------------")



# view specific student 
def show_specific_student(students):
    std_id = (input("enter specific student id : "))

    while True:
        if std_id.isdigit():
            # std_id = int(std_id)        
            if std_id in students:
                subjects = list(students[std_id]['subject'].keys())
                
                print("------+--------------+--------------+--------------+--------------+------------+------------+--------------+------------+------------+--------------+")
                print(f"{"S.no":<5} | {"FNAME":<12} | {"LNAME":<12} | {"CONTACT":<12} | {"SUBJECT-1":<12} | {"S1-MARKS":<10} | {"S1-FEES":<10} | {"SUBJECT-2":<12} | {"S2-MARKS":<10} | {"S2-FEES":<10} | {"FACULTY":<12}")
                print("------+--------------+--------------+--------------+--------------+------------+------------+--------------+------------+------------+--------------+")

                print(f"{std_id:<5} | {students[std_id]["fname"]:<12} | {students[std_id]["lname"]:<12} | {students[std_id]["contact"]:<12} |",end="")

                for k in subjects:
                    # remember to store this in seperate variables like fees and marks for better understanding 
                    print(f"{k:<13} | {students[std_id]['subject'][k]['marks']:<10} | {students[std_id]['subject'][k]['fees']:<10} | ",end="")

                print(f"{students[std_id]["faculty"]} ")
                print("------+--------------+--------------+--------------+--------------+------------+------------+--------------+------------+------------+--------------+")
                break

            else:
                print("\nStudent not exist")
                break
        else:
            print("invalid input")
            std_id = int(input("Enter again specific student id : "))




# add marks to student (faculty)
def add_marks(students,faculty):
    for key, val in students.items():
            
        if students[key]["faculty"] == faculty:

            while True:
                std_id = input("enter a student id : ")
                
                if std_id.isdigit():
                    std_id = int(std_id)

                    if std_id in students:
                        name = students[std_id]["fname"]
                        subjects = list(students[std_id]["subject"].keys())
                        print(f"\tID : {std_id:<6}\n\tNAME : {name:<6}\n\tMARKS:")
                
                        for k in subjects:
                            sub = students[std_id]['subject'][k]

                            print(f"{"\t"}{k:<4} : {sub["marks"]} ")
                            marks = input(f"\tEnter marks for {k} : ")
                            
                            sub["marks"] = marks
                            print()
                        break
                
                    else:
                        print("\nstudent not found")
                
                else:
                    print("\nInvalid student id")

        else:
            break
    return students


# generate log file
def log_generator(name,id,operation):

    time = datetime.datetime.now()
    f = ""
    if os.path.exists("logs.txt"):
        f = open("logs.txt","a")
    else:
        f = open("logs.txt","w")

    f.write(f"{id} {name} {time} {operation}\n")    
    f.close()
    



# show log file 
def show_logs():
    file = open("logs.txt","r")
    
    print(f"{"ID":<11}{"NAME":<11}{"DATE":<12}{"TIME":<16}{"OPERATION"}")
    print("".center(61,"-"))
    lines = file.readlines()
    for line in lines:
        if not line.isspace():
            line = line.split()

            [print(word.ljust(9),end="  ") for word in line]
            print()
            print("".center(61,"-"))
    
    file.close()



# parsing data to data.json file

def add_to_json(students):

    file = open("data.json","w")
    json.dump(students, file, indent=4)
    file.close()


#loading from json file

def load_from_json(students):
    
    file = open("data.json","r")
    students = json.load(file)
    file.close()

    return students

