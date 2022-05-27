# This script creates a group of three and a group of two.
# Groups from previous weeks are not taken into consideration 

import random

# Set file_path to desired path
file_path = "/Users/marisolmata/Desktop/Code+/names.txt"

with open(file_path) as f:
    lines = f.readlines()
    names = [line.strip() for line in lines]
            
triple_threat = []
for i in range (3):
    tt = random.choice(names)
    triple_threat.append(tt)
    names.remove(tt)
dynamite_duo = []
for k in range (2):
    dd = random.choice(names)
    dynamite_duo.append(dd)
    names.remove(dd)

print(f"This week's dynamite duo is {dynamite_duo}")
print(f"This week's triple threat is {triple_threat}")