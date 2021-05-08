n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
if a != b:
    print(-1)
else:
    print(b[-1]-b[0])
