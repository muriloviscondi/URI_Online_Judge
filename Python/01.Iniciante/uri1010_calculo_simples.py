primeira_entrada: str = input().split(' ')
segunda_entrada: str = input().split(' ')

total_primeiro_produto: float = float(primeira_entrada[1]) * float(primeira_entrada[2])
total_segundo_produto: float = float(segunda_entrada[1]) * float(segunda_entrada[2])

print(f'VALOR A PAGAR: R$ {(total_segundo_produto + total_primeiro_produto):.2f}')
