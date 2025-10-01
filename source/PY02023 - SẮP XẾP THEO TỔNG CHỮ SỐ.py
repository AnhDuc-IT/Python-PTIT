from functools import cmp_to_key
from math import*
def sum_digit(n):
    total = 0
    while n != 0:
        total += n % 10
        n //= 10
    return total
def cmp(a, b):
    if(sum_digit(a) == sum_digit(b)):
        return a - b
    return sum_digit(a) - sum_digit(b)
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort(key = cmp_to_key(cmp))
        for x in a:
            print(x, end = " ")
        print()