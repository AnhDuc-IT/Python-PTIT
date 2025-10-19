def process(s):
    res = 0
    for x in s:
        res += ord(x) - ord('0')
    return res
if __name__ == "__main__":
    s = input()
    if len(s) <= 1:
        print(1)
    else:
        cnt = 0
        while len(s) > 1:
            cnt += 1
            s = str(process(s))
        print(cnt)