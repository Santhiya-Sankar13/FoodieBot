# FoodieBot - Food Recommendation and Ordering Chatbot

print("====================================")
print("        Welcome to FoodieBot!")
print("====================================")
print("I can help you choose food and place an order.\n")

menu = {
    "south indian": {
        "idli": 50,
        "dosa": 80,
        "pongal": 70,
        "vada": 40
    },
    "north indian": {
        "paneer butter masala": 180,
        "naan": 50,
        "chole bhature": 120,
        "aloo paratha": 100
    },
    "fast food": {
        "burger": 150,
        "pizza": 250,
        "french fries": 100,
        "sandwich": 120
    },
    "chinese": {
        "fried rice": 140,
        "noodles": 130,
        "manchurian": 160,
        "spring roll": 100
    }
}

cart = {}

while True:
    print("\nWhat would you like to do?")
    print("1. Get food recommendations")
    print("2. View menu")
    print("3. Order food")
    print("4. View cart")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Food recommendation
    if choice == "1":
        print("\nAvailable food types:")
        print("1. South Indian")
        print("2. North Indian")
        print("3. Fast Food")
        print("4. Chinese")

        food_type = input("What type of food do you like? ").lower()

        if food_type in menu:
            print("\nFood recommendations:")
            for food, price in menu[food_type].items():
                print(f"- {food.title()} - ₹{price}")
        else:
            print("Sorry, that food type is not available.")

    # Display menu
    elif choice == "2":
        print("\n========== FOOD MENU ==========")

        for category, foods in menu.items():
            print(f"\n{category.upper()}")

            for food, price in foods.items():
                print(f"{food.title()} - ₹{price}")

    # Order food
    elif choice == "3":
        food_name = input("Enter the food you want to order: ").lower()

        found = False

        for category in menu:
            if food_name in menu[category]:
                price = menu[category][food_name]

                try:
                    quantity = int(input("Enter quantity: "))

                    if quantity <= 0:
                        print("Quantity must be greater than zero.")
                    else:
                        cart[food_name] = cart.get(food_name, 0) + quantity

                        print(
                            f"{quantity} x {food_name.title()} "
                            f"added to your cart."
                        )

                except ValueError:
                    print("Please enter a valid quantity.")

                found = True
                break

        if not found:
            print("Sorry, this food is not available.")

    # View cart
    elif choice == "4":
        print("\n========== YOUR CART ==========")

        if not cart:
            print("Your cart is empty.")
        else:
            total = 0

            for food, quantity in cart.items():

                for category in menu:
                    if food in menu[category]:
                        price = menu[category][food]
                        item_total = price * quantity
                        total += item_total

                        print(
                            f"{food.title()} x {quantity} "
                            f"= ₹{item_total}"
                        )

            print("-------------------------------")
            print(f"Total Amount: ₹{total}")

            confirm = input("Do you want to place the order? (yes/no): ")

            if confirm.lower() == "yes":
                print("\nOrder placed successfully!")
                print("Thank you for ordering with FoodieBot!")
                cart.clear()
            else:
                print("Order not placed.")

    # Exit
    elif choice == "5":
        print("\nThank you for using FoodieBot!")
        print("Have a delicious day!")
        break

    else:
        print("Invalid choice. Please try again.")
