from math import*
if __name__ == "__main__":
    s = input()
    while(len(s) > 1):
        mid = len(s) // 2
        m = s[:mid]
        n = s[mid:]
        k = int(n) + int(m)
        print(k)
        s = str(k)