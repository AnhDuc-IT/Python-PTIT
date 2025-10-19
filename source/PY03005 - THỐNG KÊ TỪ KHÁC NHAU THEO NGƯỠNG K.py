import re
from collections import Counter

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = {}
    for _ in range(n):
        for x in re.split("[^a-z0-9]", input().lower()):
            if x != "":
                if arr.get(x) is None:
                    arr[x] = 1
                else:
                    arr[x] += 1
    res = sorted(arr, key = lambda x : (-arr[x], x))
    for x in res:
        if arr[x] >= k:
            print(x, arr[x])
