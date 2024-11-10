# Nathanael Penuel
# Date: 11/10/2024
# Assignment: P4HW2
# This program calculates gross pay for multiple employees

# Pseudocode:
# 1. Initialize variables for total overtime pay, total regular pay, and employee count.
# 2. Start a loop to collect employee data until the user enters "Done" as the employee's name.
#    - Ask for the employee's name.
#    - If the name is "Done", exit the loop.
#    - Otherwise, ask for the hours worked and pay rate.
#    - Calculate regular hours, overtime hours, and respective pay.
#       - If hours worked are greater than 40, calculate overtime hours as (hours worked - 40)
#         and set regular hours to 40.
#       - If hours worked are 40 or less, set overtime hours to 0 and regular hours to hours worked.
#    - Calculate overtime pay as overtime hours * pay rate * 1.5.
#    - Calculate regular pay as regular hours * pay rate.
#    - Calculate gross pay as the sum of regular pay and overtime pay.
#    - Update the total overtime pay, regular pay, gross pay, and employee count.
#    - Display the calculated details for the employee.
# 3. After exiting the loop, display the total number of employees, total overtime pay, total regular pay, and total gross pay for all employees.

# Initialize 
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0
employee_count = 0

# Loop to process
while True:
    # Get employee name
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    if employee_name == "Done":
        break

    # Get hours worked and pay rate
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    # Calculate overtime and regular pay
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = regular_hours * pay_rate
    gross_pay = overtime_pay + regular_pay

    # Update
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Display 
    print("\nEmployee name: ", employee_name)
    print("Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
    print("-------------------------------------------------------------------------")
    print(f"{hours_worked:<14.1f}{pay_rate:<11.2f}{overtime_hours:<12.1f}"
          f"{overtime_pay:<14.2f}{regular_pay:<13.2f}{gross_pay:<10.2f}")
    print()

# Display summary
print("\nTotal number of employees entered:", employee_count)
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
