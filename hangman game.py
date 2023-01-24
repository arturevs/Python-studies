palavra_teste = ["b","a","n","a","n","a"]
palavra_resposta = ["*","*","*","*","*","*"]
erros = 0
while True:
  if palavra_resposta == palavra_teste:
    print("você venceu!!!")
    break
  elif erros == 5:
    print("você perdeu!!!")
    break
  entrada = (input("Digite a letra: "))
  if len(entrada) > 1:
    print("Digite apenas uma letra.")
    continue
  if entrada in palavra_teste:
    for i in range(len(palavra_teste)):
      if palavra_teste[i] == entrada:
        palavra_resposta.pop(i)
        palavra_resposta.insert(i, entrada)
    print(*palavra_resposta)
  else:
    print(f"{entrada} não está na palavra")
    erros += 1