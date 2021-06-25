tabela:list = [
    [1, 'Cachorro Quente', 4.00],
    [2, 'X-Salada', 4.50],
    [3, 'X-Bacon', 5.00],
    [4, 'Torrada simples', 2.00],
    [5, 'Refrigerante', 1.50]
]

entrada: str = str(input()).split()

codigo: int = int(entrada[0])
quantidade: int = int(entrada[1])

total_pedido: float

for i in range(len(tabela)):
    if codigo == tabela[i][0]:
        total_pedido = tabela[i][2] * quantidade

print(f'Total: R$ {total_pedido:.2f}')
