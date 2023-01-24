
time = input("Que horas são? Escreva com ':' entre as horas e minutos: ")
try:
  tempo = time.split(":")
  hora = int(tempo[0])
  minuto = int(tempo[1])
  hora < 24
  if 0<= hora < 12:
    print("Bom dia %i horas e %i minutos" % (hora, minuto))
  elif 12 <= hora < 17:
    print("Boa tarde %i horas e %i minutos" % (hora, minuto))
  elif 17 <= hora < 24:
    print("Boa noite %i horas e %i minutos" % (hora, minuto))
  else:
      print("Escreva uma hora correta.")
except:
  print("Escreva uma hora correta.")
