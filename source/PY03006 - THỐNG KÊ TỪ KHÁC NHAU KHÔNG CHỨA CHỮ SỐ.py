import re
from collections import Counter
def check(s):
    for x in s:
        if '0' <= x and x <= '9':
            return False
    return True
if __name__ == "__main__":
    n = int(input())
    arr = {}
    for _ in range(n):
        for x in re.split("[^a-z]", input().lower()):
            if x != "":
                if arr.get(x) is None:
                    arr[x] = 1
                else:
                    arr[x] += 1
    res = sorted(arr, key = lambda x : (-arr[x], x))
    for x in res:
        if check(x):
            print(x, arr[x])