import math

def add(a1: int, a2: int):
    """
    Adds two integers and returns their sum.

    Args:
        a1 (int): The first integer to add.
        a2 (int): The second integer to add.

    Returns:
        int: The sum of a1 and a2.

    Raises:
        TypeError: If either a1 or a2 is not an integer.
    """
    if not isinstance(a1, int) or not isinstance(a2, int):
        raise TypeError("Both arguments must be integers.")
    return a1 + a2

def sub(a1: int, a2: int):
    """
    Subtracts the second integer from the first and returns the result.

    Args:
        a1 (int): The first integer.
        a2 (int): The second integer.

    Returns:
        int: The result of a1 - a2.

    Raises:
        TypeError: If either a1 or a2 is not an integer.
    """
    if not isinstance(a1, int) or not isinstance(a2, int):
        raise TypeError("Both arguments must be integers.")
    return a1 - a2

def mul(a1: int, a2: int):
    """
    Multiplies two integers and returns the result.

    Args:
        a1 (int): The first integer to multiply.
        a2 (int): The second integer to multiply.

    Returns:
        int: The product of a1 and a2.

    Raises:
        TypeError: If either a1 or a2 is not an integer.
    """
    if not isinstance(a1, int) or not isinstance(a2, int):
        raise TypeError("Both arguments must be integers.")
    return a1 * a2

def div(a1: int, a2: int):
    """
    Divides the first integer by the second and returns the result.

    Args:
        a1 (int): The numerator.
        a2 (int): The denominator.

    Returns:
        float: The result of a1 / a2, or None if division by zero occurs.

    Raises:
        TypeError: If either a1 or a2 is not an integer.
    """
    if not isinstance(a1, int) or not isinstance(a2, int):
        raise TypeError("Both arguments must be integers.")
    try:
        return a1 / a2
    except ZeroDivisionError:
        print("Division by zero error: denominator is 0")  
        return None

def mod(a1: int, a2: int):
    """
    Calculates the remainder of a1 divided by a2.

    Args:
        a1 (int): The dividend.
        a2 (int): The divisor.

    Returns:
        int: The remainder of a1 / a2.
        None: If division by zero occurs.

    Raises:
        TypeError: If either a1 or a2 is not an integer.
    """
    if not isinstance(a1, int) or not isinstance(a2, int):
        raise TypeError("Both arguments must be integers.")
    try:
        return a1 % a2
    except ZeroDivisionError:
        print("Division by zero error: denominator is 0")  
        return None

