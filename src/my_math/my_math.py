def fibonacci(n):
    """
    Returns the n-th Fibonacci number
    :param n:
    :return:
    """
    if n < 0:
        raise ValueError("Fibonacci number is not defined for negative numbers")

    if n in {0, 1}:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


def catalan_number(n):
    if n < 0:
        raise ValueError("Catalan number is not defined for negative numbers")
    return factorial(2 * n) // (factorial(n + 1) * factorial(n))
