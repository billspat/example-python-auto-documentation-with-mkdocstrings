"""(this documentation was automatically extracted from the module docstring at the top of /main_code_goes_here/arith_ops.py)

Defines basic arithmetic operations

- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.

Examples:
    >>> from main_code_goes_here import arith_ops
    >>> arith_ops.add(2, 4)
    6.0
    >>> arith_ops.multiply(2.0, 4.0)
    8.0
    >>> arith_ops.divide(9.0, 2)
    4.5
"""


def add(a: int | float, b: int | float) -> float:
    """Compute and return the sum of two numbers.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Args:
        a (int|float): A number representing the first addend in the addition.
        b (int|float): A number representing the second addend in the addition.

    Returns:
        float: A number representing the arithmetic sum of `a` and `b`.
    """
    return float(a + b)


def subtract(a: int | float, b: int | float) -> float:
    """Calculate the difference of two numbers.

    Examples:
        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(4, 2)
        2.0

    Args:
        a (int|float): A number representing the minuend in the subtraction.
        b (int|float): A number representing the subtrahend in the subtraction.

    Returns:
        float: A number representing the difference between `a` and `b`.
    """
    return float(a - b)


def multiply(a: int | float, b: int | float) -> float:
    """Compute and return the product of two numbers.

    Examples:
        >>> multiply(4.0, 2.0)
        8.0
        >>> multiply(4, 2)
        8.0

    Args:
        a (int|float): A number representing the multiplicand in the multiplication.
        b (int|float): A number representing the multiplier in the multiplication.

    Returns:
        float: A number representing the product of `a` and `b`.
    """
    return float(a * b)


def divide(a: int | float, b: int | float) -> float:
    """Compute and return the quotient of two numbers.

    Examples:
        >>> divide(4.0, 2.0)
        2.0
        >>> divide(4, 2)
        2.0
        >>> divide(4, 0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: division by zero

    Args:
        a (int|float): A number representing the dividend in the division.
        b (int|float): A number representing the divisor in the division.

    Returns:
        float: A number representing the quotient of `a` and `b`.

    Raises:
        ZeroDivisionError: An error occurs when the divisor is `0`.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)
