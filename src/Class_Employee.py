class Employee:

    def __init__(self,first_name,last_name,pay):
        self.first_name=first_name
        self.last_name=last_name
        self.pay=pay
        self.email=first_name + '.' + last_name + '@company.com'

    def fullname(self):
        print('{} {}'.format(self.first_name,self.last_name))

    def apply_raise(self):
        self.pay = int(self.pay * 2)

emp1 = Employee('Arun','Dayakar','50000')
emp2 = Employee('Aria','Arun','60000')

print(emp1.email)

emp1.fullname()
emp2.fullname()