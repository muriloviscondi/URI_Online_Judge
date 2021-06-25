nome_funcionario: str = str(input())
salario_fixo: float = float(input())
vendas_mes: float = float(input())

valor_comissao = vendas_mes * 0.15
total_salario = valor_comissao + salario_fixo

print(f'TOTAL = R$ {total_salario:.2f}')
