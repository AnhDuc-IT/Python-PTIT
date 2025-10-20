def check(arr):
    for x in arr:
        if x < 0 or x > 255:
            return False
    return len(arr) == 4
for _ in range(int(input())):
    try:
        arr = list(map(int, input().split('.')))
        if check(arr):
            print("YES")
        else:
            print("NO")
    except:
        print("NO")