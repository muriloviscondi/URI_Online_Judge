distancia_percorrida: int = int(input())
total_combustivel: float = float(input())

consumo_medio: float = distancia_percorrida / total_combustivel

print(f'{consumo_medio:.3f} km/l')
