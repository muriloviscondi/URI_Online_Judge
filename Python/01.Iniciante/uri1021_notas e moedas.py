valor: float = float(input())

nota_cem: float = 0
nota_cinquenta: float = 0
nota_vinte: float = 0
nota_dez: float = 0
nota_cinco: float = 0
nota_dois: float = 0
moeda_um_inteiro: float = 0
moeda_cinquenta: float = 0
moeda_vinte_e_cinco: float = 0
moeda_dez: float = 0
moeda_cinco: float = 0
moeda_um: float = 0

valor_total: float = valor

while valor > 0:
    valor = round(valor, 2)
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
        moeda_um_inteiro += 1
        valor -= 1
    elif valor >= 0.50:
        moeda_cinquenta += 1
        valor -= 0.50
    elif valor >= 0.25:
        moeda_vinte_e_cinco += 1
        valor -= 0.25
    elif valor >= 0.10:
        moeda_dez += 1
        valor -= 0.10
    elif valor >= 0.05:
        moeda_cinco += 1
        valor -= 0.05
    else:
        moeda_um += 1
        valor -= 0.01


print(
    f'NOTAS:'
    f'\n{valor_total}'
    f'\n{nota_cem} nota(s) de R$ 100.00'
    f'\n{nota_cinquenta} nota(s) de R$ 50.00'
    f'\n{nota_vinte} nota(s) de R$ 20.00'
    f'\n{nota_dez} nota(s) de R$ 10.00'
    f'\n{nota_cinco} nota(s) de R$ 5.00'
    f'\n{nota_dois} nota(s) de R$ 2.00'
    f'\nMOEDAS:'
    f'\n{moeda_um_inteiro} moeda(s) de R$ 1.00'
    f'\n{moeda_cinquenta} moeda(s) de R$ 0.50'
    f'\n{moeda_vinte_e_cinco} moeda(s) de R$ 0.25'
    f'\n{moeda_dez} moeda(s) de R$ 0.10'
    f'\n{moeda_cinco} moeda(s) de R$ 0.05'
    f'\n{moeda_um} moeda(s) de R$ 0.01'
)
