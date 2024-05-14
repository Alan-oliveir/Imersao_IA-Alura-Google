def fibonacci(n):
  """Calcula a sequência de Fibonacci até n termos.

  Args:
      n: O número de termos na sequência.

  Returns:
      Uma lista contendo a sequência de Fibonacci até n termos.
  """

  # Inicializa os dois primeiros termos da sequência
  a = 0
  b = 1
  # Cria uma lista para armazenar a sequência
  sequencia = [a, b]

  # Calcula os termos restantes da sequência
  for _ in range(2, n):
    # Calcula o próximo termo
    proximo = a + b
    # Adiciona o próximo termo à lista
    sequencia.append(proximo)
    # Atualiza a e b para os próximos dois termos
    a = b
    b = proximo

  return sequencia

# Obtém o número de termos do usuário
num_termos = int(input("Digite o número de termos: "))

# Calcula a sequência de Fibonacci
sequencia = fibonacci(num_termos)

# Imprime a sequência
print("Sequência de Fibonacci:")
print(sequencia)