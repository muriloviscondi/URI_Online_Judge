entrada: str = str(input()).split(' ')

A: int = int(entrada[0])
B: int = int(entrada[1])
C: int = int(entrada[2])

maiorAB = (A + B + abs(A - B)) / 2

maior = C if maiorAB < C else maiorAB

print(f'{int(maior)} eh o maior')
