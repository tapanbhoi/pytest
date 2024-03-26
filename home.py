def add_numbers(num1, num2):
    """Adds two numbers, handling potential type mismatches and errors.

    Args:
        num1: The first number.
        num2: The second number.

    Returns:
        The sum of the two numbers if possible, otherwise an error message.
    """

    try:
        # Attempt conversion to float for maximum flexibility
        result = float(num1) + float(num2)
        return result
    except (TypeError, ValueError):
        return "Invalid input. Please enter numerical values."

# Example usage
print(add_numbers(5, 3))         # Output: 8.0
print(add_numbers("2.5", 4))      # Output: 6.5
print(add_numbers("hello", "5"))  # Output: Invalid input. Please enter numerical values.
