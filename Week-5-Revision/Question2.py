
# Shopping Cart System

products = {
    "Laptop": {"price": 800, "quantity": 5},
    "Mouse": {"price": 20, "quantity": 10},
    "Keyboard": {"price": 35, "quantity": 8},
    "Monitor": {"price": 200, "quantity": 4},
    "Headphones": {"price": 50, "quantity": 6},
    "USB": {"price": 10, "quantity": 12}
}

cart = {}

def add_product(name, quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    if quantity > products[name]["quantity"]:
        raise ValueError("Not enough stock available.")

    products[name]["quantity"] -= quantity
    cart[name] = cart.get(name, 0) + quantity

def calculate_total():
    total = 0
    for name, quantity in cart.items():
        total += products[name]["price"] * quantity
    return total

def display_cart():
    print("\nShopping Cart")
    for name, quantity in cart.items():
        price = products[name]["price"]
        print(name, "x", quantity, "=", price * quantity)
    print("Final Bill: $", calculate_total())

print("Available Products:", list(products.keys()))

while True:
    name = input("\nEnter product name (or 'done'): ").strip()

    if name.lower() == "done":
        break

    try:
        product_name = next(
            p for p in products
            if p.lower() == name.lower()
        )

        quantity = int(input("Enter quantity: "))
        add_product(product_name, quantity)
        print("Product added successfully.")

    except StopIteration:
        print("Error: Product does not exist.")

    except ValueError as error:
        print("Error:", error)

display_cart()