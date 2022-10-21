class RangeInteger:

    def __init__(self, name, min_value, max_value):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value

    def __set__(self, instance, value):
        if value < self.min_value or value > self.max_value:
            raise ValueError(f'Expected value in a range of ({self.min_value};{self.max_value})')


class Employee():
    kpi_score = RangeInteger(name='kpi_score', min_value=0, max_value=100)


emp = Employee()
emp.kpi_score = 10
emp.kpi_score = 101
