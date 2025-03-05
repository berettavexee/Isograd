
"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code
Challenge de code CA 2025 - Prequalif 2 (code)
"""
import sys

def log(message):
    print(message, file=sys.stderr, flush=True)

def distance(a, b):
    return sum((x-y)**2 for x, y in zip(a, b))

lines = []
for line in sys.stdin:
  lines.append(line.rstrip('\n'))
  
N = int(lines.pop(1))
data = []
for line in lines:
    data.append(list(map(int, line.split())))

target = data.pop(0)
#log(f'Target: {target}')
#log(f'Wines: {data}')

r = []
for idx, i in enumerate(data):
    r.append((distance(target, i), idx))

r.sort()
log(f'result: {r}')
print(r[0][1])

"""
https://www.isograd-testingservices.com/FR/solutions-challenges-de-code
Challenge de code CA 2025 - Prequalif CA 2 (optim) - Faussaire de vins
"""
import sys
import random

def log(message):
    print(message, file=sys.stderr, flush=True)

def calculer_ecart(melange, preferences):
    ecart = 0
    for i in range(10):
        ecart += (preferences[i] - melange[i]) ** 2
    return ecart

def calculer_norme_gout(preferences):
    norme = 0
    for i in range(10):
        norme += preferences[i] ** 2
    return norme

def calculer_melange(vins_selectionnes, cave):
    melange = [0] * 10
    for vin_index in vins_selectionnes:
        for i in range(10):
            melange[i] += cave[vin_index][i]
    if len(vins_selectionnes) > 0 :
        for i in range(10):
            melange[i] /= len(vins_selectionnes)
    return melange

def calculer_score(vins_selectionnes, preferences, cave):
    melange = calculer_melange(vins_selectionnes, cave)
    ecart = calculer_ecart(melange, preferences)
    norme_gout = calculer_norme_gout(preferences)
    score = (1.0 - (ecart / norme_gout)) * 1000000
    return max(0, score)

def generer_solution_aleatoire(nombre_vins_cave):
    nombre_vins_melange = random.randint(1, 50)
    return [random.randint(0, nombre_vins_cave - 1) for _ in range(nombre_vins_melange)]

def croisement(parent1, parent2):
    point_croisement = random.randint(0, min(len(parent1), len(parent2)))
    enfant1 = parent1[:point_croisement] + parent2[point_croisement:]
    enfant2 = parent2[:point_croisement] + parent1[point_croisement:]
    return enfant1, enfant2

def mutation(solution, nombre_vins_cave):
    if random.random() < 0.1:  # Probabilité de mutation
        index_mutation = random.randint(0, len(solution) - 1)
        solution[index_mutation] = random.randint(0, nombre_vins_cave - 1)
    return solution

def algorithme_genetique(preferences, cave, taille_population=100, nombre_generations=100):
    nombre_vins_cave = len(cave)
    population = [generer_solution_aleatoire(nombre_vins_cave) for _ in range(taille_population)]
    meilleure_solution = None
    meilleur_score = 0

    for generation in range(nombre_generations):
        population_scores = [(calculer_score(solution, preferences, cave), solution) for solution in population]
        population_scores.sort(key=lambda x: x[0], reverse=True)

        if population_scores[0][0] > meilleur_score:
            meilleur_score = population_scores[0][0]
            meilleure_solution = population_scores[0][1]

        nouvelle_population = [solution for _, solution in population_scores[:taille_population // 2]]  # Sélection des meilleurs

        while len(nouvelle_population) < taille_population:
            parent1, parent2 = random.choice(nouvelle_population), random.choice(nouvelle_population)
            enfant1, enfant2 = croisement(parent1, parent2)
            nouvelle_population.extend([mutation(enfant1, nombre_vins_cave), mutation(enfant2, nombre_vins_cave)])

        population = nouvelle_population[:taille_population]

    return meilleure_solution

# Exemple d'utilisation
preferences = list(map(int, input().split()))
nombre_vins_cave = int(input())
cave = [list(map(int, input().split())) for _ in range(nombre_vins_cave)]

meilleure_solution = algorithme_genetique(preferences, cave)
print(*meilleure_solution)