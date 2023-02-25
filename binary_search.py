from typing import Sequence

def binary_search(value: int, seq: Sequence) -> int:
    left = 0
    right = len(seq) - 1
    while left <= right:
        mid = (right + left) // 2
        if seq[mid] == value:
            while seq[mid] == value:
                if 0 <= (mid - 1) < len(seq) and seq[mid - 1] == value:
                    mid -= 1
                else:
                    break
            return mid
        elif seq[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    raise ValueError(f'{value} в списке нет')


seq_ = [1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6]
print(binary_search(1, seq_))