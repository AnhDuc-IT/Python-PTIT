from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        cnt = [0] * 1000000
        n = int(input())
        a = list(map(int ,input().split()))
        a.sort()
        max_ans = -1e9
        pos = 0
        for i in range(n):
            cnt[a[i]] += 1
            if(cnt[a[i]] > max_ans):
                max_ans = cnt[a[i]]
                pos = a[i]
        if max_ans > n / 2:
            print(pos)
        else:
            print("NO")