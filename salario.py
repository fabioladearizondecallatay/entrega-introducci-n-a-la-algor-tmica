def calculate_overtime_amount(gross_monthly_salary, overtime_hours_worked):
    # Define the number of normal hours per month
    normal_hours_per_month = 35 * 4  # 35 hours per week, 4 weeks per month
    
    # Calculate the salary per normal hour
    normal_hourly_rate = gross_monthly_salary / normal_hours_per_month
    
    # Initialize the total amount for overtime hours
    overtime_amount = 0
    
    # Calculate the amount for overtime hours
    if overtime_hours_worked > 0:
        if overtime_hours_worked <= 7:
            overtime_amount += normal_hourly_rate * 1.25 * overtime_hours_worked
        elif overtime_hours_worked <= 8:
            overtime_amount += normal_hourly_rate * 1.25 * 7
            overtime_amount += normal_hourly_rate * 1.5 * (overtime_hours_worked - 7)
        else:
            overtime_amount += normal_hourly_rate * 1.25 * 7
            overtime_amount += normal_hourly_rate * 1.5 * (overtime_hours_worked - 8)
    
    return overtime_amount

# Ask the user to input the gross monthly salary and the number of overtime hours worked
gross_monthly_salary = float(input("Enter the gross monthly salary: "))
overtime_hours_worked = int(input("Enter the number of overtime hours worked in the month: "))

# Calculate the amount for overtime hours using the calculate_overtime_amount function
overtime_amount = calculate_overtime_amount(gross_monthly_salary, overtime_hours_worked)

# Display the result to the user
print("The amount for overtime hours to be paid is:", overtime_amount)
