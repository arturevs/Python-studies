nome = input()
idade = int(input())
if(nome != '' and idade != 0):
  print("Seu nome é %s.\n" % nome)
  print("Seu nome ao contrário é %s.\n" % nome[::-1])
  espacos = (' ' in nome)
  if espacos:
    print("Seu nome possui espaços.\n")
  else:
    print("Seu nome não possui espaços.\n")
  t_nome = len(nome)
  for coisa in nome:
    if coisa == ' ':
      t_nome -= 1
  print("Seu nome tem %i letras.\n" % t_nome)
  print("A primeira letra do seu nome é %c.\n" % nome[0])
  print("A última letra do seu nome é %c.\n" % nome[-1])
else:
  print("Desculpe, você deixou campos vazios\n")