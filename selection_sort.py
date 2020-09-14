from typing import List


def find_smallest(arr: List[int]) -> int:
    min = arr[0]
    min_index = 0

    for index in range(1, len(arr)):
        if min > arr[index]:
            min = arr[index]
            min_index = index

    return min_index


# O(n^2)
def selection_sort(arr: List[int]) -> List[int]:
    result = []
    for x in range(len(arr)):
        min = find_smallest(arr)
        result.append(arr.pop(min))

    return result


print(selection_sort([3, 2, 2, -1, 6, 11, 15, 7]))
print(selection_sort([3, 2, -1]))
print(selection_sort([3, 2]))
