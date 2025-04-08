def fibonacci(n):
    if memoi[n]: return memoi[n]
    memoi[n] = fibonacci(n-1) + fibonacci(n-2)
    return memoi[n]

memoi = [None for _ in range(100)]
memoi[0] = 0
memoi[1] = 1
memoi[2] = 1

print(fibonacci(int(input())))
