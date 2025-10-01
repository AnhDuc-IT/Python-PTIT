if __name__ == "__main__":
        s = input()
        if len(s) % 3 == 1:
            s = "00" + s
        else:
            s = "0" + s
        res = ""
        i = len(s) - 3
        while(i >= 0):
            temp = s[i: i + 3]
            res = str(int(temp, 2)) + res
            i -= 3
        print(res)