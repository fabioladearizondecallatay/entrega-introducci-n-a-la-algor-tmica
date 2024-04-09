def calculate_weighted_mean(nums, weights):
    #un error si 
    if len(nums) != len(weights):
        raise ValueError("The lengths of the numbers and weights lists must be equal.")
    
    # Calculate the weighted sum
    weighted_sum = sum(num * weight for num, weight in zip(nums, weights))
    
    # Calculate the total weight
    total_weight = sum(weights)
    
    # Calculate the weighted mean
    weighted_mean = weighted_sum / total_weight
    
    return weighted_mean

# Ask the user to input the three numbers
nums = []
weights = []
for i in range(3):
    num = float(input(f"Enter number {i+1}: "))
    nums.append(num)
    weight = float(input(f"Enter the weight for number {i+1}: "))
    weights.append(weight)

# Calculate the weighted mean using the calculate_weighted_mean function
weighted_mean = calculate_weighted_mean(nums, weights)

# Display the result to the user
print("The weighted mean of the three numbers is:", weighted_mean)
