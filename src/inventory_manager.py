import pandas as pd
from src.product import Product

class InventoryManager:
    """
    Handles all inventory operations like add, update, delete
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.load_inventory()

    def load_inventory(self):
        """
        Load inventory data from CSV file
        """
        self.df = pd.read_csv(self.file_path)

    def save_inventory(self):
        """
        Save inventory back to CSV file
        """
        self.df.to_csv(self.file_path, index=False)

    def view_products(self):
        """
        Display all products
        """
        print("\nCurrent Inventory:")
        print(self.df)

    def add_product(self, product: Product):
        """
        Add a new product to inventory
        """
        self.df = pd.concat([self.df, pd.DataFrame([product.to_dict()])], ignore_index=True)
        self.save_inventory()
        print("Product added successfully.")

    def update_quantity(self, product_id, new_quantity):
        """
        Update quantity of an existing product
        """
        self.df.loc[self.df["product_id"] == product_id, "quantity"] = new_quantity
        self.save_inventory()
        print("Quantity updated successfully.")

    def delete_product(self, product_id):
        """
        Remove a product from inventory
        """
        self.df = self.df[self.df["product_id"] != product_id]
        self.save_inventory()
        print("Product deleted successfully.")

