from math import*
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 1
    a.sort()
    for i in range(len(a)):
        if(a[i] == cnt):
            cnt += 1
    print(cnt)