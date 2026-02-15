"""
Product class - A completed example for students to reference.

This class was developed using TDD. See tests/test_product.py for the tests
that drove this implementation.
"""


class Product:
    """
    Represents a product that can be added to a shopping cart.
    
    Attributes:
        name (str): The name of the product
        price (float): The price of the product (must be non-negative)
        category (str): Optional category for discount purposes
    """
    
    def __init__(self, name: str, price: float, category: str = "general"):
        """
        Create a new product.
        
        Args:
            name: The product name (cannot be empty)
            price: The product price (must be >= 0)
            category: Optional category (default: "general")
            
        Raises:
            ValueError: If price is negative or name is empty
        """
        if not name or not name.strip():
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        
        self.name = name.strip()
        self.price = float(price)
        self.category = category
    
    def __repr__(self):
        return f"Product('{self.name}', ${self.price:.2f})"
    
    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price
    
    def __hash__(self):
        return hash((self.name, self.price))
