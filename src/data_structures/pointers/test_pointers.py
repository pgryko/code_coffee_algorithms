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
                             [0, 0, 4, 0, 0, 7, 0, 0, 10, 0, 0, 13, 0, 0, 16, 0, 0, 19, 0, 0, 22, 0, 0, 25, 0, 0, 28, 0,
                              0, 31, 0, 0, 34, 0, 0, 37, 0, 0, 40, 0, 0, 43, 0, 0, 46, 0, 0, 49, 0, 0, 52, 0, 0, 55, 0,
                              0, 58, 0, 0, None])

        self.assertEqual(list_1.capacity(), 20)

        list_2 = LinkedListSingleArray(capacity=5)

        self.assertListEqual(list_2._buffer,
                             [0, 0, 4, 0, 0, 7, 0, 0, 10, 0, 0, 13, 0, 0, None])

        self.assertEqual(list_2.capacity(), 5)

    def test_resize(self):
        list_1 = LinkedListSingleArray(capacity=2)
        self.assertListEqual(list_1._buffer,
                             [0, 0, 4, 0, 0, None])

        self.assertEqual(list_1.capacity(), 2)

        list_1._resize()

        self.assertListEqual(list_1._buffer,
                             [0, 0, 4, 0, 0, 7, 0, 0, 10, 0, 0, None])

        self.assertEqual(list_1.capacity(), 4)

        list_1._resize()

        self.assertListEqual(list_1._buffer,
                             [0, 0, 4, 0, 0, 7, 0, 0, 10, 0, 0, 13, 0, 0, 16, 0, 0, 19, 0, 0, 22, 0, 0, None])

        self.assertEqual(list_1.capacity(), 8)


if __name__ == '__main__':
    unittest.main()
