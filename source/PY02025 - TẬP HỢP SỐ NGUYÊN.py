
if __name__ == "__main__":
    n, m = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    res = (a & b)
    ans = a.difference(b)
    result = b.difference(a)
    print(*res)
    print(*ans)
    print(*result)