import math
num_stud = int(input())
dd = {}
for n in range(num_stud):
    name, grade = input().split()
    if name not in dd:
        dd[name] = []
        dd[name].append(grade)
    else:
        dd[name].append(grade)

for key, value in dd.items():
    tkn = ' '.join(dd[key])
    avg = [float(x) for x in dd[key]]
    avg = round(sum(avg) / len(dd[key]), 2)
    print(f"{key} -> {tkn} (avg: {avg:.2f})")

x = set(1, 2, 3, 4)