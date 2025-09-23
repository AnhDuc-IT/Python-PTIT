from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return True
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        s = input()
        temp = s[0]
        cnt = 0
        for i in range(len(s)):
            if(s[i] == temp):
                cnt += 1
            else:
                print(cnt, temp,  sep = "", end = "")
                cnt = 1
                temp = s[i]
        print(cnt, temp, sep = "")
        t -= 1
