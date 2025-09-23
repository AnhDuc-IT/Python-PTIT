from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
def check(n):
    dem = [0] * 10
    for i in range(len(n) - 2):
        if n[i] != n[i + 2]: return False
        dem[int(n[i])] += 1
    dem[int(n[len(n) - 1])] += 1
    dem[int(n[len(n) - 2])] += 1
    cnt = 0
    for i in range(10):
        if dem[i] != 0:
            cnt += 1
    return cnt == 2

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a = input()
        n = list(map(int, a))
        m = n[::-1]
        temp = 0
        s = len(m)
        for i in range(s - 1):
            if m[i] + temp >= 5:
                temp = 1
                m[i] = 0
            else:
                m[i] = 0
                temp = 0
        if m[s - 1] + temp >= 10:
            m[s - 1] = 0
            m.append(1)
        else:
            m[s - 1] += temp
        n = m[::-1]
        for x in n:
            print(x, end = "")
        print("")
