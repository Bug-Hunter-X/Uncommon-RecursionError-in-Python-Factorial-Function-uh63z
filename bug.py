def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5)) # This works fine
print(factorial(-1)) # This causes RecursionError