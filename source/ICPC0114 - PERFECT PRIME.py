from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
def check(n):
    m = n[::-1]
    total = 0
    for i in range(len(n)):
        temp = ord(n[i]) - ord('0')
        total += temp
        if(Prime(temp) == False): return False
    return Prime(int(n)) and Prime(int(m)) and Prime(total)
    
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = input()
        if check(n): print("Yes")
        else: print("No")
        t -= 1
