from sys import stdin

def solve():
    n = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))

    ans = float("inf")

    for i in range(n):  # chọn đỉnh
        B = [A[j] + abs(i - j) for j in range(n)]
        B.sort()
        median = B[n // 2]
        cost = sum(abs(b - median) for b in B)
        ans = min(ans, cost)

    print(ans)

if __name__ == "__main__":
    solve()