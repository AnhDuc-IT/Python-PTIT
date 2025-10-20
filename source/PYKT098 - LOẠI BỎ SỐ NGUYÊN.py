def check(s):
    if s == '' or len(s) > 10:
        return False
    for x in s:
        if not x.isdigit():
            return False
    return True

if __name__ == "__main__":
    file = open("DATA.in", "r")
    arr = file.read().split()
    res = []
    for x in arr:
        if not check(x):
            res.append(x)
    res.sort()
    for x in res:
        print(x, end = " ")