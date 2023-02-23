from typing import Sequence

def binary_search(value: int, seq: Sequence) -> int:
    left = 0
    right = len(seq) - 1
    while left <= right:
        mid = (right + left) // 2
        if seq[mid] == value:
            while seq[mid] == value:
                if not 0 < (mid - 1) < len(seq) or seq[mid - 1] != value:
                    break
                else:
                    mid -= 1
            return mid
        if seq[mid] < value:
            left = mid + 1
        elif seq[mid] > value:
            right = mid - 1
    raise ValueError(f'{value} в списке нет')


# seq_ = [1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6]
# print(binary_search(3, seq_))