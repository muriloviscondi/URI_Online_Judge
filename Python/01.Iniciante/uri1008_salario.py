numero_funcionario: int = int(input())
horas_trabalhadas: int = int(input())
valor_horas: float = float(input())


print(f'NUMBER = {numero_funcionario}'
      f'\nSALARY = U$ {(horas_trabalhadas * valor_horas):.2f}')
