from app.db_manager import setup_db
from app.flavor_manager import add_flavor, search_flavors, add_allergen_to_flavor
from app.cart_manager import add_to_cart, view_cart
from app.customer_manager import add_customer_suggestion

def main():
    setup_db()
    while True:
        print("\nIce Cream Parlor Menu")
        print("1. Add Seasonal Flavor")
        print("2. Search Flavors")
        print("3. Add Allergen to Flavor")
        print("4. Add to Cart")
        print("5. View Cart")
        print("6. Add Customer Suggestion")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter flavor name: ")
            description = input("Enter description: ")
            allergens = input("Enter allergens (comma-separated): ")
            add_flavor(name, description, allergens)
            print("Flavor added successfully!")
        elif choice == "2":
            keyword = input("Enter keyword to search: ")
            flavors = search_flavors(keyword)
            for flavor in flavors:
                print(f"{flavor[0]}. {flavor[1]} - {flavor[2]}")
        elif choice == "3":
            flavor_id = int(input("Enter flavor ID: "))
            allergen = input("Enter allergen: ")
            add_allergen_to_flavor(flavor_id, allergen)
            print("Allergen added successfully!")
        elif choice == "4":
            flavor_id = int(input("Enter flavor ID to add to cart: "))
            add_to_cart(flavor_id)
            print("Flavor added to cart!")
        elif choice == "5":
            cart_items = view_cart()
            print("Your Cart:")
            for item in cart_items:
                print(f"- {item}")
        elif choice == "6":
            suggestion = input("Enter your flavor suggestion: ")
            allergens = input("Enter allergens (if any): ")
            add_customer_suggestion(suggestion, allergens)
            print("Suggestion added successfully!")
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
