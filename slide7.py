from datetime import datetime


class PersonMeta(type):
    def __new__(cls, name, bases, attrs):
        for n, v in attrs.items():
            if isinstance(v, NonNegative):
                v.label = n

        return super(PersonMeta, cls).__new__(cls, name, bases, attrs)


class NonNegative(object):
    """A descriptor that forbids negative values"""
    def __init__(self, default):
        self.default = default
        self.data = dict()

    def __get__(self, instance, owner):
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Only positive numbers allowed for age")
        self.data[instance] = value


class Person(object):

    year_of_birth = NonNegative(40)
    salary = NonNegative(200)
    offspring = NonNegative(0)

    def __init__(self, first_name="John", last_name="Doe",
                 year_of_birth=1979, salary=200, offspring=0):
        self.first_name = first_name
        self.last_name = last_name
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


jd = Person()
jd.salary = 10000
