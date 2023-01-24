# this function will return the biggest number between two, if the numbers are equal it returns the number and if not numbers it returns 0.
# if you don't want the messages printed by the function, erase lines 16, 14, 11 and 8 in this order
def Search_Biggest(a, b):
  try:
    a = float(a)
    b = float(b)
  except:
    print("there is a non numeric value being compared.")
    return 0
  if a > b:
    print(f"between {a} and {b}, the biggest value is: {a}.")
    return a
  elif b > a:
    print(f"between {a} and {b}, the biggest value is: {b}.")
    return b
  print(f"the numbers {a} and {b} are the same.")
  return a
x = input("first value: ")
y = input("second value: ")
z = Search_Biggest(x, y)

