entrada: str = str(input()).split(' ')

A: float = float(entrada[0])
B: float = float(entrada[1])
C: float = float(entrada[2])

area_triangulo: float = (A * C) / 2
area_circulo: float = 3.14159 * pow(C, 2)
area_trapezio: float = ((A + B) / 2) * C
area_quadrado: float = pow(B, 2)
area_retangulo: float = A * B

print(f'TRIANGULO: {area_triangulo:.3f}'
      f'\nCIRCULO: {area_circulo:.3f}'
      f'\nTRAPEZIO: {area_trapezio:.3f}'
      f'\nQUADRADO: {area_quadrado:.3f}'
      f'\nRETANGULO: {area_retangulo:.3f}')
