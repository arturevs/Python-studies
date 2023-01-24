# this function will return the biggest number between two, if the numbers are equal it returns the number and if not numbers it returns 0.
def Search_Biggest(a, b):
  try:
    a = float(a)
    b = float(b)
  except:
    return 0
  if a > b:
    return a
  elif b > a:
    return b
  return a
x = input("first value: ")
y = input("second value: ")
z = Search_Biggest(x, y)

