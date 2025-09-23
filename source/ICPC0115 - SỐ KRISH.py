from math import*
def check(n):
    total = 0
    temp = n
    while(temp > 0):
        total += factorial(temp % 10)
        temp //= 10
    return total == n
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        if(check(n)): print("Yes")
        else: print("No")
