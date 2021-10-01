# Lazy Initialization

___
LazyInit() work as Metaclass to automatically transform
the future class [class using this metaclass] parameter
to self attributes.
___

    Example:

        class Person(metaclass=LazyInit):
            def __init__(self, name, age): pass

    Will Equivalent to:

        class Person(metaclass=LazyInit):
            def __init__(self, name, age): 
                self.name = name
                self.age = age



## DISCLAIMER!
    no guarantee of completeness, accuracy, timeliness or 
    of the results obtained from the use of this information

### For more information:
	Visit [Wikipedia](https://en.wikipedia.org/wiki/Metaclass)