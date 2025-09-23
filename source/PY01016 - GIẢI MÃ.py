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
        for i in range(len(s)):
            temp = s[i - 1]
            if s[i].isdigit():
                for j in range(ord(s[i]) - ord('0')):
                    print(temp, end = "", sep = "")
        print("")
        t -= 1
