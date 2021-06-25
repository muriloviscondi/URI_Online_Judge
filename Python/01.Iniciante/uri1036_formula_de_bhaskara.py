from math import sqrt

entrada: str = str(input()).split(' ')

a: float = float(entrada[0])
b: float = float(entrada[1])
c: float = float(entrada[2])

if a == 0:
    print('Impossivel calcular')
else:
    delta: float = pow(b, 2) - 4 * a * c

    if delta < 0:
        print('Impossivel calcular')
    else:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)

        print(f'R1 = {x1:.5f}'
              f'\nR2 = {x2:.5f}')
