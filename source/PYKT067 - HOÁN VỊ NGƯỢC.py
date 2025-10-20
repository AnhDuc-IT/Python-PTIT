def start():
    global arr, n
    for i in range(1, n + 1):
        arr[i] = i
def Generate():
    global arr, n, check
    i = n - 1
    while i >= 1 and arr[i] > arr[i + 1]:
        i -= 1
    if i == 0:
        check = False
    else:
        j = n
        while arr[i] > arr[j]:
            j -= 1
        arr[j], arr[i] = arr[i], arr[j]
        arr[i + 1:] = reversed(arr[i + 1:])
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = list(range(1, n + 1))
        arr = [0] * (n + 1)
        start()
        check = True
        res = []
        while check:
            ans = "".join(str(a[arr[i] - 1]) for i in range(1, n + 1))
            res.append(ans)
            Generate()
        print(len(res))
        res = reversed(res)
        for x in res:
            print(x, end = " ")
        print()