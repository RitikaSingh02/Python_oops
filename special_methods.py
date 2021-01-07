class Employee:
    # here we made self as our instance or u can say a constructor is being created
    default_var = 123

    def __init__(self, first, last, pay):  # this is run everytime we create an instance
        self.first = first
        self.last = last
        self.fname = first+last
        self.pay = pay

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

    def __add__(first, second):
        return first.pay+second.pay


# whenever we try to create an instance like here emp_1 the instance argument self is passed automatically to the __init__ method
emp_1 = Employee('ritika', 'singh', 400)
emp_2 = Employee('vartika', 'singh', 800)

print(Employee.__add__(emp_1, emp_2))  # 1200
print(emp_1+emp_2)  # 1200
