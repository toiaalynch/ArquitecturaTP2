def find_values():
    for x in range(-10, 10):  # Permitir valores negativos y positivos para x
        for z in range(-100, -1):  # El rango de z sigue siendo negativo
            y = x ^ (2 * z)  # Calculamos y basado en la ecuación
            if y >= 0:  # Aseguramos que y sea un número positivo o cero
                print(f"x = {x}, y = {y}, z = {z}")

# Llamamos a la función para buscar los valores
find_values()

# Elijo:
# x = -1, y = 3, z = -2

# x = -1, y = 59, z = -30
# x = -1, y = 57, z = -29
# x = -1, y = 55, z = -28
# x = -1, y = 53, z = -27
# x = -1, y = 51, z = -26
# x = -1, y = 49, z = -25
# x = -1, y = 47, z = -24
# x = -1, y = 45, z = -23
# x = -1, y = 43, z = -22
# x = -1, y = 41, z = -21
# x = -1, y = 39, z = -20
# x = -1, y = 37, z = -19
# x = -1, y = 35, z = -18
# x = -1, y = 33, z = -17
# x = -1, y = 31, z = -16
# x = -1, y = 29, z = -15
# x = -1, y = 27, z = -14
# x = -1, y = 25, z = -13
# x = -1, y = 23, z = -12
# x = -1, y = 21, z = -11
# x = -1, y = 19, z = -10
# x = -1, y = 17, z = -9
# x = -1, y = 15, z = -8
# x = -1, y = 13, z = -7
# x = -1, y = 11, z = -6
# x = -1, y = 9, z = -5
# x = -1, y = 7, z = -4
# x = -1, y = 5, z = -3
# x = -1, y = 3, z = -2