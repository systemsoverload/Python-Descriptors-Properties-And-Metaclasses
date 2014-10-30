from datetime import datetime


class Person(object):

    def get_age(self):
        return datetime.now().year - self.year_of_birth

    def set_age(self, new_age):
        self.year_of_birth = datetime.now().year - new_age

    age = property(get_age, set_age, None, "The calculated age of a Person instance")

    def __init__(self, first_name="John", last_name="Doe", year_of_birth=1979):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth

jd = Person()
assert jd.age == 35

jd.age = 44
assert jd.year_of_birth == 1970
