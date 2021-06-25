valor: int = int(input())

nota_cem: int = 0
nota_cinquenta: int = 0
nota_vinte: int = 0
nota_dez: int = 0
nota_cinco: int = 0
nota_dois: int = 0
nota_um: int = 0

valor_total: int = valor

while valor > 0:
    if valor >= 100:
        nota_cem += 1
        valor -= 100
    elif valor >= 50:
        nota_cinquenta += 1
        valor -= 50
    elif valor >= 20:
        nota_vinte += 1
        valor -= 20
    elif valor >= 10:
        nota_dez += 1
        valor -= 10
    elif valor >= 5:
        nota_cinco += 1
        valor -= 5
    elif valor >= 2:
        nota_dois += 1
        valor -= 2
    elif valor >= 1:
        nota_um += 1
        valor -= 1

print(
    f'{valor_total}'
    f'\n{nota_cem} notas de R$ 100,00'
    f'\n{nota_cinquenta} notas de R$ 50,00'
    f'\n{nota_vinte} notas de R$ 20,00'
    f'\n{nota_dez} notas de R$ 10,00'
    f'\n{nota_cinco} notas de R$ 5,00'
    f'\n{nota_dois} notas de R$ 2,00'
    f'\n{nota_um} notas de R$ 1,00'
)
