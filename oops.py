###correct###

# class Employee:
#     pass


# emp_1 = Employee()  # instance of employee
# emp_1.first = "ritika"
# emp_1.last = "singh"
# print(emp_1.first)

# variables:attributes
##functions : method
import datetime


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


# whenever we try to create an instance like here emp_1 the instance argument self is passed automatically to the __init__ method
emp_1 = Employee('ritika', 'singh')
# print(emp_1.fullname)
# <bound method Employee.fullname of <__main__.Employee object at 0x7f8adb755eb0>>

# print(emp_1.fullname())  # whenerver a method of an object is called then the instance emp_1 is passed as self automatically so in the func definition u will always have to mention the self argument as it is always passed
# ritika singh

# print('{} {}'.format(emp_1.first, emp_1.last))

# print(Employee.__dict__) #prints the whole namespace

# Employee.alter_class_var(2)
# print(emp_1.default_var)  # 2
# print(Employee.default_var)  # 2

# so using class methods we can let the instances of the class too change the val of the class variables
# emp_1.alter_class_var(2)
# print(emp_1.default_var)  # 2
# print(Employee.default_var)  # 2

# print(Employee.form_instance("vartika-singh").__dict__)
#{'first': 'vartika', 'last': 'singh', 'fname': 'vartikasingh'}
# so here we used classmethods as alternative instance constructors


day = datetime.date(2021, 1, 7)
print(Employee.working_day(day))
