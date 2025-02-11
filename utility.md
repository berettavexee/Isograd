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

g = defaultdict(list)
for u, v in data:
    g[u].append(v)
    g[v].append(u)
```

Algorithme de recherche en largeur / Breadth First Search, c'est l'algo de parcours de graph le plus courant pour trouver le chemin minimal.
* Entrées: un graph / l'index du sommet de départ
* Retour: un dictionnaire avec la distance par rapport au départ, un dictionnaire avec l'index du noeud précédént.
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

Même Algo mais avec une liste de index pour les différents sommets de départ.
```Python
from collections import deque

def bfs_multi(graph, start_nodes):
    # Breadth First Search
    # graph is an adjacency list
    # start_nodes is a list of node index 
    distance = {node: 0 for node in start_nodes}
    previous = {node: None for node in start_nodes}
    queue = deque(start_nodes)
    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if u not in distance:
                distance[u] = distance[v] + 1
                previous[u] = v
                queue.append(u)
    return distance, previous
```

# Grille 2D

Ce code implémente une recherche en largeur (Breadth First Search, BFS) sur un cadrillage réguilier. 
* Entrée grid, la matrice 2D representant le cadrillage.
* Retour, les dictionnaires distance et previous.

```Python
"""
Breadth First Search
in a square grid
"""
from collections import deque

def bfs_grid(grid, start_nodes):
    # Breadth First Search on square grid
    distance = {start_node: 0 for start_node in start_nodes}
    previous = {start_node: None for start_node in start_nodes}
    queue = deque(start_nodes)
    h, w = len(grid), len(grid[0])

    # Directions for neighbors (right, left, down, up)
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) in distance:
                continue
            if 0 <= ny < h and 0 <= nx < w:
                distance[(nx, ny)] = distance[(x, y)] + 1
                previous[(nx, ny)] = (x, y)
                queue.append((nx, ny))
    return distance, previous
```


# Coloration de Graph

L'algorithme de recherche de cardinalité maximale (Maximum Cardinality Search, MCS) est utilisé pour ordonner les sommets d'un graphe de manière à faciliter des opérations sur les graphs, notamment la coloration via l'algo glouton. L'approche naïve d'attaquer dans le sens de numérotation des sommets ne marche pas toujours.

```Python 
"""
Function to perform Maximum Cardinality Search (MCS)

This function implements the Maximum Cardinality Search algorithm on a given graph.
The algorithm selects vertices in a specific order to maximize the number of edges
between previously selected vertices and the current vertex.

Parameters:
    graph (list of lists): The adjacency list representation of the graph. Each index
                           represents a vertex, and the list at each index contains
                           the neighbors of that vertex.

Returns:
    list: A list of vertices in the order they were selected by the MCS algorithm.
"""

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
```

Algo glouton de coloration des sommets:
```Python
def greedy_coloring(ordering, g):
    """
    Greedy coloring based on the MCS ordering

    This function performs a greedy graph coloring algorithm using the ordering obtained
    from the Maximum Cardinality Search (MCS). It assigns colors to each vertex such
    that no two adjacent vertices share the same color.

    Parameters:
        ordering (list): A list of vertices in the order they were selected by the MCS algorithm.
        g (list of lists): The adjacency list representation of the graph. Each index
                            represents a vertex, and the list at each index contains
                            the neighbors of that vertex.

    Returns:
        list: A list where the index represents the vertex and the value at that index
             represents the color assigned to that vertex.
    """
    p = len(g)
    colors = [None] * p
    # Use a set for available colors.  Initialize with all possible colors (0 to p-1).
    available_colors = set(range(p))

    for v in ordering:
        neighbor_colors = set()
        for u in g[v]:  # Iterate through neighbors
          if colors[u] is not None: # only add color of colored neighbors
            neighbor_colors.add(colors[u])


        # Find the smallest available color not used by neighbors
        for color in available_colors:
            if color not in neighbor_colors:
                colors[v] = color
                break

    return colors
```
