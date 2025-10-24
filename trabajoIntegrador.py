import random

numero_secreto = random.randint(1, 50)
intentos = 0
max_intentos = 5
acertado = False

print("Tienes 5 intentos para adivinar el número secreto entre 1 y 50\n")

while intentos < max_intentos and not acertado:
    numero = int(input(f"Intento {intentos + 1}: Ingresa un número entre 1 y 50 = "))
    intentos = intentos + 1

    if numero == numero_secreto:
        print(f"Número acertado en {intentos} intentos")
        acertado = True
    elif numero < numero_secreto:
            print("El número secreto es mayor\n")
    else:
            print("El número secreto es menor\n")

if not acertado:
    print(f"Has perdido. El número secreto era {numero_secreto}")
