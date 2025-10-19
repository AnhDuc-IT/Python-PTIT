
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = sorted(set(a))
b = sorted(set(b))
if len(a) != len(b):
    print("NO")
else:
    check = False
    for i in range(len(a)):
        if a[i] != b[i]:
            print("NO")
            check = True
            break
    if not check:
        print("YES")