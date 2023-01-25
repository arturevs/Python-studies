shop_list = []
while True:
  action = input("type add, delete, list or final list: ")
  if action == "add":  # this will add an item to the list.
    item = input("what item do you wish to buy? ")
    shop_list.append(item)


  elif action == "delete":  # this will delete the typed item from the list.
    deleted = input("which item do you want to delete from the list? ")
    shop_list.remove(deleted)


  elif action == "list":  # this will print the list's actual state.
    for a, b in enumerate(shop_list, start = 1):
      print(f"{a}- {b}")

      
  elif action == "final list":  # this will print the list and wait for an input to close the program.
    for a, b in enumerate(shop_list, start = 1):
      print(f"{a}- {b}")
    input()
    break
  else:
    print("please type a valid action")