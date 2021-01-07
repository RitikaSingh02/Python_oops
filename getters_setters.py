class Employee:
    # here we made self as our instance or u can say a constructor is being created
    default_var = 123

    def __init__(self, first, last):  # this is run everytime we create an instance
        self.first = first
        self.last = last

    def fullname(self):  # a method
        return '{} {}'.format(self.first, self.last)

    @classmethod
    def alter_class_var(cls, var):
        cls.default_var = var

    @classmethod
    def form_instance(cls, string):
        first, last = string.split('-')
        return cls(first, last)  # this line creates the instance of class

    # use them when u dont want to have anything of the class or the instance its just that u want that func inside of that class (it works as a normal func)
    @staticmethod
    def working_day(day):
        if day.weekday() == 5 or day.weekday() == 6:  # i.e a sat or sun
            return False
        return True

    @property  # getters
    def fname(self):
        return self.first+self.last

    @fname.setter  # setters
    def fname(self, name):
        first, last = name.split(',')
        self.first, self.last = first, last

    @fname.deleter  # deleters
    def fname(self):
        print('delete')
        self.first = None
        self.last = None


emp = Employee('ritika', 'singh')
emp.first = "vartika"

# print(emp.first)  # vartika
# print(emp.fname)  # ritikasingh

# so the fname is not changed as the __init__ is not called again so it usses the prior stored values
# so to remove this prob we have property decoraters : getters,setters,deleters

# print(emp.fname)  # vartikasingh

# u can not assign property decoraters attribute
# emp.fname="vartikasingh"#incorrect

# so to solve this problem we use setter decorators and these setters can also update our initial values too

emp.fname = "natasha,romanoff"
print(emp.first)
print(emp.last)
print(emp.fname)

del emp.fname
print(emp.first)
print(emp.last)
