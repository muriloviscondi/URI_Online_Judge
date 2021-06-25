entrada: str = str(input()).split()

x: int = int(entrada[0])
y: int = int(entrada[1])

if x > y:
    if x % y == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
else:
    if y % x == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
