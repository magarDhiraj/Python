# Exercise 18: Product Information
product = {
    "name": "Laptop",
    "brand": "Dell",
    "price": 75000,
    "quantity": 5
}

print("Product name:", product["name"])
print("Brand:", product["brand"])
print("Price:", product["price"])
print("Available quantity:", product["quantity"])

total_value = product["price"] * product["quantity"]
print("Total value:", total_value)

# Sell 2 laptops
product["quantity"] -= 2
print("Quantity after selling 2 laptops:", product["quantity"])