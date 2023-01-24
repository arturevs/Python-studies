
def swap_char(string1, char1, char2):
  string2 = []
  contador = 0
  for i in string1:
    if i == char1:
      string2[contador] = char2
      contador += 1
    else:
      string2[contador] = i
      contador += 1
    return string(string2)

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = input("Digite sua altura em metros: ")
altura = swap_char(altura, ',', '.')
altura = float(altura)
print(f'{nome} tem {altura} metros de altura, pesa {peso} quilos e seu IMC é {IMC:.2f}')
