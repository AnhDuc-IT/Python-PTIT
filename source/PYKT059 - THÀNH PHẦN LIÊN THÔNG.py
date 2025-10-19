n, m, z = map(int, input().split())
ke = [[] for i in range(0, n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    ke[x].append(y)
    ke[y].append(x)
visited, q = [0] * (n + 1), [z]
visited[z] = 1
while len(q) > 0:
    u = q.pop()
    for i in ke[u]:
        if visited[i] == 0:
            q.append(i)
            visited[i] = 1
check = True
for i in range(1, n + 1):
    if visited[i] == 0:
        print(i)
        check = False
if check:
    print(0)