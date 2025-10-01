from math import*
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort()
        b.sort()
        check = True
        for i in range(n):
            if a[i] > b[i]:
                print("NO")
                check = False
                break
        if check:
            print("YES")