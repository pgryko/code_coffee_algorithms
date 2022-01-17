# Uses heap's algorithm to generate a permutation of elements in a list
# Note this is not an optimal solution
from typing import List


def permutate(arrayin: List):
    # def _permutate(n: int, array: List):
    #
    #     if n < 1:
    #         yield array
    #     else:
    #         for i in range(0, n):
    #             yield from _permutate(n - 1, array)
    #             if n % 2 == 0:
    #                 array[i], array[n - 1] = array[n - 1], array[i]
    #             else:
    #                 array[0], array[n - 1] = array[n - 1], array[0]
    #
    # yield from _permutate(len(array), array)

    def _permutate(n: int, array: List):
        if n < 1:
            yield array
        else:
            for i in range(0, n):
                yield from _permutate(n - 1, array)
                if n % 2 == 0:
                    array[i], array[n - 1] = array[n - 1], array[i]
                else:
                    array[0], array[n - 1] = array[n - 1], array[0]

    yield from _permutate(len(arrayin), arrayin)

if __name__ == '__main__':
    # permutate(['a','b','c','d'])
    # print('stuff')
    for element in permutate(['a', 'b', 'c', 'd']):
        print(element)
