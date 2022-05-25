import random

group1 = [];

with open('esnames.txt') as f:
    lines = f.readlines();

for i in range(len(lines)):
    lines[i] = lines[i].strip()


for i in range(0,3):
    random_obj = random.choice(lines)
    lines.remove(random_obj)
    group1.append(random_obj)

print(group1)
print(lines)

f.close()