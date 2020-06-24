# О(logn * n)
def qsort(arr):
    if len(arr) < 2:
        return arr

    mid = arr[0]

    less = []
    greater = []

    for num in arr[1:]:
        if num >= mid:
            greater.append(num)
        else:
            less.append(num)
    return qsort(less) + [mid] + qsort(greater)


arr = [3, 2, 2, 2, 5, -1, -3]
print(qsort(arr))
