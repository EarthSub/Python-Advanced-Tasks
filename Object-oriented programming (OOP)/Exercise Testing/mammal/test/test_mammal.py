

from project.mammal import Mammal

from unittest import TestCase, main


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("cat", "cats", "meow")


    def test_init(self):
        self.assertEqual("cat", self.mammal.name)
        self.assertEqual("cats", self.mammal.type)
        self.assertEqual("meow", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("cat makes meow", result)

    def test_get_kingdon(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual("cat is of type cats", self.mammal.info())


if __name__ == "__main__":
    main()
