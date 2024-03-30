from datetime import timedelta
import unittest
from student import Student
from unittest.mock import patch


class StudentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print("\nRunning setUp method...")
        self.student = Student("george","smith")

    def tearDown(self):
        print("Running tearDown method...")

    def test_student_name(self):
        self.assertEqual(self.student.full_name, "george smith")

    def test_alert_santa(self):
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_student_email(self):
        self.assertEqual(self.student.student_email, "george.smith@email.com")
    
    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)

        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))

    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule,"Success")

    def test_course_schedule_failed(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule,"something went wrong")



if __name__ == "__main__":
    unittest.main()