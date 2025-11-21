import csv
import os
import math

# Configuration
CSV_FILE = "Employee.csv"
FIELDNAMES = ["Emp_ID", "Name", "Salary", "Designation"]

def get_all_records():
    if not os.path.exists(CSV_FILE):
        return []
        
    try:
        with open(CSV_FILE, 'r', newline='') as f:
            reader = csv.DictReader(f)      # Read all rows into a list of dictionaries
            return list(reader)
    except Exception as e:
        print(f"Error reading records: {e}")
        return []

def write_all_records(records):
    try:
        with open(CSV_FILE, 'w', newline='') as f:    # 'w' mode overwrites the file, ensuring only the current data is present
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(records)
        return True
    except Exception as e:
        print(f"Error writing records: {e}")
        return False

def write_new_records():
    print("\n--- Add New Records ---")
    
    # Get existing records first
    all_records = get_all_records()
    new_records = []
    
    try:
        num_records = int(input("Enter the number of records to add: "))
    except ValueError:
        print("Invalid number entered. Please try again.")
        return

    for i in range(num_records):
        print(f"\n--- Record {i+1} ---")
        try:
            r = input("Enter Emp ID (numeric): ")
            # Ensure ID is unique and an integer
            if not r.isdigit():
                 print("Error: ID must be a number.")
                 continue
            r = int(r)
            
            # Check for existing ID
            if any(int(record['Emp_ID']) == r for record in all_records):
                print(f"Error: Employee ID {r} already exists. Skipping record.")
                continue

            n = input("Enter name: ")
            s_str = input("Enter salary (numeric): ")
            if not s_str.isdigit():
                 print("Error: Salary must be a number. Skipping record.")
                 continue
            s = int(s_str)
            d = input("Enter designation: ")
            
            # Create a dictionary for the new record
            record_data = {
                "Emp_ID": str(r), # Store as string in DictWriter/CSV
                "Name": n,
                "Salary": str(s),
                "Designation": d
            }
            new_records.append(record_data)

        except Exception as e:
            print(f"An error occurred while inputting data: {e}")
            
    # Combine existing and new records and write back to file
    if new_records:
        all_records.extend(new_records)
        if write_all_records(all_records):
            print("\nSuccessfully entered and saved the new record(s)!!")
    else:
        print("\nNo valid records were entered.")
    
def read_records():
    print("\n--- Employee Records ---")
    records = get_all_records()

    if not records:
        print("No records found in the file.")
        return

    # Print Header
    print(f"{'Emp_ID':<8} {'Name':<20} {'Salary':<10} {'Designation':<20}")
    print("-" * 60)
    
    # Print Data Rows
    for record in records:
        print(
            f"{record['Emp_ID']:<8} "
            f"{record['Name']:<20} "
            f"{record['Salary']:<10} "
            f"{record['Designation']:<20}"
        )
    print("-" * 60)

def update_record(target_id):
    print("\n--- Update Record ---")
    all_records = get_all_records()
    found = False
    
    for record in all_records:
        # ID comparison must be done carefully (string vs int)
        if record['Emp_ID'] == str(target_id):
            found = True
            try:
                new_salary_str = input(f"Enter the updated salary for ID {target_id}: ")
                if not new_salary_str.isdigit():
                    print("Error: Salary must be a valid number. Update aborted.")
                    return
                record['Salary'] = new_salary_str
                print("Salary updated successfully!")
                break
            except Exception as e:
                print(f"Error during salary input: {e}")
                return

    if not found:
        print(f"Record with ID {target_id} not found.")
        return
        
    # Rewrite the entire file with the updated records
    if write_all_records(all_records):
        print("File saved with updated salary.")
    

def delete_record(target_id):
    print("\n--- Delete Record ---")
    all_records = get_all_records()
    initial_count = len(all_records)

    # Filter the list to exclude the record with the matching ID
    # Use list comprehension to create a new list without the target record
    updated_records = [record for record in all_records if record['Emp_ID'] != str(target_id)]

    if len(updated_records) < initial_count:
        # A record was successfully removed
        if write_all_records(updated_records):
            print(f"Record with ID {target_id} has been successfully deleted.")
    else:
        # No record was removed
        print(f"Record with ID {target_id} not found.")


def calculate_performance_metrics():
    print("\n--- Performance Metrics ---")
    records = get_all_records()

    if not records:
        print("No records found to analyze.")
        return

    # Print Header
    print(f"{'Emp_ID':<8} {'Name':<20} {'Salary':<10} {'Perf. Index':<15} {'Estimated Bonus':<20}")
    print("-" * 75)

    for record in records:
        try:
            # Convert salary string to integer for calculations
            salary = int(record['Salary'])

    
            # 1. Using math.sqrt() for a conceptual 'Performance Index'
            # Index = Square root of (Salary / 100)
            performance_index = math.sqrt(salary / 100.0)

            # 2. Using math.ceil() for a conceptual 'Estimated Bonus'
            # Bonus is 5.5% of salary, rounded UP to the nearest whole number
            estimated_bonus = math.ceil(salary * 0.055)

            print(
                f"{record['Emp_ID']:<8} "
                f"{record['Name']:<20} "
                f"{record['Salary']:<10} "
                f"{performance_index:<15.2f} "   # Format Index to 2 decimal places
                f"{estimated_bonus:<20.0f}"     # Format Bonus as a whole number
            )
        except ValueError:
            print(f"Skipping record {record.get('Emp_ID', 'N/A')} due to invalid salary value (must be numeric).")
        except Exception as e:
            print(f"An error occurred during calculation: {e}")
    print("-" * 75)



#Main
def main():
    while True:
        print("\n==================================")
        print("Employee Database Manager (CSV)")
        print("==================================")
        print("Enter 1 to write new records")
        print("Enter 2 to read all records")
        print("Enter 3 to update salary by ID")
        print("Enter 4 to delete record by ID")
        print("Enter 5 to calculate performance metrics (using math module)") 
        print("Enter 6 to exit program")
        
        try:
            choice = input("Enter choice: ")
            if not choice.isdigit():
                print("Invalid choice. Please enter a number from 1 to 6.")
                continue
                
            x = int(choice)
            
            if x == 1:
                write_new_records()
            elif x == 2:
                read_records()
            elif x == 3:
                try:
                    o = int(input("Enter the Employee ID to update salary for: "))
                    update_record(o)
                except ValueError:
                    print("Invalid ID entered. Must be numeric.")
            elif x == 4:
                try:
                    k = int(input("Enter the Employee ID to delete: "))
                    delete_record(k)
                except ValueError:
                    print("Invalid ID entered. Must be numeric.")
            elif x == 5:
                calculate_performance_metrics()
            elif x == 6:
                print("Exiting program... Thank you!")
                break
            else:
                print("Enter one of the given numbers (1-6).")
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
