def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n in (0, 1):
            cache[n] = n
            return cache[n]
        if n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n-1)+fibonacci(n-2)
            return cache[n]
    return fibonacci
fib = caching_fibonacci()
print(fib(6))
print(fib(8))
print(fib(11))
