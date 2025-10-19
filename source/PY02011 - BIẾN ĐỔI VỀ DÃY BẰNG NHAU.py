from math import*
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    res = float("infinity")
    value = 0
    for i in range(n):
        total = 0
        for j in range(n):
            total = total + abs(arr[i] - arr[j])
        if total < res:
            value = arr[i]
            res = total
    print(res, value)