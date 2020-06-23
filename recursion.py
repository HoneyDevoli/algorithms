def my_sum(list):
    if not list:
        return 0
    return list[0] + my_sum(list[1:])


def my_count(list):
    if list == []:
        return 0
    return 1 + my_count(list[1:])


def my_max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = my_max(list[1:])
    return list[0] if list[0] > sub_max else sub_max


assert sum([3, 2, 2, 5]) == 12
assert my_count([3, 2, 5, 2, 1]) == 5
assert my_max([1, 2, 4, 5, 6, 1, 2]) == 6
