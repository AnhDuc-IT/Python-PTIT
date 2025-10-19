from collections import Counter
n, m = map(int, input().split())
arr = list(map(int, input().split()))
res = Counter(arr)
b = set(res.values())
if len(b) == 1:
    print("NONE")
else:
    b = sorted(b)
    ans = b[-2]
    for i in range(len(arr)):
        if res[arr[i]] == ans:
            print(arr[i])
            break