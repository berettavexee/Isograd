"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=100
Meilleur Dev de France Mai 2014
MDF 2023 - JO - 1 - Pierre Feuille Ciseaux 
"""

entre = list(input())

d = {
    'P': 'C',  # Pierre bat Ciseaux
    'C': 'F',  # Ciseaux battent Feuille
    'F': 'P'   # Feuille bat Pierre
}

while len(entre) > 1:
  a = entre.pop(0)
  if d[a] == entre[0]:
    entre[0] == a

print(entre[0])

"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=100
Meilleur Dev de France Mai 2014
MDF 2023 - JO - 2 - Il n'y a plus de saisons
"""

N = int(input())
K = int(input())
saisons = list(map(int, input().split()))

K = K % sum(saisons)
jours = 0
for i in range(N):
    jours += saisons[i]
    if K <= jours:
        print(i+1)



"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=100
Meilleur Dev de France Mai 2014
MDF 2023 - JO - 3 - Jeux Olympiques - Ascenseurs
"""
import sys

lines = []
for line in sys.stdin:
    l = line.rstrip('\n')
    lines.append(list(map(int, l.split())))

N, _, E = lines.pop(0)
log(f'Etages {N}, Etage de départ {E}')
stack = {}
for line in lines:
    a, b = line
    if a not in stack:
        stack[a] = 1
    else:
        stack[a] += 1
    if b not in stack:
        stack[b] = -1
    else:
        stack[b] -= 1

assenceur = 0
sorted_keys = sorted(stack.keys()) # les clés ne sont pas ordonnées
for i in sorted_keys:
    assenceur += stack[i]
    if N > i >= E and assenceur <= 0:
        break
    if i >= N and assenceur >= 0:
        print('YES')
        exit()
print('NO')