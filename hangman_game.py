original_word = ["b","a","n","a","n","a"]
change_word = ["*","*","*","*","*","*"]
errors = 0
while True:
  if change_word == original_word:
    print("you win!!!")
    break
  elif errors == 5:
    print("you lose!!!")
    break
  letter = (input("Type the letter: "))
  if len(letter) > 1:
    print("Type only one letter.")
    continue
  if letter in original_word:
    for i in range(len(original_word)):
      if original_word[i] == letter:
        change_word.pop(i)
        change_word.insert(i, letter)
    print(*change_word)
  else:
    print(f"{letter} not in the word.")
    errors += 1