from list.project.extended_list import IntegerList

from unittest import TestCase, main


class TestIntegersList(TestCase):
    def setUp(self):
        self.cl = IntegerList(1, 2, 3)

    def test_init_int_values(self):
        self.assertEqual([1, 2, 3], self.cl._IntegerList__data)

    def test_init_non_integers_are_skipped(self):
        new_list = IntegerList("asd", 4.8, [1, 2, 3], 5)
        self.assertEqual([5], new_list._IntegerList__data)

    def test_get_data_return_private__data(self):
        result = self.cl.get_data()

        self.assertEqual([1, 2, 3], result)
        self.assertIs(self.cl._IntegerList__data, result)

    def test_add_not_integer_raises(self):
        self.assertEqual([1, 2, 3], self.cl._IntegerList__data)

        with self.assertRaises(ValueError) as ex:
            self.cl.add("da")
            self.cl.add(3.14)
            self.cl.add([1, 2, 3])

        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual([1, 2, 3], self.cl._IntegerList__data)

    def test_add_integer(self):
        self.assertEqual([1, 2, 3], self.cl._IntegerList__data)

        result = self.cl.add(5)

        self.assertEqual([1, 2, 3, 5], self.cl._IntegerList__data)

        self.assertIs(self.cl._IntegerList__data, result)

    def test_remove_index_invalid_index_raises(self):
        length_index = len(self.cl._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.cl.remove_index(length_index)
            length_index += 1
            self.cl.remove_index(length_index)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index(self):
        self.assertEqual([1, 2, 3], self.cl._IntegerList__data)

        result = self.cl.remove_index(1)
        self.assertEqual(2, result)

        self.assertListEqual([1, 3], self.cl._IntegerList__data)
        self.assertNotIn(2, self.cl._IntegerList__data)

    def test_get_element_by_invalid_index_raises(self):
        length_index = len(self.cl._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.cl.get(length_index)
            length_index += 1
            self.cl.get(length_index)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_element_by_index_(self):
        self.assertEqual([1, 2, 3], self.cl._IntegerList__data)

        result = self.cl.get(1)

        self.assertEqual(2, result)
        self.assertListEqual([1, 2, 3], self.cl._IntegerList__data)

    def test_invalid_valid_index_insert_raises(self):
        length_index = len(self.cl._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.cl.insert(length_index, 5)
            length_index += 1
            self.cl.insert(length_index, 4)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_invalid_element_raises(self):
        element = "dada"

        with self.assertRaises(ValueError) as ex:
            self.cl.insert(0, element)
            element = 3.14
            self.cl.insert(0, element)
            element = [1, 3, 5]
            self.cl.insert(0, element)

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert(self):
        self.assertEqual([1, 2, 3], self.cl._IntegerList__data)

        result = self.cl.insert(0, 7)

        self.assertIsNone(result)

        self.assertListEqual([7, 1, 2, 3], self.cl._IntegerList__data)

    def test_get_biggest(self):
        new_list = IntegerList(3, 7, 9, 13, 5, 1)

        result = new_list.get_biggest()

        self.assertEqual(13, result)

    def test_get_index(self):
        self.assertIn(1, self.cl._IntegerList__data)
        self.assertEqual(1,self.cl._IntegerList__data[0])

        result = self.cl.get_index(1)

        self.assertEqual(0, result)


if __name__ == "__main__":
    main()
