def calculate_interest(capital, interest_rate, time_months):
    #calcula el interes 
    interest_amount = capital * (interest_rate / 100) * (time_months / 12)
    return interest_amount

#pregunta al usuario el capital invertido, el interes dado y el tiempo
capital = float(input("Enter the capital amount: "))
interest_rate = float(input("Enter the interest rate (in percentage): "))
time_months = int(input("Enter the time period (in months): "))

interest_amount = calculate_interest(capital, interest_rate, time_months)

print("The interest amount generated is:", interest_amount)
