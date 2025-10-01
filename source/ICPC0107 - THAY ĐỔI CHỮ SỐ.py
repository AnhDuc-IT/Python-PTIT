from math import*
def Convert(a, p, q):
    res = ""
    for i in range(len(a)):
        if a[i] == p:
            res += q
        else:
            res += a[i]
    return res
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        p, q = map(int, input().split())
        a = input().strip()
        if(a.count(' ')): a, b = a.split()
        else: b = input()
        if(p > q):
            temp = q
            q = p
            p = temp
        p = str(p)
        q = str(q)
        c = int(Convert(a, p, q)) + int(Convert(b, p, q))
        d = int(Convert(a, q, p)) + int(Convert(b, q, p))
        print(d, c)