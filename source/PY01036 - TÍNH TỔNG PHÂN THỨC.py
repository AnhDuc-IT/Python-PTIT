from math import*
def change(a ,b):
    return a, b
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        total = 0
        if n % 2 == 0:
            for i in range(2, n + 1, 2):
                total += 1 / i
        else:
            for i in range(1, n + 1, 2):
                total += 1 / i
        print("{:.6f}".format(total))
        t -= 1

