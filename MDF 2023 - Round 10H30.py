"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=99
MDF 2023 - Round 1  - Round 10H30 - Pizza - 1
"""
import sys

def log(message):
    print(message, file=sys.stderr, flush=True)

lines = []
for line in sys.stdin:
  lines.append(line.rstrip('\n'))
  
lines.pop(0)
ingredients = set()

for line in lines:
    for i in line.split():
        ingredients.add(i.lower())
        
print(len(ingredients))

"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=99
MDF 2023 - Round 2  - Round 10H30 - Pizza - 2
"""
import sys

def log(message):
    print(message, file=sys.stderr, flush=True)

def dst(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

lines = []
for line in sys.stdin:
  l = line.rstrip('\n')
  x,y = map(int, l.split())
  lines.append((x, y))

N, M = lines.pop(0)

pizzeria = lines[:N]
commandes = lines[N:]

log(f'Pizzeria: {pizzeria}')
log(f'Commandes: {commandes}')

d = 0
for c in commandes:
    d += min(dst(c, p) for p in pizzeria) * 2

print(d)

"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=99
MDF 2023 - Round 3  - Round 10H30 - Pizza - 3
"""
import sys

def compter_parts_pizza(pizza):
    """
    Compte le nombre de parts de pizza dans une image en noir et blanc.

    Args:
        pizza: Une liste de chaînes de caractères représentant l'image de la pizza.

    Returns:
        Le nombre de parts de pizza.
    """

    n = len(pizza)
    visite = [[False] * n for _ in range(n)]
    nombre_parts = 0

    def est_valide(x, y):
        return 0 <= x < n and 0 <= y < n

    def bfs(x, y):
        queue = [(x, y)]
        visite[x][y] = True

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            cx, cy = queue.pop(0)

            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy

                if est_valide(nx, ny) and pizza[nx][ny] == '#' and not visite[nx][ny]:
                    queue.append((nx, ny))
                    visite[nx][ny] = True

    for i in range(n):
        for j in range(n):
            if pizza[i][j] == '#' and not visite[i][j]:
                bfs(i, j)
                nombre_parts += 1

    return nombre_parts
  
# Lecture de l'entrée
n = int(input())
image = [input() for _ in range(n)]

# Calcul et affichage du résultat
resultat = compter_parts_pizza(image)
print(resultat)
