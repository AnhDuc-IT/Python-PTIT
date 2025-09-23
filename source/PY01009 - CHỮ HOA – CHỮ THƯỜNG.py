from math import*
if __name__ == "__main__":
    s = input()
    lower, upper = 0, 0
    for i in range(len(s)):
        if s[i].islower():
            lower += 1
        else:
            upper += 1
    if(lower >= upper):
        for i in range(len(s)):
            print(s[i].lower(), end = "")
    else:
        for i in range(len(s)):
            print(s[i].upper(), end = "")
