import random

file1 = open("esnames.txt", "r") 
names = file1.readlines()
print(names)
group1 = []
for i in range(len(names)):
    names[i] = names[i].strip()


for i in range (0,3):
    choice = random.choice(names)
    group1.append(choice)
    names.remove(choice)
print(group1)
print(names)

print("Carpe diem amicus meus!")




file1.close()