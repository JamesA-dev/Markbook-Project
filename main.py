# Modules #
import sys
import time
import json

# Formating #
def Title(type): 
    sys.stdout.write("\033[4m"+"\033[1m"+type+"\033[0m"+"\n")

def Italics(type): 
    sys.stdout.write("\033[3m"+type+"\033[0m"+"\n")

def Bold(type): 
    sys.stdout.write("\033[1m"+type+"\033[0m"+"\n")

# Public Variables #
markbook = {}

#---------------------------------#
#            Functions            #
#---------------------------------#

# Adds a new student to the markbook #
def add_student():
    
    firstName = input("Enter student's first name: ")
    lastName = input("Enter student's last name: ")
    studentID = input("Enter student ID (5 digits): ")
    
    # Validate student ID
    if not studentID.isdigit() or len(studentID) != 5:
        Italics("\nInvalid student ID. Please enter a 5-digit numeric ID.\n")
        time.sleep(1)
        return
    elif studentID in markbook:
        Italics('\nStudentID already exists.\n')
        time.sleep(1)
        return
    #Check names
    elif not firstName or not lastName:
        Italics('\nCannot leave details blank.\n')
        time.sleep(1)
        return
    
    markbook[studentID] = {"firstName": firstName, "lastName": lastName, "marks": [], "grade": "N/A"}
    Bold("\nStudent successfully added.\n")
    time.sleep(1)
    print('-------[Student Details]-------')
    print(f'Student First Name:',firstName)
    print(f'Student Last Name:',lastName)
    print(f'Student ID:',studentID)
    print('-------------------------------\n')
    time.sleep(1)

# Enables user to add marks for a specific student #
def add_marks():

    studentID = input("Enter student ID to add marks: ")
    if studentID not in markbook:
        Italics("\nStudent not found.\n")
        time.sleep(1)
        return
    
    mark = input("Enter mark (0-100): ")
    if not mark.isdigit() or not (0 <= int(mark) <= 100):
        Italics("\nInvalid mark. Please enter a number between 0 and 100.\n")
        time.sleep(1)
        return
    
    markbook[studentID]["marks"].append(int(mark))
    Bold("\nMark added successfully.\n")

def calculate_grade(mark):
    match mark:
        case mark if mark in range(90, 101):
            return 'A'
        case mark if mark in range(74, 90):
            return 'B'
        case mark if mark in range(60, 74):
            return 'C'
        case mark if mark in range(50, 60):
            return 'D'
        case mark if mark in range(0, 50):
            return 'F'
        case _:
            return 'N/A'

# Calculates overall grade for each student
def calculate_overall_grade():
    for studentID, data in markbook.items():
        marks = data["marks"]
        if marks:
            avg_mark = round(sum(marks) / len(marks))
            grade = calculate_grade(avg_mark)
            markbook[studentID]["grade"] = grade
            Italics('\nSuccessfully Calculated.\n')
            time.sleep(1)

# Displays all the data stored in the selected markbook #
def display_markbook():

    if not markbook:
        Italics("\nMarkbook is empty.\n")
        time.sleep(1)
        return
    
    print("\n{:<10} {:<15} {:<15} {:<10} {:<10}".format("Student ID", "First Name", "Last Name", "Marks", "Grade"))
    for studentID, data in markbook.items():
        firstName = data["firstName"]
        lastName = data["lastName"]
        marks = ', '.join(map(str, data["marks"]))  # Convert list of marks to comma-separated string
        grade = data["grade"]
        print("{:<10} {:<15} {:<15} {:<10} {:<10}".format(studentID, firstName, lastName, marks, grade))
    print('\n')
    time.sleep(1)

# Saves the current markbook to a file #
def save_markbook():

    file_name = input("Enter file name to save markbook: ")
    if not file_name.strip():
        Italics("\nInvalid file name.\n")
        time.sleep(1)
        return 
    try:
        with open(file_name + ".json", "w") as file:
            json.dump(markbook, file)
        Bold("\nMarkbook saved successfully.\n")
    except Exception as e:
        Italics("\nError saving markbook:", e, "\n")
        time.sleep(1)

# Loads the current markbook from a file #
def load_markbook():

    file_name = input("Enter file name to load markbook: ")
    if not file_name.strip():
        Italics("\nInvalid file name.\n")
        time.sleep(1)
        return
    
    try:
        with open(file_name + ".json", "r") as file:
            global markbook
            markbook = json.load(file)
        Bold("\nMarkbook loaded successfully.\n")
        time.sleep(1)
    except FileNotFoundError:
        Italics("\nFile not found.\n")
        time.sleep(1)
    except Exception as e:
        Italics("\nError loading markbook:", e, "\n")
        time.sleep(1)

# Exits the user from the program #
def exit_program():
    Italics("\nExiting the program.\n")
    time.sleep(1)
    exit()

# The main menu function handling all user options and run the markbook program #
def main():
    while True:
        Title("Assesment Markbook")
        print("1. Add a new student")
        print("2. Add marks for a student")
        print("3. Calculate and store overall grade of a student")
        print("4. Display all the data stored in the markbook")
        print("5. Save the markbook to a file")
        print("6. Load the markbook from a file")
        print("7. Exit")
        
        choice = input("--")
        if choice == '1':
            add_student()
        elif choice == '2':
            add_marks()
        elif choice == '3':
            calculate_overall_grade()
        elif choice == '4':
            display_markbook()
        elif choice == '5':
            save_markbook()
        elif choice == '6':
            load_markbook()
        elif choice == '7':
            exit_program()
        else:
            Italics("\nInvalid choice. Please enter a number from 1 to 7.\n")
            time.sleep(1)

if __name__ == "__main__":
    main()