import math

# 1: 1
# 2: 0
# 3: 3 * (1)
# 4: 4 * (1 + 3)
# 5: 5 * (1 + 6 + 15  + (20 - 4) + 3) = (C(6,0) + C(6,1) + C(6,2) + (C(6,3) - 4) + (C(6,4) - 4*3))
# 6: 6 * (C(10,0) + C(10,1) + C(10,2) + C(10,3) +
# + (C(10,4) - 5) + (C(10,5) - 5 * 6) + (С(10,6) - 5*15) + (C(10,7) - ???))

n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(0)
else:
    res = 0
    k = (n - 1) * (n - 2) // 2
    for i in range(n - 2):
        res += math.comb(k, i)

    for i in range(n - 2, k - n // 2 + 1):
        temp = math.comb(k - n + 2, i - (n - 2))

        res += math.comb(k, i) - temp * (n - 1)

    print((res * n) % (10 ** 9 + 7))
