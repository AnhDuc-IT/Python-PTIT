file = open("source/CONTACT.in", "r")
arr = file.read().split()
res = set()
for x in arr:
    res.add(x.lower())
res = sorted(res)
for x in res:
    print(x)