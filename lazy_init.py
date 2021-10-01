"""
LazyInit() work as Metaclass to automatically transform
the future class [class using this metaclass] parameter
to self attributes.

Example:

    class Person(metaclass=LazyInit):
        def __init__(self, name, age): pass

Will Equivalent to:

    class Person(metaclass=LazyInit):
        def __init__(self, name, age): 
            self.name = name
            self.age = age
"""

class LazyInit(type):
    def __call__(self, *args, **kwargs):
        varnames = list(self.__init__.__code__.co_varnames)[1:]
        for i, name in enumerate(varnames):
            setattr(self, name, args[i])
        return self


if __name__ == "__main__":
    print(__doc__)
    print("Testing for " + __file__)

    class Person(metaclass=LazyInit):
        def __init__(self, name, age): pass

    class Circle(metaclass=LazyInit):
        def __init__(self, x, ray): pass

    a_person = Person('Luke', 21)
    a_circle = Circle(1,5)

    print(a_person.name == "Luke" and a_person.age == 21)
    print(a_circle.x == 1 and a_circle.ray == 5)