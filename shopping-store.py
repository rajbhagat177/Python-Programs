print("Welcome to our Ecommerce Store!")

# Display categories
print("\nCategories:")
print("1. Electronics")
print("2. Clothing")
print("3. Books")

# Get user's category choice
category_choice = int(input("Choose a category (1-3): "))

if category_choice == 1:
    print("\nElectronics:")
    print("1. Smartphone - $500")
    print("2. Laptop - $1000")
    print("3. Headphones - $150")
    print("4. Smartwatch - $250")
    print("5. Camera - $700")
    item_prices = [500, 1000, 150, 250, 700]

elif category_choice == 2:
    print("\nClothing:")
    print("1. T-Shirt - $20")
    print("2. Jeans - $40")
    print("3. Jacket - $80")
    print("4. Shoes - $60")
    print("5. Dress - $50")
    item_prices = [20, 40, 80, 60, 50]

elif category_choice == 3:
    print("\nBooks:")
    print("1. Novel - $15")
    print("2. Textbook - $30")
    print("3. Comic Book - $10")
    print("4. Biography - $25")
    print("5. Cookbook - $20")
    item_prices = [15, 30, 10, 25, 20]

else:
    print("Invalid category choice. Please enter a number between 1 and 3.")
    item_prices = []

# Get user's item choice if category is valid
if item_prices:
    item_choice = int(input("Choose an item (1-5): "))

    if 1 <= item_choice <= 5:
        item_price = item_prices[item_choice - 1]

        # Display price and checkout option
        print(f"\nItem price: ${item_price}")
        checkout_choice = input("\nCheckout? (yes/no): ").strip().lower()

        if checkout_choice == "yes":
            print(f"\nThank you for your purchase! Your total is ${item_price}.")
        else:
            print("\nYour item has been removed from the cart.")
    else:
        print("Invalid item choice. Please enter a number between 1 and 5.")