from math import*
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        s = input()
        ans, temp = -1e9, 0
        check = False
        for i in range(len(s)):
            if(s[i].isdigit()):
                temp = temp * 10 + int(s[i])
                check = True
            elif(check):
                ans = max(ans, temp)
                temp = 0
                check = False
        if(check):
            ans = max(ans, temp)
        print(ans)
        t -= 1
