# Code utilitaire
## Starterpack 
Une petite fonction pour ne pas avoir a se battre avec des sys.stderr.write() pour afficher des erreurs ou faire de debuggage.

```Python 
def log(message):
    # Fonction pour afficher des messages
    print(message, file=sys.stderr, flush=True)
```

Dans l'énorme majorité des cas on peut commencer la résolution par ce bout de code:

```Python 
import sys

def log(message):
    # Fonction pour afficher des messages
    print(message, file=sys.stderr, flush=True)

# Lecture des données 
lines = []
for line in sys.stdin:
  lines.append(line.rstrip('\n'))
# On dégage la line 0 généralement inutile 
_ = lines.pop(0) 

# Mise en forme des données 
data = []
for line in lines:
    x, y = map(int, line.split())
    data.append(x, y)
# Affichage pour être sur qu'on a bien les donnée attendue
log(f'Input data:\n {data}')
```
# Graph 
Voici comment représenté un graph sous la forme d'un dictionnaire de liste d'arrêt pour chaque noeud/vertex. Isograd/Codingame fournit toujours la graph sous la forme d'une liste d’arêtes et dans l'énorme majorité des cas les graph sont non orientés. 
On importe les bibliothéques standards defaultdict et deque. Elles nous font gagner du temps sur l'initialisation des dictionnaire et sur les algo qui viendront après.
```Python 
from collections import defaultdict, deque 

adjacencyList = defaultdict(list)
for i in range(l):
    u, v = [int(j) for j in input().split()]
    adjacencyList[u].append(v)
    adjacencyList[v].append(u)
```

Algorithme de recherche en largeur / Breadth First Search, c'est l'algo de parcours de graph le plus courant pour trouver le chemin minimal.
```Python
from collections import deque

def bfs(graph, start):
    distance = {start: 0}
    previous = {start: None}
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if u not in distance:
                distance[u] = distance[v] + 1
                previous[u] = v
                queue.append(u)
    return distance, previous
```

