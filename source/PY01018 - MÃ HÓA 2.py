p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    temp = list(map(str, input().split()))
    k = int(temp[0])
    if k == 0:
        break
    s = list(temp[1])
    for i in range(len(s)):
        pos = p.index(s[i])
        s[i] = p[(pos + k) % 28]
    s = s[::-1]
    print("".join(s))
