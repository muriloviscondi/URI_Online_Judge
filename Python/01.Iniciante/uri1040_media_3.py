notas_finais: str = str(input()).split()

nota_1: float = float(notas_finais[0])
nota_2: float = float(notas_finais[1])
nota_3: float = float(notas_finais[2])
nota_4: float = float(notas_finais[3])

media_notas_finais = (nota_1 * 2 + nota_2 * 3 + nota_3 * 4 + nota_4 * 1) / (2 + 3 + 4 + 1)
media_recuperacao: float = -1

print(f'Media: {media_notas_finais:.1f}')

if 5.0 <= media_notas_finais <= 6.9:
    nota_exame:float = float(input())
    media_recuperacao = (media_notas_finais + nota_exame) / 2

    print(
        f'Aluno em exame.'
        f'\nNota do exame: {nota_exame:.1f}'
    )

if media_notas_finais >= 7 or media_recuperacao >= 5:
    print('Aluno aprovado.')
else:
    print('Aluno reprovado.')

if media_recuperacao != -1:
    print(f'Media final: {media_recuperacao}')
