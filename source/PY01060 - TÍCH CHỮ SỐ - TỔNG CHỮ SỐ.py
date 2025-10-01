from math import*
def solution(n):
    ans, res = 1, 0
    for i in range(0, len(n), 2):
        if int(n[i]) != 0:
            ans *= int(n[i])
    for i in range(1,len(n), 2):
        res += int(n[i])
    return ans, res
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        p, q = solution(n)
        print(p, q)