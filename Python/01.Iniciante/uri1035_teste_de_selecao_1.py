entrada: str = str(input()).split(' ')

a: int = int(entrada[0])
b: int = int(entrada[1])
c: int = int(entrada[2])
d: int = int(entrada[3])

if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
