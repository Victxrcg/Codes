def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

# Exemplo de uso
print(fatorial(5))  # Saída: 120
