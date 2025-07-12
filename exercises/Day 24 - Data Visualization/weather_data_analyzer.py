"""
Exercise 2: Weather Data Analyzer
Build a weather data analyzer that:
- Displays temperature distributions (histogram)
- Compares rainfall across months (boxplot)
- Creates a heatmap of temperature correlations
(Simulate data if no file.)
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class WeatherDataAnalyzer:
    """Analyze and visualize weather data"""
    
    def __init__(self):
        # Simulate weather data
        self.temps = np.random.normal(20, 5, size=365)
        self.rainfall = np.random.gamma(2, 5, size=(12, 30))  # 12 months, 30 days each
        self.temp_matrix = np.random.normal(20, 5, size=(12, 30))
    
    def plot_temperature_histogram(self):
        plt.figure(figsize=(7, 4))
        plt.hist(self.temps, bins=30, color='skyblue', edgecolor='black')
        plt.title('Temperature Distribution')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()
    
    def plot_rainfall_boxplot(self):
        plt.figure(figsize=(8, 4))
        plt.boxplot(self.rainfall.T, labels=[f'Month {i+1}' for i in range(12)])
        plt.title('Rainfall by Month')
        plt.xlabel('Month')
        plt.ylabel('Rainfall (mm)')
        plt.tight_layout()
        plt.show()
    
    def plot_temperature_heatmap(self):
        plt.figure(figsize=(10, 4))
        plt.imshow(self.temp_matrix, aspect='auto', cmap='hot', interpolation='nearest')
        plt.colorbar(label='Temperature (°C)')
        plt.title('Temperature Correlation Heatmap')
        plt.xlabel('Day')
        plt.ylabel('Month')
        plt.tight_layout()
        plt.show()
    
    def visualize(self):
        self.plot_temperature_histogram()
        self.plot_rainfall_boxplot()
        self.plot_temperature_heatmap()

def main():
    print("=== Weather Data Analyzer ===")
    analyzer = WeatherDataAnalyzer()
    analyzer.visualize()

if __name__ == "__main__":
    main() 