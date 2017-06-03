#super class
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

#subclass define a function that call the superclass's method calcualate_wage wrapped it with full_time_wage()
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)

#an intance with name "milton"
milton = PartTimeEmployee("milton")
# the instance call the superclass
print milton.full_time_wage(20)