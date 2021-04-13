def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def flashSort(arr, start, end, l):

    if end - start <= 4:
        arr[start:end] = bubbleSort(arr[start:end])

    else:
        flashSort(arr, 0, round(3 * l / 5), round(3 * l / 5))
        flashSort(arr, l - round(3 * l / 5), l, round(3 * l / 5))
        flashSort(arr, round(l / 5), l - round(l / 5), 3 * l // 5)


arr = [int(i) for i in input().split()]
n = len(arr)

flashSort(arr, 0, n, n)
print(arr)
