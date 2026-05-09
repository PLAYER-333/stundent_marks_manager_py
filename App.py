'''
STUDENT MARKS MANAGER IN PYTHON

FUNCTIONS:
    1. Add Student
    2. View Student
    3. Check Result
    4. Exit
    
'''


students = {} #Database of Students
user_name = "Admin" 
password = "admin000"


def student_marks_manager():
    while True:

        print("\n------------ STUDENT MARKS MANAGER ------------")
        print("\nFunctions:\n")
        print("1. Add Student")
        print("2. View Student")
        print("3. Check Result")
        print("4. Exit")

        choice = int(input("\nEnter Choice: "))

        #Add Student
        if (choice==1):
            name = input("Enter Student Name: ")
            marks = int(input("Enter Student Marks: "))
            students[name] = marks
            print(f"\n{name} is SuccessFully Added into the Database")
        
    
        #View Student
        elif (choice==2):
            def view_student():
                    while True:
                        username = input("\nEnter Username: ")
                        key = input("\nEnter Password: ")
                        if username == user_name and key == password:
                            print("Login Successfull !")
                            if not students:
                                print("No Student Found!")
                                user_input = input("Want to Try Again (Y/N) ? ").lower()
                                if (user_input == "y" or user_input == "yes"):
                                    pass
                                elif (user_input == "n" or user_input == "no"):
                                    print("Exit....")
                                    break
                            else:
                                print("\nStudents List: ")
                                for name,marks in students.items():
                                    print(name , ":" , marks)
                                print("Exit....")
                                return True
                        else:
                            print("Incorrect Username & Password Try Again ")
                            user_input = input("Want to Try Again (Y/N) ? ").lower()
                            if (user_input == "y" or user_input == "yes"):
                                return False
                            elif (user_input == "n" or user_input == "no"):
                                break
            view_student()
                        

        #View Result
        elif (choice==3):
            def student_result():
                while True:
                    username = input("\nEnter Username: ")
                    key = input("\nEnter Password: ")
                    if username == user_name and key == password:
                        print("\nLogin Successfull")
                        name = input("\nEnter Name: ")
                        if name in students:
                            marks = students[name]
                    
                            if 80 <= marks <= 100:
                                print("\nResult: PASS\nGrade: A+")

                            elif 65 <= marks <= 79:
                                print("\nResult: PASS\nGrade: A")

                            elif 50 <= marks <= 64:
                                print("\nResult: PASS\nGrade: B+")

                            elif 40 <= marks <= 49:
                                print("\nResult: PASS\nGrade: B")

                            elif 34 <= marks <= 39:
                                print("\nResult: PASS\nGrade: C")

                            elif 20 <= marks <= 33:
                                print("\nResult: PASS\nGrade: D")

                            elif 0 <= marks < 20:
                                print("\nResult: FAIL\nGrade: -")
                    
                            else:
                                print("\nInvalid Marks")
                                return False
                        else:
                            print(f"\nNo Student Named {name} Found in Database")
            
                    else:
                        print("Incorrect Username & Password")

            student_result()


         #Exit Option
        elif (choice==4):
            print("\nExit....")
            break

        else:
            print("Invalid Choice")
            return False


student_marks_manager()