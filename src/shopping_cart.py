"""
Shopping Cart - YOUR TDD IMPLEMENTATION

Instructions:
1. Open tests/test_shopping_cart.py
2. Read Exercise 1
3. Run the test (it will fail - RED)
4. Come back here and write code to make it pass (GREEN)
5. Refactor if needed
6. Move to the next exercise

Remember: Only write enough code to pass the current failing test!
"""

from src.product import Product


class ShoppingCart:
    """
    A shopping cart that holds products and calculates totals.
    
    You will implement this class using TDD.
    Start with the tests in tests/test_shopping_cart.py
    """
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        # TODO: Exercise 1 - Initialize the cart
        self.items = []
        self.overall_total = 0.0
        self.discount_amount = 0.0
        self.bulk_discounts = {}
        
    def is_empty(self):
        return len(self.items) == 0
    
    def item_count(self):
        return len(self.items)
    
    def total(self):
        return round(self.overall_total, 2)
    
    def add(self, product, quantity=1):
        for _ in range(quantity):
            self.items.append(product)
    
        if product in self.bulk_discounts:
            self._recalculate_total()
        else:
            self.overall_total += product.price * quantity


    
    def contains(self, product):
        if product in self.items: return True
        return False
    
    def get_quantity(self, item):
        return self.items.count(item)
    
    def remove(self, product, quantity=1):
        removed = 0
        if product not in self.items:
            raise ValueError("Product not in cart")
        while product in self.items and removed < quantity:
            self.items.remove(product)
            self.overall_total -= product.price
            removed += 1
    
    def clear(self):
        self.items.clear()
        self.overall_total = 0

    
    def apply_discount(self, percent):
        if percent < 0 or percent > 100:
            raise ValueError("Discount must be between 0 and 100.")

        if not hasattr(self, "original_total"):
            self.original_total = self.overall_total

        discount_amount = self.original_total * (percent / 100)
        self.overall_total = self.original_total - discount_amount
    
    def remove_discount(self):
        self.overall_total = self.original_total + self.discount_amount

    def set_bulk_discount(self, product, buy_quantity, free_quantity):
        self.bulk_discounts[product] = {
        "buy": buy_quantity,
        "free": free_quantity
    }
        
    def _apply_bulk_discount(self, product):
    
        info = self.bulk_discounts[product]
        buy = info["buy"]
        free = info["free"]
    
        qty = self.get_quantity(product)
 
        cycle_size = buy + free
        free_items = (qty // cycle_size) * free

        total_price = product.price * (qty - free_items)

        self._recalculate_total()

    def _recalculate_total(self):
        total = 0
        for product in set(self.items):
            qty = self.get_quantity(product)
            if product in self.bulk_discounts:
                info = self.bulk_discounts[product]
                buy = info["buy"]
                free = info["free"]
                cycle_size = buy + free
                free_items = (qty // cycle_size) * free
                total += product.price * (qty - free_items)
            else:
                total += product.price * qty
        self.overall_total = total  


