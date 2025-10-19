if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        s = input()
        ss = input()
        cnt = 0
        while ss in s:
            found = s.find(ss)
            cnt += 1
            s = s[found + len(ss):]
        print(cnt)