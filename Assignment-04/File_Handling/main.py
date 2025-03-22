import os

# Function to create a new file with header (if it doesn't exist)
def create_file(file_name):
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            file.write("Name, Age, Grade\n")  # Adding header
        print(f"File '{file_name}' created successfully.")
    else:
        print(f"File '{file_name}' already exists.")

# Function to add a new student record to the file
def add_student(file_name, name, age, grade):
    with open(file_name, "a") as file:  # Open in append mode
        file.write(f"{name}, {age}, {grade}\n")
    print(f"Student {name} added to the file.")

# Function to read and display all student records
def read_students(file_name):
    try:
        with open(file_name, "r") as file:
            data = file.readlines()
            if len(data) > 1:  # Skip the header
                print("Student Records:")
                for line in data[1:]:
                    print(line.strip())
            else:
                print("No student records found.")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")

# Function to search for a student by name
def search_student(file_name, search_name):
    try:
        with open(file_name, "r") as file:
            records = file.readlines()
            found = False
            for record in records[1:]:
                if search_name.lower() in record.lower():
                    print(f"Found: {record.strip()}")
                    found = True
                    break
            if not found:
                print(f"No student named '{search_name}' found.")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")

# Function to delete a student record
def delete_student(file_name, name_to_delete):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        
        with open(file_name, "w") as file:
            found = False
            for line in lines:
                if name_to_delete.lower() not in line.lower():
                    file.write(line)
                else:
                    found = True
            if found:
                print(f"Student {name_to_delete} deleted.")
            else:
                print(f"No student named '{name_to_delete}' found.")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")

# Example usage of the functions
file_name = "students.txt"


create_file(file_name)
add_student(file_name, "John Doe", 16, "A")
add_student(file_name, "Jane Smith", 15, "B")
add_student(file_name, "Emily Davis", 17, "A+")

read_students(file_name)

# Search for a student
search_student(file_name, "Jane Smith")

# Delete a student
delete_student(file_name, "Jane Smith")


read_students(file_name)
