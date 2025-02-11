"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=129
Meilleur Dev de France Mai 2014
MDF 2014 - 4 -Le centre de la matrice
"""
import sys
from collections import Counter

def log(message):
    """Function to print messages to stderr."""
    print(message, file=sys.stderr, flush=True)

lines = []
for line in sys.stdin:
  lines.append(line.rstrip('\n'))
  
p = int(lines.pop(0))

matrice = []
for line in lines:
    matrice.append(list(map(int, line.split())))

# Extraction de la sous-matrice centrale
sous_matrice = []
debut = p // 4
fin = 3 * p // 4
for i in range(debut, fin):
    sous_matrice.extend(matrice[i][debut:fin])

# Calcul des statistiques
minimum = min(sous_matrice)
maximum = max(sous_matrice)

# Calcul de la médiane
sous_matrice.sort()
n = len(sous_matrice) // 2 
mediane = (sous_matrice[n - 1] + sous_matrice[n]) / 2
    
# Calcul du mode avec Counter
C = Counter(sous_matrice)
log(f'Counter :\n {C}')
mode = C.most_common(1)[0][0]  # Récupère l'élément le plus fréquent

print(f'{minimum} {maximum} {mediane:.1f} {mode} ' )