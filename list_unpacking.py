# * is used to determine the variable that stores the rest of the list as other list.


#in this case _ will store an empty list, because there are no elements to store.
nome1, nome2, nome3, *_= ["artur", "raquel", "carol"]

#in this case _ will store ["raquel", "carol"].
nome1, *_ = ["artur", "raquel", "carol"]

#in this case, the list is fully unpacked.
nome1, nome2, nome3 = ["artur", "raquel", "carol"]
print(nome1, nome2, nome3)