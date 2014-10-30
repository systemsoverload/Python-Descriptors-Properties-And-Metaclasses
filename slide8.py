class Foo(object):
    pass

type(1) == int
type('foo') == str
type(123.456) == float
type({}) == dict
type([]) == list
type(int) == type
type(str) == type
type()
type(Foo) == type
# Wait... wat?
