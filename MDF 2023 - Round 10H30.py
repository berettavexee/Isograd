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
from collections import deque

def algo(image):
    n = len(image)
    visited = [[False] * n for _ in range(n)]
    compteur_parts = 0

    def is_valid(line, col):
        return 0 <= line < n and 0 <= col < n

    def bfs(line, col):
        queue = deque([(line, col)])
        visited[line][col] = True

        while queue:
            line, col = queue.popleft()
            for dline, dcol in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nline, ncol = line + dline, col + dcol
                if is_valid(nline, ncol) and image[nline][ncol] == '#' and not visited[nline][ncol]:
                    queue.append((nline, ncol))
                    visited[nline][ncol] = True

    for i in range(n):
        for j in range(n):
            if image[i][j] == '#' and not visited[i][j]:
                bfs(i, j)
                compteur_parts += 1

    return compteur_parts

# Lecture de l'entrée
n = int(input())
image = [input() for _ in range(n)]

# Calcul et affichage du résultat
resultat = algo(image)
print(resultat)