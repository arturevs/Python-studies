nome = input("Digite seu primeiro nome: ")
j = 0
for i in nome:
  if i == " ":
    print("Digite apenas seu primeiro nome.")
    j = 1
if j == 0:
  if len(nome) <= 4:
    print("Seu nome é pequeno.")
  elif 4 < len(nome) <= 6:
    print("Seu nome é médio.")
  elif 6 < len(nome) <= 12:
    print("Seu nome é grande.")  
  else:
    print("Seu nome é muito grande.")