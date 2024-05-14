def fibonacci_recursivo(n):
  """Calcula o enésimo termo da sequência de Fibonacci recursivamente.

  Args:
      n: O índice do termo na sequência (começando de 0).

  Returns:
      O enésimo termo da sequência de Fibonacci.
  """

  if n <= 1:
    return n
  else:
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# Obtém o índice do termo do usuário
n = int(input("Digite o índice do termo: "))

# Calcula o termo da sequência de Fibonacci
termo = fibonacci_recursivo(n)

# Imprime o termo
print(f"O {n}-ésimo termo da sequência de Fibonacci é: {termo}")