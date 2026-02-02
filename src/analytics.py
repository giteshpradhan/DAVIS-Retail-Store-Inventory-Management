import pandas as pd

class InventoryAnalytics:
    """
    Performs basic analytics on inventory data
    """

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def total_inventory_value(self):
        """
        Calculate total inventory value
        """
        self.df["value"] = self.df["price"] * self.df["quantity"]
        return self.df["value"].sum()

    def low_stock_products(self, threshold=10):
        """
        Identify products with low stock
        """
        return self.df[self.df["quantity"] < threshold]

    def category_summary(self):
        """
        Category-wise stock summary
        """
        return self.df.groupby("category")["quantity"].sum()
