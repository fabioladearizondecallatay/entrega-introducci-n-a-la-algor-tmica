def calculate_triangle_area(base, height):
    # Calculate the area of the triangle using the formula: area = (base * height) / 2
    area = (base * height) / 2
    return area

# Ask the user to input the length of the base and the height
base_length = float(input("Enter the length of the base of the triangle: "))
height_length = float(input("Enter the length of the height relative to the base: "))

# Calculate the area of the triangle using the calculate_triangle_area function
triangle_area = calculate_triangle_area(base_length, height_length)

# Display the result to the user
print("The area of the triangle is:", triangle_area)
