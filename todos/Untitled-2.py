def fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def verificar_fibonacci(num):
    fib_sequence = fibonacci(num)
    if num in fib_sequence:
        return f"O número {num} pertence à sequência de Fibonacci!"
    else:
        return f"O número {num} NÃO pertence à sequência de Fibonacci!"

numero = int(input("Digite um número para verificar na sequência de Fibonacci: "))
print(verificar_fibonacci(numero))