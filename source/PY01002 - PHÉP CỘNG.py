from math import*
if __name__ == "__main__":
    s = input()
    temp, a, b, c = 0, 0, 0, 0
    v = list()
    check = False
    for i in range(len(s)):
        if(s[i].isdigit()):
            temp = temp * 10 + int(s[i])
            check = True
        elif(check == True):
            v.append(temp)
            temp = 0
            check = False
    if(check):
        v.append(temp)
    if(v[0] + v[1] == v[2]):
        print("YES")
    else:
        print("NO")
