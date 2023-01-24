def Procura_Maior(a, b):
  if a > b:
    return a
  elif b > a:
    return b
  else:
    return (a+b)/2
x = 100
y = 200
print(f"entre {x} e {y}, o maior valor é: {Procura_Maior(x, y)}")
print(f"entre {x} e {x}, o maior valor é: {Procura_Maior(x, x)}")