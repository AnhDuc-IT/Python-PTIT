from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
def check(n):
    front, back = 0, 0
    for i in range(0, 3):
        front = front * 10 + int(n[i])
    for i in range(len(n) - 3, len(n)):
        back = back * 10 + int(n[i])
    return Prime(front) and Prime(back)
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        if(check(n)): print("YES")
        else: print("NO")