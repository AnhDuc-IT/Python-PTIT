if __name__ == "__main__":
    n = int(input())
    deg = [0] * (n + 1)
    for i in range(1, n):
        u, v = map(int, input().split())
        deg[u] += 1
        deg[v] += 1
    cnt = 0
    for i in range(1, n + 1):
        if deg[i] == n - 1:
            cnt += 1
        else:
            if deg[i] != 1:
                cnt = 0
                break
    if cnt == 1:
        print("Yes")
    else:
        print("No")