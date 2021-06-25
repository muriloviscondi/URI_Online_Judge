idade_em_dias: int = int(input())

anos: int = idade_em_dias / 365;
meses: int = idade_em_dias * 0.0329

while meses > 12:
    meses -= 12

dias: int = idade_em_dias - ((int(anos) * 365) + (int(meses) * 30))

if dias == 30:
    dias -= 30
    meses += 1

print(
    f'{int(anos)} ano(s)'
    f'\n{int(meses)} mes(es)'
    f'\n{int(dias)} dia(s)'
)
