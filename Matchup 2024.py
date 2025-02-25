
"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=129
Matchup 2024 - 1 
Round 1

Pas de difficulté sauf la mise en forme des données 
"""

import sys
from collections import defaultdict

def log(message):
    """Function to print messages to stderr."""
    print(message, file=sys.stderr, flush=True)

# Read input lines
lines = []
for line in sys.stdin:
  lines.append(line.rstrip('\n'))

lines.pop(0)
# Parse input data
for line in lines:
    s = sum(int(x) for x in list(line))
    if str(line[0:2]) == "42" and s == 75:
        print(tmp)


"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=129
Matchup 2024 - 2 
Round 2 - Tableau des Médailles

Pas de difficulté sauf la mise en forme des données 
"""
import sys

def log(message):
    """Function to print messages to stderr."""
    print(message, file=sys.stderr, flush=True)

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

lines.pop(0)

data = []
for line in lines:
    p, *medals = line.split()
    a, b, c = map(int, medals)
    score = a * 1000 + b * 100 +c
    data.append((p, score))

data.sort(key=lambda x: x[1])
log(data)
print(data[-1][0])

"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=129
Matchup 2024 - 3 
Round 3 - Kayak Cross

Pas de difficulté sauf la mise en forme des données 
"""
import sys

def log(message):
    """Function to print messages to stderr."""
    print(message, file=sys.stderr, flush=True)

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

lines.pop(0)

"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=129
Meilleur Dev de France Mai 2014
Matchup 2024 - 4 - Escalade
"""
import sys
from collections import deque

def log(message):
    print(message, file=sys.stderr, flush=True)

def bfs(graph, start, end):
    distance = {start: 0}
    previous = {start: None}  # Keep track of the previous node
    queue = deque([start])
    while queue:
        v = queue.popleft()
        if v == end:
            break
        for u in graph[v]:
            if u not in distance:
                distance[u] = distance[v] + 1
                previous[u] = v  # Store the previous node for path reconstruction
                queue.append(u)
    return distance, previous

def dist_sq(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

S = int(lines.pop(0))
end = tuple(map(int, lines.pop(0).split()))
start = tuple(map(int, lines.pop(0).split()))
_ = lines.pop(0)
points = []
for line in lines:
    points.append(tuple(map(int, line.split())))
"""
log(f'S: {S}')
log(f'Start: {start}')
log(f'End: {end}')
log(f'Points: {points}')
"""

graph = {}
for i in range(len(points)):
    graph[points[i]] = []
    for j in range(len(points)):
        if i != j and dist_sq(points[i], points[j]) <= S**2:
            graph[points[i]].append(points[j])

graph[start] = []
for p in points:
    if dist_sq(start, p) <= S**2:
        graph[start].append(p)

for p in points:
    graph.setdefault(p, [])
    if dist_sq(end, p) <= S**2:
        graph[p].append(end)
graph.setdefault(end, [])
if dist_sq(start, end) <= S**2:
    graph[start].append(end)


distance, previous = bfs(graph, start, end)

if end in distance:

    # Reconstruct the path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    for point in path:
        print(*point)
else:
    print(-1)

"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=129
Meilleur Dev de France Mai 2014
Matchup 2024 - 5 - Plongeon Artistique
"""
import sys

def solve_knapsack(figures, capacity):
    """Solves the knapsack problem with figure degradation and multiple usages.

    Args:
        figures: A list of tuples, where each tuple represents a figure 
                 and contains its weight and initial value.
        capacity: The maximum capacity of the knapsack.

    Returns:
        The maximum achievable value.
    """
    n = len(figures)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        figure_weight, figure_value = figures[i - 1]
        for w in range(capacity + 1):
            max_value_at_weight = dp[i - 1][w]
            usage_count = 1
            current_value = figure_value
            
            while usage_count * figure_weight <= w and current_value > 0:
                fig_score = usage_count * figure_value - usage_count * (usage_count - 1) // 2
                max_value_at_weight = max(max_value_at_weight, dp[i - 1][w - usage_count * figure_weight] + fig_score)
                current_value -= 1
                usage_count += 1
            dp[i][w] = max_value_at_weight

    return dp[-1][-1]


lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

T = int(lines.pop(0))  
N = int(lines.pop(0))

figures = []
for line in lines:
    figures.append(tuple(map(int, line.split())))

result = solve_knapsack(figures, T)  # T seems to be the capacity in this case
print(result)
