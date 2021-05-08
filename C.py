n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = sorted(a)
p1, p2 = 0, k + 1
mydict = {}
temp = sum(b[:p2]) - b[0] * p2
mydict[b[0]] = temp

for i in range(1, n):
    temp += (b[i] - b[i - 1]) * (2 * i - p1 - p2)
    while i == p2 or (p1 < i and p2 < n and b[p2] - b[i] <= b[i] - b[p1]):
        temp -= (b[i] - b[p1]) - (b[p2] - b[i])
        p1, p2 = p1+1, p2+1
    mydict[b[i]] = temp

for i in a:
    print(mydict[i], end=' ')
