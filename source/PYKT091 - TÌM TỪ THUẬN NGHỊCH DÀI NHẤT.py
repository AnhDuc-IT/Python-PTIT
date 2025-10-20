
def check(s):
    return s == s[::-1]
file = open("VANBAN.in", "r")
mp = dict()
ans = -float("infinity")
arr = []
for line in file:
    a = line.split()
    for x in a:
        arr.append(x)
        if check(x):
            if x in mp:
                mp[x] += 1
            else:
                mp[x] = 1
            if len(x) > ans:
                ans = len(x)
res = []
for x in arr:
    if check(x) and len(x) == ans and not x in res:
        print(x, mp[x])
        res.append(x)