"""
Exercise: Sales Analyzer
Create a sales analyzer that:
- Reads sales data from CSV
- Calculates total revenue per product
- Identifies best-selling items
- Exports results to new CSV
(Simulate file I/O with sample DataFrame if no file.)
"""

import pandas as pd
import os

class SalesAnalyzer:
    """Analyze sales data using pandas"""
    
    def __init__(self, csv_file="sales.csv"):
        self.csv_file = csv_file
        self.df = None
    
    def load_data(self):
        if os.path.exists(self.csv_file):
            self.df = pd.read_csv(self.csv_file)
        else:
            # Simulate with sample data
            self.df = pd.DataFrame({
                'product': ['A', 'B', 'A', 'C', 'B', 'A'],
                'units_sold': [10, 5, 7, 3, 8, 2],
                'unit_price': [2.5, 3.0, 2.5, 4.0, 3.0, 2.5]
            })
            print("Sample data loaded:")
            print(self.df)
    
    def analyze(self):
        self.df['revenue'] = self.df['units_sold'] * self.df['unit_price']
        revenue_per_product = self.df.groupby('product')['revenue'].sum().reset_index()
        best_selling = revenue_per_product.sort_values('revenue', ascending=False)
        print("\nTotal revenue per product:")
        print(revenue_per_product)
        print("\nBest-selling items:")
        print(best_selling)
        # Export to CSV
        out_file = "sales_report.csv"
        best_selling.to_csv(out_file, index=False)
        print(f"\nResults exported to {out_file}")

def main():
    print("=== Sales Analyzer ===")
    analyzer = SalesAnalyzer()
    analyzer.load_data()
    analyzer.analyze()

if __name__ == "__main__":
    main() 