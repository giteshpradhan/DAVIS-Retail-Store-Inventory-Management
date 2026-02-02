from src.inventory_manager import InventoryManager
from src.product import Product
from src.analytics import InventoryAnalytics

DATA_FILE = "data/inventory.csv"

inventory = InventoryManager(DATA_FILE)
analytics = InventoryAnalytics(DATA_FILE)

while True:
    print("\n--- Retail Inventory Management ---")
    print("1. View Products")
    print("2. Add Product")
    print("3. Update Product Quantity")
    print("4. Delete Product")
    print("5. View Analytics")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        inventory.view_products()

    elif choice == "2":
        pid = int(input("Product ID: "))
        name = input("Name: ")
        category = input("Category: ")
        price = float(input("Price: "))
        qty = int(input("Quantity: "))
        product = Product(pid, name, category, price, qty)
        inventory.add_product(product)

    elif choice == "3":
        pid = int(input("Product ID: "))
        qty = int(input("New Quantity: "))
        inventory.update_quantity(pid, qty)

    elif choice == "4":
        pid = int(input("Product ID: "))
        inventory.delete_product(pid)

    elif choice == "5":
        print("\nTotal Inventory Value: ₹", analytics.total_inventory_value())
        print("\nLow Stock Products:")
        print(analytics.low_stock_products())
        print("\nCategory Summary:")
        print(analytics.category_summary())

    elif choice == "6":
        print("Exiting system...")
        break

    else:
        print("Invalid choice. Try again.")
