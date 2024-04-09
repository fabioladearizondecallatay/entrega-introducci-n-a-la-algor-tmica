#No, este algoritmo no es adecuado para calcular el área de un triángulo rectángulo si se proporcionan las medidas de sus dos lados perpendiculares (catetos).

def calculate_triangle_area_rectangular(side1, side2):
    # Calculate the length of the hypotenuse using the Pythagorean theorem
    hypotenuse = (side1 ** 2 + side2 ** 2) ** 0.5
    
    # Calculate the area of the triangle using the formula: area = (base * height) / 2
    area = (side1 * side2) / 2
    return area

# Ask the user to input the lengths of the two perpendicular sides (catetos)
side1_length = float(input("Enter the length of the first perpendicular side (cateto): "))
side2_length = float(input("Enter the length of the second perpendicular side (cateto): "))

# Calculate the area of the triangle using the calculate_triangle_area_rectangular function
triangle_area_rectangular = calculate_triangle_area_rectangular(side1_length, side2_length)

# Display the result to the user
print("The area of the right triangle is:", triangle_area_rectangular)
