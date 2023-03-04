from typing import Dict

f = open('input.txt')
J = list(set(list(f.readline()[:-1])))
S = f.readline()
result = 0
J_dict: Dict = {}
for j in J:
    J_dict[j] = J_dict.get(j, 0) + 1
for s in S:
    result += J_dict.get(s, 0)
print(result)
f.close()
