import random

names = [];
with open('names.txt') as f:
    lines = f.readlines();

print(random.sample(lines,3))