from email.mime import base
from math import*
def Recursion(s, b):
    if(s == 0): return
    Recursion(s // b, b)
    temp = s % b
    if temp < 10:
        print(temp, end = "")
    else:
        print(chr(ord('A') + temp - 10), end = "")
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        b = int(input())
        s = input()
        res = int(s, 2)
        if res == 0:
            print("0")
        else:
            Recursion(res, b)
        print()