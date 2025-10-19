def convert(s):
    res = ""
    for x in s:
        res += x.lower()
    return res
    return s
if __name__ == "__main__":
    file1 = open("source/DATA1.in", "r")
    file2 = open("source/DATA2.in", "r")
    a = list(file1.read().split())
    b = list(file2.read().split())
    for i in range(len(a)):
        a[i] = convert(a[i])
    for i in range(len(b)):
        b[i] = convert(b[i])
    a = set(a)
    b = set(b)
    res = a.difference(b)
    ans = b.difference(a)
    print(*sorted(res))
    print(*sorted(ans))