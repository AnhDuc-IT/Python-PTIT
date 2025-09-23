from math import*
def check(n):
    total = ord(n[0]) - ord('0')
    for i in range(1, len(n)):
        if(abs(ord(n[i]) - ord(n[i - 1])) != 2): return False
        total += ord(n[i]) - ord('0')
    if(total % 10 == 0): return True
    return False



if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = input()
        if(check(n) == True):
            print("YES")
        else: print("NO")
        t -=1
