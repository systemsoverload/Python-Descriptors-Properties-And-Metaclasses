from datetime import datetime


class Person(object):

    def __init__(self, first_name="John", last_name="Doe",
                 year_of_birth=1979, salary=200, offspring=0):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.salary = salary
        self.offspring = offspring

    @property
    def age(self):
        return datetime.now().year - self.year_of_birth

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise ValueError("Only positive numbers allowed for age")
        self.year_of_birth = datetime.now().year - new_age

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Only positive numbers allowed for age")

        self._salary = value

    @property
    def offspring(self):
        return self._offspring

    @offspring.setter
    def offspring(self, value):
        if value < 0:
            raise ValueError("Only positive numbers allowed for age")
        self._offspring = value


    # ... etc ...
