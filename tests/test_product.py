"""
Product Tests - Example of TDD-style tests

These tests demonstrate good testing practices:
- Clear, descriptive test names
- Arrange-Act-Assert pattern
- Testing behavior, not implementation
- Testing edge cases and error conditions

Run these tests:
    pytest tests/test_product.py -v
"""

import pytest
from src.product import Product


# =============================================================================
# BASIC FUNCTIONALITY TESTS
# =============================================================================

class TestProductCreation:
    """Tests for creating Product instances."""
    
    def test_create_product_with_name_and_price(self):
        """A product should store its name and price."""
        # Arrange & Act
        product = Product("Apple", 1.50)
        
        # Assert
        assert product.name == "Apple"
        assert product.price == 1.50
    
    def test_create_product_with_category(self):
        """A product can have an optional category."""
        product = Product("Laptop", 999.99, category="electronics")
        
        assert product.category == "electronics"
    
    def test_product_default_category_is_general(self):
        """Products without a specified category should be 'general'."""
        product = Product("Book", 15.00)
        
        assert product.category == "general"
    
    def test_product_price_stored_as_float(self):
        """Price should be stored as a float even if given as int."""
        product = Product("Banana", 1)
        
        assert isinstance(product.price, float)
        assert product.price == 1.0


# =============================================================================
# VALIDATION TESTS
# =============================================================================

class TestProductValidation:
    """Tests for input validation."""
    
    def test_negative_price_raises_value_error(self):
        """Creating a product with negative price should raise ValueError."""
        with pytest.raises(ValueError) as exc_info:
            Product("Apple", -1.00)
        
        assert "negative" in str(exc_info.value).lower()
    
    def test_zero_price_is_allowed(self):
        """Zero price should be allowed (e.g., for free samples)."""
        product = Product("Free Sample", 0)
        
        assert product.price == 0.0
    
    def test_empty_name_raises_value_error(self):
        """Product name cannot be empty."""
        with pytest.raises(ValueError):
            Product("", 10.00)
    
    def test_whitespace_only_name_raises_value_error(self):
        """Product name cannot be just whitespace."""
        with pytest.raises(ValueError):
            Product("   ", 10.00)
    
    def test_name_is_stripped_of_whitespace(self):
        """Leading/trailing whitespace should be removed from name."""
        product = Product("  Apple  ", 1.50)
        
        assert product.name == "Apple"


# =============================================================================
# EQUALITY AND REPRESENTATION TESTS
# =============================================================================

class TestProductEquality:
    """Tests for product comparison."""
    
    def test_products_with_same_name_and_price_are_equal(self):
        """Two products with same name and price should be equal."""
        product1 = Product("Apple", 1.50)
        product2 = Product("Apple", 1.50)
        
        assert product1 == product2
    
    def test_products_with_different_names_are_not_equal(self):
        """Products with different names are not equal."""
        product1 = Product("Apple", 1.50)
        product2 = Product("Orange", 1.50)
        
        assert product1 != product2
    
    def test_products_with_different_prices_are_not_equal(self):
        """Products with different prices are not equal."""
        product1 = Product("Apple", 1.50)
        product2 = Product("Apple", 2.00)
        
        assert product1 != product2
    
    def test_product_not_equal_to_non_product(self):
        """A product should not be equal to non-Product objects."""
        product = Product("Apple", 1.50)
        
        assert product != "Apple"
        assert product != 1.50
        assert product != None


class TestProductRepresentation:
    """Tests for string representation."""
    
    def test_repr_shows_name_and_price(self):
        """repr should show product name and formatted price."""
        product = Product("Apple", 1.50)
        
        result = repr(product)
        
        assert "Apple" in result
        assert "1.50" in result


# =============================================================================
# HASH TESTS (for use in sets and as dict keys)
# =============================================================================

class TestProductHash:
    """Tests for using products in sets and as dictionary keys."""
    
    def test_equal_products_have_same_hash(self):
        """Equal products should have the same hash."""
        product1 = Product("Apple", 1.50)
        product2 = Product("Apple", 1.50)
        
        assert hash(product1) == hash(product2)
    
    def test_product_can_be_used_in_set(self):
        """Products should be usable in sets."""
        product1 = Product("Apple", 1.50)
        product2 = Product("Apple", 1.50)
        product3 = Product("Orange", 2.00)
        
        product_set = {product1, product2, product3}
        
        # product1 and product2 are equal, so set should have 2 items
        assert len(product_set) == 2
    
    def test_product_can_be_dict_key(self):
        """Products should be usable as dictionary keys."""
        product = Product("Apple", 1.50)
        
        inventory = {product: 100}
        
        assert inventory[product] == 100
