import re
from collections import Counter

if __name__ == "__main__":
    words = {}
    for _ in range(int(input())):
        for x in re.split("[^a-z0-9]", input().lower()):
            if x != '':
                if words.get(x) is None:
                    words[x] = 1
                else:
                    words[x] += 1
    res = sorted(words, key = lambda x : (-words[x], x))
    for x in res:
        print(x, words[x])