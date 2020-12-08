def fibonacci(n):
    if n < 0:
        print("Incorrect input")
        return
    if n == 0:
        return 0
    if n == 1:
        return 1
    #print(n)
    return fibonacci(n - 1) + fibonacci(n - 2)
