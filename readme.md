# Employee Database Manager

## 📌 Overview

The Employee Database Manager is a Python console application that allows users to manage employee records stored in a CSV file.
It supports CRUD operations (Create, Read, Update, Delete) and includes performance metric calculations using Python’s math module.

The project demonstrates practical file handling, input validation, data processing, and modular programming techniques in Python.

## ✨ Features
✅ 1. Add New Employee Records

Accepts multiple entries at once

Ensures employee IDs are numeric and unique

Ensures salary input is numeric

✅ 2. Read / Display All Records

Reads all data from Employee.csv

Displays it in a clean, formatted table

✅ 3. Update Salary by Employee ID

Searches for a matching ID

Updates only the salary field

Rewrites the entire CSV to maintain consistency

✅ 4. Delete Employee Record

Deletes a record matching the given ID

Automatically rewrites the file

✅ 5. Performance Metrics Calculation

For each employee:

Performance Index → sqrt(salary / 100)

Estimated Bonus → ceil(salary × 5.5%)

Clean, formatted output table

✅ 6. Fully Menu-Driven CLI

Intuitive text-based interface

Error handling for invalid input

## 🛠 Technologies / Tools Used

Python 3.x

Modules:

csv (file handling)

os (file existence check)

math (bonus + performance calculations)

## 📥 Installation & Running the Project
1. Clone or Download the Project
git clone <your-repo-url>
cd your-project-folder

2. Make Sure Python Is Installed

Check version:

python --version

3. Run the Program
python main.py


(Or whatever your file name is — ensure the script above is saved as main.py.)

## 🧪 Instructions for Testing
➡️ Test 1: Adding Records

Choose option 1

Enter number of employees

Provide valid ID, name, salary, and designation

Verify entries appear in Employee.csv

➡️ Test 2: Reading Records

Choose option 2

Ensure table format is correct

Confirm values match the CSV

➡️ Test 3: Update Salary

Choose option 3

Enter an existing Employee ID

Enter a new salary

Verify changes using Read option or by checking the CSV file

➡️ Test 4: Delete Record

Choose option 4

Enter a valid ID

Confirm deletion via Read or CSV

➡️ Test 5: Performance Metrics

Choose option 5

Verify performance index and bonus values

➡️ Test 6: Error Handling

Enter non-numeric IDs

Enter invalid choices

Input alphabetic salary

Try updating/deleting IDs that do not exist

## Screenshots:
1. Main Menu: ![alt text](image.png)
2. Add employee screen: ![alt text](image-1.png)
3. View results: ![alt text](image-3.png)
4. Delete Operation: ![alt text](image-2.png)



