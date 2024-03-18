"""
QUESTION 2
Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.
"""
def calculate_discount(price, discount_percent):
    
    if discount_percent>=20:
        calculated_price=price*(1-discount_percent/100)
    else:
        return price
    return calculated_price

price=float(input("Enter the  price of the product: "))
discount_percent=float(input("Enter the discount percentage:"))

solution= calculate_discount(price,discount_percent)
print("And the answer is: ", solution)
    
    
    