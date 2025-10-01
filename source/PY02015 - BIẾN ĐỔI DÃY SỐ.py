from math import*
def all_equal(a):
    return a[0] == a[1] == a[2] == a[3]

if __name__ == "__main__":
    while True:
        a = list(map(int, input().split()))
        if a == [0, 0, 0, 0]: break
        step = 0
        while not all_equal(a):
            b = [0] * 4
            for i in range(3):
                b[i] = abs(a[i] - a[i + 1])
            b[3] = abs(a[3] - a[0])
            step += 1
            a = b
        print(step)