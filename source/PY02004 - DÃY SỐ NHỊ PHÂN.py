from math import*
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(len(a) - 1):
        if a[i] != a[i + 1]:
            cnt += 1
    print(cnt)