arr = []
for _ in range(int(input())):
    line = input()
    for x in line:
        if not x.isdigit():
            line = line.replace(x, " ")
    a = line.split()
    for x in a:
        arr.append(int(x))
arr.sort()
for x in arr:
    print(x)