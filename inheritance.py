class Employee:
    # here we made self as our instance or u can say a constructor is being created
    default_var = 123

    def __init__(self, first, last):  # this is run everytime we create an instance
        self.first = first
        self.last = last
        self.fname = first+last

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


class Developer(Employee):
    default_var = 2

    def __init__(self, first, last, lang):
        super().__init__(first, last)
        self.lang = lang


class Jrdeveloper(Developer):
    default_var = 3

    def __init__(self, first, last, lang, experience):
        super().__init__(first, last, lang)
        self.experience = experience


# dev = Developer('dev', '1', 'python')
# print(dev.__dict__)
# print(dev.default_var) #2

junior = Jrdeveloper('dev_', '2', 'python', '1')
# print(junior.default_var)
