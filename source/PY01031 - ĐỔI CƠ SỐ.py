def to_base(n, b):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        r = n % b
        if r < 10:
            digits.append(str(r))
        else:
            digits.append(chr(ord('A') + r - 10))
        n //= b
    return ''.join(reversed(digits))
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, b = map(int, input().split())
        print(to_base(n, b))