from math import sqrt

primeira_entrada: str = str(input()).split(' ')
segunda_entrada: str = str(input()).split(' ')

x1: float = float(primeira_entrada[0])
y1: float = float(primeira_entrada[1])

x2: float = float(segunda_entrada[0])
y2: float = float(segunda_entrada[1])

distancia = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

print(f'{distancia:.4f}')
