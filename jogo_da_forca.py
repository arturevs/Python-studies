resposta = "banana"
tamanho = len(resposta)
list1 = []
palavra = tamanho * "*"
list1[:0] = palavra
vidas = 4
while vidas > 0:
  letra = input("Digite uma letra:")
  if letra in resposta:
    for i in range(tamanho):
      if list1[i] == letra:
        list1
    print(list1)
  else:
    vidas -= 1
  
string = ''.join(list1)
if resposta == string:
  print("Você ganhou!")
if vidas == 0:
  print("Você perdeu!")
