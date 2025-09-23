from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return True
if __name__ == "__main__":
    s = list(map(str, input().split()))
    for x in s:
        print(x)
