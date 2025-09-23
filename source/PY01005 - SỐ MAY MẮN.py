from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1
def Gcd(a, b):
    return gcd(a, b)
if __name__ == "__main__":
    cnt = 0
    s = input()
    for i in range(len(s)):
        if(s[i] == '4' or s[i] == '7'):
            cnt += 1
    if(cnt == 4 or cnt == 7):
        print("YES")
    else:
        print("NO")
