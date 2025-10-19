def getResult(arr):
    return max(arr), min(arr)


if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        arr = []
        for i in range(n):
            arr.append(int(input()))
        if getResult(arr)[0] == getResult(arr)[1]:
            print("BANG NHAU")
        else:
            print(getResult(arr)[1], getResult(arr)[0])