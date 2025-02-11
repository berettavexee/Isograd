"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=129
Concours La Poste 09/2023
La Poste - Qualif - 1
"""

import sys

def log(message):
    """Function to print messages to stderr."""
    print(message, file=sys.stderr, flush=True)

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

a, b, c = list(map(int, lines))

r = []
r.append((c //10 ) * b if c %10 == 0 else (c //10 + 1 ) * b)
r.append(c * a) 

print(min(r))

"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=129
Concours La Poste 09/2023
La Poste - Qualif - 2
"""


lines = []
for line in sys.stdin:
  lines.append(line.rstrip('\n'))
  
lines.pop(0)

data = []
movies = set()
for line in lines:
    data.append(line.split())
    for x in line.split():
        movies.add(x)

for movie in movies:
    if all(movie in l for l in data):
        print(movie)

"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=129
Concours La Poste 09/2023
La Poste - Qualif - 3
"""
import sys
from datetime import date

def log(message):
    """Function to print messages to stderr."""
    print(message, file=sys.stderr, flush=True)


lines = []
for line in sys.stdin:
  lines.append(line.rstrip('\n'))

date_format = '%H:%M:%S'
duration = datetime.strptime(date_format, lines.pop(0))
log(duration)


