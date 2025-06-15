# Test Cat:

# class Cat:
#     def __init__(self, name):
#         self.name = name
#         self.fed = False
#         self.sleepy = False
#         self.size = 0

#     def eat(self):
#         if self.fed:
#             raise Exception('Already fed.')

#         self.fed = True
#         self.sleepy = True
#         self.size += 1

#     def sleep(self):
#         if not self.fed:
#             raise Exception('Cannot sleep while hungry')

#         self.sleepy = False

# Create a class CatTests

# * In Judge, you must submit just the CatTests class, with the unittest module imported and the main block.

# Create the following tests:

#     · The cat's size is increased after eating
#     · Cat is fed after eating
#     · Cat cannot eat if already fed, raises an error
#     · Cat cannot fall asleep if not fed, raises an error
#     · Cat is not sleepy after sleeping

# Hints:

# Follow the logic of the previous problem



class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):

        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):

        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False



from unittest import TestCase, main


class TestCat(TestCase):

    def setUp(self):
        self.cat = Cat("Tom")

    def test_init(self):
        self.assertEqual("Tom", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_cat_is_fed_eat_raises(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_eat(self):
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_sleep_if_not_fed_raises(self):
        self.assertFalse(self.cat.fed)

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


    def test_sleep(self):
        self.cat.fed = True
        self.cat.sleepy = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)




if __name__ == "__main__":
    main()
