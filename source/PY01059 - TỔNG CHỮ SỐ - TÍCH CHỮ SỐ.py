from math import*
def solution(n):
    ans, res = 0, 1
    check = False
    for i in range(0, len(n), 2):
        ans += int(n[i])
    for i in range(1, len(n), 2):
        if int(n[i]) != 0:
            check = True
            res *= int(n[i])
    if(check):
        return ans, res
    else:
        return ans, 0
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        print(solution(n)[0], solution(n)[1])