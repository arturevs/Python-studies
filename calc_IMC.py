


name = input("Your name: ")
weight = float(input("Your weight in kilos: "))
height = input("Your height in meters, like 1.75: ")
height = float(height)
IMC = weight / height**2
print(f'{name} is {height} meters tall, weights {weight} kilos and their IMC is {IMC:.2f}')
