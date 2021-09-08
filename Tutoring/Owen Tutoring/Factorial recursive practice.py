def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return (factorial((x - 1)) * x)


print(factorial(5))