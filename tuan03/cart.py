def calculate_total(items):
    """Calculate total in VND from (price, quantity) pairs."""
    total = 0

    for price, quantity in items:
        if type(price) is not int:
            raise TypeError("Price must be an integer")
        if type(quantity) is not int:
            raise TypeError("Quantity must be an integer")
        if price < 0:
            raise ValueError("Price must not be negative")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        total += price * quantity

    return total
