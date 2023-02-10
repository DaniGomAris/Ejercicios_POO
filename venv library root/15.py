def palindromo():
  text = str(input("Ingrese texto: "))
  if text == text[::-1]:
    print("Es palindromo")
  else:
    print('No es palindromo')

palindromo()