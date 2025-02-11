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

"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=129
Meilleur Dev de France Mai 2014
MDF 2014 - 5 -Le mot le plus courant
"""
import sys
from collections import defaultdict
import string

def log(message):
    """Function to print messages to stderr."""
    print(message, file=sys.stderr, flush=True)


texts = []
for line in sys.stdin:
  texts.append(line.rstrip('\n'))
  

# Comptage des mots
word_counts = defaultdict(set)  # On utilise un set pour ne pas compter plusieurs fois le même mot dans un texte

for i, text in enumerate(texts):
    # Remove punctuation and convert to lowercase (correctly)
    text = text.lower()
    for x in string.punctuation:
        text = text.replace(x, '')
    words = text.split()

    for word in words:
        word_counts[word].add(i)  # On ajoute l'index du texte au set

# Filtrage
n = len(texts)
filtered_counts = {
    word: len(text_set)  # Count the number of texts
    for word, text_set in word_counts.items()
    if len(text_set) < n  # Keep words that appear in fewer than n texts
}

# Sort and output the top 3
sorted_words = sorted(filtered_counts.items(), key=lambda item: (-item[1], item[0]))

for word, count in sorted_words[:3]:
    print(count, word)
