
# Restaurant Order System

menu = {
    "Momo": 150,
    "Pizza": 350,
    "Burger": 250,
    "Chowmein": 180,
    "Fried Rice": 200,
    "Sandwich": 160,
    "Noodles": 170,
    "Coffee": 100
}

order = []
TAX_RATE = 13

def display_menu():
    print("\nRestaurant Menu")
    for item, price in menu.items():
        print(item, "- Rs.", price)

def add_item(name, quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    order.append({"item": name, "quantity": quantity})

def calculate_bill():
    subtotal = 0

    for entry in order:
        price = menu[entry["item"]]
        subtotal += price * entry["quantity"]

    tax = subtotal * TAX_RATE / 100
    total = subtotal + tax

    return subtotal, tax, total

def display_order():
    print("\nFinal Order")

    for entry in order:
        item = entry["item"]
        quantity = entry["quantity"]
        price = menu[item] * quantity
        print(item, "x", quantity, "= Rs.", price)

    subtotal, tax, total = calculate_bill()

    print("Subtotal: Rs.", round(subtotal, 2))
    print("Tax (13%): Rs.", round(tax, 2))
    print("Final Bill: Rs.", round(total, 2))

display_menu()

while True:
    name = input("\nEnter food item (or 'done'): ").strip()

    if name.lower() == "done":
        break

    try:
        item_name = next(
            item for item in menu
            if item.lower() == name.lower()
        )

        quantity = int(input("Enter quantity: "))
        add_item(item_name, quantity)
        print("Item added successfully.")

    except StopIteration:
        print("Error: Food item is not on the menu.")

    except ValueError:
        print("Error: Enter a valid positive whole number.")

display_order()