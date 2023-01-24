try:
  num = int(input())
  if num%2 == 0:
    print("O número %i é par" % num)
  else:
    print("O número %i é ímpar" % num)
except:
  print("O número digitado não é um inteiro")
  