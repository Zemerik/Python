"""
Exercise 1: Sales Report Visualization
Create a sales report visualization that:
- Shows monthly sales trends (line plot)
- Compares product performance (bar chart)
- Highlights top-selling days (scatter plot)
(Simulate data if no file.)
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class SalesReportVisualization:
    """Visualize sales data with matplotlib"""
    
    def __init__(self):
        # Simulate sales data
        self.months = [f"2024-{m:02d}" for m in range(1, 13)]
        self.sales = np.random.randint(1000, 5000, size=12)
        self.products = ['A', 'B', 'C']
        self.product_sales = np.random.randint(5000, 20000, size=3)
        self.days = np.arange(1, 31)
        self.daily_sales = np.random.randint(100, 1000, size=30)
    
    def plot_monthly_trends(self):
        plt.figure(figsize=(8, 4))
        plt.plot(self.months, self.sales, marker='o')
        plt.title('Monthly Sales Trends')
        plt.xlabel('Month')
        plt.ylabel('Sales')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    def plot_product_performance(self):
        plt.figure(figsize=(6, 4))
        plt.bar(self.products, self.product_sales, color=['#4caf50', '#2196f3', '#ff9800'])
        plt.title('Product Performance')
        plt.xlabel('Product')
        plt.ylabel('Total Sales')
        plt.tight_layout()
        plt.show()
    
    def plot_top_selling_days(self):
        plt.figure(figsize=(8, 4))
        plt.scatter(self.days, self.daily_sales, c='red', label='Sales')
        plt.title('Top-Selling Days')
        plt.xlabel('Day of Month')
        plt.ylabel('Sales')
        plt.legend()
        plt.tight_layout()
        plt.show()
    
    def visualize(self):
        self.plot_monthly_trends()
        self.plot_product_performance()
        self.plot_top_selling_days()

def main():
    print("=== Sales Report Visualization ===")
    viz = SalesReportVisualization()
    viz.visualize()

if __name__ == "__main__":
    main() 