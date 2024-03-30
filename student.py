from datetime import date, timedelta
import requests

class Student:
    """ A Student class as a basis for method testing """

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False
        self.list = 10
    
    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"
    
    def alert_santa(self):
        self.naughty_list = True

    @property
    def student_email(self):
        return f"{self._first_name}.{self._last_name}@email.com"
    
    def apply_extension(self,days):
        self.end_date = self.end_date + timedelta(days = days)

    def course_schedule(self):
        response = requests.get(f"http://company.com/course-schedule/{self._last_name}/{self._first_name}")

        if response.ok:
            return response.text
        else:
            return "something went wrong"

if __name__ == "__main__":
    # Create a new Student instance
    my_student = Student("George", "Smith")

    # Call the `apply_extension` method to print the value of `end_date`
    my_student.apply_extension()

