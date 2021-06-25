duracao_segundos: int = int(input())

horas: float = duracao_segundos / 3600
minutos: float = (duracao_segundos - (int(horas) * 3600)) / 60
segundos: float = duracao_segundos % 60;

print(f'{int(horas)}:{int(minutos)}:{int(segundos)}')
