class Field(object):
    def __init__(self, value=None, null=False, name=None, label_field=False, default=None):
        self._value = value
        self._null = null
        self._name = name
        self.default = default
        self.data = dict()

    def __str__(self):
        return u'{0}: {1}'.format(self.__class__.__name__, self._value)

    def __repr__(self):
        return ('<{0}: {1}>').format(self.__class__.__name__, self._name)

    def __setitem__(self, name, value):
        setattr(self, name, value)

    @property
    def value(self):
        return self._value

    @property
    def null(self):
        return self._null

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.setter
    def name(self, value):
        self._name = value

    def __get__(self, instance, owner):
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):
        self.data[instance] = value


class Options(object):

    def __init__(self, meta=None):
        if meta:
            self.verbose_name = meta.verbose_name

    def get_field_by_name(self, name):
        match = None
        for f in self.fields:
            if f.name == name:
                match = f
        return match

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, value):
        self._fields = value


class ModelBase(type):
    def __new__(cls, name, bases, dct):
        # Create a new instance of our type so we can start attaching things to it.
        # This will eventually be the bits returned by this function
        super_new = super(ModelBase, cls).__new__(cls, name, bases, dct)

        # Create a new _meta object and process `class Meta`
        meta = dct.pop('Meta', None)
        _meta = Options(meta)

        # Process fields and attach them to meta, give them a friendly name attr as well
        _meta.fields = []
        for nme, attr in super_new.__dict__.iteritems():
            if isinstance(attr, Field):
                attr['name'] = nme
                _meta.fields.append(attr)

        # Attach the _meta directly to the type we are returning, this gives us
        # the django-like ability to do inspect fields on the class and instances
        super_new._meta = _meta
        return super_new


class Model(object):
    __metaclass__ = ModelBase


class Person(Model):
    first_name = Field(null=False)
    last_name = Field()

    class Meta:
        verbose_name = "My Model"

    def __repr__(self):
        return "<Person: {} {}>".format(self.first_name, self.last_name)


tj = Person()

tj.first_name = "TJ"
tj.last_name = "Kells"
print(tj)
