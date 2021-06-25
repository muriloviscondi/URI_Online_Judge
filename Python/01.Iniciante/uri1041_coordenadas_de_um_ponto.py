entrada: str = str(input()).split()

x: float = float(entrada[0])
y: float = float(entrada[1])

if x == 0 == y:
    print("Origem")
elif x == 0:
    print("Eixo Y")
elif y == 0:
    print("Eixo X")
elif x > 0 < y:
    print("Q1")
elif x < 0 < y:
    print("Q2")
elif x < 0 > y:
    print("Q3")
elif x > 0 > y:
    print("Q4")
