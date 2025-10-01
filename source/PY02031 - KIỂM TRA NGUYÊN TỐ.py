from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        row = list(map(int ,input().split()))
        a.append(row)
    for i in range(n):
        for j in range(len(a[i])):
            if Prime(a[i][j]):
                print(1, end = " ")
            else:
                print(0, end = " ")
        print()