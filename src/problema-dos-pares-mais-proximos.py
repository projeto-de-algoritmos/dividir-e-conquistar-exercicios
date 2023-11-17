import math
import sys

# Função para calcular a distância entre dois pontos
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def closest_pair(points):
    # Função interna para classificar os pontos e encontrar o par mais próximo
    def sort_and_closest(points):
        # Se houver 3 ou menos pontos, calcule a distância diretamente
        if len(points) <= 3:
            min_d = float('inf')
            for i in range(len(points)):
                for j in range(i+1, len(points)):
                    d = distance(points[i], points[j])
                    if d < min_d:
                        min_d = d
            return min_d

        # Divida a lista de pontos pela metade
        mid = len(points) // 2
        mid_point = points[mid]

        # Recursivamente encontre a distância mínima nos subconjuntos à esquerda e à direita
        dl = sort_and_closest(points[:mid])
        dr = sort_and_closest(points[mid:])
        d = min(dl, dr)

        # Crie uma lista de pontos próximos à linha de divisão
        strip = [point for point in points if abs(point[0] - mid_point[0]) < d]

        # Classifique os pontos na lista pela coordenada y
        strip.sort(key=lambda point: point[1])

        # Encontre a distância mínima entre os pontos na lista
        for i in range(len(strip)):
            for j in range(i+1, min(i+7, len(strip))):
                d = min(d, distance(strip[i], strip[j]))

        return d

    # Classifique os pontos pela coordenada x antes de chamar a função interna
    points.sort(key=lambda point: point[0])
    min_d = sort_and_closest(points)
    return min_d

# Loop principal para ler a entrada e chamar a função closest_pair
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    points = []
    for _ in range(n):
        x, y = map(float, sys.stdin.readline().split())
        points.append((x, y))

    min_d = closest_pair(points)
    if min_d < 10000:
        print("{:.4f}".format(min_d))
    else:
        print("INFINITY")