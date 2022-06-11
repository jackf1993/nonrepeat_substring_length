def checker(start, end):
    char = [0] * 128
    for i in range(start, end + 1):
        char[ord(s[i])] += 1
        if char[ord(s[i])] > 1:
            return False
    return True


s = "abcabcbb"

n = len(s)
res = 0

for i in range(n):
    for j in range(i, n):
        if checker(i, j):
            res = max(res, j - i + 1)
print(res)


