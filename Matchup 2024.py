
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