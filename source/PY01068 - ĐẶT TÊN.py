def start():
    global arr, k
    for i in range(1, k + 1):
        arr[i] = i
def Generate():
    global arr, n, k, check
    i = k 
    while i >= 1 and arr[i] == n - k + i:
        i -= 1
    if i == 0:
        check = False
    else:
        arr[i] += 1
        for j in range(i + 1, k + 1):
            arr[j] = arr[j - 1] + 1
if __name__ == "__main__":
    n, k = map(int, input().split())
    a = sorted(set(input().split()))
    check = True
    n = len(a)
    arr = [0] * (n + 1)
    start()
    while check:
        for i in range(1, k + 1):
            print(a[arr[i] - 1], end = " ")
        print()
        Generate()