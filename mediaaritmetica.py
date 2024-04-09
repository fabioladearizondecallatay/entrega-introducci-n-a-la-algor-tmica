def calculate_mean(num1, num2, num3):
    #suma los tres numeros
    total = num1 + num2 + num3
    
    #calcula la media aritmetica dividiendo entre 3
    mean = total / 3
    
    return mean

#pregunta al usuario los numeros
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

mean = calculate_mean(num1, num2, num3)

print("The arithmetic mean of the three numbers is:", mean)
