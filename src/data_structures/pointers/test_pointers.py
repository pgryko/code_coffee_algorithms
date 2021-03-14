import copy
import unittest

from pointers import LinkedListSingleArray


class TestLinkedListSingleArray(unittest.TestCase):
    ''' Test behaviour of linked list implement inside an allocated buffer array
    '''

    def test_initialise(self):
        '''Test that initial array is initialised correctly
        '''

        list_1 = LinkedListSingleArray()

        self.assertListEqual(list_1._buffer,
                             [None, 0, 4, None, 0, 7, None, 0, 10, None, 0, 13, None, 0, 16, None, 0, 19, None, 0, 22,
                              None, 0, 25, None, 0, 28, None, 0, 31, None, 0, 34, None, 0, 37, None, 0, 40, None, 0, 43,
                              None, 0, 46, None, 0, 49, None, 0, 52, None, 0, 55, None, 0, 58, None, 0, None])

        self.assertEqual(list_1.capacity(), 20)

        list_2 = LinkedListSingleArray(capacity=5)

        self.assertListEqual(list_2._buffer,
                             [None, 0, 4, None, 0, 7, None, 0, 10, None, 0, 13, None, 0, None])
        self.assertEqual(list_2.capacity(), 5)

    def test_resize(self):
        list_1 = LinkedListSingleArray(capacity=2)
        self.assertListEqual(list_1._buffer,
                             [None, 0, 4, None, 0, None])

        self.assertEqual(list_1.capacity(), 2)

        list_1._resize()

        self.assertListEqual(list_1._buffer,
                             [None, 0, 4, None, 0, 7, None, 0, 10, None, 0, None])

        self.assertEqual(list_1.capacity(), 4)

        list_1._resize()

        self.assertListEqual(list_1._buffer,
                             [None, 0, 4, None, 0, 7, None, 0, 10, None, 0, 13, None, 0, 16, None, 0, 19, None, 0, 22,
                              None, 0, None])

        self.assertEqual(list_1.capacity(), 8)

    def test_push(self):
        list_1 = LinkedListSingleArray(capacity=3)
        self.assertListEqual(list_1._buffer,
                             [None, 0, 4, None, 0, 7, None, 0, None])

        self.assertEqual(len(list_1), 0)

        list_1.push('A')

        self.assertListEqual(list_1._buffer,
                             [None, 'A', None, None, 0, 7, None, 0, None])

        self.assertEqual(len(list_1), 1)

        list_1.push('B')

        self.assertListEqual(list_1._buffer,
                             [4, 'A', None, None, 'B', 1, None, 0, None])
        self.assertEqual(len(list_1), 2)

        list_1.push('C')

        self.assertListEqual(list_1._buffer,
                             [4, 'A', None, 7, 'B', 1, None, 'C', 4])

        self.assertEqual(len(list_1), 3)
        self.assertEqual(list_1.capacity(), 3)

        # List should be at max capacity, so check that free index is zero
        self.assertEqual(list_1._free_index, None)

        list_1.push('D')

        # This should resize the list, doubling the capacity
        self.assertEqual(list_1.capacity(), 6)

        self.assertEqual(len(list_1), 4)

        self.assertListEqual(list_1._buffer,
                             [4, 'A', None, 7, 'B', 1, 10, 'C', 4, None, 'D', 7, None, 0, 16, None, 0, None])

    def test_pop(self):
        list_1 = LinkedListSingleArray(capacity=3)
        list_1.push('A')
        list_1.push('B')
        list_1.push('C')
        list_1.push('D')

        self.assertListEqual(list_1._buffer,
                             [4, 'A', None, 7, 'B', 1, 10, 'C', 4, None, 'D', 7, None, 0, 16, None, 0, None])

        self.assertEqual(list_1.capacity(), 6)
        self.assertEqual(len(list_1), 4)

        self.assertEqual(list_1.pop(), 'D')
        self.assertEqual(list_1.capacity(), 6)
        self.assertEqual(len(list_1), 3)

        self.assertListEqual(list_1._buffer,
                             [4, 'A', None, 7, 'B', 1, 10, 'C', 4, None, 0, 13, None, 0, 16, None, 0, None])

        self.assertEqual(list_1.pop(), 'C')
        self.assertEqual(len(list_1), 2)

        self.assertEqual(list_1.pop(), 'B')
        self.assertEqual(len(list_1), 1)

        # We want to test behaviour of pushing after pop
        list_2 = copy.deepcopy(list_1)

        self.assertEqual(list_1.pop(), 'A')
        self.assertEqual(len(list_1), 0)

        with self.assertRaises(IndexError):
            list_1.pop()

        self.assertListEqual(list_1._buffer,
                             [None, 0, 4, None, 0, 7, None, 0, 10, None, 0, 13, None, 0, 16, None, 0, None]
                             )

        list_1.push('A')

        self.assertListEqual(list_1._buffer,
                             [None, 'A', None, None, 0, 7, None, 0, 10, None, 0, 13, None, 0, 16, None, 0, None])

        list_1.push('B')
        list_2.push('B')

        self.assertListEqual(list_1._buffer,
                             list_2._buffer)

        self.assertEqual(list_1._buffer,
                         [4, 'A', None, None, 'B', 1, None, 0, 10, None, 0, 13, None, 0, 16, None, 0, None])

    def test_next(self):
        list_1 = LinkedListSingleArray(capacity=3)
        list_1.push('A')
        list_1.push('B')
        list_1.push('C')
        list_1.push('D')

        forward_iterator = list_1.__next__()

        self.assertEqual(next(forward_iterator), 'D')
        self.assertEqual(next(forward_iterator), 'C')
        self.assertEqual(next(forward_iterator), 'B')
        self.assertEqual(next(forward_iterator), 'A')
        self.assertRaises(StopIteration, forward_iterator.__next__)

    def test_iterator(self):
        list_1 = LinkedListSingleArray(capacity=3)
        list_1.push('A')
        list_1.push('B')
        list_1.push('C')
        list_1.push('D')

        iterator = iter(list_1)
        self.assertEqual(next(iterator), 'D')
        self.assertEqual(next(iterator), 'C')
        self.assertEqual(next(iterator), 'B')
        self.assertEqual(next(iterator), 'A')
        self.assertRaises(StopIteration, iterator.__next__)

    def test_prev(self):
        list_1 = LinkedListSingleArray(capacity=3)
        list_1.push('A')
        list_1.push('B')
        list_1.push('C')
        list_1.push('D')

        reverse_iterator = list_1.__prev__()

        self.assertEqual(next(reverse_iterator), 'A')
        self.assertEqual(next(reverse_iterator), 'B')
        self.assertEqual(next(reverse_iterator), 'C')
        self.assertEqual(next(reverse_iterator), 'D')
        self.assertRaises(StopIteration, reverse_iterator.__next__)


if __name__ == '__main__':
    unittest.main()
