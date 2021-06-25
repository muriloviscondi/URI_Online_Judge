entrada: str = str(input()).split()
valores = [int(val) for val in entrada]

valores.sort()
[print(val) for val in valores]

print()

[print(val) for val in entrada]
