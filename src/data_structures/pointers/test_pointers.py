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
                 [None, 0, 4, None, 0, 7, None, 0, 10, None, 0, 13, None, 0, 16, None, 0, 19, None, 0, 22, None, 0, None])

        self.assertEqual(list_1.capacity(), 8)

    def test_push(self):
        list_1 = LinkedListSingleArray(capacity=3)
        self.assertListEqual(list_1._buffer,
                             [None, 0, 4, None, 0, 7, None, 0, None])

        list_1.push('A')

        self.assertListEqual(list_1._buffer,
                             [None, 'A', None, None, 0, 7, None, 0, None])

        list_1.push('B')


if __name__ == '__main__':
    unittest.main()
