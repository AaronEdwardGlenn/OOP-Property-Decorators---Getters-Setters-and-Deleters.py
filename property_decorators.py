# lets review property decorators:


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{} {}@email.com'.format(self.first, self.last)


emp_1 = Employee('Aaron', 'Glenn', 1000)

emp_1.first = 'Calvin'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())

# property decorators allow us to define a method, but we can use it like an attribute
