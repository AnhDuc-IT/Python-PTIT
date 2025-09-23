from math import*
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        for i in range(k, n):
            print(a[i], end = " ")
        for i in range(k):
            print(a[i], end = " ")
        print("")
        t -= 1
