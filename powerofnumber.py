def pow(n, p):
    if n < 0:
        print("Incorrect input")
        return
    if p == 0:
        return 1
    if p == 1:
        return n
    #print(n)
    return n*pow(n, p - 1)