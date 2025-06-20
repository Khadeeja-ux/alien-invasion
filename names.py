students = []

with open("names.csv") as f:
    for line in f:
        name , home = line.rstrip().split(",")
        students.append(f"{name} is in {home}.")

for student in sorted(students):
    print(f"{student}")