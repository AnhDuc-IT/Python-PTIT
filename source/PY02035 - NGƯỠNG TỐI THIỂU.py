from collections import Counter
s = input()
k = int(input())
arr = []
if len(s) % 2 == 1:
    s = s[:-1]
for i in range(0, len(s), 2):
    arr.append(s[i:i + 2])
res = Counter(arr)
res = sorted(res.items())
check = True
for x, y in res:
    if y >= k:
        print(x, y)
        check = False
if check:
    print("NOT FOUND")