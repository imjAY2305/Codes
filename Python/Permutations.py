from itertools import permutations as p
string1 = input()
arr = list(string1)
res = []
res.extend(list(p(arr,len(arr))))
fin = []
for i in res:
    print("".join(i))