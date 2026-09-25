list1=[]

def add_student():
    Student_id=input("enter a ID :")

    for student in list1:
        if student["Id"]==Student_id:
            print("student Id already exists")
            return

    Name=input("Enter name:")
    Age=int(input("enter a age :"))
    Course=input("enter a course :")

    dict1={"Id":Student_id, "name":Name, "age":Age, "course":Course}
    list1.append(dict1)
    print("Student", Name, "added successfully!")
   
def display_students():
    print("---Student List--")
    for x in list1:
        print("ID:",x["Id"]," , Name:",x["name"]," , Age:",x["age"]," , Course:",x["course"])

        if "marks" in x:
            print("Marks:", x["marks"])

def update_student():
    Student_id = input("enter a Student ID to update: ")

    found = False

    for student in list1:
        if student["Id"] == Student_id:
            print("Student Found")

            Name = input("Enter new name (leave blank to skip): ")
            Age = input("enter new age (leave blank to skip): ")
            Course = input("enter new course (leave blank to skip): ")

            if Name != "":
                student["name"] = Name

            if Age != "":
                student["age"] = int(Age)

            if Course != "":
                student["course"] = Course

            print("Student updated successfully!")
            found = True
            break

    if found == False:
        print("Student ID not found")
        
def add_student_marks():
    Student_id = input("enter a Student ID to add marks: ")

    found = False

    for student in list1:
        if student["Id"] == Student_id:


            while True:
                math = int(input("Enter marks for Math: "))

                if 0 <= math <= 100:
                    break
                else:
                    print("Invalid marks. Enter marks between 0 and 100.")

            while True:
                science = int(input("Enter marks for Science: "))

                if 0 <= science <= 100:
                    break
                else:
                    print("Invalid marks. Enter marks between 0 and 100.")
            while True:
                english = int(input("Enter marks for english: "))
            
                if 0 <= english <= 100:
                    break
                else:
                    print("Invalid marks. Enter marks between 0 and 100.")
            while True:
                computer = int(input("Enter marks for computer: "))
            
                if 0 <= computer <= 100:
                    break
                else:
                    print("Invalid marks. Enter marks between 0 and 100.")
            while True:
                history = int(input("Enter marks for history: "))
            
                if 0 <= history <= 100:
                    break
                else:
                    print("Invalid marks. Enter marks between 0 and 100.")

            marks = {
                "Math": math,
                "Science": science,
                "English": english,
                "Computer": computer,
                "History": history
            }

            student["marks"] = marks

            
            print("Marks", student["name"], "added successfully!")
            found = True
            break

    if found == False:
        print("Student ID not found")
                  
def delete_student():
    Student_id = input("enter a Student ID to delete: ")

    found = False

    for student in list1:
        if student["Id"] == Student_id:
            list1.remove(student)
            print("Student ID", Student_id, "deleted successfully")

            found = True
            break

    if found == False:
        print("Student ID not found")
        
while True:
    print("Menu")
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Add Marks to Student")
    print("6. Exit")

    var1=int(input("enter your choice: "))
    if var1==1:
        add_student()
    elif var1==2:
        display_students()
    elif var1==3:
        update_student()
    elif var1==4:
        delete_student()
    elif var1==5:
        add_student_marks()
    elif var1==6:
        print("Exiting Student Management System. Goodbye!")
        break
    else:
        print("Invalid number")
        
        
    
