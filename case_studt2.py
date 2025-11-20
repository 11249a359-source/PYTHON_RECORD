inventory = {
    "Laptop": (1200, 10),
    "Mouse": (25, 50),
    "Keyboard": (75, 20)
}

def add_product(product_name, price, quantity):
    inventory[product_name] = (price, quantity)
    print(f"Product '{product_name}' added.")

def update_quantity(product_name, new_quantity):
    if product_name in inventory:
        price, _ = inventory[product_name]
        inventory[product_name] = (price, new_quantity)
        print(f"Quantity of '{product_name}' updated to {new_quantity}.")
    else:
        print("Product not found.")

def list_products():
    print("Current Inventory:")
    for product, details in inventory.items():
        price, quantity = details
        print(f"- {product}: Price=${price}, Quantity={quantity}")

add_product("Monitor", 300, 15)
update_quantity("Laptop", 8)
list_products()


# Case Study 3: Unique User Tags System
user_tags = {
    "U001": {"admin", "developer", "tester"},
    "U002": {"developer", "frontend"},
    "U003": {"tester"}
}

def add_tag_to_user(user_id, tag):
    if user_id in user_tags:
        user_tags[user_id].add(tag)
        print(f"Tag '{tag}' added to user '{user_id}'.")
    else:
        print("User not found.")

def check_user_has_tag(user_id, tag):
    if user_id in user_tags:
        if tag in user_tags[user_id]:
            print(f"User '{user_id}' HAS tag '{tag}'.")
            return True
        else:
            print(f"User '{user_id}' DOES NOT have tag '{tag}'.")
            return False
    else:
        print("User not found.")
        return False

add_tag_to_user("U001", "backend")
check_user_has_tag("U002", "developer")
check_user_has_tag("U003", "admin")
