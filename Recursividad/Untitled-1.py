


    #Recursividad

    # 5! = 5 * 4 * 3 *2 * 1 =
def factorial_iterativo(n: int):
    factorial = 1
    for i in range(1..n):
        factorial = factorial * i
    return factorial

def factorial_recursivo(n: int):
    if n <= 1:
        return 1
    return factorial_recursivo(n-1)