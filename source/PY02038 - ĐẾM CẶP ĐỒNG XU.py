from math import*
if __name__ == "__main__":
    n = int(input())
    a = []
    column = [0] * n
    row = [0] * n
    for i in range(n):
        b = input()
        a.append(b)
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'C':
                row[i] += 1
    for j in range(n):
        for i in range(n):
            if a[i][j] == 'C':
                column[j] += 1
    res = 0
    for i in range(n):
        res += comb(column[i], 2)
        res += comb(row[i], 2)
    print(res)

# derivative: dẫn xuất, phát sinh