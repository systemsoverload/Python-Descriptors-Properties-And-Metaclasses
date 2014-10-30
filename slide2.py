from datetime import datetime
class Person(object):

    def __init__(self, first_name="John", last_name="Doe", year_of_birth=1979):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth

    def get_age(self):
        return datetime.now().year - self.year_of_birth

    def set_age(self, age):
        self.year_of_birth = datetime.now().year - age

jd = Person()
assert jd.get_age() == 35

jd.set_age(44)
assert jd.year_of_birth == 1970
