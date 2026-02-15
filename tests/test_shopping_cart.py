"""
Shopping Cart Tests - YOUR TDD EXERCISES

=============================================================================
HOW TO USE THIS FILE
=============================================================================

1. Tests are organized into EXERCISES (1-7)
2. Each exercise has tests that are initially SKIPPED
3. Work through exercises IN ORDER:
   a. Remove the @pytest.mark.skip decorator from ONE test
   b. Run pytest - watch it FAIL (RED)
   c. Write code in src/shopping_cart.py to make it PASS (GREEN)
   d. Refactor if needed
   e. Move to the next test

Run tests with: pytest tests/test_shopping_cart.py -v

TIP: Run a single exercise with: pytest -k "Exercise1" -v

=============================================================================
"""

import pytest
from src.product import Product
from src.shopping_cart import ShoppingCart


# =============================================================================
# EXERCISE 1: Empty Cart (Difficulty: ⭐)
# =============================================================================

class TestExercise1_EmptyCart:
    """Start here! Remove @pytest.mark.skip one test at a time."""
    
    
    def test_new_cart_is_empty(self):
        """A newly created cart should have no items."""
        cart = ShoppingCart()
        assert cart.is_empty() == True
    
    
    def test_new_cart_has_zero_items(self):
        """A newly created cart should have item_count of 0."""
        cart = ShoppingCart()
        assert cart.item_count() == 0
    
    
    def test_new_cart_has_zero_total(self):
        """A newly created cart should have total of 0."""
        cart = ShoppingCart()
        assert cart.total() == 0.0


# =============================================================================
# EXERCISE 2: Adding Products (Difficulty: ⭐)
# =============================================================================

class TestExercise2_AddingProducts:
    """Now let's add products to our cart!"""
    
    
    def test_add_single_product(self):
        """Adding a product should increase item count."""
        cart = ShoppingCart()
        apple = Product("Apple", 1.50)
        cart.add(apple)
        assert cart.item_count() == 1
        assert cart.is_empty() == False
    
    
    def test_add_multiple_different_products(self):
        """Adding multiple products should increase item count accordingly."""
        cart = ShoppingCart()
        apple = Product("Apple", 1.50)
        banana = Product("Banana", 0.75)
        cart.add(apple)
        cart.add(banana)
        assert cart.item_count() == 2
    
    
    def test_cart_contains_added_product(self):
        """Cart should be able to check if it contains a product."""
        cart = ShoppingCart()
        apple = Product("Apple", 1.50)
        orange = Product("Orange", 2.00)
        cart.add(apple)
        assert cart.contains(apple) == True
        assert cart.contains(orange) == False


# =============================================================================
# EXERCISE 3: Calculating Total (Difficulty: ⭐⭐)
# =============================================================================

class TestExercise3_CalculatingTotal:
    """Time to calculate money!"""
    

    def test_total_with_single_item(self):
        """Total should equal the price of a single item."""
        cart = ShoppingCart()
        apple = Product("Apple", 1.50)
        cart.add(apple)
        assert cart.total() == 1.50
    

    def test_total_with_multiple_items(self):
        """Total should be sum of all item prices."""
        cart = ShoppingCart()
        cart.add(Product("Apple", 1.50))
        cart.add(Product("Banana", 0.75))
        cart.add(Product("Orange", 2.00))
        assert cart.total() == 4.25
    
    
    def test_total_rounds_to_two_decimal_places(self):
        """Total should be rounded to 2 decimal places (cents)."""
        cart = ShoppingCart()
        cart.add(Product("Item1", 0.1))
        cart.add(Product("Item2", 0.2))
        assert cart.total() == 0.30


# =============================================================================
# EXERCISE 4: Quantities (Difficulty: ⭐⭐)
# =============================================================================

class TestExercise4_Quantities:
    """Real carts need to handle '3 apples' not just 'apple, apple, apple'"""
    
    
    def test_add_product_with_quantity(self):
        """Should be able to add multiple of the same product at once."""
        cart = ShoppingCart()
        apple = Product("Apple", 1.50)
        cart.add(apple, quantity=3)
        assert cart.item_count() == 3
    

    def test_total_reflects_quantity(self):
        """Total should account for quantities."""
        cart = ShoppingCart()
        apple = Product("Apple", 1.50)
        cart.add(apple, quantity=4)
        assert cart.total() == 6.00
    
    
    def test_adding_same_product_increases_quantity(self):
        """Adding the same product twice should combine quantities."""
        cart = ShoppingCart()
        apple = Product("Apple", 1.50)
        cart.add(apple, quantity=2)
        cart.add(apple, quantity=3)
        assert cart.item_count() == 5
        assert cart.total() == 7.50
    
    
    def test_get_quantity_of_product(self):
        """Should be able to check quantity of a specific product."""
        cart = ShoppingCart()
        apple = Product("Apple", 1.50)
        orange = Product("Orange", 2.00)
        cart.add(apple, quantity=3)
        cart.add(orange, quantity=2)
        assert cart.get_quantity(apple) == 3
        assert cart.get_quantity(orange) == 2
    
    
    def test_get_quantity_of_missing_product_returns_zero(self):
        """Getting quantity of product not in cart should return 0."""
        cart = ShoppingCart()
        apple = Product("Apple", 1.50)
        assert cart.get_quantity(apple) == 0


# =============================================================================
# EXERCISE 5: Removing Products (Difficulty: ⭐⭐)
# =============================================================================

class TestExercise5_RemovingProducts:
    """Customers change their minds - let them remove items!"""
    
    
    def test_remove_product_decreases_count(self):
        """Removing a product should decrease item count."""
        cart = ShoppingCart()
        apple = Product("Apple", 1.50)
        cart.add(apple, quantity=3)
        cart.remove(apple)
        assert cart.item_count() == 2
    
    
    def test_remove_product_with_quantity(self):
        """Should be able to remove specific quantity."""
        cart = ShoppingCart()
        apple = Product("Apple", 1.50)
        cart.add(apple, quantity=5)
        cart.remove(apple, quantity=3)
        assert cart.item_count() == 2
    
    
    def test_remove_all_of_product(self):
        """Removing all of a product should remove it completely."""
        cart = ShoppingCart()
        apple = Product("Apple", 1.50)
        cart.add(apple, quantity=3)
        cart.remove(apple, quantity=3)
        assert cart.contains(apple) == False
        assert cart.item_count() == 0
    
    
    def test_remove_more_than_available_removes_all(self):
        """Removing more than available should just remove all."""
        cart = ShoppingCart()
        apple = Product("Apple", 1.50)
        cart.add(apple, quantity=2)
        cart.remove(apple, quantity=10)
        assert cart.contains(apple) == False
    
    
    def test_remove_product_not_in_cart_raises_error(self):
        """Trying to remove a product not in cart should raise ValueError."""
        cart = ShoppingCart()
        apple = Product("Apple", 1.50)
        with pytest.raises(ValueError) as exc_info:
            cart.remove(apple)
        assert "not in cart" in str(exc_info.value).lower()
    
    
    def test_clear_cart(self):
        """Should be able to clear all items from cart."""
        cart = ShoppingCart()
        cart.add(Product("Apple", 1.50), quantity=2)
        cart.add(Product("Banana", 0.75), quantity=3)
        cart.clear()
        assert cart.is_empty() == True
        assert cart.total() == 0


# =============================================================================
# EXERCISE 6: Discounts (Difficulty: ⭐⭐⭐)
# =============================================================================

class TestExercise6_Discounts:
    """Everyone loves a good discount!"""
    
    def test_apply_percentage_discount(self):
        """Should be able to apply a percentage discount."""
        cart = ShoppingCart()
        cart.add(Product("Laptop", 1000.00))
        cart.apply_discount(10)
        assert cart.total() == 900.00
    

    def test_discount_applies_to_multiple_items(self):
        """Discount should apply to entire cart total."""
        cart = ShoppingCart()
        cart.add(Product("Item1", 50.00))
        cart.add(Product("Item2", 50.00))
        cart.apply_discount(20)
        assert cart.total() == 80.00
    

    def test_discount_percentage_must_be_valid(self):
        """Discount must be between 0 and 100."""
        cart = ShoppingCart()
        cart.add(Product("Item", 100.00))
        with pytest.raises(ValueError):
            cart.apply_discount(-10)
        with pytest.raises(ValueError):
            cart.apply_discount(101)
    

    def test_applying_new_discount_replaces_old(self):
        """Applying a new discount should replace the previous one."""
        cart = ShoppingCart()
        cart.add(Product("Item", 100.00))
        cart.apply_discount(10)
        cart.apply_discount(25)
        assert cart.total() == 75.00
    

    def test_remove_discount(self):
        """Should be able to remove the discount."""
        cart = ShoppingCart()
        cart.add(Product("Item", 100.00))
        cart.apply_discount(20)
        cart.remove_discount()
        assert cart.total() == 100.00


# =============================================================================
# EXERCISE 7: Bulk Discounts (Difficulty: ⭐⭐⭐)
# =============================================================================

class TestExercise7_BulkDiscounts:
    """Buy more, save more!"""
    

    def test_bulk_discount_buy_2_get_1_free(self):
        """Buy 2 get 1 free: For every 3 items, 1 is free."""
        cart = ShoppingCart()
        apple = Product("Apple", 3.00)
        cart.set_bulk_discount(apple, buy_quantity=2, free_quantity=1)
        cart.add(apple, quantity=3)
        assert cart.total() == 6.00
    

    def test_bulk_discount_applies_multiple_times(self):
        """Bulk discount should apply as many times as possible."""
        cart = ShoppingCart()
        apple = Product("Apple", 3.00)
        cart.set_bulk_discount(apple, buy_quantity=2, free_quantity=1)
        cart.add(apple, quantity=6)
        assert cart.total() == 12.00
    

    def test_bulk_discount_partial_cycle(self):
        """Extra items beyond complete cycles should be full price."""
        cart = ShoppingCart()
        apple = Product("Apple", 3.00)
        cart.set_bulk_discount(apple, buy_quantity=2, free_quantity=1)
        cart.add(apple, quantity=5)
        assert cart.total() == 12.00
    
    
    def test_bulk_discount_combines_with_cart_discount(self):
        """Bulk discount should apply first, then cart-wide discount."""
        cart = ShoppingCart()
        apple = Product("Apple", 10.00)
        cart.set_bulk_discount(apple, buy_quantity=2, free_quantity=1)
        cart.add(apple, quantity=3)
        cart.apply_discount(10)
        assert cart.total() == 18.00
    
    
    def test_bulk_discount_only_applies_to_specified_product(self):
        """Bulk discount for one product shouldn't affect others."""
        cart = ShoppingCart()
        apple = Product("Apple", 3.00)
        orange = Product("Orange", 2.00)
        cart.set_bulk_discount(apple, buy_quantity=2, free_quantity=1)
        cart.add(apple, quantity=3)
        cart.add(orange, quantity=3)
        assert cart.total() == 12.00


# =============================================================================
# BONUS: Additional Edge Cases (Optional)
# =============================================================================

class TestBonus_EdgeCases:
    """Extra credit! These test some tricky edge cases."""
    
    @pytest.mark.skip(reason="Bonus 1")
    def test_cart_summary_string(self):
        """Cart should provide a readable summary."""
        cart = ShoppingCart()
        cart.add(Product("Apple", 1.50), quantity=2)
        cart.add(Product("Banana", 0.75), quantity=1)
        summary = str(cart)
        assert "Apple" in summary
        assert "Banana" in summary
    
    @pytest.mark.skip(reason="Bonus 2")
    def test_cart_is_iterable(self):
        """Should be able to iterate over cart items."""
        cart = ShoppingCart()
        apple = Product("Apple", 1.50)
        banana = Product("Banana", 0.75)
        cart.add(apple)
        cart.add(banana)
        products = [item for item in cart]
        assert apple in products
        assert banana in products
    
    @pytest.mark.skip(reason="Bonus 3")
    def test_cart_with_free_products(self):
        """Cart should handle products with zero price."""
        cart = ShoppingCart()
        cart.add(Product("Free Sample", 0.00), quantity=5)
        cart.add(Product("Paid Item", 10.00))
        assert cart.item_count() == 6
        assert cart.total() == 10.00
