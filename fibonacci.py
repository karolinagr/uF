def fibonacci(n):
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 1
    elif n == 4:
        return 2
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    fibonacci(1000)
