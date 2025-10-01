from math import*
def fibo(n):
    f = [0] * 93
    f[1], f[2] = 1, 1
    for i in range(3, 93):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b = map(int ,input().split())
        for i in range(a, b + 1):
            print(fibo(i), end = " ")
        print()