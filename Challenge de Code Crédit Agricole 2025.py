"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code
Challenge de Code Crédit Agricole 2025
Round 1
Benchmarking
"""
import sys

def log(message):
    # Fonction pour afficher des messages
    print(message, file=sys.stderr, flush=True)

lines = []
for line in sys.stdin:
  lines.append(line.rstrip('\n'))

  
lines.pop(0)
r = []

for line in lines:
    a, *b = line.split() 
      # b est une liste de taille variable
    b = sum(float(x) for x in b)/len(b) 
      # erreur ou résultat faux en d'utilisation de int()
    r.append((a,b))

r.sort(key=lambda x: x[1])
print(r[-1][0])

"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code
Challenge de Code Crédit Agricole 2025
Round 2
Hallucination
"""
import sys

def log(message):
    # Fonction pour afficher des messages
    print(message, file=sys.stderr, flush=True)

lines = []
for line in sys.stdin:
  lines.append(int(line.rstrip('\n')))
 
eye, leg, tail = lines
log(f'{eye} {leg} {tail}')

if eye % 2 == 1 or leg % 2 == 1:
    print('Hallucination')
    exit()

# Math
n_human = eye // 2 - tail 
n_bird = n_human + 2 * tail - leg // 2
n_dog = tail - n_bird

if min(n_human, n_bird, n_dog) < 0:
    print('Hallucination')
else:
    print(n_human)
    print(n_dog)
    print(n_bird)


"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code
Challenge de Code Crédit Agricole 2025
Round 3
"""
import sys

def log(message):
    # Fonction pour afficher des messages
    print(message, file=sys.stderr, flush=True)

def get_neighbors(grid):
    """
    Takes a 2D array as input and returns a 2D array where each
    cell contains a list of its neighboring cell contents
    """
    h = len(grid)
    w = len(grid[0])
    neighbors_grid = [[[] for _ in range(w)] for _ in range(h)]
    
    # Directions for neighbors (right, left, down, up)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for r in range(h):
        for c in range(w):
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w:
                    neighbors_grid[r][c].append(grid[nr][nc])
    
    return neighbors_grid

lines = []
for line in sys.stdin:
  lines.append(line.rstrip('\n'))

w, h = map(int, lines[0].split())
grid = [list(map(int, line)) for line in lines[1:]]

records = []
for i in range(1000):
    log(f"Loop {i}")    #Debug
    log(grid)           #Debug
    if grid in records:
        idx = records.index(grid) 
        log(idx)        #Debug
        log(i-idx)      #Debug
        print(idx)
        print(i - idx)
        exit()
    else:
        copied_grid = [row[:] for row in grid]
        # Deep copy to prevent reference errors
        records.append(copied_grid)
    
    neighbors = get_neighbors(grid)
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell != 1:
                grid[r][c] +=  -1
            else:
                if 5 in neighbors[r][c]:
                    grid[r][c] = 5
                elif neighbors[r][c].count(1) >= 2:
                    grid[r][c] = 1
                else:
                    grid[r][c] = 3