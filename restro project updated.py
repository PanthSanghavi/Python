menu = {}

def create_menu(category_name=None):
    if category_name is None:
        category_name = input("Enter category name: ")

    dish_quantity = int(input("Enter dish quantity: "))

    dish_details = []
    for _ in range(dish_quantity):
        dish_name = input("Enter dish name: ")
        dish_price = float(input("Enter dish price: "))
        dish_details.append({"name": dish_name, "price": dish_price})

    confirm = input("Confirm dish (yes/no): ")
    if confirm.lower() == "yes":
        if category_name in menu:
            menu[category_name].extend(dish_details)
        else:
            menu[category_name] = dish_details

        add_more = input("Do you want to add more dishes? (yes/no): ")
        if add_more.lower() == "yes":
            create_menu(category_name)  # Pass the category name as an argument
        else:
            print("Menu updated successfully.")
    else:
        print("Dish not added.")

def update_menu():
    category_name = input("Enter category name to update: ")
    if category_name in menu:
        print("Current dishes in", category_name, "category:")
        for i, dish in enumerate(menu[category_name], start=1):
            print(f"{i}. {dish['name']} (Price: {dish['price']})")
        dish_indices = input("Enter the dish numbers to update: ")
        dish_indices = [int(index.strip()) for index in dish_indices.split(",") if index.strip().isdigit()]
        dish_indices = list(set(dish_indices))

        dish_details = []
        for index in dish_indices:
            if 0 < index <= len(menu[category_name]):
                dish_name = input(f"Enter new dish name for dish {index}: ")
                dish_price = float(input(f"Enter new dish price for dish {index}: "))
                dish_details.append({"name": dish_name, "price": dish_price})

        confirm = input("Confirm dish update (yes/no): ")
        if confirm.lower() == "yes":
            for index, dish_detail in zip(dish_indices, dish_details):
                menu[category_name][index - 1] = dish_detail
            print("Menu updated successfully.")
        else:
            print("Dish not updated.")
    else:
        print("Category not found.")

def delete_category():
    category_name = input("Enter category name to delete: ")
    if category_name in menu:
        confirm = input("Are you sure to delet the category (yes/no): ")
        if confirm.lower() == "yes":
            del menu[category_name]
            print("Category deleted successfully.")
        else:
            print("Category not deleted.")
    else:
        print("Category not found.")

def delete_dish():
    category_name = input("Enter category name of the dish to delete: ")
    if category_name in menu:
        print("Current dishes in", category_name, "category:")
        for i, dish in enumerate(menu[category_name], start=1):
            print(f"{i}. {dish['name']} (Price: {dish['price']})")
        dish_indices = input("Enter the dish numbers to delete: ")
        dish_indices = [int(index.strip()) for index in dish_indices.split(",") if index.strip().isdigit()]
        dish_indices = list(set(dish_indices))
        
        dish_indices.sort(reverse=True)
        for index in dish_indices:
            if 0 < index <= len(menu[category_name]):
                del menu[category_name][index - 1]

        print("Dish deleted successfully.")
    else:
        print("Category not found.")

def view_menu():
    print("Current Menu:")
    for category, dishes in menu.items():
        print(category + ":")
        for i, dish in enumerate(dishes, start=1):
            print(f"{i}. {dish['name']} (Price: {dish['price']})")

while True:
    print("\nWelcome to Savan Restaurants!")
    print("1. Create Menu")
    print("2. Update Menu")
    print("3. Delete Category")
    print("4. Delete Dish")
    print("5. View Menu")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        create_menu()
    elif choice == "2":
        update_menu()
    elif choice == "3":
        delete_category()
    elif choice == "4":
        delete_dish()
    elif choice == "5":
        view_menu()
    elif choice == "6":
        print("Thank you for using Savan Restaurants. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")  