# Create a menu option for user input
while True:
    # Request user to select an option
    option = int(input('''Please select an option:
    1. Add a student
    2. View students: \n'''))

    if option == 1:
        # Store user input
        name = input("Enter student name: ")
        student_no = input("Enter student number: ")
        birth_day = input("Birth date: ")

        # Write data to student.txt file
        with open('students.txt', 'a') as f:
            f.write(f"{name} {student_no} {birth_day} \n")

    elif option == 2:
        # Prompt user to select a view option
        view_option = int(input('''Select an option to view:
        1. Student names
        2. Student numbers: \n'''))

        output = None
        try:
            output = open("students.txt","r")
            string = output.readlines()

            if view_option == 1:
                # View student names 
                print("Student names: ")
                for item in string:
                    list = item.split(" ")
                    print(list[0])
            
            elif view_option == 2:    
                # View student numbers
                print("Student numbers: ")
                for item in string:
                    list = item.split(" ")
                    print(list[1])

            else:
                print("Invalid selection")

            break

        except FileNotFoundError:
            print("The file that you are trying to open does not exist")

        finally:
            if output is not None:
                output.close()
        