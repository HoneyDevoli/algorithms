# O(log n)
def bi_search(list, num) -> bool:
    if len(list) == 1:
        return list[0] == num

    new_len = len(list) // 2
    if list[new_len] > num:
        return bi_search(list[:new_len], num)
    else:
        return bi_search(list[new_len:], num)


assert bi_search([1, 2, 3, 4, 5, 6, 7], 4) == True
assert bi_search([1, 2, 5, 6, 7], 5) == True
assert bi_search([1, 2, 5, 6, 7], 9) == False
