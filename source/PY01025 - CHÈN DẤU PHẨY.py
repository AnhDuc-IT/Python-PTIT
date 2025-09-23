from math import*
def check(n):
    total = ord(n[0]) - ord('0')
    for i in range(1, len(n)):
        if(abs(ord(n[i]) - ord(n[i - 1])) != 2): return False
        total += ord(n[i]) - ord('0')
    if(total % 10 == 0): return True
    return False



if __name__ == "__main__":
    s = input()
    cnt = 0
    if(len(s) % 3 == 0):
        for i in range(len(s)):
            if(cnt % 3 == 0 and cnt != 0):
                print(",", end = '', sep = '')
            cnt += 1
            print(s[i], end = "", sep = "")
    elif(len(s) % 3 == 1):
        cnt = -1
        for i in range(len(s)):
            if((cnt % 3 == 0 or cnt == 0 ) and cnt != -1):
                print(",", end = '', sep = '')
            cnt += 1
            print(s[i], end = "", sep = "")
    else:
        cnt =- 2
        for i in range(len(s)):
            if((cnt % 3 == 0 ) and cnt != -2):
                print(",", end = '', sep = '')
            cnt += 1
            print(s[i], end = "", sep = "")
