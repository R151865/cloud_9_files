
"""
Created on 15/05/20

@author: sulthan
"""

class BusinessDeveloper:
    def __init__(self, name: str, age: int, base_salary: int):
        self.name = name
        self.age = age
        self.base_salary = base_salary

    def _get_designer_bonus(self):
        return 4000

    def get_total_salary(self):
        total_salary = self.base_salary + self._get_designer_bonus()
        print('{} - business_developer: {}'.format(self.name, total_salary))
        return total_salary
