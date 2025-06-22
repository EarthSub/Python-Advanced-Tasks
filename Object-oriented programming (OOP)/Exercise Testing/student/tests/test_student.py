
from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student1 = Student("Student 1",
                                {"Python": ["note 1", "note 2"],
                                 "JS": ["note 1"]})
        self.student2 = Student("Student 2")

    def test_init_with_courses(self):
        self.assertEqual("Student 1", self.student1.name)
        self.assertEqual({"Python": ["note 1", "note 2"],
                          "JS": ["note 1"]}, self.student1.courses)
        self.assertIsInstance(self.student1.name, str)
        self.assertIsInstance(self.student1.courses, dict)

    def test_init_without_courses(self):
        self.assertEqual("Student 2", self.student2.name)
        self.assertEqual({}, self.student2.courses)
        self.assertIsInstance(self.student2.name, str)
        self.assertIsInstance(self.student2.courses, dict)

    def test_enroll_in_existing_course(self):
        result = self.student1.enroll("Python", ["Note 3", "Note 4"], "Y")

        self.assertEqual({"Python": ["note 1", "note 2", "Note 3", "Note 4"],
                          "JS": ["note 1"]}, self.student1.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

        result = self.student1.enroll("Python", ["Note 5", "Note 6"], "N")

        self.assertEqual({"Python": ["note 1", "note 2", "Note 3", "Note 4", "Note 5", "Note 6"],
                          "JS": ["note 1"]}, self.student1.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_in_not_existing_course_adding_notes_with_empty_str(self):
        result = self.student1.enroll("Java", ["Note 1, Note 2"], "")

        self.assertIn("Java", self.student1.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["Note 1, Note 2"], self.student1.courses["Java"])

    def test_enroll_in_not_existing_course_adding_notes_with_empty_Y(self):
        result = self.student1.enroll("Java", ["Note 1, Note 2"], "Y")

        self.assertIn("Java", self.student1.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["Note 1, Note 2"], self.student1.courses["Java"])

    def test_enroll_in_not_existing_course_not_adding_notes(self):
        result = self.student2.enroll("Java", ["Note 1, Note 2"], "N")

        self.assertIn("Java", self.student2.courses)
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student2.courses["Java"])

    def test_add_notes_to_existing_course(self):
        self.student2.enroll("Java", ["Note 1, Note 2"])
        result = self.student2.add_notes("Java", "Note 3")

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["Note 1, Note 2", "Note 3"], self.student2.courses["Java"])

    def test_add_notes_to_note_existing_course_raises_ex(self):
        with self.assertRaises(Exception) as ex:
            self.student2.add_notes("Python", "Note 1")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):
        result = self.student1.leave_course("JS")

        self.assertEqual("Course has been removed", result)
        self.assertNotIn("JS", self.student1.courses)

    def test_leave_not_existing_course_raises_ex(self):
        with self.assertRaises(Exception) as ex:
            self.student1.leave_course("Java")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))



if __name__ == "__main__":
    main()
