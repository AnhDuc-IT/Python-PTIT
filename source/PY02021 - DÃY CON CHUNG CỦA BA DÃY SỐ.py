from collections import Counter
# thiet ke co so du lieu chi co phu hop hay khong phu hop, khong co dung sai
if __name__ == "__main__":
    for _ in range(int(input())):
        n, m, p = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))
        ca = Counter(a)
        cb = Counter(b)
        cc = Counter(c)
        res = []
        for x in ca:
            if x in cb and x in cc:
                cnt = min(ca[x],cb[x], cc[x])
                res.extend([x] * cnt)
        if res:
            print(*sorted(res))
        else:
            print("NO")