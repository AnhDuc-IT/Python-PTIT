n = int(input())
arr = list(map(int, input().split()))
res = max(arr)
cnt, lenght = 0, 0
for x in arr:
    if x == res:
        cnt += 1
        lenght = max(lenght, cnt)
    else:
        cnt = 0
print(lenght)
