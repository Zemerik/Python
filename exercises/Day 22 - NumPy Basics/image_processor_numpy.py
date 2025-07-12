"""
Exercise 2: NumPy Image Processor Simulation
Build an image processor simulation that:
- Creates 3D array representing RGB image
- Applies grayscale conversion
- Implements edge detection kernel
"""

import numpy as np

class ImageProcessorNumPy:
    """Simulate image processing with NumPy arrays"""
    
    def __init__(self, height=5, width=5):
        self.height = height
        self.width = width
        # Create random RGB image (values 0-255)
        self.image = np.random.randint(0, 256, size=(height, width, 3), dtype=np.uint8)
    
    def to_grayscale(self):
        # Standard grayscale conversion
        return np.dot(self.image[...,:3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
    
    def edge_detection(self):
        # Simple Sobel kernel for edge detection (horizontal)
        kernel = np.array([[-1, 0, 1],
                          [-2, 0, 2],
                          [-1, 0, 1]])
        gray = self.to_grayscale()
        # Pad the grayscale image
        padded = np.pad(gray, 1, mode='constant')
        edges = np.zeros_like(gray)
        for i in range(1, gray.shape[0]+1):
            for j in range(1, gray.shape[1]+1):
                region = padded[i-1:i+2, j-1:j+2]
                edges[i-1, j-1] = np.clip(np.sum(region * kernel), 0, 255)
        return edges.astype(np.uint8)
    
    def display(self):
        print("Original RGB image:")
        print(self.image)
        print("\nGrayscale image:")
        print(self.to_grayscale())
        print("\nEdge detection result:")
        print(self.edge_detection())

def main():
    print("=== NumPy Image Processor Simulation ===")
    processor = ImageProcessorNumPy()
    processor.display()

if __name__ == "__main__":
    main() 