def change(s):
    res = s[0].upper()
    for x in s[1:]:
        res += x.lower()
    return res
def convert(s):
    res = ""
    for x in s:
        res += x.lower()
    return res
if __name__ == "__main__":
    arr = []
    while True:
        try:
            line = list(map(str, input().split()))
            for x in line:
                arr.append(x)
        except EOFError:
            break
    check = True
    for x in arr:
        if check:
            if '.' in x or '!' in x or '?' in x:
                print(change(x[:-1]))
                check = True
            else:
                print(change(x), end = " ")
                check = False
        else:
            if '.' in x or '!' in x or '?' in x:
                print(convert(x[:-1]))
                check = True
            else:
                print(convert(x), end = " ")
                check = False

