from math import*
if __name__ == "__main__":
    a = []
    while(len(a) < 10):
        a.extend(map(int, input().split()))
    se = set(x % 42 for x in a)
    print(len(se))