"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code
Euro Informations 2024 - 1
Round 1
La cible

Approximation du nombre Pi, difficulté manipulation des flottants
mise en forme, nombre de décimales
"""
import sys

def log(message):
    # Fonction pour afficher des messages
    print(message, file=sys.stderr, flush=True)

lines = []
for line in sys.stdin:
  lines.append(line.rstrip('\n'))

touche = 0
tirs = int(lines[0])

for line in lines[1:]:
    x, y = map(float, line.split())
    if x** 2 + y ** 2 <= 1:
        touche += 1

pi = (4 * touche) / tirs

print(f"{pi:.3f}")  #3 décimales après la virgule



"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code
Euro Informations 2024 - 2
Round 2
Anatomie d'une chute
Warning: Enoncé merdique 
"""
import sys

def log(message):
    # Fonction pour afficher des messages
    print(message, file=sys.stderr, flush=True)

lines = []
for line in sys.stdin:
  lines.append(line.rstrip('\n'))

data = []
l = int(lines[0])
for line in lines[1:]:
    a, b = line.split()
    a = int(a)
    data.append((a, b))
    
log(data)
n = 0
data2, color = [data[0]], data[0][1]
visible = True 
for wall in data[1:]:
    if wall[0] > max((x[0] for x in data2)):
        if wall[1] == color:
            data2[-1] = wall
            n += 1 + visible 
            visible = False 
        else:
            data2.append(wall)
            visible = True
        color = wall[1]
    else:
        color = None
        

log(f'visible {data2}')
log(f'confusion: {n}')
print(n)

"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code
Concours Euro Information 2024
Round - 3 
Au fil de l'épée
"""
import sys

def log(message):
    # Fonction pour afficher des messages
    print(message, file=sys.stderr, flush=True)

def test(a, b):
  return sum(x > y for x, y in zip(a, b)) >= 2:

lines = sys.stdin.readlines() 
lines.pop(0)  # Remove the first line

data = [tuple(map(int, line.split())) for line in lines]

leader = data[0]
pool = [leader] # init pool with the first player

for _ in range(4): # depth limit to 4 iterations
    new_pool = []
    for p2 in data:
        if any(test(p2, p1) for p1 in pool):
            new_pool.append(p2)
    pool = new_pool

print("Yes" if leader in pool else "No")

"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code
Concours Euro Information 2024
Round - 4
À bout de souffle

C'est pas un probléme de combinatoire mais un problème partitionnement.
Solution récupérer sur internet "dynamic programing climbing the stairway" 

"""

import sys

def log(message):
    # Fonction pour afficher des messages
    print(message, file=sys.stderr, flush=True)

lines = sys.stdin.readlines() 

data = list(map(int, lines))
a, b, c = data


ways = [1 if i <= a else 0 for i in range(c + 2)]

for i in range(a + 1, c + 2):
    start_index = max(i - b - 1, 0)
    end_index = i - a
    ways[i] = sum(ways[start_index:end_index])
log(ways)

print(ways[-1])


"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code
Concours Euro Information 2024
Round - 5

C'est un problème de coloration de graph NP-hard. Il est presque impossible 
d'être absolument sûr que l'on a la solution minimale. Pour une raison qui 
m'échappe, le challenge accepte la solution basée sur l'heuristique de 
Recherche de cardinalité maximale (MCS) et n'accepte pas DEsatur 
(désaturation). J'ai perdue trois heures sur cette partie.

les commentaires sont fait par copilot car flemme
"""

import sys
from collections import defaultdict

def log(message):
    """Function to print messages to stderr."""
    print(message, file=sys.stderr, flush=True)

# Read input lines
lines = sys.stdin.readlines()

# Parse input data
data = []
for line in lines:
    data.append(tuple(map(int, line.split())))

# Extract the number of vertices (p) and edges (i)
p, i = data.pop(0)

# Build the graph using an adjacency list
g = defaultdict(set)
for u, v in data:
    g[u].add(v)
    g[v].add(u)

# Function to perform Maximum Cardinality Search (MCS)
def maximum_cardinality_search(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    weights = [0] * num_vertices
    ordering = []

    for _ in range(num_vertices):
        # Select the unvisited vertex with the highest weight
        max_weight = -1
        max_vertex = -1
        for v in range(num_vertices):
            if not visited[v] and weights[v] > max_weight:
                max_weight = weights[v]
                max_vertex = v
        
        # Mark the vertex as visited and add it to the ordering
        visited[max_vertex] = True
        ordering.append(max_vertex)
        
        # Increase the weight of all its unvisited neighbors
        for neighbor in graph[max_vertex]:
            if not visited[neighbor]:
                weights[neighbor] += 1
    
    return ordering

# Perform MCS to get the vertex ordering
ordering = maximum_cardinality_search(g)
log(f'MCS: {ordering}')

# Greedy coloring based on the MCS ordering
colors = [None] * p
frequencies = set(range(p)) 
for v in ordering:
    neighbor_colors = set([colors[u] for u in g[v]])
    colors[v] = min(frequencies - neighbor_colors)

log(f'Colors: {colors}')

# Print the number of colors used
print(max(colors) + 1)