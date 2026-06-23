inventory=[

    {
        "name": "notebook",
        "quantity": 12,
        "price" :float(1400.00)
    },

    {
        "name": "bucket",
        "quantity": 10,
        "price" :float(4400.00)
    },

    {
        "name": "computer",
        "quantity": 12,
        "price" :float(95000.00)
    }
]

while True:
    print("you can buy the following items:\nA.Add New Item \nB. View All items \nC. Update Stock\nD. Remove an item\nE. Search item by name\nF. Exit")

    choice = input("Choose between A, B, C, D, E or F: ").upper()

    if choice == "A":
        name = input("What item you want to add: ").lower()
        itemRepeated = False
        for item in inventory:
            if item["name"] == name:
                print("Item already exists in the inventory.")
                itemRepeated = True
                break
        if itemRepeated==False:
            try:
                quantity = int(input("What is the quantity of the item: "))
                price = float(input("What is the price of the item: "))
                inventory.append({"name": name, "quantity": quantity, "price": price})
                print(f"{name} has been added to the inventory.")
            except ValueError:
                print("Please type an integer for the quantity and a number for the price!")
    elif choice == "B":
        for item in inventory:
            print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}")
    elif choice == "C":
        item_changing = input("Which item do you want to update the stock for: ").lower()
        changed = False
        for item in inventory:
            if item["name"]== item_changing:
                changed = True
                item_category =input("Do you want to change the name, quantity or price: ").lower()
                if item_category == "name":
                    updated_name = input("What is the new name of the item: ").lower()
                    item["name"] = updated_name
                    break
                elif item_category == "quantity":
                    Updated_quantity = int(input("What is the new quantity of the item: "))
                    item["quantity"] = Updated_quantity
                elif item_category == "price":
                    Updated_price = float(input("What is the new price of the item: "))
                    item["price"] = Updated_price
                    break
                else:
                    print("Invalid Choice! Try again")
            if changed == False:
                print("Item not found in the inventory.")
                print("Item not found in the inventory.")
    elif choice == "D":
        delete_item = input("Which item do you want to delete: ").lower()

        deletion = False
        for item in inventory:
            if item["name"] == delete_item:
                inventory.remove(item)
                print("Deleted successfully!")
                deletion = True
                break
        if deletion == False:
            print("Item not found in the inventory.")
    elif choice == "E":
        searched=input("what is the name of the item you are looking for: ")

        is_searched = False
        for item in inventory:
            if searched in item["name"]:
                print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}")
                is_searched = True
        if is_searched == False:
            print("Item not found in the inventory.")
    elif choice == "F":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please choose between A, B, C, D, E or F.")
