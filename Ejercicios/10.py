def factorial(numero):
  if numero == 0 or numero == 1:
    resultado = 1
  else:
    resultado = numero * factorial (numero - 1)
  return resultado

factorial(5)