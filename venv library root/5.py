def conversion_temperatura():
  F = int(input("ingrese grados Farenheit:"))
  C = (F - 32) / 1.8
  print(F,"Farenheit", 'son:', C, 'Celsius')

conversion_temperatura()