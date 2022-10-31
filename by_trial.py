import collections
import random

ODDS = [0.3, 0.25, 0.2, 0.15, 0.1]
GOAL = 4
REPEAT = 10_000_000

def raffle():
    scores = [0] * len(ODDS)

    while max(scores) < GOAL:
        i = random.choices(range(len(ODDS)), weights=ODDS)[0]

        scores[i] += 1

    print(scores)

    return scores.index(GOAL)

results = list()

for _ in range(REPEAT):
    results.append(raffle())

results.sort()

counter = collections.Counter(results)

print('\n[Result]')
for k, v in counter.items():
    print(f'Player{k+1}: {v/REPEAT*100:.5f}%')