# Could be done in a oneliner bin(int(a,2) + int(b,2))
from collections import deque


def add_binary(a: str, b: str) -> str:
    max_length = max(len(a), len(b))

    a_padded = a.zfill(max_length)
    b_padded = b.zfill(max_length)
    remainder: int = 0
    bit_list = deque()
    # We want to go from end, to beginning
    for i in range(max_length - 1, -1, -1):
        local_sum = int(a_padded[i]) + int(b_padded[i]) + remainder

        bit = "1" if local_sum % 2 else "0"

        remainder = 1 if local_sum > 1 else 0

        bit_list.insert(0, bit)

    if remainder:
        bit_list.insert(0, "1")

    return "".join(bit_list)
