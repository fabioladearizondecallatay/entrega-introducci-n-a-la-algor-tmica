def calculate_price_with_taxes(price_without_taxes, tax_percentage):
    
    #calcula el porcentage de IV
    tax_amount = price_without_taxes * (tax_percentage / 100)
    
    #suma el IVA al precio inicial
    price_with_taxes = price_without_taxes + tax_amount
    
    return price_with_taxes

    #pregunta al usuario el precio sin impuestos y el porcentage de IVA
price_without_taxes = float(input("Enter the price without taxes: "))
tax_percentage = float(input("Enter the tax percentage: "))

#precio con impuestos incluidos
price_with_taxes = calculate_price_with_taxes(price_without_taxes, tax_percentage)

print("The price with taxes included is:", price_with_taxes)
