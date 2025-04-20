from bs4 import BeautifulSoup

html_doc = """
<html>
  <body>
    <div class="product">
      <h2>Widget X</h2>
      <p class="price">$19.99</p>
      <p class="stock">In stock</p>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html_doc, "html.parser")
product = soup.find(class_="product")

# Navigate DOM
price = product.find(class_="price").text
stock = product.find(class_="stock").find_next_sibling().text
print(f"Price: {price}, Stock: {stock}")