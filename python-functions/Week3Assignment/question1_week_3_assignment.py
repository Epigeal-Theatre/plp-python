"""_
QUESTION 1
Submit a github repo link for the assignment below


Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.

"""

def calculate_discount(price, discount_percent):
    if discount_percent >=20:
            discounted_price =  price * (1 - discount_percent /100)
    else:
        return price
    return discounted_price


solution=calculate_discount(500,20)
print("And the answer is:",solution)

