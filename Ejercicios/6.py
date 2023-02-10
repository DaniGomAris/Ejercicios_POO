def sumar(list):
  if list == []:
    return 0
  else:
    suma = list[0] + sumar(list[1:])
  return suma

sumar([1, 2])