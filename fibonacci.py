def Fibonacci(n):
    """
    Return the n value of the fibonacci sequence.
    [0, 1, 1, 2, 3, 5, ...]
    """
    if n < 2:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
